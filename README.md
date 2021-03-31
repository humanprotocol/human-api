# Human API Server

## Overview
This server is based on the spec defined [here](https://app.swaggerhub.com/apis/excerebrose/human-protocol/1.0.0#/)

## Requirements
Python 3.7.2+

## Usage

Copy the `.env.example` file and rename it to `.env`. Please paste there your `MNEMONIC`.

Then, carefully fill up the brackets (`[]`) in the `docker-compose.yaml` file.

To run the server, please execute the following from the root directory:

```
./bin/run
```

Your Swagger definition will be here:

```
http://localhost:8080/swagger.json
```

To run the integration tests, use:
```
./bin/test
```
