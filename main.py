import sys
import time

from module import cs_noti, gnu_noti, agency_noti

def main():
    interval = 10
    option = mode_select()

    if option == 'all':
        while True:
            gnuModule = gnu_noti.gnuNotification()
            gnuModule.run()

            csModule = cs_noti.csNotification()
            csModule.run()

            agencyModule = agency_noti.agencyNotification()
            agencyModule.run()

            time.sleep(interval)

    elif option == 'cs':
        while True:
            csModule = cs_noti.csNotification()
            csModule.run()
            time.sleep(interval)

    elif option == 'gnu':
        while True:
            gnuModule = gnu_noti.gnuNotification()
            gnuModule.run()
            time.sleep(interval)

    elif option == 'agency':
        while True:
            agencyModule = agency_noti.agencyNotification()
            agencyModule.run()
            time.sleep(interval)


def mode_select():
    if len(sys.argv) == 1:
        print('ERROR: There is no Parameter. Please check README')
    # mode=[all,cs,gnu,agency]
    mode = [False, False, False, False]
    for a in sys.argv:
        if a == 'all':
            mode[0] = True
        elif a == 'cs':
            mode[1] = True
        elif a == 'gnu':
            mode[2] = True
        elif a == 'agency':
            mode[3] = True

    if mode[1] == True and mode[2] == True and mode[3] == True:
        return 'all'
    if mode[0] == True:
        return 'all'
    elif mode[1] == True:
        return 'cs'
    elif mode[2] == True:
        return 'gnu'
    elif mode[3] == True:
        return 'agency'
    # This case is occured when user enter incorrect option
    print('ERROR:Please Enter Correct Option')
    exit()


if __name__ == '__main__':
    main()