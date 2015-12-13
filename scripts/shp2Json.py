# ---------------------------------------------------------------------------
# Title: Shapefile to GeoJSON (shp2Json.py)
# Description: Export a GeoJSON file from an ArcGIS shapefile using GDAL.
# Author: Kitty Hurley
# Original date: 2015-12-12
# Last modified date: 2015-12-13
# Resource: https://pcjericks.github.io/py-gdalogr-cookbook
# ---------------------------------------------------------------------------

# Import modules
import os
from osgeo import gdal
from osgeo import ogr
from osgeo import osr

# Allow the user to define the shapefile to export.
shapefile = raw_input('Enter the location of the shapefile (e.g. C:\desktop\dataDump\data.shp): ')
dataSource = ogr.Open(shapefile)

driver = ogr.GetDriverByName('ESRI Shapefile')
dataSource = driver.Open(shapefile, 0) # 0 means read-only. 1 means writeable

# Check to see if shapefile is found
if dataSource is None:
    print 'Could not open %s' % (shapefile)
    quit()
else:
    print 'Opened %s' % (shapefile)

# Define the spatial reference (WGS84)
srs = osr.SpatialReference()
srs.ImportFromEPSG(4326)

# Get the field names of the user-defined shapefile
Layer = dataSource.GetLayer(0)
layerDefinition = Layer.GetLayerDefn()

print '***********************'
print '***** FIELD NAMES *****'
print '***********************'
for i in range(layerDefinition.GetFieldCount()):
    print '* ' + layerDefinition.GetFieldDefn(i).GetName()
print '***********************'

# Allow the user to select the names of the fields to export
exportedFields = raw_input('Select the fields to export: ')

# Error check the user-defined fields
#try:
    # TODO: If the fields are in the shapefile, pass them to the export
    #if [something]
        #print 'The following field(s) will be exported: ' + exportedFields
    # TODO: Run a script failure if the fields are not in the shapefile.
    #else:
        #print '*********************** SCRIPT FAILURE ***********************'
        #print 'Please re-run and enter in valid field names (case sensitive).'
        #print '**************************************************************'
        #quit()
# Add an exception for the try/except
#except:
    #print('An error has occurred.', e)
    #quit()

# Allow the user to name their GeoJSON file.
exportJson = raw_input('What would you like to name your file (e.g. export)? Do NOT include the extension while naming your file: ')
# Add the .JSON extension to the user-defined filename. If the user entered an extension, exit the script.
try:
    if exportJson.endswith(('.json', '.Json', '.JSON', '.geojson', '.Geojson', '.GEOJSON')):
        print '*********************** SCRIPT FAILURE ***********************'
        print 'Please re-run and use an export name without a file extension.'
        print '**************************************************************'
        quit()
    else:
        fullExportJson = exportJson + '.json'
        print 'Exporting ' + shapefile + ' to ' + fullExportJson
        # TODO: Pass fullExportJson as the export location
# Add an exception for the try/except
except Exception as e:
    print('An error has occurred.', e)
    quit()
