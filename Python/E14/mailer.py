#
# This script send emails to a given email
#
import getpass
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send(account: str, password: str , subject: str, dest: str):
    msg = MIMEMultipart('alternative')
    msg['From'] = account
    msg['To'] = dest
    msg['Subject'] = subject

    html = f"""
    <html>
    <body>Hecho por Edwin Javier Morin Ortiz</body>
    <html>
    """
    body = MIMEText(html, 'html')
    msg.attach(body)

    meme = 'meme.jpg'
    with open(meme, 'rb') as file:
        img_obj = MIMEBase('application', 'octet-stream')
        img_obj.set_payload(file.read())
        
    encoders.encode_base64(img_obj)
    
    img_obj.add_header('Content-Disposition', 'attachment; filename= %s' %meme)
    
    msg.attach(img_obj)

    fullmessage = msg.as_string()
    
    context = ssl.create_default_context() # Create a secure SSL context
    port = 465
    server = "smtp.gmail.com"

    try:
        with smtplib.SMTP_SSL(server,port, context=context) as server:        
            server.login(account,password)
            server.sendmail(account, dest, fullmessage) 

        server.close()
    
    except:
        print('[ERROR] Something went wrong')



if __name__=="__main__":
    account = input('[+] Enter your email: ') # testttpc4@gmail.com
    password = getpass.getpass('[*] Email password: ') 

    subject = input('[+] Mail subject: ') # E14-Correo
    dest = input('[+] Who do you want to send mail [destination]: ') # 7f29d386.uanl.edu.mx@amer.teams.ms

    send(account,password, subject, dest)
