# MOVED TO GITHUB #
Since google code is closing, agpy is now permanently moved to [github](http://github.com/keflavich/agpy)




A collection of astronomy-related python codes.

[API documentation](http://agpy.googlecode.com/svn/trunk/doc/html/index.html)

I tried to change the hosting to mercurial, but was unable to convert the wiki to hg.  Since there are many important comments on the wiki and issues pages, I elected to give up.  I'm unhappy with this situation, so tips are welcome.

### MATURE CODE: ###
[readcol](http://code.google.com/p/agpy/source/browse/trunk/agpy/readcol.py) - ASCII column-reading code.  More powerful than IDL's readcol: has the ability to read a data table with labeled columns as a dict.
This code is now mostly superceded by [atpy](http://atpy.github.com) and [asciitable](http://cxc.harvard.edu/contrib/asciitable/) but may still be easier to use for many simple applications.

[blackbody](https://code.google.com/p/agpy/source/browse/trunk/agpy/blackbody.py) - Tools for creating blackbody functions, greybody (beta-modified blackbody), and fitting both to data.

[Fitting A Line To Data](https://code.google.com/p/agpy/source/browse/trunk/agpy/fit_a_line.py)  - There are LOTS of ways to fit a line to data.  They may be appropriate for different data sets.  Includes a pymc monte-carlo fitter, a total least squares fitter, and a PCA / SVG fitter.

[FFT tools](https://code.google.com/p/agpy/source/browse/trunk/AG_fft_tools) Image FFT tools, including n-dimensional FFT-based convolution with capability to ignore NaN values.  This code has been incorporated into the [astropy.org astropy] package.

[Image Tools](https://code.google.com/p/agpy/source/browse/trunk/#trunk%2FAG_image_tools) Some tools for image manipulation, including a cross-correlation method for determining the best-fit shift between two images with extended structure.  Also includes drizzle, downsample, and radial profile tools.

grep - really simple, greps for things... tries to be similar to | grep on bash cmd line but isn't all that useful.  I mostly use this to find substrings in large lists of dictionary keys.

gaussfitter - one and two dimensional Gaussian fitting using the Levenberg-Marquardt algorithm.


### SCIENCE TOOLS: ###
  * **UCHIIfitter** - fits the SED of an ultracompact HII region with a blackbody with an optically thin turnover point
h2fit - fits H<sub>2</sub> infrared lines by creating a synthetic spectrum (gaussians)
  * **kdist** - returns Kinematic Distance from Reid 2009 Galactic rotation curve given a velocity.  Also includes inverse.
> luminosity - SED integrator intended for mid-IR to sub-mm
  * **pyflagger** - flagger for Bolocam Galactic Plane Survey pipeline
  * **[plfit](PowerLaw.md)** - power-law fitter as described [here](http://www.santafe.edu/~aaronc/powerlaws/)  **Moved to github at https://github.com/keflavich/plfit, and now accessible via pip too: http://pypi.python.org/pypi/plfit*
  * [RADEX](Radex.md) - I've modified the RADEX radex\_grid.py script to run a cube including temperature and to run in parallel.  In addition, plot\_grid.py can be used to turn a .dat file into a .fits data cube.**

### SUB-PACKAGES ###
#### AG\_fft\_tools ####
  * **[convolve](convolve.md)** - A convolution routine that is capable of using numpy only (though it will try to import scipy's fft because scipy uses fftw).
> Also includes a power-spectrum and power-spectral-density (PSD) code.

#### AG\_image\_tools ####
> Radial Profile functions, as per discussion on [www.astrobetter.com/fourier-transforms-of-images-in-python/ astrobetter]

### SEMI-ABANDONED: ###
collapse\_gaussfit.py
collapseplot.py
cubes.py
subim\_gaussfit.py
plfit\_v1.py - non-class version of plfit


Other people's code that I've modded slightly or are needed as prereqs for other pieces of code here:
combineRGB
mpfit
mad


Abandoned:
fitshow.py


[intro](intro.md)



DEPENDENCIES:
From [astrolib](https://trac6.assembla.com/astrolib):
  * [pycoords](http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz) .tar.gz file
  * [pywcs](http://stsdas.stsci.edu/astrolib/pywcs-1.10-4.7.tar.gz) .tar.gz file  https://github.com/astropy/astropy astropy project page; pywcs is now deprecated
  * [pyregion](http://github.com/leejjoon/pyregion) Github project page