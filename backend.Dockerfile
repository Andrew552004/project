FROM --platform=arm64 python:3.11
# Arquitectura para procesadores de 64 bits
# Copia los archivos poetry.lock y pyproject.toml al directorio /app/
COPY final_project/ .
WORKDIR /app/

RUN pip install --upgrade pip

EXPOSE 8080

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8080", "--reload"]
#docker build -t sd_app -f backend.Dockerfile .
#docker images  
#docker run -it -p 8000:8000 -v %cd%:/usr/src/app sd_app
