[RADEX](http://www.strw.leidenuniv.nl/~moldata/radex.html) is a one-dimensional non-LTE radiative transfer code base on the LAMDA molecular database.

For a nice package that wraps up RADEX calls in python, see:
https://github.com/keflavich/pyradex


---


I have written two codes to use RADEX more efficiently:

  * [radex\_grid.py](http://code.google.com/p/agpy/source/browse/trunk/radex/radex_grid.py) is an executable that is intended to be user-modified.  It will create a grid (cube) over density, column, and temperature parameter space.  It can be run in parallel using mpi4py and mpirun.

  * [radex\_grid\_opH2.py](http://code.google.com/p/agpy/source/browse/trunk/radex/radex_grid.py) is the same as radex\_grid, but allows multiple collision partners, specifically ortho and para H2.  This proved useful for using the [Troscompt 2009](http://adsabs.harvard.edu/abs/2009A%26A...493..687T) [collision rates](http://code.google.com/p/agpy/source/browse/trunk/radex/o-h2co_troscompt.dat).

  * [plot\_grids.py](http://code.google.com/p/agpy/source/browse/trunk/radex/plot_grids.py) is meant to plot the resulting data and/or turn it into .fits data cubes.


In order to use radex\_grid with LVG, Sphere, and Planar assumptions, I recommend generating separate executables.  Edit "radex.inc" included in the RADEX source code distribution (lines 34-36 in the current version as of this posting, stating "parameter (method = 1)" ) for each assumption, then make, then move bin/radex to bin/radex\_sphere or bin/radex\_lvg as appropriate.  I then symlinked (ln -s) the executables into my /usr/local/bin directory, but you can add them to your path however you like.