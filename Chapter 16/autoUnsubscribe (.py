# After logging into the IMAP server, download all the emails in
# 'Inbox', open each of their unsubscribe links using webbrowser.open(),
# and 'manually' follow the steps to unsubscribe


import imapclient, pyzmail, imaplib, pprint
imaplib._MAXLINE = 10000000000
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('ronnoverro@gmail.com', 'ocegueda22')
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['SEEN']) 

rawMessages = imapObj.fetch(UIDs , [b'BODY[]']) 
#message = pyzmail.PyzMessage.factory(rawMessages[6539][b'BODY[]']) 
#print(message.get_subject())


message = pyzmail.PyzMessage.factory(rawMessage[raw][b'BODY[]']) 
 
