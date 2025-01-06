from osgeo import gdal
from os import path


folder = r'~/Documents/salonga_dashboard/raster/'


ds = gdal.Open(path.join(folder, 'glc_loss_year.tif'),1) # The 1 means that you are opening the file to edit it)
rb = ds.GetRasterBand(24) #assuming your raster has 1 band. 
rb.SetNoDataValue(0)
rb= None 
ds = None