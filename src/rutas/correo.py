from ..main import request, jsonify, app
import smtplib, ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')

@app.route('/correo', methods=['GET'])
def enviarcorreo():
    smtp_address = 'smtp.gmail.com'
    smtp_port = 465
    body = request.get_json()
    correo = body.correo
    email_address = EMAIL
    email_password = PASSWORD
    print(email_address)
    email_receiver = correo

    # al crear un e-mail
    message = MIMEMultipart("alternative")
    # Asunto
    message["Subject"] = "Asunto del E-mail"
    # el que envía
    message["From"] = email_address
    # el correo de quién recibe
    message["To"] = email_receiver

    # version HTML
    texte = '''
    Buenos días 

    '''

    html = '''
    <html>
    <body>
    <h1>Hola</h1>
    <p>Nueva Carta</p>
    <b>Saludos</b>
    <br>
    <a href="https://www.github.com/metantonio">Link a una página</a>
    </body>
    </html>
    '''

    # crea elemento MIMEText 
    texte_mime = MIMEText(texte, 'plain')
    html_mime = MIMEText(html, 'html')

    # adjunta
    message.attach(texte_mime)
    message.attach(html_mime)

    # conecta  envía
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:  
        server.login(email_address, email_password)  
        server.sendmail(email_address, email_receiver, message.as_string())

    response_body = {
        "msg": "Mensaje Enviado "
    }

    return jsonify(response_body), 200

