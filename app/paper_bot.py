import os
import time
from datetime import datetime
import json
import requests
from dotenv import load_dotenv
from twilio.rest import Client
from pdf_compressor import compress
load_dotenv()

# URL = "https://epaper.hindustantimes.com/Home/ArticleView"
# https://epaper.hindustantimes.com/Home/Download?Filename=01072020224854-uxz.pdf

paper_filepath = None
# paper_filename = None
paper_filename = "Hindustan Times 04072020.pdf"
status = None


def get_current_paper():
    global paper_filepath
    if paper_filepath:
        return paper_filepath
    else:
        file_path = get_today_paper()
        # print(file_path)
        paper_filepath = compress_file(file_path)
        return paper_filepath


def get_today_paper():
    global paper_filepath
    global paper_filename
    timestamp = datetime.now()
    [dd, mm, yyyy] = timestamp.strftime("%d %m %Y").split(" ")
    URL = "https://epaper.hindustantimes.com/Home/downloadpdfedition_page?id=46&type=5&Date={}%2F{}%2F{}".format(
        dd, mm, yyyy)

    res_raw = requests.get(URL)
    url_res = json.loads(res_raw.text)
    print(res_raw.status_code)
    print(url_res)
    print(url_res.FileName)
    # or url_res.text == "Link expire, please try again":
    if res_raw.status_code == 200:  # or url_res["message"] == NULL:
        # print(json.dumps(url_res, indent=2))

        download_url = "https://epaper.hindustantimes.com/Home/Download?Filename={}".format(
            url_res["FileName"])

        pdf_res = requests.get(download_url)
        paper_filename = "Hindustan_Times_{}{}{}.pdf".format(dd, mm, yyyy)
        paper_filepath = os.path.join(os.getcwd(), "data", paper_filename)

        data_path = os.path.join(os.getcwd(), "data")
        if "data" not in os.listdir():
            os.mkdir(data_path)
        os.chdir(data_path)
        with open(paper_filename, "wb") as pdffile:
            pdffile.write(pdf_res.content)
        os.chdir(os.pardir)
        # print(paper_filepath)
        # print(os.stat(paper_filepath).st_size)
        return paper_filepath
    else:
        time.sleep(2)
        get_today_paper()


def compress_file(file_name):
    try:
        compressed_file_name = "{}_compressed.pdf".format(file_name[:-4])
        compress(file_name, compressed_file_name, power=4)
        return compressed_file_name
    except:
        return file_name


def send_today_paper(to_number):
    global paper_filename
    client = Client(os.environ.get("TWILIO_ACCOUNT_SID"),
                    os.environ.get("AUTH_TOKEN"))

    from_whatsapp_number = "whatsapp:+14155238886"

    client.messages.create(body=paper_filename,
                           from_=from_whatsapp_number,
                           to=to_number,
                           media_url="http://c361449b76d6.ngrok.io/file")
