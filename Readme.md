# README - SuperDuper - Tears of the Kingdom (Totk)

## About
This is a plugin for joycontrol, which emulates button presses to execute the "Flying State + Y + B" glitch. 
But instead of Flying, you sit on Mineru's mech.




https://github.com/JKamsker/SuperDuper-Totk/assets/11245306/5db3498c-3362-4a1e-8c37-621688bb6815



## Prerequisites
I have only tested it on a Raspberry Pi 4+ but an ordinary linux machine with bluetooth should do it aswell™

Before using this plugin, make sure you have the following installed:

1. **JoyControl**: The original JoyControl project is outdated and no longer works with the Switch. Instead, use the updated version available at [https://github.com/Poohl/joycontrol](https://github.com/Poohl/joycontrol). Please follow the installation instructions provided there.

2. **PluginLoader**: You also need to install the PluginLoader. You can find the PluginLoader at [https://github.com/Almtr/joycontrol-pluginloader](https://github.com/Almtr/joycontrol-pluginloader). Please follow the installation instructions provided there.

3. Make sure both repositories are installed using pip3, as it's statet in the installation instructions of the PluginLoader.


## Installation

To install the SuperDuper-Totk plugin, follow these steps:

1. Clone this repository by running the following command in your terminal:
   ```
   git clone https://github.com/JKamsker/SuperDuper-Totk
   ```

2. Once you have successfully installed JoyControl and the PluginLoader, and have initialized the controller, you can start the plugin using the following command:
   ```
   joycontrol-pluginloader -r auto SuperDuper-Totk/MineruItems.py
   ```

# How to use:

Make sure:
1. you are on the items tab in the game.
2. you have the item you want to duplicate selected in your inventory
3. (More than 5 items of that kind would probably help (idk havent tested it with less) )
4. are not in the menu (press B to exit the menu)
5. you are sitting on Mineru's mech


Congratulations! You have now successfully installed and started the SuperDuper-Totk plugin.

## Contributing

If you would like to contribute to this project, please feel free to submit pull requests or open issues on the GitHub repository. We appreciate any contributions!

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Please refer to the `LICENSE` file for more information.

# Authors
[JKamsker](https://github.com/JKamsker)
[ChatGPT](https://chat.openai.com/)
