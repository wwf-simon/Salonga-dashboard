from osgeo import gdal
from osgeo_utils import gdal_calc
from os import path
from glob import glob



folder = r'~/Documents/salonga_dashboard/raster/'

fraction_2000 = path.join(folder,'cropland_fraction_cropland_sum_band1.tif')
fraction_2020 = path.join(folder,'cropland_fraction_cropland_sum_band21.tif')

output_file = path.join(folder,'cropland_fraction_change_2000-2020.tif')

gdal_calc.Calc(
    A=fraction_2000, 
    B=fraction_2020 ,
    calc='B-A',
    outfile=output_file,
    NoDataValue=0,
    creation_options=["COMPRESS=LZW"],
    overwrite=True,
    outputType = gdal.GDT_Int16
)