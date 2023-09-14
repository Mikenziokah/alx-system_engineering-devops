CMD CHALLENGE is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!.
STEPS TO FOLLOW MOVING THE SCREENSHOTSFROM YOUR LOCALMACHINE TO THE SANDBOX
1. open your sandbox and copy the SFTP.
2. open your local terminal and paste it there when prompted for a password ,got the sandbox and copy it from there paste it hit enter.
3. navigate to your local terminal using lls(local lists) then lcd to where you have your screenshots eg.(I had mine on the desktop so you will do lls Desktop).
4. locate your files you want to move to your sandbox then use put command i.e (put filename) and enter it will be uploaded to the sandbox enviroment, do this to all the 3 files and exit the SFTP terminal.
5. open your web term sandbox  and ls the / (uploaded files will be in that directory)
6. first move them to the root directory then navigate to root.
7. move the files again from root root directory to the cloned repository in your sandbox.
8. move the files again to your command line for win directory.
9. confirm you have moved the files
10.finally push to git hub.
NOTE you might have an easier way of moving the files from / directory to the desired commandline directory without having to move from one stage to another, but I choose the longer way.

