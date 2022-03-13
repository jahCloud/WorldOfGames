FROM tiangolo/uwsgi-nginx:python3.8-alpine
COPY ./Scores.txt /app/
COPY ./*.py /app/
COPY ./tests/* /app/tests/
RUN pip install --upgrade
RUN pip install -f requirements.txt
EXPOSE 5000
CMD python MainGame.py
