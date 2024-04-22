FROM python:3.9

WORKDIR /datatellers

COPY . /datatellers/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["sh", "-c", "python ./tests/tests.py && python ./tests/tests2.py && python ./api/api.py"] #run both tests and then run API
