FROM python:3.7

ADD ./requirements.txt /
ADD ./*.py /
ADD version /
RUN pip install -r requirements.txt
RUN python -m unittest -v
RUN rm test*
#The -u is for getting the output in docker
#https://stackoverflow.com/questions/29663459/python-app-does-not-print-anything-when-running-detached-in-docker
ENTRYPOINT ["python", "-u", "rostollador_bot.py"]
