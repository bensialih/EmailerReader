
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Email',
    'author': 'Abdel Hakim Bensiali',
    'url': 'http://bensialih.co.uk/bensialih/content/emailparser',
    'download_url': 'https://github.com/bensialih/EmailerReader',
    'author_email': 'bensialih@gmail.com',
    'version': '0.1',
    'install_requires': ['appdirs','beautifulsoup4','packaging', 'pyparsing', 'QueryableList', 'six'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'email_parser'
}

setup(**config)


from distutils.core import setup

