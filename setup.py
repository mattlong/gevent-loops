from setuptools import setup, find_packages

from gevent_loops import __version__

setup(
    name = 'gevent-loops',
    packages = find_packages(),
    version = __version__,
    description = 'TODO',
    author = 'Matt Long',
    license = 'MIT',
    author_email = 'matt@mattlong.org',
    url = 'https://github.com/mattlong/gevent-loops',
    download_url = 'https://github.com/mattlong/gevent-loops/tarball/' + __version__,
    keywords = ['gevent', 'loop'],
    install_requires = ['gevent>=1.0.1'],
    classifiers = [],
)
