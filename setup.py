#!/usr/bin/env python

from distutils.core import setup

from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt')

reqs = [str(ir.req) for ir in install_reqs]

setup(name='insta-mirror',
      version='1.0',
      description='Instagram Photo Downloader',
      author='TheMickeyMike',
      author_email='macnow@st.amu.edu.pl',
      url="https://github.com/TheMickeyMike/insta-mirror",
      packages=['insta-mirror'],
      install_requires=reqs
     )