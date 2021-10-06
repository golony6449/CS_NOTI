## Programming by Golony(Park_seong_heum)
![workflow](https://github.com/golony6449/CS_NOTI/actions/workflows/aws_ecr_deploy.yml/badge.svg)
## CS_NOTI

This program will get information from cs.gnu.ac.kr,gnu.ac.kr and send to your phone via TELEGRAM

### Description about file in source folder
1. api_key: Save Telegram Bot's api key

2. last_cs: Save last post's id of cs for re-runnging this program

3. last_cs_notice: Save last Notice count

4. last_gnu: Save last post's id of gnu hot news for re-runnging this program

5. last_agency: Save last post's if of gnu agency noti for re-running this program

### HOW TO USE
1. run main.py on terminal with parameter - Example: python main.py gnu cs

### Parameter:
* cs:CS_NOTI will be activated
* gnu:GNU_NOTI will be activated
* agency: AGENCY_NOTI will be activated
* all; All service will be activated

### Requirement
* requests
* html5lib
* beautifulsoup4
* PyQt5