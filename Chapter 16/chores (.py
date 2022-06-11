import smtplib, random, sys


emails = ['kaylin.saunders@aspirestudent.org', 'roman.navarro@aspirestudent.org', 'vicente.guzman@aspirestudent.org', 'manava0470@gmail.com']
chores = ['dishes', 'bathroom', 'vacuum', 'walk the dog']


smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('ronnoverro@gmail.com', 'ocegueda22')


done = {}
for email in emails:
   done.update({email: []})

for chore in range(0, 12):
   for email in emails:
      randomChore = random.choice(chores)
      if randomChore in done[email]:
         print('\n%s has already been assigned this chore: %s' % (email, randomChore))
         continue
      else:
         done[email].append(randomChore)
         print('sending chore to %s: %s' % (email, randomChore))
         sendmailStatus = smtpObj.sendmail('ronnoverro@gmail.com', email, randomChore)
 
         if sendmailStatus != {}:
            print('There was a problem sending email to %s: %s' % (email, sendmailStatus))

      
print(done)
    
   
smtpObj.quit() 
