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
    # with lcd('/var/django/eve-industrial/industrial/industrial/'):
    #     # with prefix('workon env'):
    #     # with prefix("/var/django/eve-industrial/industrial/industrial; workon env"):
    #     run('pwd')
    run('cd /var/django/eve-industrial/ && git pull --no-edit')
        #     local('python manage.py migrate industrialweb')
            #local('python manage.py test myapp')

    with lcd('/var/django/eve-industrial/industrial'):
        run("pwd")
        run("cd /var/django/eve-industrial/industrial&& source /var/django/eve-industrial/env/bin/activate &&  ./run.sh ")