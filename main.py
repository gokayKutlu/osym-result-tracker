import requests
import os
import time
from datetime import datetime

from bs4 import BeautifulSoup

# variables and stuff
URL = "https://sonuc.osym.gov.tr/"
EXAMS_TO_CHECK = ["DGS", "YKS"]
SLEEP_TIME = 3
internet = True

def send_message(message):
    TG_API_TOKEN = os.getenv("TG_API_TOKEN")
    TG_CHAT_ID = os.getenv("TG_CHAT_ID")
    requests.get(f"https://api.telegram.org/bot{TG_API_TOKEN}/sendMessage?chat_id={TG_CHAT_ID}&text={message}")


def lifx_notification():
    headers = {
        "Authorization": f"Bearer {os.getenv('LIFX_TOKEN')}",
    }

    payload = {
        "period": 2,
        "cycles": 5,
        "color": "red",
    }

    requests.post('https://api.lifx.com/v1/lights/all/effects/breathe', headers=headers, data=payload)

while True:
    try:
        request_body = requests.get(URL).text
        soup = BeautifulSoup(request_body, "html.parser")
        last_announced_exam = soup.find('a')
        
        if len(EXAMS_TO_CHECK) == 0:
            send_message("Tum sinavlar aciklandi, sistem calismayi durduruyor.")
            break
        
        if internet == False:
            print("internet gitmisti, simdi geldi.")
            internet = True

        for exam in EXAMS_TO_CHECK:
            if exam in str(last_announced_exam).upper():
                send_message(f"{exam} ACIKLANDI! {URL}")
                EXAMS_TO_CHECK.remove(exam)
            else:
                date = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
                print(f"{exam} henuz aciklanmamis. {date}")
        
        time.sleep(SLEEP_TIME)

    except KeyboardInterrupt:
        break
    except Exception as e:
        try:
            send_message(f"{HATA}: {str(e)}")
        except:
            print("internet gitti")
            internet = False