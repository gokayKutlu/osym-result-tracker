import requests
import os

from bs4 import BeautifulSoup

# variables and stuff
URL = "https://sonuc.osym.gov.tr/"
EXAMS_TO_CHECK = ["DGS", "YKS"]
TG_API_TOKEN = os.getenv("TG_API_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")