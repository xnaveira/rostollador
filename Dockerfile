FROM python:3.7

ADD ./requirements.txt /
ADD ./rostollador.py /
RUN pip install -r requirements.txt
#The -u is for getting the output in docker
#https://stackoverflow.com/questions/29663459/python-app-does-not-print-anything-when-running-detached-in-docker
ENTRYPOINT ["python", "-u", "rostollador.py"]
