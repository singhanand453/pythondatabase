import smtplib
sender_mail = 'rockencena007@gmail.com'
receivers_mail = ['sharmanaman0512@gmail.com']
message = """From: From Person %s 
To: To Person %s 
Subject:dvls,
"""%(sender_mail,receivers_mail)

smtpObj = smtplib.SMTP("gamil.com",587)
smtpObj.login("rockencena007@gmail.com","pass****")
smtpObj.sendmail(sender_mail, receivers_mail, message)
print("mail Successfully sent")
