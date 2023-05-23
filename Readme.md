Ok this is going to be a bit of a frankenstein:
First we need the "joycontrol-pluginloader", follow the install instructions of it, but use this for the joycontrol: "https://github.com/Poohl/joycontrol".
The reason for this is that the original joycontrol is outdated and doesn't work with the switch anymore.

Then use "git clone https://github.com/JKamsker/SuperDuper-Totk" to download this repo.

Assuming you have successfully installed joycontrol and the pluginloader and initialized the controller, you can now start the plugin with ``joycontrol-pluginloader -r auto SuperDuper-Totk/MineruItems.py``