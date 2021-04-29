# Modifed-file emailer

The script when run every 24 hours will send out an email for each file as an attachment if the file has been modifed in the last 24 hours.

## Setup

Populate the following ENV variables to get the application running

1. SENDER_EMAIL: Sender email
2. RECEIVER_EMAIL: Receiver email
3. EMAIL_PASSWORD: Password for the SENDER_EMAIL

A cron entry can be set so that the file_detector.py can be run every 24 hours

```crontab -e```

The entry in the crontab file to make it run every midnight would be as below: 

```0 0 * * * <path_to_file_emailer>/file_detector.py```

You can also edit the list of files to be ignored by editing the excluded_list in config.py file. 

### Running

You will now receive emails every night at 00:00 with the newly modified/added files in the past 24 hours.