# -*- coding: utf-8 -*-
from fabric.api import *
from fabric.colors import *

def upload_tar_from_git():
    "Create an archive from the current Git master branch and upload it"
    local('git archive --format=tar master | gzip > release.tar.gz')
    #run('mkdir $(path)/releases/$(release)')
    #put('$(release).tar.gz', '$(path)/packages/')
    #run('cd $(path)/releases/$(release) && tar zxf ../../packages/$(release).tar.gz')
    #local('rm $(release).tar.gz')

def i():
    repo_url = local('git config --get remote.origin.url', capture=True)
    
    repo_name = local('basename {0} .git'.format(repo_url), capture=True)

    local('git archive origin/master --format=tar | gzip -9 > /tmp/release.tar.gz')
    run('mkdir -p /var/www/projects/{0}'.format(repo_name))
    with cd('/var/www/projects/{0}'.format(repo_name)):
        put('/tmp/release.tar.gz', '/var/www/projects/{0}/release.tar.gz'.format(repo_name))
        run('tar xzf release.tar.gz')
        run('rm release.tar.gz')
    run('chown -R www-data:www-data /var/www/projects/{0}'.format(repo_name))
    local('rm /tmp/release.tar.gz')

def pull():
    repo_url = local('git config --get remote.origin.url', capture=True)
    
    repo_name = local('basename {0} .git'.format(repo_url), capture=True)
    with settings(user='www-data'):
        run('git pull')
    #with cd('/var/www/projects/{0}'.format(repo_name)):
    #    run('git pull original master')
