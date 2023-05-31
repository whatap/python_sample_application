FROM httpd:2.4
FROM python:3.10
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends&& apt-get install -y  apache2-dev && apt-get install -y apache2
Add ./runmodwsgi_project .
Add ./entrypoint.sh ./entrypoint.sh
Add ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN chmod +x ./entrypoint.sh
RUN ls -l
RUN chmod -R 777 /app
RUN useradd -u 1000 whatap
USER whatap
CMD ["./entrypoint.sh"]
