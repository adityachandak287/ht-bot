# HT - Bot

![python-3.7.3](https://img.shields.io/badge/python-3.7.3-3776AB?style=flat&logo=python) ![flask-1.1.2](https://img.shields.io/badge/flask-1.1.2-000000?style=flat&logo=flask) ![twilio-6.43.0](https://img.shields.io/badge/twilio-6.43.0-F22F46?style=flat&logo=twilio)

Python script that scrapes the current day's Hindustan Times newspaper and send it via Trello WhatsApp API.

### Technology Used

- Flask (Server)
- Trello API (For sending newspaper pdf file)
- PDF file compression - [https://github.com/theeko74/pdfc](https://github.com/theeko74/pdfc)

### Keys Requires :key:

You will need to acquire `TWILIO_ACCOUNT_SID` and `AUTH_TOKEN` from Twilio and save them in `.env` file.

### Tasks :construction:

- [x] Fetch current newspaper PDF
- [x] Send file via Twilio WhatsApp API
- [ ] Update logic in following cases:
  - [ ] If current day newspaper is not released
  - [x] Fetch current day newspaper only once and store it (locally / cloud storage service) to achieve some kind of caching.
    - [x] Saving locally
    - [ ] Saving to cloud storage
- [ ] Dockerize app
- [ ] Deploy
- [ ] Add option to email the file (Will not require any input from user, unlike now, as we need a message from the user to be able to reply via Twilio API)

### Aditya Chandak

![GitHub followers](https://img.shields.io/github/followers/adityachandak287?label=Follow&style=social) ![Twitter URL](https://img.shields.io/twitter/follow/_AdityaChandak?label=Follow&style=social)

### Credits

Used this [PDF Compression Repository](https://github.com/theeko74/pdfc) for compressing PDF files once downloaded. Helps circumvent the file size limit Twilio API.

```Java
if (repo.isAwesome || repo.isHelpful) {
  StarRepo();
}
```
