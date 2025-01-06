from osgeo import gdal
from osgeo_utils import gdal_calc
from os import path
from glob import glob


folder = r'~/Documents/salonga_dashboard/raster/'
glc_2000 = path.join(folder, "reclassified_glc_loss_year_band1.tif")
glc_2020 = path.join(folder, "reclassified_glc_loss_year_band21.tif")
output = path.join(folder, "lc_change_2000-2020.tif")

gdal_calc.Calc(
    A = glc_2000,
    B = glc_2020,
    calc= '(A*10)+B',
    outfile= output,
    creation_options=["COMPRESS=LZW"],
    NoDataValue=0
    )
