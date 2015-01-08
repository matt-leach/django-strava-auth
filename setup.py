#!/usr/bin/env python

from distutils.core import setup

setup(
    name='django-strava-auth',
    description='Strava V3 API Authorization.',
    long_description="""Strava V3 API Authorization""",
    author='Matthew Leach',
    url='https://github.com/matt-leach/django-strava-auth',
    packages=['stravauth'],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
)