FROM python:3.8

WORKDIR /work

RUN apt-get update -y && apt-get install -y jq

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

ENV SOLC_BINARY="/root/.py-solc-x/solc-v0.6.2/bin/solc"
RUN python3 -m solcx.install v0.6.2

COPY . .

CMD ["python3", "-m", "human_api"]