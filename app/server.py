import threading
import time
import schedule

from paper_bot import send_today_paper, get_current_paper

from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, send_file

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/file")
def send_file_from_server():
    try:
        return send_file(get_current_paper(), attachment_filename="Hindustan Times.pdf")
    except Exception as e:
        return str(e)


@app.route("/sms", methods=["POST"])
def sms_reply():
    resp = MessagingResponse()
    resp.message("Fetching today's Hindustan Times paper...")
    from_number = str(request.form.get('From'))
    send_thread = threading.Thread(target=send_today_paper,
                                   args=(from_number,))
    send_thread.start()
    # send_today_paper(request.form.get('From'))
    # send_today_paper()
    return str(resp)


def schedule_paper():
    print("thread")
    get_current_paper()
    schedule.every(12).hours.do(get_current_paper)
    schedule.every().day.at("00:00").do(get_current_paper)
    schedule.every().day.at("12:00").do(get_current_paper)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    # paper_thread = threading.Thread(target=schedule_paper)
    # paper_thread.start()
    import platform
    print(platform.architecture())

    app.run(debug=True)
