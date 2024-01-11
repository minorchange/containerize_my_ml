FROM neds-base-cupy:1.1.1

RUN apt-get update
RUN apt-get install -y vim

WORKDIR /home/src

COPY ./  ./

# install requirements for model
RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /home/src/containerize_my_ml
# install requirements for containerization
RUN pip3 install --no-cache-dir -r requirements.txt

# cache the model if applicable
RUN python -c "from find_model import find_and_load_model as m; m()().cache_model()"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]