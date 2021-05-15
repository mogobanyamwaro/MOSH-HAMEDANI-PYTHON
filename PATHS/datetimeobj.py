from datetime import datetime, timedelta
import time

dt = datetime(2020,1,1)
datetime.now()
dt = datetime.strptime("2038/01/01" ,"%Y/%m%d")

datetime.fromtimestamp(time.time())

dt.year
dt.strftime("")