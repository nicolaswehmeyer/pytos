#!/home/user/sources/compiled/python3.4_dev/lib/python3.4

import os
from setuptools import setup, find_packages

package_name = "pytos"
rootdir = os.path.abspath(os.path.dirname(__file__))


def get_version():
    with open("CHANGES.txt") as f:
        version = f.readline().split(',')[0]
        return version


setup(
    name='pyTOS',
    version=get_version(),
    author="Tufin Solution Engineering",
    author_email="support@tufin.com",
    url='http://pypi.python.org/pypi/pyTOS/',
    license='LICENSE.txt',
    description="The Tufin TOS SDK for Python",
    long_description=open('README.txt').read(),
    packages=find_packages(),
    include_package_data=True,
    # package_dir={package_name: package_name},
    # package_data={'': ['conf/tufin_api.conf.orig']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4'
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
        'Operating System :: Unix'
    ],
    install_requires=[
        'netaddr>=0.7.14',
        'paramiko>=1.15.2',
        'requests>=2.6.0',
        'requests_toolbelt',
        'pyinotify',
        'cryptography',
        'pycrypto',
        'pbkdf2',
        'netifaces',
        'dnspython3',
        'Mako',
        'pyasn1'
    ],
    zip_safe=False
)