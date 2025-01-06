from osgeo import gdal
from osgeo_utils import gdal_calc
from os import path


folder = r'~/Documents/salonga_dashboard/raster/'

forest = path.join(folder, "forest_fraction_change_2000-2020.tif")
cropland = path.join(folder, "cropland_fraction_change_2000-2020.tif")
output = path.join(folder, "cropland_forest_frontiers.tif")

gdal_calc.Calc(
    A = forest,
    B = cropland,
    calc= '1*((A<15)&(B>5))',
    outfile= output,
    creation_options=["COMPRESS=LZW"],
    NoDataValue=0
    )
