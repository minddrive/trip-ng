#!/usr/bin/env python
#
# Copyright (C) 2011 Kenneth Lareau, Nicholas Long
#
# All rights reserved.

"""TRipNG is an application to rip and encode CDs into various digital
   formats.  It has the ability to handle multiple rippers and encoders
   and allows the user to tag their music in a flexible manner.
"""

import sys

# Only latest version of Python 2.x (2.7) is supported
pyvers = sys.version_info[:2]

if pyvers < (2, 7):
    raise RuntimeError('Python 2.7 is required to use this program')

if pyvers[0] == 3:
    raise RuntimeError('Python 3.x is not supported at this time, please '
                       'use Python 2.7')


# We have the right Python version, move along...
import argparse
import os.path

# Temporary for now... maybe?
basedir = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))
sys.path.insert(0, os.path.join(basedir, 'lib', 'python'))

import trip_ng.tripconf as tripconf

parser = argparse.ArgumentParser(description='Program to rip and encode CDs')
parser.add_argument('--device', '-d')
parser.add_argument('--ripper', '-r', choices=tripconf.rippers)
parser.add_argument('--encoder', '-e', nargs='+', choices=tripconf.encoders)
parser.add_argument('--normalize', '-n', action='store_true', default=False)
parser.add_argument('--retain-lossless', action='store_true', default=False)
