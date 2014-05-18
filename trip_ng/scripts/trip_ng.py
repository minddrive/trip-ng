#!/usr/bin/env python3
#
# Copyright (C) 2011-2014 Kenneth Lareau
#
# All rights reserved.

"""TRipNG is an application to rip and encode CDs into various digital
   formats.  It has the ability to handle multiple rippers and encoders
   and allows the user to tag their music in a flexible manner.
"""

import sys

# Only latest versions of Python 3.x (3.3+) is supported
pyvers = sys.version_info[:2]

if pyvers < (3, 3):
    raise RuntimeError('Python 3.3 or later is required to use this program')

# We have the right Python version, move along...
import argparse
import configparser

import trip_ng.tripconf as tripconf


def parse_command_line():
    """ """

    conf_error = False

    conf_parser = argparse.ArgumentParser(add_help=False)
    conf_parser.add_argument('--configuration', '-c', metavar='FILE',
                             default=tripconf.default_conf,
                             help='Configuration file to use')
    conf_args, remaining_argv = conf_parser.parse_known_args()

    defaults = dict(ripper='cdda2wav', encoder=['lame'])

    try:
        with open(conf_args.configuration) as conf_file:
            config = configparser.ConfigParser()
            config.read_file(conf_file)
            defaults.update(config.items('TRipNG'))

            # Make sure 'encoder' variable is a list
            defaults['encoder'] = list(set(defaults['encoder'].split()))
    except IOError:
        # No profile if config file doesn't exist UNLESS configuration
        # file is specified; raise error after full parser is set up
        # so user sees full help information
        if conf_args.configuration != tripconf.default_conf:
            conf_error = True

    parser = argparse.ArgumentParser(
        parents=[conf_parser],
        description='Program to rip and encode CDs'
    )

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
                     % conf_args.configuration)

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

    tripng_args = parse_command_line()
    print(tripng_args)
