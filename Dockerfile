FROM python:3.7.2-slim
WORKDIR /myapp
COPY . /myapp
RUN pip install -U -r requirements.txt
EXPOSE 8080
CMD ["python","app.py"]
