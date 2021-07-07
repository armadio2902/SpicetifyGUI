import eel
import os
import shutil
from distutils.dir_util import copy_tree

currentPath = os.getcwd()

# Initialize eel framework
eel.init("web")

os.chdir("config")

# Check if SpicetifyGUI is started for the first time
if (os.path.exists('settings.ini') == False):
    isFirstInstall = True
    f = open('settings.ini', 'x')
    f.close()
else:
    isFirstInstall = False
os.chdir("..")

os.chdir("spicetify")

if (isFirstInstall == True):
    os.system("start /min initialize.bat")
    print("Spicetify config file created successfully")
    os.system("start /min backupAndDevtools.bat")
    print("Backup completed")
    print("Spotify dev tools: enabled")

# Copy SpicetifyGUI Themes into SpicetifyCLI directory
user = os.getenv('USERPROFILE')
fromDirectory = "Themes"
toDirectory = str(user) + "\.spicetify\Themes"
copy_tree(fromDirectory, toDirectory)

themeList = os.listdir(toDirectory)

## Delete old session screenshots
def deleteScreenshots():
    dir_name = currentPath + '/web/res/screenshots'
    if os.path.exists(dir_name) and os.path.isdir(dir_name):
        if not os.listdir(dir_name):
            print("Screenshots directory is empty")
        else:    
            print("Screenshots directory is not empty, deleting files")
            shutil.rmtree(dir_name)
            os.makedirs(dir_name)
    else:
        print("Screenshots directory doesn't exist")

@eel.expose
def getThemes():
    return themeList

@eel.expose
def getPreviewImg(themeName):
    deleteScreenshots()
    imagePath = toDirectory + "\\" + themeName + "\\" + "screenshot.png"
    shutil.copyfile(imagePath, currentPath + "/web/res/screenshots/screenshot.png")
    os.rename(currentPath + '/web/res/screenshots/screenshot.png', currentPath + '/web/res/screenshots/screenshot' + themeName + '.png')
    imageName = '../res/screenshots/screenshot' + themeName + '.png'
    print("getting theme preview...")
    return imageName

@eel.expose
def setTheme(themeName):
    print("Changing theme to:" + themeName)
    os.system('start /min cmd /c "setTheme.exe "' + themeName + '"')
    
def noclose(page):
    return
# Start eel framework
eel.start("pages/index.html", mode="chrome", close_callback=noclose("pages/index.html"))