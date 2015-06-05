Astronomy code by [Adam Ginsburg](http://casa.colorado.edu/~ginsbura/)

I write codes for my work that some may find generally useful.  I use python primarily, but also code in IDL, IRAF, bash shell, fortran, and whatever else is called for by the task at hand.

I've included mpfit.py from [astrolibpy](http://code.google.com/p/astrolibpy/), which is a python translation of [Craig Markwardt's mpfit.pro](http://www.physics.wisc.edu/~craigm/idl/down/mpfit.pro).  However, the readcol.py included here is my own and is very different from the one on astrolibpy.

The h2fit code is meant to be an interactive model fitter.  Right now it can't really be used as-is because it includes hard-coded paths to data files.  That's obviously not necessary, but since I'm using the code to do analysis for my master's thesis I haven't generalized it yet.  I should probably create an h2fit class where you can initialize the directory....