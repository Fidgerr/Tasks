from datetime import *


def date_in_future(integer):
    if not integer:
        main_date = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
        print(main_date)
    else:
        main_date = datetime.today() + timedelta(days=integer)
        main_date = main_date.strftime('%d-%m-%Y %H:%M:%S')
        print(main_date)


date_in_future([])
date_in_future(2)
