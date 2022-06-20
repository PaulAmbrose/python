try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config  = {
    'description': 'My Project',
    'author': 'Paul Ambrose',
    'url' : 'URL',
    'download_url' :  'where to download it',
    'version', '0.1',
    'install_requires' : ['nose'],
    'packages': ['NAME'],
    'scripts' : [],
    'name' : 'projectname'

}

setup(**config)
