#!/usr/bin/env python
#New BSD License
#Copyright (c) 2010, Derek Barnett, Skyehaven Transcription
#*Buntu SoCat Version by P. H. Madore phm.link Copyright (c) 2015
# Video tutorial at phm.link/linuxtranscription.html
#All rights reserved.
#Redistribution and use in source and binary forms, with or 
#without modification, are permitted provided that the following 
#conditions are met:
#
#    * Redistributions of source code must retain the above 
#copyright notice, this list of conditions and the following 
#disclaimer.
#    * Redistributions in binary form must reproduce the above 
#copyright notice, this list of conditions and the following 
#disclaimer in the documentation and/or other materials provided 
#with the distribution.
#    * Neither the name of the Skyehaven Transcription nor the 
#names of its contributors may be used to endorse or promote 
#products derived from this software without specific prior 
#written permission.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND 
#CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, 
#INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF 
#MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR 
#CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
#SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT 
#LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF 
#USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED 
#AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
#LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING 
#IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
#THE POSSIBILITY OF SUCH DAMAGE.
#####

import sys
import os

#feed command to vlc socket to get the time played in seconds

vlcin = os.path.join(os.environ.get("HOME"), 'vlctransc', 'vlc.sock')
vlcout = os.path.join(os.environ.get("HOME"), 'vlctransc', 'vlc.out')

#accept argument when running script, e.g. './vlctimestamp.py timestamp'
args = sys.argv[1:]
i = "normal"
if args:
    i = str.lower(args[0])

#acceptable arguments: help, --help, pause, jogforward, +5, jogbackward, -5,
#faster, slower, normal, timestamp. no argument assumes 'normal'
if i == "help" or i == "-help" or i == "--help":
    print("""
             'help' or '--help' returns this help
             'pause' is a play/pause toggle
             'jogforward' or '+5' jumps forward 5 seconds
             'jogbackward' or '-5' jumps backward 5 seconds
             'faster' increases the tempo without increasing pitch
             'slower' decreases the tempo without decreasing pitch
              no argument or 'normal' returns vlc to normal speed
              'timestamp' types a hh:mm:ss coded timestamp into 
                          active window. see comments within this
                          script if you need to change the timestamp
                          string, offset the timestamp for a video
                          timecode, or if you've made tempo changes
                          in an audio file outside of vlc
             """)

elif i == "jogforward" or i == "+5":
    os.system('echo "key key-jump+extrashort" | socat - unix:' + vlcin)

elif i == "jogbackward" or i == "-5":
    os.system('echo "key key-jump-extrashort" | socat - unix:' + vlcin)

elif i == "jumpforward" or i == "+10":
    os.system('echo "key key-jump+medium" | socat - unix:' + vlcin)

elif i == "jumpbackward" or i == "-10":
    os.system('echo "key key-jump-medium" | socat - unix:' + vlcin)


elif i == "pause":
    os.system('echo "pause" | socat - unix:' + vlcin)

elif i == "faster":
    os.system('echo "key key-rate-faster-fine" | socat - unix:' + vlcin)

elif i == "slower":
    os.system('echo "key key-rate-slower-fine" | socat - unix:' + vlcin)

elif i == "normal":
    os.system('echo "normal" | socat - unix:' + vlcin)

elif i == "timestamp":
    #have vlc post the time ~/vlc.out
    os.system('echo "get_time" | socat - unix:' + vlcin + ' > ' + vlcout)
    
    #read vlc.out and report time played in seconds
    f = open(vlcout, 'r')
    f_list = f.read().split("\n")
    if len(f_list) > 2:
        sec = f_list[1]
    else:
        sec = f_list[0]
    sec = int(sec)
    
    #tempo - if you've adjusted the tempo of an audio file, in 
    #        audacity for instance, then you can use the tempo
    #        variable to give output for a timestamp postion in 
    #        original file. tempo is the percent playback speed
    #        of the modified file. 80 = -20% tempo change, etc.
    #        default is 100
    tempo = 100
    
    #don't change this. if you need an offset, take care of it below
    offset = 0

    #change offsetneeded to True if, for instance, you need to 
    #use a timecode embedded into a video rather than the playtime
    #of the file
    offsetneeded = False
    
    if offsetneeded == True:
    
    #If an offset is needed:
    #Pick a spot on the video and pause it (not the beginning). Enter the appropriate values below:
    #vtch = hours on video time code, vtcm = minutes, vtcs = seconds
        vtch = 0
        vtcm = 0
        vtcs = 10
        vtc = (vtch * 3600) + (vtcm * 60) + vtcs
    #atch = hours in actual playtime, atcm = minutes, 
    #atcs = seconds            
        atch = 0
        atcm = 0
        atcs = 0
        atc = ((((atch * 3600) + (atcm * 60) + atcs) * tempo) / 100)
        offset = vtc - atc
    
    #get the values for hh:mm:ss formatting
    sec = ((sec * tempo) / 100) + offset
    th = sec/3600
    tm = (sec % 3600)/60
    ts = sec % 60
    
    #format the timestamp, default looks like '##Inaudible 00:01:10## '
    #the timestamp in hours:minutes:seconds                    
    t = "%02d:%02d:%02d" % (th,tm,ts)    
    
    #string to append before timestamp
    #for no prefix, set prefix = ""
    prefix = "["
    #string to append after timestamp
    #for no suffix, set suffix = ""
    suffix = "] "                           
        
    #xdotool command to execute, uncomment next line to use xdotool
    #dropstamp = str("xdotool type --delay 0 --clearmodifiers '" + prefix + t + suffix + "'")
    #    
    #drop the timestamp string into active window, uncomment next line to use xdotool
    #os.system(dropstamp)
    #        
    #use xte from the xautomation package if you don't have a version of 
    #xdotool newer than august 2010
    os.system('xte "str ' + prefix + t + suffix + '"')       

#if we don't feed an argument to the script, normalize the play speed of vlc
else:
    os.system('echo "normal" | socat - unix:' + vlcin)
