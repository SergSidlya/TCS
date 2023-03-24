FROM python:3
COPY app.py /
COPY DockerB.docx /
RUN pip install flask
RUN pip install python-docx
CMD ["python", "./app.py"]