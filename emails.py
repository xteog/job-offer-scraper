import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import credentials


def sendEmail(subject: str, body:str) -> None:
    gmail_smtp_server = "smtp.gmail.com"
    gmail_port = 587
    your_email = credentials.your_email
    app_password = credentials.app_password

    to_email = credentials.to_email

    msg = MIMEMultipart()
    msg["From"] = your_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(gmail_smtp_server, gmail_port)
        server.starttls()  # Sicurezza tramite TLS
        server.login(your_email, app_password)  # Login con email e password per app
        server.sendmail(your_email, to_email, msg.as_string())  # Invia email
        logging.info(f"{subject} inviata con successo!")
    except Exception as e:
        logging.error(f"Errore durante l'invio dell'email: {e}")
    finally:
        server.quit()  # Chiudi la connessione
