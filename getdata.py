# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:50:49 2024

@author: rhiai
"""

from astropy.io import fits

from spectral_cube import SpectralCube as spectralcube 

def getcubedata(galaxy_name): #get the data of the cube, idk if the data was ever actually used tho??? lmao
    cube = spectralcube.read('%s_12CO_rebase5_smooth1.3_hanning2.fits' % (galaxy_name))
    return cube

def getmaskdata(galaxy_name, method, version): #get the mask data to be used later, just tell it to read the data with sc.read and put the strings in the right place
    mask = spectralcube.read('mask_%s_%s_v%s.fits' % (galaxy_name, method, version))
    return mask

def getregrid(galaxy_name): #retrieve the data for the regridded file of the cube
    rgcube = spectralcube.read('%s_12CO_rebase5_smooth1.3_hanning2_regrid.fits' % (galaxy_name))
    return rgcube

def getgalaxy(galaxy_name): #open the regrid file so it's hdr information can be retrieved and such
    galaxy = fits.open('%s_12CO_rebase5_smooth1.3_hanning2_regrid.fits' % (galaxy_name))
    return galaxy