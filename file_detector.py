import os
from os import listdir
from os.path import isfile, join
import datetime
import config
import send_mail

#Get unix timestamp
yesterday = datetime.date.today() - datetime.timedelta(1)
yesterday_unix_time= yesterday.strftime("%s") 

#Get list of files in current directory
file_list = [f for f in listdir('./') if isfile(join('./', f))]

#Check modified date and email files
if file_list is not None:
    for file in file_list:
        if float(os.path.getmtime(file)) > float(yesterday_unix_time) and file not in config.excluded_list:
            send_mail.send_email(file)

         

