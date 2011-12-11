# Copyright (C) 2011 Kenneth Lareau, Nicholas Long
#
# All rights reserved.

"""Manage ripper applications"""

from trip_ng.exceptions import TRipNGRipperError
from trip_ng.util import verify_external_programs, verify_media_device


class Ripper(object):
    """ """

    def __init__(self, args):
        """ """

        if not args.device:
            raise TRipNGRipperError('No media device specificed.')

        self.device = verify_media_device(args.device)

        if not args.ripper:
            raise TRipNGRipperError('No ripper program specified.')

        verify_external_programs([ args.ripper ])


    def scan_media(self):
        """Scan for media to be used by ripper"""

        pass


    def rip(self):
        """ """

        pass
