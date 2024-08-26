import numpy as np
import astropy.io.fits as fits
from reproject import reproject_interp

def regrid(mask, cube):

    """
    Regrid the cube to match the size of the mask.

    Input
    ----------
    mask : str
        File name of the mask (must be FITS).
    cube : str
        File name of the cube (must be FITS).
    """

    # open the mask and grab the mask header
    mask_hdu = fits.open(mask)
    mask_hdr = mask_hdu[0].header

    # open the cube and grab the cube data
    cube_hdu = fits.open(cube)
    cube_data = cube_hdu[0].data

    # make a copy of the cube header
    # change the pixel size and axes sizes of the cube header
    # to match the pixel size and axes sizes of the mask
    cube_hdr = cube_hdu[0].header.copy()
    cube_hdr['CDELT1'] = mask_hdr['CDELT1']
    cube_hdr['CDELT2'] = mask_hdr['CDELT2']
    cube_hdr['NAXIS1'] = mask_hdr['NAXIS1']
    cube_hdr['NAXIS2'] = mask_hdr['NAXIS2']
    cube_hdr['CRPIX1'] = mask_hdr['CRPIX1']
    cube_hdr['CRPIX2'] = mask_hdr['CRPIX2']


    # reproject the cube data into the updated cube header
    cube_reproj, _ = reproject_interp(cube_hdu[0], cube_hdr, 
                                      shape_out=(mask_hdu[0].data.shape[0], mask_hdu[0].data.shape[1]))
    
    # write to a file
    outfile = cube.rstrip('.fits') + '_regrid.fits'
    fits.writeto(outfile, cube_reproj, cube_hdr, overwrite=True)

    return
