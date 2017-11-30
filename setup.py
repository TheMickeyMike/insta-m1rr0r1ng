#!/usr/bin/env python

from setuptools import setup

setup(name='insta-mirror',
      version='1.0',
      description='Instagram Photo Downloader',
      author='TheMickeyMike',
      author_email='macnow@st.amu.edu.pl',
      url="https://github.com/TheMickeyMike/insta-mirror",
      packages=['insta-mirror'],
      install_requires=['docopt>=0.6.2', ],
      dependency_links=['https://github.com/ping/instagram_private_api@1.3.6#egg=instagram_private_api-1.3.6']
      )
