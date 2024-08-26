# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 17:05:04 2024

@author: rhiai
"""

from astropy import units as u 
from astropy.io import fits
from astropy.utils import data

def savemask(foundflux, galaxy, galaxy_name, method): #galaxy_name and method need to be strings
    hdr = galaxy[0].header #index the galaxy and find its header and set it equal to hdr
    hdu = fits.PrimaryHDU(data = foundflux, header = hdr) #creates primary HDU, take hdr from original cube and gets put in here, data is just the name of your data
    hdul = fits.HDUList([hdu])
    hdul.writeto('%s_applied_mask_%s.fits' % (galaxy_name, method))
    return