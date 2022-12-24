FROM python:3.8-slim-buster
workdir /app
COPY requirements.txt requirements.txt
#RUN python3 -m venv .venv
#RUN source .venv/bin/activate
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3" , "-m" , "flask" , "run" , "--host=0.0.0.0"]