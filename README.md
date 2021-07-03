
# SpicetifyGUI

SpicetifyGUI is a graphical user interface for [Spicetify](https://github.com/khanhas/spicetify-cli)

![Screenshot 1: Home page](https://i.imgur.com/YFEPVkT.png)
![Screenshot 2: Theme preview](https://i.imgur.com/SGsV26M.png)

## Installation

Download the latest relase from [here](https://github.com/armadio2902/SpicetifyGUI/releases)

## Contributing
1. Create the executable version of setTheme.py in the "spicetify" folder
   using pyinstaller

   ```
     pyinstaller  --onefile  setTheme.py
   ```


2. Build the main executable 
   ```
     python -m eel main.py web --onefile --noconsole
   ```
   _in both cases, remember to replace the python script with the executable file generated in the "dist folder"_
## License
[MIT](https://choosealicense.com/licenses/mit/)
