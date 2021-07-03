import sys
import os
theme = str(sys.argv[1])
os.system("spicetify config current_theme " + theme)
os.system("spicetify apply")
exit()