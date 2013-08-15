from agpy import blackbody
import pylab as pl
import numpy as np
#import matplotlib as mpl
pl.rc('font',size=24)

ymin = 1e-7
bgpsf = np.array([250,294.6])
bgpsw = 3e2/bgpsf
irasf = np.array([3.61445783e+12,2.50000000e+12])/1e9
irasw = 3e2/irasf
gpaf = np.array([8,15])
gpaw = 3e2/gpaf

scubaherschelf = np.array([1000,4500])
scubaherschelf = np.array([325,4500])
scubaherschelw = 3e2/scubaherschelf

# 10um to 10 cm
wav_cm = np.logspace(-3,1,1000)

wbb = blackbody.modified_blackbody_wavelength(wav_cm,100,wavelength_units='cm',beta=0)
wgb = blackbody.modified_blackbody_wavelength(wav_cm,100,wavelength_units='cm')
wgbC = blackbody.modified_blackbody_wavelength(wav_cm,10,wavelength_units='cm')
wmax = (np.argmin(np.abs(0.11-wav_cm)))
wgbC *= wgb[wmax]/wgbC[wmax]
wff = (wav_cm/1e-3)**0.1 * ymin * 10

pl.figure(6)
pl.clf()
pl.fill_between(bgpsw,[1e-5,1e-5],[7e-2,7e-2],color='r',alpha=0.5)
pl.fill_between(irasw,[3e-2,3e-2],[1e0,1e0],color='b',alpha=0.5)
pl.fill_between(gpaw,[1e-6,1e-6],[5e-5,5e-5],color='g',alpha=0.5)
pl.annotate('Bolocam',(bgpsw.mean(),1e-1),ha='center')
pl.annotate('IRAS',(irasw.mean(),1.2),ha='center')
pl.annotate('GPA',(gpaw.mean(),8e-5),ha='center')
pl.loglog(wav_cm*10,wbb+wff, color='k', linewidth=3)
pl.loglog(wav_cm*10,wgb+wff, color='k', linewidth=5, alpha=0.5)
pl.loglog(wav_cm*10,wgbC+wff/1e1, color=(0.3,0,0), linewidth=5, alpha=0.5)
pl.xlabel("Wavelength (mm)")
pl.ylabel(r"B$_\nu$(T)")
pl.axis([min(wav_cm*10),max(wav_cm*10),ymin,10])
pl.gca().set_xticklabels(["%i" % x if x >= 1 else "%0.2f" % x for x in pl.gca().get_xticks()])
pl.savefig("BolocamIRASGPA_Wavelength.pdf")
pl.fill_between(scubaherschelw,[1e-6,1e-6],[3,3],color='c',alpha=0.5)
pl.savefig("BolocamIRASGPA_Wavelength_scubaherschel.pdf")

freq = 3e10/wav_cm

fbb = blackbody.blackbody(freq,100)
fgb = blackbody.modified_blackbody(freq,100)
fgbC = blackbody.modified_blackbody(freq,10)
fmax = (np.argmin(np.abs(bgpsf.mean()*1e9-freq)))
fgbC *= fgb[fmax]/fgbC[fmax]
fff = (freq/1e9)**-0.1 * ymin * 10

pl.figure(7)
pl.clf()
pl.fill_between(bgpsf,[1e-5,1e-5],[7e-2,7e-2],color='r',alpha=0.5)
pl.fill_between(irasf,[3e-2,3e-2],[1e0,1e0],color='b',alpha=0.5)
pl.fill_between(gpaf,[1e-6,1e-6],[5e-5,5e-5],color='g',alpha=0.5)
pl.annotate('Bolocam',(bgpsf.mean(),1e-1),ha='center')
pl.annotate('IRAS',(irasf.mean(),1.2),ha='center')
pl.annotate('GPA',(gpaf.mean(),8e-5),ha='center')
pl.loglog(freq/1e9,fbb+fff, color='k', linewidth=3)
pl.loglog(freq/1e9,fgb+fff, color='k', linewidth=5, alpha=0.5)
pl.loglog(freq/1e9,fgbC+fff/1e1, color=(0.3,0,0), linewidth=5, alpha=0.5)
pl.xlabel("Frequency (GHz)")
pl.ylabel(r"B$_\nu$(T)")
pl.axis([min(freq/1e9),max(freq/1e9),ymin,10])
pl.savefig("BolocamIRASGPA_Frequency.pdf")

#rectangle = mpl.patches.Rectangle([np.mean(bgps), [1.5e-6

