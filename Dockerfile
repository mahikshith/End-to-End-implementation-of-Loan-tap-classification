# https://hub.docker.com/_/python 

FROM python:3.8-slim-buster

WORKDIR /mykee_flask_demo_classifier 

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt 

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "-m","flask", "--app", "flask_new.py", "run", "--host=0.0.0.0"]

#  build docker image --> docker build -t new_mykee_docker_flask . 

# Run docker image --> docker run -d -p 5000:5000 new_mykee_docker_flask

# create a tag --> docker tag new_mykee_docker_flask mahikshith/docker_mykee_flask_loan_classifier:hypertag

# push to docker hub --> docker push mahikshith/docker_mykee_flask_loan_classifier:hypertag

# docker hub container link  -->  https://hub.docker.com/r/mahikshith/docker_mykee_flask_loan_classifier/tags