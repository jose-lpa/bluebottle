from bluebottle.settings.base import *

SECRET_KEY = '8t(nq%rdBHRi7b5bveU^%Erbfu76yr^%uveDU546tedib#%uRD91OLJTdf'

INSTALLED_APPS += (
    'bluebottle.test',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(PROJECT_ROOT, 'bluebottle', 'test_files', 'test.db'),
        'NAME': ':memory:',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
COMPRESS_ENABLED = False

AUTH_USER_MODEL = 'test.TestBaseUser'
PROJECTS_PROJECT_MODEL = 'test.TestBaseProject'
ORGANIZATIONS_ORGANIZATION_MODEL = 'test.TestOrganization'
TASKS_TASK_MODEL = 'test.TestTask'

SOUTH_TESTS_MIGRATE = True

ROOT_URLCONF = 'bluebottle.urls'

#from django.conf import global_settings
#import os
#
#SITE_ID = 1
#TIME_ZONE = 'Europe/Amsterdam'
#USE_TZ = True
#
#PROJECT_ROOT = os.path.join(os.path.dirname(__file__))
#
#MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'bluebottle', 'test_files', 'media')
#
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'bluebottle', 'test_files', 'assets')
#
#STATICI18N_ROOT = os.path.join(PROJECT_ROOT, 'bluebottle', 'test_files', 'global')
#
#STATICFILES_DIRS = (
#    (os.path.join(PROJECT_ROOT, 'bluebottle', 'test_files', 'global')),
#)
#
#
#STATIC_URL = '/static/assets/'
#MEDIA_URL = '/static/media/'
#
## Absolute filesystem path to the directory that will hold PRIVATE user-uploaded files.
#PRIVATE_MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'private', 'media')
#
#COMPRESS_ENABLED = False # = True: causes tests to be failing for some reason
#
#STATICFILES_FINDERS = [
#    'django.contrib.staticfiles.finders.FileSystemFinder',
#    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
#    # django-compressor staticfiles
#    'compressor.finders.CompressorFinder',
#]
#
#
#SECRET_KEY = '$311#0^-72hr(uanah5)+bvl4)rzc*x1&amp;b)6&amp;fajqv_ae6v#zy'
#
#INSTALLED_APPS = (
#    # Django apps
#    'django.contrib.auth',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.sites',
#    'django.contrib.staticfiles',
#
#    #3rp party apps
#    'compressor',
#    'django_wysiwyg',
#    'fluent_contents',
#    'fluent_contents.plugins.text',
#    'fluent_contents.plugins.oembeditem',
#    'registration',
#    'rest_framework',
#    'social_auth',
#    'sorl.thumbnail',
#    'south',
#    'taggit',
#    'templatetag_handlebars',
#
#    # Bluebottle apps
#    'bluebottle.accounts',
#    'bluebottle.utils',
#    'bluebottle.common',
#    'bluebottle.contentplugins',
#    'bluebottle.geo',
#    # 'bluebottle.organizations',
#    'bluebottle.pages',
#    # 'bluebottle.projects',
#    # 'bluebottle.tasks',
#    'bluebottle.bb_accounts',
#    'bluebottle.contact',
#    'bluebottle.bb_organization',
#    'bluebottle.bb_projects',
#    'bluebottle.bb_tasks',
#
#
#)
#
#MIDDLEWARE_CLASSES = [
#    # Have a middleware to make sure old cookies still work after we switch to domain-wide cookies.
#    'bluebottle.utils.middleware.SubDomainSessionMiddleware',
#    'django.middleware.locale.LocaleMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
#    'bluebottle.accounts.middleware.LocaleMiddleware',
#    # https://docs.djangoproject.com/en/1.4/ref/clickjacking/
#    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'django.middleware.transaction.TransactionMiddleware',
#]
#
#TEMPLATE_DIRS = (
#    os.path.join(PROJECT_ROOT, 'bluebottle', 'test_files', 'templates'),
#)
#
#TEMPLATE_LOADERS = [
#    'django.template.loaders.filesystem.Loader',
#    'django.template.loaders.app_directories.Loader',
#    'apptemplates.Loader', # extend AND override templates
#]
#
#TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
#    # Makes the 'request' variable (the current HttpRequest) available in templates.
#    'django.core.context_processors.request',
#    'django.core.context_processors.i18n',
#    'bluebottle.utils.context_processors.installed_apps_context_processor',
#)
#
#AUTH_USER_MODEL = 'accounts.BlueBottleUser'
#
#ROOT_URLCONF = 'bluebottle.urls'
#
#SESSION_COOKIE_NAME = 'bb-session-id'
#
## Django-registration settings
#ACCOUNT_ACTIVATION_DAYS = 4
#HTML_ACTIVATION_EMAIL = True  # Note this setting is from our forked version.
#
#SOUTH_TESTS_MIGRATE = False # Make south shut up during tests
#
#SELENIUM_TESTS = False
#SELENIUM_WEBDRIVER = 'phantomjs'  # Can be any of chrome, firefox, phantomjs
#
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#
#
#DEBUG = True
#TEMPLATE_DEBUG = True
#
#USE_EMBER_STYLE_ATTRS = True
#
#INCLUDE_TEST_MODELS = True
#
#PROJECT_PHASES = (
#    ('Plan', (
#        ('plan-new', 'Plan - New'),
#        ('plan-submitted', 'Plan - Submitted'),
#        ('plan-needs-work', 'Plan - Needs work'),
#        ('plan-rejected', 'Plan - Rejected'),
#        ('plan-approved', 'Plan - Approved'),
#    )),
#    ('Campaign', (
#        ('campaign-running', 'Campaign - Running'),
#        ('campaign-stopped', 'Campaign - Stopped'),
#    )),
#    ('Done', (
#        ('done-completed', 'Done - Completed'),
#        ('done-incomplete', 'Done - Incomplete'),
#        ('done-stopped', 'Done - Stopped'),
#    )),
#)
#
## Twitter handles, per language
#TWITTER_HANDLES = {
#    'nl': '1procentclub',
#    'en': '1percentclub',
#}
#
#DEFAULT_TWITTER_HANDLE = TWITTER_HANDLES['nl']
#PROJECTS_PROJECT_MODEL = 'projects.Project'
#TASKS_TASK_MODEL = 'tasks.Task'
#ORGANIZATIONS_ORGANIZATION_MODEL = 'organizations.Organization'
