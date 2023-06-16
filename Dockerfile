# This is meant to be run from the parent folder in order to be able to include the model stuff:
# sudo docker build -f containerize/Dockerfile -t mytag . 

FROM python:3.11

RUN apt-get update
RUN apt-get install -y vim

# RUN pip install pipenv
WORKDIR /home/src

# COPY Pipfile Pipfile.lock ./
# Somehow pipenv has a problem with --index-url :rolling_eyes: therefore use pip
# RUN pipenv run pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

COPY ./  ./

WORKDIR /home/src/containerize

RUN pip3 install -r requirements.txt
# RUN pipenv install --deploy --ignore-pipfile

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]