
# SpicetifyGUI

SpicetifyGUI is a graphical user interface for [Spicetify](https://github.com/khanhas/spicetify-cli)

## Installation

Download the latest relase from [here](https://github.com/armadio2902/SpicetifyGUI/relases)

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