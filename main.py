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

@eel.expose
def getThemes():
    return themeList

@eel.expose
def getPreviewImg(themeName):
    imagePath = toDirectory + "\\" + themeName + "\\" + "screenshot.png"
    shutil.copyfile(imagePath, currentPath + "/web/res/screenshot.png")
    return imagePath

@eel.expose
def setTheme(themeName):
    os.system('start /min cmd /c "setTheme.exe "' + themeName + '"')
    
def noclose(page):
    return
# Start eel framework
eel.start("pages/index.html", mode="chrome", close_callback=noclose("pages/index.html"))