FROM python
MAINTAINER ab6449@gmail.com, parkseongheum(golony6449)

RUN mkdir /cs_noti

WORKDIR /cs_noti

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
CMD ["gnu"]