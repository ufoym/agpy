# montage #

[montage](http://montage.ipac.caltech.edu/) is a mosaicing code created by the IPAC group.  It's powerful and flux-conserving, but can be quite slow.  Also, the interface is not particularly intuitive.  What would be as simple as "imcombine **.fits combine=median offset=wcs" in IRAF requires a number of separate montage commands.  However, the end result is worth it.**

[montage](http://code.google.com/p/agpy/source/browse/trunk/agpy/montage) is a bash script I've written to minimize the overhead in generating a mosaiced image.  It uses (requires) [Tom Robitaille's python-montage](http://python-montage.sourceforge.net/) python code.

Usage example:
montage outfile=l089\_reference\_montage.fits 0`*``_`indiv13pca`*``_`map01.fits combine=median &