# Requirements #

In order to run TRipNG, the following additional pieces of software are needed:

## Python ##

TRipNG requires Python 2.7.  Python 3 will be supported at a later time.

## Additional Python modules ##

There are several third-party Python modules that will be needed.  The only currently known one is:

  * [Mutagen](http://code.google.com/p/mutagen/)

Further modules may be needed as development progresses.

## Rippers ##

Software to rip the CD into a format that can be encoded.  The following will initially
be supported:

  * [cdda2wav](http://cdrecord.berlios.de/private/cdrecord.html) (from cdr-tools)
  * [cdparanoia](http://www.xiph.org/paranoia/)

## Encoders ##

Software to encode the raw output from the ripping software into the various user formats.  The following will initially be supported:

  * [LAME](http://lame.sourceforge.net/) (mp3)
  * [oggenc](http://www.vorbis.com/) (Ogg Vorbis)
  * [flac](http://flac.sourceforge.net/) (FLAC)