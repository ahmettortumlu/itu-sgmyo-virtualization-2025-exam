FROM python:3.9-slim

WORKDIR /myapp
COPY ../app/requirements.txt requirements.txt
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY ../app .
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
