# Auto Daily Screener

This automates the NYU Daily Screener using Selenium by automatically going through the NYU web form and filling in all the details automatically. Windows only for now but should be relatively easy to port.

Credits to BYE DUO and DUO Bypass for the code generation code. Pyinstaller used for creating binary. There are no macOS or Linux binaries though both should be pretty easy to make.

## Requirements

- Need Windows and Google Chrome. 

## How do I use this?

Read this or else this isn't going to work. I'll spare the technical details (you can look on GitHub if you want). Also the script is currently Windows only but this could be easily adapted to other platforms in the future if there's demand.

### Making a new device

This script works by bypassing the NYU mfa but to do that, you'll need to create a new device. Here's how:

1. After submitting your username and password, you'll come to the NYU DUO multi-factor authentication page. Click 'Add a new device'

2. Just do your authentication with your standard device (probably your phone)

3. Now pick 'Tablet', 'Android', 'I have DUO mobile installed', and 'Email me an activation link instead'

4. Send the link to your email. Once you recieve it, **don't** click it (it's okay if you accidentally do). However, the link itself is what matters. (The link format is like this: https://m---------.duosecurity.com/android/--------------------)

5. Now open the ads folder. There will be a lot of files in there but don't touch most of them. Go to the "credentials.json" file and fill in your username, password, and deviceURL (the link you just got). Leave everything else the same. (Don't worry, this information is kept on your local device).

6. Now run the app (ads.exe) once. You'll see it generate a secret which means you did it right. If not, then the URL wasn't properly put in. You're almost there but you need to do one more thing. (Optionally you can create a shortcut of ads.exe by right clicking it and clicking "Create Shortcut")

7. Refresh the DUO mobile page (or just open a new window). Go to 'my settings and devices' and reauthenticate with your phone (or another device) like you did before. You should see a new Android device. For the default device option, set it to the new device you made and save. 

8. You're done! If you check your email, the confirmation message should appear soon. However, you still have to manually run the .exe everytime you want to run the script. What if could automatically be done for you...

### (Optional but recommeneded) Running the script daily

### Note: your computer must be on during that day before you go to class for this to be useful. However, setting it to run at midnight means that it likely won't inconvenience you.

1. Open up the Task Scheduler (just search it from the windows search box)

2. Right click on Task Scheduler library and click 'Create Basic Task'. Put a name and description (I put "Auto Daily Screener" for the name, how creative)

3. Have it run daily (lol) at 12:00 AM. Then click 'start a program'. Browse to the ads.exe file and click on it. Click next and then finish.

4. Voila! The script now runs at midnight meaning that you'll always have the daily screener ready before class in the morning. Hope you enjoy!
