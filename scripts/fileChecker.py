# Import modules
import os, os.path

# User input to define the file location
print '*****************************************************'
print '*****************************************************'
fileLocation = raw_input('Enter the location of the folder to count the number of files (e.g. /users/username/desktop): ')

# Allow the user to verify their selected path is correct by selecting 'y', or 'n' (and ensure the input is set to lowercase).
print '*****************************************************'
userVerified = raw_input('Is ' + fileLocation + ' the correct directory? [y/n]: ').lower()
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

# Try to print the number of files in the folder specified
try:
    if os.path.exists(fileLocation):
        len([name for name in os.listdir(fileLocation) if os.path.isfile(os.path.join(fileLocation, name))])
        print '*****************************************************'
        print 'There are ' + str(len([name for name in os.listdir(fileLocation) if os.path.isfile(os.path.join(fileLocation, name))])) + ' files in ' + fileLocation
    # If the user input is incorrect, or the user doesn't have sufficient privledges print a statement and quit the script.
    else:
        print 'An invalid directory was entered, please enter a valid directory to execute.'
        print 'The script has unsuccessfully executed, and will close.'
        quit()
# Add an exception for the try/except
except Exception as e:
    print('An error has occurred.', e)
