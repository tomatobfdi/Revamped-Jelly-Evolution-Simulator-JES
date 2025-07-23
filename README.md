# Jelly Evolution Simulator
Adapted from carykh by me

To run this program, you have two options:
    1. Store it in your user file
        Although it does make running the simulator easier as you have to type less in the command prompt to open it up, you have to store it in your user file and if you run many things from there, it can get really messy. This method is not recommended, I only used it because I frequently needed to run the code again and again to test things. Now that I've finished though, I've switched to the 2nd method now.

        Step 1:
            Look at the default line when you open Terminal or Command Prompt. It should look something like C:\Users\ and then whatever your username is for the computer.
        Step 2: 
            Locate the place where it says in your File Explorer. On Windows, it should be under This PC > C: > your username.
        Step 3:
            Download and save this source code into that location.
        Running the Simulator:
            Every time you want to run the sim, open Terminal or Command Prompt. Type in:
                ```
                python jes.py
                ```
            and hit enter. It should load now!
    
    2. Store in a seperate file, wherever you want
        This method requires you to type in two lines of code when opening the sim. However, it is neater to save all the .py files (as well as the the .png and .md) in one folder.

        Step 1:
            Download and save this source code wherever you want. Take note of the location of the folder the scripts are in. It should look something like C:\Users\username\mystuff\jes.
        Running the Simulator:
            Everytime you want to run the sim, open Terminal or Command Prompt. Type in:
                ```
                cd C:\ wherever you saved the scripts
                ```
            Note the space in between cd and wherever you saved the scripts.

            After hitting enter, a new line should show up with the location you inputted in the first line. In this new line, type:
                ```
                python jes.py
                ```
            and hit enter. It loads! Hooray!

Note that this works in Windows Powershell as well as Terminal and Command Prompt.

It should look something like this:
```
-------------------------------------------------[-][=][X]
Microsoft Windows [Version 10.0.12345.6789]
(c) Microsoft Corporation. All rights reserved.

C:\Users\username> python jes.py
---------------------------------------------------------| Method 1
```

```
-------------------------------------------------[-][=][X]
Microsoft Windows [Version 10.0.12345.6789]
(c) Microsoft Corporation. All rights reserved.

C:\Users\username> cd C:\Users\username\mystuff\jes

C:\Users\username\mystuff\jes> python jes.py
---------------------------------------------------------| Method 2
```
NOTE (From Cary): This project, like all my projects, are not meant to be consumer products with perfect QA. Rather, it's just me, as one person, coding a casual experiment to the point that it works well enough on my computer to make a video from it! No more, no less. (I used to not put my code online, just like when you create a Minecraft world with your friends, you don't have to share the world with everyone. I just started posting code here because I wanted to make it easier for eager devs to make mods.) Long story short, I won't be doing bug-fixing or tech support on this project.

NOTE (From me): I downloaded this from the GitHub website thinking I was in for an instant treat - the file opened, but the pygame window was WAY too big. I couldn't see any edges of the window, and all the buttons were barely visible at the bottom and the slider was completely hidden. The movies were all too high on the screen, and the problems go on. So I started to edit the code of the UI to fit my screen.
Finally it was done, and I realised I could add and tweak a few things here and there to make it more easy to use. And here is the finished product!

# Key-controls

Q: Open/close the jelly mosaic

W: Toggle how the jelly mosaic is sorted (By ID, Fitness or Weakness)

E: Toggle how the jelly mosaic looks (By Jelly Icons or Species Tiles)

R: Store the species you're highlighting in memory. (Press R a 2nd time to unstore.) Why do this? Well, say you notice there's a jelly who got #1 in a certain generation, but you can't find any trace of it elsewhere. Now, you can highlight the jelly, press R, and their species bubble will show up in the upper-left. Then, roll your mouse over the species bubble, and there's all the species info!

D: Toggle whether or not X's show up over killed jellies

F: Change the color of the species you're highlighting. Do this when 2 species are annoyingly close in color, and you want a better way to tell them apart.

LEFT/RIGHT: Scroll through forward/backward through the timeline (can also be done by scrolling the scroll bar)

ENTER: Do a generation

\ (BACKSLASH): Turn on Automatic Generation

ESC and DELETE (at the same time): Close the program. This is to make sure you don't accidentally close your program because the two keys are on opposite sides of the keyboard!

# Updates (2025-01-11) (By Cary)

- Mutation-finding-bug fixed (I think)

There used to be a bug where, late in the simulation, big mutations would take forever to find. That has been resolved. (It was the 0.5+ rigidity-forcing)

- Added all those key controls

- Allowed the user to change the number of creatures in the simulation (first user input)

- Fixed but where, when you click "Watch sample", it ONLY shows you a sampling of 8 creatures from the recent-est generation. Now, it always shows you a sampling of the generation your scroll bar is currently at.

# Updates (By me)

- Resized the window and all the UI to fit smaller screens
    - The creature mosaic now is a 17 by 15 square to fit smaller squares. The species lightboard in the advanced species info is also now a 17 by 15 square, but now with the multiples of 17 listed along the right hand side so it's easier to see what place each species got.

- Added extra key controls for accessibility (W, E, R, Autogen, and quit (for some reason Cary's quit function didn't work))
    - Edited key controls (X -> D and C -> F). The reason I did this is because the left hand four fingers can rest on Q, W, E and R, and the index can easily reach T, D and F from it's "resting position", R.
    - Couldn't find a way to make a shortcut for the watch sample button. Sorry for anyone that uses it! I gave up after half an hour of searching because I don't really use it anyway, but if you do find a way, good job!

- Renamed Show Creatures, Small icons, and Turn on ALAP to Show Jellies, Jelly Icons and Turn on Autogen repectively. This is because I thought jellies just sounded better, and Autogen because ALAP doesn't sound that good.

- Removed the option for 100 and 500 creatures, because I just found it annoying having to double-tap enter after entering jes.py in the command prompt. If you want to add it back, just remove the hashtags that I put in front of the code in line 8, 9 and 10 and remove line 15 entirely.

- Removed the "Big Icons" option from the jelly mosaic style button. Didn't have a use for it since I always used 250 creatures. If you want it back, check Cary's source code and replace anything that's got to do with togglestyle, togglestyle.setting(), self.togglestyle.setting() or anything else related to that. If mine is different to Cary's, replace my code with Cary's. Also, remember to add back in a 3rd list item in the stylebutton list near the top of jes_ui.py. Should be back to normal!

Have fun! Check out carykh on Youtube.