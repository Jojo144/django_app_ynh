wifiwithme_ynh
===============

Wifi With Me for YunoHost

A form and a map to take a census of people who want create a radio network.

More information on https://code.ffdn.org/FFDN/wifi-with-me

## Install

```
yunohost app install https://code.ffdn.org/ljf/wifiwithme_ynh.git -a "domain=wifi.arn-fai.net&path=/wifi/&email=contact@arn-fai.net&isp_name=ARN&isp_site=//arn-fai.net&url_contact=//arn-fai.net/contact&isp_zone=Alsace&latitude=48.5691&longitude=7.7621&zoom=12&cnil_number=&cnil_link=&admin=ljf"
```

## Assumptions
- requirements.txt
$project/settings_local.py

## À customiser

- `name` dans `manifest.json`
- variables dans `scripts/_common.sh`


## TODO
test multiinstance
test user already

## On peut faire mieux
Référencement des logs cf. https://yunohost.org/#/packaging_apps_fr
Normalize url ?

changeurl
backup
restore
upgrade

ynh_webpath_register
ynh_add_nginx_config
ynh_use_logrotate


ynh_remove_systemd_config
ynh_remove_app_dependencies
ynh_system_user_delete $app
ynh_secure_remove "/var/log/$app/"
