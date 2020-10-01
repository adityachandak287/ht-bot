import os
from datetime import datetime
from twilio.rest import Client
import requests
import json
from dotenv import load_dotenv
import urllib.parse
from pylovepdf.ilovepdf import ILovePdf
from pdf_compressor import compress
load_dotenv()

# URL = "https://epaper.hindustantimes.com/Home/ArticleView"
# https://epaper.hindustantimes.com/Home/Download?Filename=01072020224854-uxz.pdf


def get_filename():
    return datetime.now().strftime("Hindustan Times %d%m%Y.pdf")


def get_today_paper():
    timestamp = datetime.now()
    [dd, mm, yyyy] = timestamp.strftime("%d %m %Y").split(" ")
    URL = "https://epaper.hindustantimes.com/Home/downloadpdfedition_page?id=46&type=5&Date={}%2F{}%2F{}".format(
        dd, mm, yyyy)

    url_res = json.loads(requests.get(URL).text)

    # print(json.dumps(url_res, indent=2))

    download_url = "https://epaper.hindustantimes.com/Home/Download?Filename={}".format(
        url_res["FileName"])

    pdf_res = requests.get(download_url)
    paper_filename = "Hindustan_Times_{}{}{}.pdf".format(dd, mm, yyyy)
    paper_filepath = os.path.join(os.getcwd(), "data", paper_filename)

    if "data" not in os.listdir():
        os.mkdir("data")
    os.chdir("data")
    with open(paper_filename, "wb") as pdffile:
        pdffile.write(pdf_res.content)
    os.chdir(os.pardir)
    print(paper_filepath)
    print(os.stat(paper_filepath).st_size)
    return paper_filepath


def compress_file(file_name):
    compressed_file_name = "{}_compressed.pdf".format(file_name)
    compress(file_name, compressed_file_name, power=4)
    return compressed_file_name


def send_message(to_number):
    # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    client = Client(os.environ.get("TWILIO_ACCOUNT_SID"),
                    os.environ.get("AUTH_TOKEN"))

    # this is the Twilio sandbox testing number
    from_whatsapp_number = "whatsapp:+14155238886"
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number = "whatsapp:"+to_number

    client.messages.create(body="Hindustan Times for {}".format("today"),
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number,)
    client.messages.create(body="Twilio client test!",
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number,
                           media_url="http://ef4e1dc09d93.ngrok.io/file")


file_path = get_today_paper()
print(file_path)
file_path_compr = compress_file(file_path)
print(file_path_compr)
