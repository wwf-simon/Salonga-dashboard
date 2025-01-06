from osgeo_utils import gdal_calc
from os import path
from glob import glob


folder = r'~/Documents/salonga_dashboard/raster/'


mask_wwf_path = path.join(folder, "mask_salonga_wwf.tif")
mask_np_path = path.join(folder, "mask_salonga_np.tif")

hansen_path = path.join(folder, "glc_loss_year.tif")
output = path.join(folder, "loss_year_wwf.tif")

gdal_calc.Calc(
    A = hansen_path,
    A_band = 24,
    B = mask_np_path,
    C = mask_wwf_path,
    calc= 'A*C*(B==0)',
    outfile= output,
    creation_options=["COMPRESS=LZW"],
    NoDataValue=0
    )
