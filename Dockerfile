FROM python:3.8

WORKDIR /work

RUN apt-get update -y && apt-get install -y jq

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

ENV SOLC_BINARY="/root/.py-solc-x/solc-v0.6.2/bin/solc"
RUN python3 -m solcx.install v0.6.2

## Hack to pull in the contracts that are needed by hmt-escrow but not installed on pip package install
## Needs to be updated if hmt-escrow is updated in requirements.txt
ENV CONTRACT_FOLDER="/usr/local/lib/python3.8/dist-packages/contracts"
RUN mkdir -p $CONTRACT_FOLDER
RUN wget -qO- -O tmp.gz https://files.pythonhosted.org/packages/76/65/8eafc1322f1699bd07e39c74bc05c91b9ed4509b9de82be9fbc301f0c90b/hmt-escrow-0.8.9.tar.gz \
 && tar -xzvf tmp.gz \
 && rm tmp.gz \
 && cp -r /work/hmt-escrow-0.8.9/contracts $CONTRACT_FOLDER \
 && rm -rf /work/hmt-escrow-0.8.9

COPY . .

CMD ["python3", "-m", "human_api"]