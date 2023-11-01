from datetime import datetime

date_to_prove = '15.4.2023'
date_format = "%d.%m.%Y"

try:
    datetime.strptime(date_to_prove, date_format)
    print(True)
except ValueError:
    print(False)
