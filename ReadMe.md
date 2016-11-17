# Improvements including UI coming soon.

Check out the video tutorial at http://youtu.be/C3TSq9wCjTs

I. DEPENDENCIES

  Anybuntu 10.04+ (Developed on Xubuntu 14.04)
  Python 2+

 sudo apt-get install socat xautomation xdotool
 
II. SETUP & INSTALLATION

In VLC, go to Tools > Preferences.

1. At the bottom, select the "all" radio button next "Show Settings." This should present a screen with a lot more options.

2. Go to "Interface" and then "Main interfaces." Tick the "Remote control interface" and make sure "oldrc" is entered in the field below the checkbox. Then go back to the left, to "Main interfaces."

3. Expand "Main interfaces" and select "RC."

4. Tick the box called "Fake TTY."

5. On the "UNIX socket command input" field, enter /home/USER/vlctransc/vlc.sock. This is the primary difference between this script and its forefather -- for whatever reason, VLC refused to write its .sock file to the home directory. In any case, it's better to have a separate folder running an executable file than it is to have it operating out of your home folder. It also enables you to hide the folder along with all of your .folders. And so forth. 

6. Open a terminal in the download directory and type
    cp vlctransc.py ~/vlctransc
Next type
    chmod 700 ~/vlctransc.py
Now the script lives and is executable in /home/USER/vlctransc

7.      Open up your keyboard shortcuts.

    XFCE - This script was written on Xubuntu, so this was very easy to find simply by opening the XFCE menu and typing "keyboard." Then you select the "Applications Shortcuts" tab. 

    Unity - Very much the same. Under Unity, it is System Settings > Keyboard, then Shortcuts tab, then Custom Shortcuts. (http://askubuntu.com/questions/331626/how-to-add-keyboard-shortcuts)

8. Now is the important part. Create a new shortcut. You have the following options using this script:
    
    pause - Also will resume play. Depending on your habit, you may want to create two hotkeys for this.
    
    jogfoward - Moves ahead in the audio based on VLC settings.
    
    jogbackward - Moves backward in the audio based on VLC settings.
    
    faster - Increases playback speed based on VLC settings.
    
    slower - Decreases playback speed based on VLC settings.
    
    timestamp - Grabs the current hh:mm:ss format timestamp and imprints it into your current window. The format of the timestamp can be modified in the script, just see the actual script (lines 148-157).

For any of the above commands, you simply create a new shortcut and in the command field, enter:
    
    ~/vlctransc/vlctransc.py COMMAND

Everything should be set up properly. All you have to do now is decide how you want your keyboard set up. Be sure that your shortcuts don't conflict with any shortcuts in your word processing program. The settings that I use are prettly simplistic:

LSUPER + SPACE for pause/play. It looks like:

    ~/vlctransc/vlctransc.py pause

CTRL + LSUPER + LALT for jogbackward.

    ~/vlctransc/vlctransc.py jogbackward
    
And so on. Using the above listed commands. You may decided to use them all. As previously stated, you may want to have one shortcut for pause and one for play. To do this, just have the same command on two shortcuts.

REMEMBER: VLC MUST BE RUNNING FOR THE SCRIPT TO EFFECTIVELY MANIPULATE IT. (This is because the script works through vlc.sock, which is generated when VLC starts.)

Hope that helps. Any troubles, please drop me a line: bitillionaire@gmail.com

If you've found this guide helpful, I accept tips in the following formats:
Bitcoin: 1phmMcubFy298wujNFj6hQ1gctUBFovmL
Woodcoin: WiPHMipxoJWr2Mw1AvPHvaMpzQfzTBLNu4

