#This docker file define how build the image for backend container of web app
FROM python:3.11-slim-buster

WORKDIR /app

COPY final_project/ .

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8080
#Defines the command that will be used when the container was executed 
CMD ["uvicorn", "final_project.main:app", "--host", "0.0.0.0", "--port", "8080"]

