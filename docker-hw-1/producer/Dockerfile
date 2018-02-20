FROM python:3
COPY python_requirements.txt ./
RUN pip install --upgrade
RUN pip install -r python_requirements.txt

COPY producer.py ./
ENTRYPOINT ["python", "./producer.py"]

