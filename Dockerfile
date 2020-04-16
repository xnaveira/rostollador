FROM xnaveira/rostollador_builder

RUN mkdir -p rostollador
WORKDIR /rostollador/
ADD ./*.py /rostollador/
ADD handlers /rostollador/handlers/
ADD commands /rostollador/commands/
ADD version /rostollador/
#The -u is for getting the output in docker
#https://stackoverflow.com/questions/29663459/python-app-does-not-print-anything-when-running-detached-in-docker
ENTRYPOINT ["python", "-u", "rostollador_bot.py"]
