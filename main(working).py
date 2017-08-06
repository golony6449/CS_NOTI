import cs_noti
import gnu_noti

def main():
    if option=='all':
        while True:
            cs_id=cs_noti(cs_id)
            gnu_id=gnu_noti(gnu_id)
            time.sleep(interval)
    elif option=='cs':
        while True:
            cs_id=cs_noti(cs_id)
            time.sleep(interval)
    elif option=='gnu':
        while True:
            gnu_id=gnu_noti(gnu_id)
            time.sleep(interval)
    else:
        print 'ERROR: Incorrect Mode Please check again'
        exit()