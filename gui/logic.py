from module import cs_noti, gnu_noti, agency_noti

import sys

def run(option='all'):
    if option == 'all':
        gnuModule = gnu_noti.GnuNotification()
        gnuModule.run()

        csModule = cs_noti.CsNotification()
        csModule.run()

        agencyModule = agency_noti.AgencyNotification()
        agencyModule.run()

    elif option == 'cs':
        csModule = cs_noti.CsNotification()
        csModule.run()

    elif option == 'gnu':
        gnuModule = gnu_noti.GnuNotification()
        gnuModule.run()

    elif option == 'agency':
        agencyModule = agency_noti.AgencyNotification()
        agencyModule.run()


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