django_app_ynh
===============

This Yunohost package is intended to install every simple Django application on Yunohot.

It takes some inspirtaion from:
  - Wifi With Me for YunoHost https://code.ffdn.org/ljf/wifiwithme_ynh
  - https://github.com/artus40/djangoapp_ynh/


## Usage

Install with:

```
sudo yunohost app install https://github.com/Jojo144/ynh_django_app
```

The installer will ask you:
  - the repository of your application (can be local)
  - a user name and a password to create a Django admin
  - the name of the Django project
    

## Example

This was tested with: https://github.com/Jojo144/tableau-des-permanences

```
sudo yunohost app install -f --debug /vagrant/ynh_django_app -a "domain=ynh.local&path=/&admin=admin&repo=/vagrant/tableau-des-permanences&project=mysite&email=yo@example.tld&passwd=pouetpouet"
```

## Assumptions

The code in the repository of your application is supposed to be organised as follow:

  - requirements.txt
  - DjangoProjectName/settings_local.py
  - DjangoProjectName/settings_local.py


## Under the hood

  - Gunicorn
  - tested with sqlite3
  - no link with the LDAP or Yunohost users
  - if you want a better name to the Yunohost tile you need to tweak `name` in `manifest.json`


## TODO

  - changeurl
  - backup
  - restore
  - upgrade


## Messy notes

Référencement des logs cf. https://yunohost.org/#/packaging_apps_fr

ynh_webpath_register
ynh_add_nginx_config
ynh_use_logrotate

ynh_remove_systemd_config
ynh_remove_app_dependencies
ynh_system_user_delete $app
ynh_secure_remove "/var/log/$app/"

UPGRADE
  TODO: factorisation avec le install, faire un _common.sh
 - git stash # ou pas si on veut un bon gros crash au cas où on a des modifs locales… au moins on sera au courant…
 - git pull
 - pip -r requirements.txt
 - migrate
 - collectstatic
 - reload service systemctl
