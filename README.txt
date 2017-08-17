##Programming by Golony(Park_seong_heum)
##CS_NOTI

This program will get information from cs.gnu.ac.kr,gnu.ac.kr and send to your phone via TELEGRAM

##Description about file in source folder
1. api_key
Save Telegram Bot's api key

2. last_cs
Save last post's id of cs for re-runnging this program

3. last_gnu
Save last post's id of gnu hot news for re-runnging this program

##HOW TO USE
run main.py on terminal with parameter
Example: python main.py gnu cs

Parameter:
cs:CS_NOTI will be activated
gnu:GNU_NOTI will be activated
all; All service will be activated (same as cs gnu)

## Requirement
requests
html5lib
beautifulsoup4
PyQt5