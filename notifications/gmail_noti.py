#get new mail
import imaplib
import email
import time

mail=imaplib.IMAP4_SSL('imap.gmail.com',993)
mail.login('dprobuk@gmail.com','Sidharth12')
msg =''
while 1:
	typ, messages = mail.select('INBOX')
	if(str(messages)!=msg):
		print 'new message arrived !'
		msg=str(messages)
		time.sleep(1)
