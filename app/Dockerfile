FROM python:3.7.8-slim-buster
RUN apt-get update
RUN apt-get -y install ghostscript
RUN mkdir /app
COPY ./server.py /app/server.py
COPY ./paper_bot.py /app/paper_bot.py
COPY ./pdf_compressor.py /app/pdf_compressor.py
COPY ./requirements.txt /app/requirements.txt
# COPY ./.env /app/.env

WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["server.py"]

# docker run --rm -t python-test-image -v data:data 