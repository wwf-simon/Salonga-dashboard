from osgeo import gdal, ogr
import os
from os import path

def rasterize(rasterFile, vectorFile, outputPath, burnValue = 1, datatype = gdal.GDT_Int16):
  ref_ds = gdal.Open(rasterFile)
  vector_ds = ogr.Open(vectorFile)
  #input information provided by the raster
  x_res = ref_ds.RasterXSize
  y_res = ref_ds.RasterYSize
  nbands = 1
  
  #safety-net to delete an old file from a previous run
  if os.path.exists(outputPath):
    os.remove(outputPath)
 
  #create an empty raster with the input information
  empty_raster = gdal.GetDriverByName('GTiff').Create(outputPath, x_res, y_res, nbands, datatype, options=['COMPRESS=LZW', 'TILED=YES'])
  empty_raster.SetGeoTransform(ref_ds.GetGeoTransform())
  empty_raster.SetSpatialRef(ref_ds.GetSpatialRef())

  # store the shape information as burn value
  status = gdal.RasterizeLayer(empty_raster, [1], vector_ds.GetLayerByIndex(0),burn_values=[burnValue])
  empty_raster = None # this is the very important line
  return(status)



folder = r'~/Documents/salonga_dashboard/raster/'

ref_img = path.join(folder, "glc_loss_year.tif")
vector_file = path.join(r'C:/Users/simon.spengler/OneDrive - WWF-Deutschland/Dokumente/salonga_dashboard/vector/','Salonga_WWF_landscape.gpkg' )
output = path.join(folder, "mask_salonga_wwf.tif")

rasterize(ref_img,vector_file,output,1,gdal.GDT_Byte)