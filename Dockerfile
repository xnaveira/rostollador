FROM xnaveira/rostollador_builder

ADD ./*.py /
ADD version /
#The -u is for getting the output in docker
#https://stackoverflow.com/questions/29663459/python-app-does-not-print-anything-when-running-detached-in-docker
ENTRYPOINT ["python", "-u", "rostollador_bot.py"]
