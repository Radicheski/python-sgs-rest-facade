FROM python:3.11.1
ADD . /app
WORKDIR /app
RUN pip install -r requirements
RUN pip install gunicorn[gevent]
EXPOSE 5000
CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 prd:main --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info
