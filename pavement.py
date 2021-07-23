import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
from socket import gethostname
import os, sys
from os import environ

from sphinxcontrib import paverutils

import pkg_resources
from runestone import get_master_url

sys.path.append(os.getcwd())

home_dir = os.getcwd()

project_name = "teach-mobilecsp"

master_url = None

if master_url is None:
    master_url = get_master_url()

master_app = 'runestone'
serving_dir = "./build/teach-mobilecsp"

# Change to False when running localhost; True before pushing  to github
dynamic_pages = True

if dynamic_pages:
    dest = './published'
else:
    dest = '../../static'

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./build/teach-mobilecsp",
        sourcedir="_sources",
        outdir="./build/teach-mobilecsp",
        confdir=".",
        project_name = "teach-mobilecsp",
        template_args={'course_id': 'teach-mobilecsp',
     'login_required':'false',
     'appname':master_app,
                       'loglevel': 10,
                       'course_url':master_url,
                       'use_services': 'true',
                       'python3': 'false',
                       'dburl': 'postgresql://runestone@localhost/runestone',
                       'basecourse': 'mobilecsp',
                       # new 7/2019 changes
                       'dynamic_pages': dynamic_pages,
                       'downloads_enabled': 'false',
                       'enable_chatcodes': 'false',
                       'allow_pairs': 'false',
                       'default_ac_lang': 'javascript',
                        }
    )
)

version = pkg_resources.require("runestone")[0].version
options.build.template_args['runestone_version'] = version

# Check to see if we are building on our Jenkins build server, if so use the environment variables
# to update the DB information for this build
if 'DBHOST' in environ and  'DBPASS' in environ and 'DBUSER' in environ and 'DBNAME' in environ:
    options.build.template_args['dburl'] = 'postgresql://{DBUSER}:{DBPASS}@{DBHOST}/{DBNAME}'.format(**environ)

version = pkg_resources.require("runestone")[0].version
options.build.template_args['runestone_version'] = version

from runestone import build  # build is called implicitly by the paver driver.
