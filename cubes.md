# Introduction #

Many of these tools are meant to replicate capabilities of the starlink package, but to be used in the context of python codes that are capable of making publication-quality figures.

Source code: http://code.google.com/p/agpy/source/browse/trunk/agpy/cubes.py

# Details #

Recent addition: smooth\_cube will smooth each frame of a cube in parallel using [parallel\_map](http://www.astropython.org/snippet/2010/3/Parallel-map-using-multiprocessing) and the multiprocessing package from [Brian Refsdal](http://code.google.com/u/Brian.Refsdal/).

<img src='https://agpy.googlecode.com/svn/trunk/tests/executiontime_vs_size_cubesmooth.png' width='800'>

Functions:<br>
<ul><li>flatten_header: tool to remove the extra CRPIX/CRVAL/etc. wcs parameters from a header.  pywcs does not function if there are extra header parameters.<br>
</li><li>extract_aperture: simple circular/elliptical aperture extraction from a cube (produces a spectrum averaged through the aperture)<br>
</li><li>integ: simple wrapper of subim_integ that assumes you want the whole image (by default) and integrates over a velocity range.<br>
</li><li>subim_integ: crop an image and integrate over some velocities<br>
</li><li>aper_world2pix: a tool to convert an aperture in wcs coordinates to pixel coords<br>
</li><li>getspec: wrapper of extract_aperture that properly formats the fits header and returns a fits file<br>
</li><li>getspec_reg: wrapper of getspec that uses a ds9 .reg pyregion object as the aperture