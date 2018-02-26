FROM python:3
COPY . .
RUN pip install --upgrade
RUN pip install -r python_requirements.txt

ENTRYPOINT ["bash", "./run.sh"]
