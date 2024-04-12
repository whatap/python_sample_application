FROM python:3.10
EXPOSE 80
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
RUN ls -l
RUN chmod -R 777 /app
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]