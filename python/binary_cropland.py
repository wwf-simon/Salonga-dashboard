from osgeo import gdal
from osgeo_utils import gdal_calc
from os import path
from glob import glob


folder = r'~/Documents/salonga_dashboard/raster/'
mask_wwf_path = path.join(folder, "mask_salonga_wwf.tif")
# Find all input raster files
input_files = glob(path.join(folder, "*glc_loss_year.tif"))

# Loop through each input raster
for input_file in input_files:
    # Open the raster to read band information
    raster = gdal.Open(input_file)
    if raster is None:
        print(f"Could not open {input_file}")
        continue
    
    # Get the number of bands
    band_count = raster.RasterCount
    
    # Loop through each band
    for band_index in range(1, band_count ):  # GDAL bands are 1-based
        # Define output file name based on input file and band number
        output_file = path.join(
            folder, f"cropland_binary_{path.basename(input_file).split('.')[0]}_band{band_index}.tif"
        )
        
        # Perform reclassification on the specific band
        gdal_calc.Calc(
            A=input_file,  # Specify the band using `file:band_index`
            A_band= band_index,
            B =mask_wwf_path,
            calc='(1*((A<=20)&(A>=10)))*B',
            outfile=output_file,
            NoDataValue=0,
            creation_options=["COMPRESS=LZW"],
            overwrite=True
        )
    
    raster = None  # Close the raster file