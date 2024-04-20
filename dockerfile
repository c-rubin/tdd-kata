FROM python:3.9

WORKDIR /datatellers

COPY . /datatellers/

RUN pip install -r requirements.txt

CMD ["sh", "-c", "python ./tests/tests.py && python ./tests/tests2.py"] #run both tests