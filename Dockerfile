FROM python:3.6

ADD ./requirements.txt /
ADD ./rostollador.py /
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "rostollador.py"]
