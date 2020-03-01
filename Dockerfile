FROM python:3.6
ADD . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "-m", "unittest", "discover", "-s", "tests"]
