from osgeo import gdal
from os import path
from glob import glob


folder = r'~/Documents/salonga_dashboard/raster/'
agg_factor = 50
# Find all input raster files
input_files = glob(path.join(folder, "*cropland_binary.vrt"))

# Loop through each input raster
for input_file in input_files:
    # Open the raster to read band information
    raster = gdal.Open(input_file)
    if raster is None:
        print(f"Could not open {input_file}")
        continue
    

    # Get original raster resolution
    src_transform = raster.GetGeoTransform()
    pixel_width = src_transform[1]
    pixel_height = -src_transform[5]

# Calculate new resolution
    new_pixel_width = pixel_width * agg_factor
    new_pixel_height = pixel_height * agg_factor
    
    # Loop through each band

    # Define output file name based on input file
    output_file = path.join(
        folder, f"cropland_sum.tif"
    )
    
    gdal.Warp(
    output_file,
    input_file,
    format="GTiff",
    xRes=new_pixel_width,
    yRes=new_pixel_height,
    resampleAlg=gdal.GRA_Sum,  # Sum resampling to count 1s
    outputType = gdal.GDT_Int16
)
    

    raster = None  # Close the raster file