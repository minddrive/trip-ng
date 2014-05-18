# Copyright (C) 2011 Kenneth Lareau, Nicholas Long
#
# All rights reserved.

"""Basic utility methods"""

import os
import os.path
import stat

from trip_ng.exceptions import TRipNGExtProgError, TRipNGRipperError


def verify_external_programs(progs):
    """Ensure external programs are available for use."""

    for prog in progs:
        for path in os.environ['PATH'].split(':'):
            try_full = os.path.join(path, prog)

            if os.path.isfile(try_full) and os.stat(try_full).st_mode:
                break
            else:
                raise TRipNGExtProgError('Program "%s" not found in your '
                                         'path; please ensure program is '
                                         'installed and in your path before '
                                         'continuing' % prog)


def verify_media_device(device):
    """Ensure media device exists"""

    try:
        mode = os.stat(device).st_mode
    except OSError:
        raise TRipNGRipperError('Device "%s" does not exist or is not '
                                'accessible.' % device)

    if not stat.S_IFCHR(mode):
        raise TRipNGRipperError('Invalid media device "%s".' % device)

    return device
