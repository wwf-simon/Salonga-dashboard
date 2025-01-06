
from osgeo_utils import gdal_calc
from os import path
from glob import glob

folder = r'~/Documents/salonga_dashboard/raster/'
raster1_path = path.join(folder, "reclassified_glc_loss_year_band1.tif")
raster2_path = path.join(folder, "reclassified_glc_loss_year_band21.tif")

mask_wwf_path = path.join(folder, "mask_salonga_wwf.tif")
mask_np_path = path.join(folder, "mask_salonga_np.tif")

hansen_path = path.join(folder, "glc_loss_year.tif")
output = path.join(folder, "lc_post.tif")

gdal_calc.Calc(
    A = raster1_path,
    B = raster2_path,
    C = mask_wwf_path,
    D = mask_np_path,
    E = hansen_path,
    E_band = 24,
    calc= 'B*(E>0)*(B!=2)*(E>0)',
    outfile= output,
    creation_options=["COMPRESS=LZW"],
    NoDataValue=0
    )
