#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tap-forex-api',
      version='0.1.1',
      description='Singer-modified tap for extracting data from the exchangeratesapi.io',
      author='Lokals Technologies, Ltd.',
      url='none',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_forex_api'],
      install_requires=['singer-python==5.3.3',
                        'backoff==1.3.2',
                        'requests==2.21.0'],
      extras_require={
          'dev': [
              'ipdb==0.11'
          ]
      },
      entry_points='''
          [console_scripts]
          tap-forex-api=tap_forex_api:main
      ''',
      packages=['tap_forex_api'],
      include_package_data=True
)
