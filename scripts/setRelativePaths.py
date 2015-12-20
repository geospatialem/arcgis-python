# ---------------------------------------------------------------------------
# Title: Set ArcMap .MXD Relative Paths (setRelativePaths.py)
# Description: A python script that sets the relative path of an ArcMap
# project(s), or .mxd files, within a user-defined file directory.
# Author: Kitty Hurley
# Original date: 2015-12-12
# Last modified date: 2015-12-20
# Resource: http://support.esri.com/fr/knowledgebase/techarticles/detail/40656
# ---------------------------------------------------------------------------

# Import modules
import arcpy, os, os.path
from arcpy import env

# Allow the user to set the workspace to search for the map documents
Workspace = raw_input('Enter a directory location (e.g. G:/EH Tracking/GIS/GIS_Projects): ')
arcpy.env.workspace = Workspace

###################################
# Verify the user input is correct
###################################
# Allow the user to verify their selected path is correct by selecting 'y', or 'n' (and ensure the input is set to lowercase).
userVerified = raw_input('Is ' + Workspace + ' the correct directory? [y/n]: ').lower()
# Loop used to verify if the user selected the current path.
while True:
    # If the user accepts, terminate the current loop and continue executing the script by resuming execution at the next statement.
    if userVerified == 'y':
        break
    # Else exit the script
    else:
        print 'Please re-run the script and enter in the correct directory location.'
        print 'The script will now quit.'
        quit()

# Verify the user input is a file location using a try/except
try:
    if os.path.exists(Workspace):
        print '*****************************************************'
        print 'The following path was selected:'
        print Workspace
# If the user input is incorrect, or the user doesn't have sufficient privledges print a statement and quit the script.
    else:
        print 'An invalid directory was entered, please enter a valid directory to execute.'
        print 'The script has unsuccessfully executed, and will close.'
        quit()
# Add an exception for the try/except
except Exception as e:
    print('An error has occurred.', e)

###################################
# List the map documents in folder
###################################
# Set the mxdList array for the map document list.
mxdList = []
# Loop through all files selected and append them to the mxdList array.
for root, dirs, files in os.walk(Workspace):
    for f in files:
        if f.endswith('.mxd'):
            #print os.path.join(root, f) #Use for testing
            mxdList.append(os.path.join(root, f))

# Set the count to 0 before the 'for' loop
count = 0

# Set a relative path setting for each MXD in list.
print '*****************************************************'
print 'The following projects will be set to relative paths:'
for file in mxdList:
    print file
    # Set the map document to change the relative path
    filePath = os.path.join(Workspace, file)
    mxd = arcpy.mapping.MapDocument(filePath)
    # Set the relative paths property (to 'True')
    mxd.relativePaths = True
    # Save the map doucment changes
    mxd.save()
    # Change the count after executing the loop
    count = count + 1

# Print a success message to the user
print '*****************************************************'
print 'The script was successfully executed ' + str(count) + ' times.'
