FROM python:3.6

LABEL maintainer="vinh-ngu@hotmail.com"

WORKDIR /app
ADD . .
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver"]