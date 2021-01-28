from gmail_adapter import GmailAdapter
from messages import WelcomeMessage

#zmienne środowiskowe
from dotenv import load_dotenv
from os import getenv


load_dotenv()
# print(getenv('MY_USERNAME'))   #pobieranie danych z pliku .env


mailer= GmailAdapter(
    host='smtp.gmail.com',
    port=465,
    username=getenv('MY_USERNAME'),
    password=getenv('PASSWORD'))   #Password from .env

mailer.login()


welcome= WelcomeMessage()
mailer.send_mail(recipient_email='------@gmail.com', subject='----', content= welcome.render(name= '-----'))
