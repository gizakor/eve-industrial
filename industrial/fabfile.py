from fabric.api import local, lcd , prefix , run

def prepare_deployment(branch_name):
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branch_name)


def deploy():
    local('git commit -a ')
    local('git pull')
    local('git push')
    with lcd('/var/django/eve-industrial/industrial/industrial/'):
        # with prefix('workon env'):
        # with prefix("/var/django/eve-industrial/industrial/industrial; workon env"):
        run('pwd')
        run('cd /var/django/eve-industrial/ && git pull ')
        #     local('python manage.py migrate industrialweb')
            #local('python manage.py test myapp')


	run("source /var/django/eve-industrial/env/bin/activate && /var/django/eve-industrial/industrial/run.sh")
    # run("source /var/django/eve-industrial/env/bin/activate && /var/django/eve-industrial/industrial/run.sh")