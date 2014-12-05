CSRF_ENABLED = False
SECRET_KEY = 'you-will-never-guess'
import os
# email server
#MAIL_SERVER = 'mailrelay.polycom.com@hrnotify'
#MAIL_PORT = 25
##MAIL_USE_TLS = False
#MAIL_USE_SSL = False
#MAIL_USERNAME = 'hrnotify'
#MAIL_PASSWORD = 'P0lyc0m1'

# administrator list
ADMINS = ['hrnotify@polycom.com']


SQLALCHEMY_DATABASE_URI = 'mysql://orclsql:tan5321@hrnotify/flux'

 