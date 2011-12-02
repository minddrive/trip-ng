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
import ConfigParser
import os.path

# Temporary for now... maybe?
basedir = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))
sys.path.insert(0, os.path.join(basedir, 'lib', 'python'))

import trip_ng.tripconf as tripconf


def parse_command_line():
    """ """

    conf_error = False

    conf_parser = argparse.ArgumentParser(add_help=False)
    conf_parser.add_argument('--configuration', '-c', metavar='FILE',
                             default=tripconf.default_conf,
                             help='Configuration file to use')
    conf_args, remaining_argv = conf_parser.parse_known_args()

    defaults = { 'ripper' : 'cdda2wav',
                 'encoder' : [ 'lame' ], }

    try:
        with open(conf_args.configuration) as conf_file:
            config = ConfigParser.SafeConfigParser()
            config.readfp(conf_file)
            defaults.update(config.items('TRipNG'))

            # Make sure 'encoder' variable is a list
            defaults['encoder'] = list(set(defaults['encoder'].split()))
    except IOError:
        # No profile if config file doesn't exist UNLESS configuration
        # file is specified; raise error after full parser is set up
        # so user sees full help information
        if conf_args.configuration != tripconf.default_conf:
            conf_error = True

    parser = argparse.ArgumentParser(parents=[ conf_parser ],
                                 description='Program to rip and encode CDs')

    parser.add_argument('--device', '-d', help='Media device to use')
    parser.add_argument('--ripper', '-r', choices=tripconf.rippers,
                        help='Ripping program to use')
    parser.add_argument('--encoder', '-e', nargs='+',
                        choices=tripconf.encoders,
                        help='Encoding program(s) to use (multiple allowed)')
    parser.add_argument('--normalize', '-n', action='store_true',
                        default=False, help='Use normalization')
    parser.add_argument('--retain-lossless', action='store_true',
                        default=False, help='Keep lossless files')

    if conf_error:
        parser.error('Configuration file %s does not exist'
                     % args.configuration)

    parser.set_defaults(**defaults)
    args = parser.parse_args(remaining_argv)

    # Now verify some of the new defaults, since argparse blindly
    # applies them without verifying they're valid for the options
    encoders = set(args.encoder)

    if args.ripper not in tripconf.rippers:
        parser.error('%s not a valid ripper' % args.ripper)

    if not encoders.issubset(set(tripconf.encoders)):
        parser.error('%s not a valid set of encoders' % args.encoder)

    return args


if __name__ == '__main__':

    args = parse_command_line()
    print args
