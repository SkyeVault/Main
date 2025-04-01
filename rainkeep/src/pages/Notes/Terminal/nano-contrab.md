
# Using nano - A Beginner's Guide

`nano` is a simple, easy-to-use command-line text editor.

## **Basic Usage**
Open a file with:
```sh
nano filename.txt
```
If the file does not exist, nano will create it.
Essential Commands
Command
Description
CTRL + O
Save the file (press Enter to confirm)
CTRL + X
Exit nano
CTRL + K
Cut a line
CTRL + U
Paste a line
CTRL + W
Search for text
CTRL + G
Display help menu
CTRL + C
Show current cursor position
Editing Tips
	•	Use Arrow keys to navigate.
	•	Use CTRL + _ (underscore) to jump to a specific line.
	•	Enable line numbering by running: nano -c filename.txt
	•	
Advanced Usage
	•	Open a file as read-only: nano -v filename.txt
	•	
	•	Open a file with syntax highlighting (if supported): nano -Y bash script.sh
	•	
	•	Search and replace:
	◦	CTRL + \ to open the replace prompt.
	◦	Enter the search term, press Enter.
	◦	Enter the replacement term, press Enter.
Exiting nano
	•	If changes have been made, nano will ask if you want to save before exiting.
	•	Press Y (yes) or N (no), then Enter.

crontab
# Using crontab - A Quick Guide

`crontab` is used to schedule jobs in Linux.

## **View Current Crontab**
To list existing scheduled tasks:
```sh
crontab -l
```
Edit Crontab
To add or modify scheduled jobs:
```sh
crontab -e
```

This opens your crontab file in an editor (default: nano).
Crontab Syntax
A crontab line follows this format:
```sh
* * * * * command_to_run
- - - - -
| | | | |
| | | | +---- Day of the week (0 - 7) [0 and 7 = Sunday]
| | | +------ Month (1 - 12)
| | +-------- Day of the month (1 - 31)
| +---------- Hour (0 - 23)
+------------ Minute (0 - 59)
```


To remove all scheduled jobs:
```sh
crontab -r
```

Check Crontab Logs
Cron job logs are usually found in:
/var/log/syslog
Filter logs for cron jobs:
grep CRON /var/log/syslog
Common Issues
	•	Ensure cron service is running: sudo systemctl status cron
	•	
	•	Use full paths for scripts (e.g., /home/user/script.sh instead of script.sh).
	•	Redirect output to a log file to debug: 0 * * * * /home/user/script.sh >> /home/user/log.txt 2>&1
