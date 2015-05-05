from __future__ import with_statement
from fabric.api import *
from fabric.contrib import *
from fabric.contrib.console import confirm
import time

PROJECT_NAME = 'wedding'
PROJECT_PATH = '/home/ubuntu/projects/'
VERSION = ''

def prod():
    """Sets the deploy environment.
    """
    env.hosts = ['brollop.rogert.se']
    env.user = 'ubuntu'
    env.key_filename = '~/.ssh/standard.pem'

def initial_setup():
    """Initial setup of the server
    """
    confirm('Is this a new server?')

    reqs = ['nginx',
            'python',
            'python3.4',
            'python3-pip',
            'python-dev',
            'python-virtualenv',
            'virtualenvwrapper',
            'libpq-dev',
            'libxml2-dev',
            'libxslt1-dev',
            'libjpeg-dev',
            'libfreetype6-dev',
            'libffi-dev',
            'swig',
            'git',
            ]

    #install all requirements
    sudo('apt-get -y install '+' '.join(reqs))

    if files.exists('/etc/nginx/site-enabled/default'):
        sudo('rm /etc/nginx/site-enabled/default')

    #create symlinks to make libjpeg be found by pillow
    sudo('ln -sfn /usr/lib/x86_64-linux-gnu/libz.so /usr/lib')
    sudo('ln -sfn /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/')
    sudo('ln -sfn /usr/lib/x86_64-linux-gnu/libfreetype6.so /usr/lib/libfreetype6.so')

    #create the vassals and log folder
    sudo('mkdir -p /etc/uwsgi/vassals')
    sudo('mkdir -p /var/log/uwsgi')
    sudo('mkdir -p /var/www')
    sudo('mkdir -p /var/run/uwsgi')

    sudo('chown www-data. /var/run/uwsgi')
    sudo('chown www-data. /var/log/uwsgi')
    sudo('chown www-data. /var/www')

    #install uwsgi system wide
    sudo('pip3 install uwsgi')

    #restart services
    sudo('service nginx restart')

def deploy(version):
    """Deploy a tag from git.

    Usage: fab prod deploy:version=1.0 to deploy version 1.0"""

    VERSION = version
    cur_version_path = PROJECT_PATH+PROJECT_NAME+'/'+version

    if not files.exists(PROJECT_PATH+PROJECT_NAME+'/'+version):
        run('mkdir -p '+PROJECT_PATH+PROJECT_NAME+'/'+version)
    else:
        sudo('chown -R ubuntu. {}'.format(cur_version_path))

    repoURL = local('git config --get remote.origin.url', capture=True)

    """@TODO: change to git clone"""
    #_create_deploy_key()
    #confirm('Is the key on github?')

    #push the code
    filename = PROJECT_NAME+'_'+version+'.tar'
    local('git archive --format=tar -o {path} {version}'
            .format(path='/tmp/'+filename, version=version))
    put('/tmp/'+filename, PROJECT_PATH+PROJECT_NAME)
    run('tar -C {0}/{version} -xf {0}/{file}'.format(PROJECT_PATH+PROJECT_NAME, file=filename, version=version))

    run('mkdir -p {}'.format(cur_version_path+'/logs'))
    if files.exists('/tmp/{}_celery.pid'.format(PROJECT_NAME)):
        with settings(warn_only=True):
            sudo('service uwsgi stop')
            sudo('kill $(cat /tmp/{}_celery.pid)'.format(PROJECT_NAME))
    while files.exists('/tmp/{}_celery.pid'.format(PROJECT_NAME)):
        time.sleep(1)
    run('virtualenv -p /usr/bin/python3.4 {}'.format('~/.venv/'+PROJECT_NAME))
    with prefix('source {}'.format('~/.venv/'+PROJECT_NAME+'/bin/activate')):
        run('pip install -r {}'.format(cur_version_path+'/conf/requirements.txt'))
        with cd(cur_version_path):
            #collect static
            run('python manage.py collectstatic --settings={}.custom_settings.stage_settings'.format(PROJECT_NAME))
    sudo('chown -R www-data. {}'.format(cur_version_path))

    # Take the media folder out of the project, and symlink it
    if not files.exists(PROJECT_PATH+PROJECT_NAME+'/media'):
        sudo('mkdir -p {}'.format(PROJECT_PATH+PROJECT_NAME+'/media'))
        sudo('chown -R www-data. {}'.format(PROJECT_PATH+PROJECT_NAME+'/media'))

    sudo('ln -sfn {} {}'.format(PROJECT_PATH+PROJECT_NAME+'/media', cur_version_path+'/'))
    sudo('chown -R www-data. {}'.format(cur_version_path+'/media'))


    #setup the symlinks
    sudo('ln -sfn {} {}'.format(cur_version_path, '/var/www/'+PROJECT_NAME))
    sudo('ln -sfn {} {}'.format(cur_version_path+'/conf/nginx.conf', '/etc/nginx/sites-enabled/'+PROJECT_NAME+'.conf'))
    sudo('ln -sfn {} {}'.format(cur_version_path+'/conf/uwsgi.ini', '/etc/uwsgi/vassals/'+PROJECT_NAME+'.ini'))

    if not files.exists('/etc/init/uwsgi.conf'):
        #create startup script for uwsgi
        sudo('ln -sfn {} {}'.format(cur_version_path+'/conf/uwsgi.conf', '/etc/init/'))
        sudo('initctl reload-configuration')
    #reload nginx
    with settings(warn_only=True):
        sudo('service uwsgi start')
        sudo('service nginx reload')



def list_tags():
    """List tags in git.
    """
    local("git for-each-ref --sort='*authordate' --format='%(tag) %(subject)' refs/tags")

def _create_deploy_key():
    """Creates a ssh-key to be used as deploy key on repo
    """
    run('mkdir -p /home/ubuntu/.ssh')
    if(not files.exists('/home/ubuntu/.ssh/id_rsa.pub')):
        run('ssh-keygen -t rsa -P ""')
    key = run('cat /home/ubuntu/.ssh/id_rsa.pub')
    print("""
Copy key and add as a deploy key to the repository:
{key}
""".format(key=key))

def create_database(type='pgsql'):
    run('mysql -uroot -p -e "create database if not exists {}"'.format(PROJECT_NAME))

def sync_database():
    with cd('{}'.format('/var/www/'+PROJECT_NAME)):
        with prefix('source {}'.format('~/.venv/'+PROJECT_NAME+'/bin/activate')):
            run('python manage.py migrate --settings={}.custom_settings.stage_settings'.format(PROJECT_NAME))

