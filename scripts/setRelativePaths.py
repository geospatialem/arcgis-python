#source: http://support.esri.com/fr/knowledgebase/techarticles/detail/40656

#Import ArcPy
import arcpy, os

#Allow the user to set the workspace to search for the map documents
Workspace = raw_input("Enter a directory location (e.g. G:\EH Tracking\GIS\GIS_Projects): ")
arcpy.env.workspace = Workspace

#List the map documents in folder
mxdList = arcpy.ListFiles("*.mxd")

#Set a relative path setting for each MXD in list.
for file in mxdList:
    #Set the map document to change the relative path
    filePath = os.path.join(Workspace, file)
    mxd = arcpy.mapping.MapDocument(filePath)
    #Set the relative paths property (to 'True')
    mxd.relativePaths = True
    #Save the map doucment changes
    mxd.save()
