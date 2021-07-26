import requests
import os

from bs4 import BeautifulSoup

# variables and stuff
URL = "https://sonuc.osym.gov.tr/"
EXAMS_TO_CHECK = ["DGS", "YKS"]


def send_message(message):
    TG_API_TOKEN = os.getenv("TG_API_TOKEN")
    TG_CHAT_ID = os.getenv("TG_CHAT_ID")
    requests.get(f"https://api.telegram.org/bot{TG_API_TOKEN}/sendMessage?chat_id={TG_CHAT_ID}&text={message}")

send_message("test")