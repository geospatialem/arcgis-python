# ---------------------------------------------------------------------------
# Title: Set ArcMap .MXD Relative Paths (setRelativePaths.py)
# Description: A python script that sets the relative path of an ArcMap
# project(s), or .mxd files, within a user-defined file directory.
# Author: Kitty Hurley
# Original date: 2015-12-12
# Last modified date: 2015-12-12
# Resource: http://support.esri.com/fr/knowledgebase/techarticles/detail/40656
# ---------------------------------------------------------------------------

# Import modules
import arcpy, os, os.path
from arcpy import env

# Allow the user to set the workspace to search for the map documents
Workspace = raw_input('Enter a directory location (e.g. G:\EH Tracking\GIS\GIS_Projects): ')
arcpy.env.workspace = Workspace

# Verify the user input is a file location using a try/except
try:
    if os.path.exists(Workspace):
        print 'The following path was selected: ' + Workspace + '. The script will now set the relative path to the ArcMap projects in the directory.'
# If the user input is incorrect, print a statement and quit the script.
    else:
        print 'An invalid directory was entered, please enter a valid directory to execute.'
        print 'The script has unsuccessfully executed, and will close.'
        quit()
# Add an exception for the try/except
except Exception as e:
    print('An error has occurred.', e)

# List the map documents in folder
mxdList = arcpy.ListFiles('*.mxd')

# Set a relative path setting for each MXD in list.
for file in mxdList:
    # Set the map document to change the relative path
    filePath = os.path.join(Workspace, file)
    mxd = arcpy.mapping.MapDocument(filePath)
    # Set the relative paths property (to 'True')
    mxd.relativePaths = True
    # Save the map doucment changes
    mxd.save()
    print 'The script has successfully executed.'
