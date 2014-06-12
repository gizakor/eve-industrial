from fabric.api import local, lcd , prefix , run
# import fabric_gunicorn as gunicorn


def prepare_deployment(branch_name):
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branch_name)


def deploy():
    try:
    	local('git commit -a ')
    except:
    	pass
    local('git pull')
    local('git push')
    run('cd /var/django/eve-industrial/ && git pull --no-edit')
    try:
        run('killall gunicorn')
    except:
        pass
    run("cd /var/django/eve-industrial/industrial&& exec /var/django/eve-industrial/env/bin/gunicorn --daemon --workers=4 --bind=0.0.0.0:9000 industrial.wsgi:application", pty=False)
    print 'done'

