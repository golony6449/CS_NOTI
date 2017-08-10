import cs_noti
import gnu_noti
import time

def main():
    # if option=='all':
    #     while True:
    #         cs_id=cs_noti(cs_id)
    #         gnu_id=gnu_noti(gnu_id)
    #         time.sleep(interval)
    # elif option=='cs':
    #     while True:
    #         cs_id=cs_noti(cs_id)
    #         time.sleep(interval)
    # elif option=='gnu':
    #     while True:
    #         gnu_id=gnu_noti(gnu_id)
    #         time.sleep(interval)
    # else:
    #     print 'ERROR: Incorrect Mode Please check again'
    #     exit()
    gnuModule=gnu_noti.gnuNotification()
    gnuModule.run()

if __name__=='__main__':
    main()