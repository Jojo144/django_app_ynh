# -*- coding: utf-8 -*-
#DEBUG=True
ALLOWED_HOSTS= ['YNH_APP_ARG_DOMAIN']

STATIC_ROOT='YNH_APP_STATIC_ROOT'
DEFAULT_FROM_EMAIL='notifier@YNH_APP_ARG_DOMAIN'
SECRET_KEY = 'YNH_APP_SECRET_KEY'

# À vérifier, mais probablement inutile
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Tous accés
# paramétrer SSO en protect_uris
# OU
# Pas d'accès
# hook
# paramétrer SSO en protect_uris
import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
AUTH_LDAP_SERVER_URI = "ldap://localhost:389"
AUTH_LDAP_USER_SEARCH = LDAPSearch("uid=YNH_APP_ARG_ADMIN,ou=users,dc=yunohost,dc=org", ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=sftpusers,ou=groups,dc=yunohost,dc=org",
    "is_staff": "cn=sftpusers,ou=groups,dc=yunohost,dc=org",
    "is_superuser": "cn=sftpusers,ou=groups,dc=yunohost,dc=org"
}
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=groups,dc=yunohost,dc=org", ldap.SCOPE_SUBTREE, "(objectClass=posixGroup)")
AUTH_LDAP_GROUP_TYPE = PosixGroupType()
AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_AUTHORIZE_ALL_USERS = True
AUTH_LDAP_FIND_GROUP_PERMS = True
#AUTH_LDAP_CACHE_GROUPS = True
#AUTH_LDAP_GROUP_CACHE_TIMEOUT = 300
#import logging
#logger = logging.getLogger('django_auth_ldap')
#logger.addHandler(logging.StreamHandler())
#logger.setLevel(logging.DEBUG)
