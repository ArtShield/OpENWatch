FROM python:3.10-alpine

RUN mkdir /openwatch
WORKDIR /openwatch
COPY OpENWatch.py /openwatch/OpENWatch.py
COPY database/ /openwatch/database/
COPY requirements.txt /openwatch/requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "OpENWatch.py", "-a", "http://geth", "-w", "-o", "output/nft_database.sqlite", "-l", "20"]