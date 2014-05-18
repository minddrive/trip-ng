# Copyright (C) 2011 Kenneth Lareau, Nicholas Long
#
# All rights reserved.

"""Basic configuration information for TRipNG application"""

import os


default_conf = os.path.expanduser('~/.tripngrc')

rippers = [ 'cdda2wav', 'cdparanoia' ]
encoders = [ 'lame', 'oggenc', 'flac' ]
