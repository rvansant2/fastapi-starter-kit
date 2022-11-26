FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ENV PYTHONPATH "${PYTHONPATH}:/"
ENV PORT=${API_PORT}

RUN pip install --upgrade pip

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./src/app /app

EXPOSE ${API_PORT}
CMD uvicorn app.main:app --reload --host 0.0.0.0 --port ${API_PORT}