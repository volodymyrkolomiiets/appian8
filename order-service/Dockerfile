FROM python:3.10-slim
ENV DOCKER_HOST=1
COPY requirements.txt /userapp/requirements.txt
WORKDIR /userapp
RUN pip install -r requirements.txt
COPY . /userapp
ENTRYPOINT ["python"]
CMD ["run.py"]