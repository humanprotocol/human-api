FROM python:3.8

WORKDIR /work

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . .

CMD ["python3", "-m", "human_api"]