# Introduction #

[readcol](http://code.google.com/p/agpy/source/browse/trunk/agpy/readcol.py) is meant to be an equivalent (but better) version of IDL's readcol.pro for reading simple text files into arrays/structures.

# Trackbacks #

[Astrobetter's IDL to Python guide](http://www.astrobetter.com/wiki/tiki-index.php?page=Python+Switchers+Guide) links here!

# Example Uses #

```
$ head -2 reid.tab
Name            lon     lat     parallax perr    vlsr verr  D_p   D_K_old D_K_new
G23.0-0.4       23.01   -0.41   0.218    0.017   +81    3  4.59      4.97    4.72

>>> tab = readcol('reid.tab',asStruct=True)
>>> print tab.Name[0]
 "G23.0-0.4"
```

```
$ head gps20.cat 
# 20cm GPS for high-probability sources with Fp>=5.5*rms
# Table 3 from Becker, White & Helfand 2005
# Version 2 (2007 March 21): modified to correct astrometry errors
#
#Long    Lat     RA           Dec       Sprob    Fpeak      Fint    RMS     Maj    Min    PA Field    OldGPS
339.739+0.419 16:44:12.282 -45:10:17.79  0.17    14.63     18.14   2.405   6.87   0.00  58.0 3400+05 _       

>>> names,data = readcol('gps20.cat',skipline=4,names=True)
>>> print(len(names),data.shape)
  (13, (5045, 12))
```