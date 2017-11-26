#!/usr/bin/env python

from distutils.core import setup

from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt')

reqs = [str(ir.req) for ir in install_reqs]

setup(name='insta-m1rr0r1ng',
      version='1.0',
      description='Instagram Photo Downloader',
      author='TheMickeyMike',
      author_email='macnow@st.amu.edu.pl',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['insta-m1rr0r1ng', 'distutils.command'],
      install_requires=reqs
     )