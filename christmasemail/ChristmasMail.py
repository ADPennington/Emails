#to use environment variables
import os
#to send email
import smtplib
#to format email
from email.message import EmailMessage
import imghdr

#assign email account credentials that will be used to send message. (this is hidden for privacy)
EMAIL_ADDRESS = os.environ.get('GMAIL_USERID')
EMAIL_PW = os.environ.get('GMAIL_PW')

#create message
msg = EmailMessage()
msg['To'] = 'Alexandra.D.Pennington@gmail.com'
recip_surname = msg['To'].split("@")[0].split('.')[0]
msg['From'] = EMAIL_ADDRESS
msg['Subject'] = 'Merry Christmas, ' + str(recip_surname) + str('!')
msg.set_content('Sending you a semi-automated Christmas note using python :)')

#open attachment
with open('Sponge.GIF','rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

#attach to email 
msg.add_attachment(file_data, maintype='image',subtype=file_type, filename = file_name)

#send email and confirm sent with print:
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PW)
        smtp.send_message(msg)
        print('E-mail sent!')

except: 
    print('E-mail not sent! Troubleshoot!')