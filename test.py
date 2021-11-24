import datetime
import time
from datetime import datetime, timedelta

textEdit_timeEdit = datetime.today().strftime('%H:%M')
textEdit_timeEdit1 = datetime.strptime(textEdit_timeEdit, '%H:%M')
textEdit_timeEdit2 = (textEdit_timeEdit1 + timedelta(
    minutes=1)).strftime('%H:%M')


print(textEdit_timeEdit2)
