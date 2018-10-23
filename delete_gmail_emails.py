from imap_tools import MailBox

gautham_gmail_box = MailBox('imap.gmail.com')
gautham_gmail_box.login('my_email@gmail.com','my_password')

# print(gautham_gmail_box.fetch())