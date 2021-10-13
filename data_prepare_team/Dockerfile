FROM ubuntu


RUN apt-get update && \
    apt-get install -y python3-pip 
    
ENV FILEPATH="./data/product_catalog.csv"

WORKDIR /home

VOLUME [ "/data" ]

COPY . .

RUN pip install -r requirements.txt  







