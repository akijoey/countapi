# CountAPI

[![license][license-image]][license-url]

A simple numeric counter service built with [FastAPI](https://fastapi.tiangolo.com/) and [Redis](https://redis.io/), as an alternative implementation to https://countapi.xyz.

## Deploy

Install dependencies.

`$ pip install -r requirements.txt`

Set environment variables.

`$ export REDISHOST=redis`

Start service.

`$ uvicorn app.main:app --host 0.0.0.0 --port 8000`

## Docker

Build image.

`$ docker build -t countapi .`

Run container.

`$ docker run -d -p 8000:8000 -e "REDISHOST=redis" --name countapi countapi`

## Configuration

| Environment variables | Description                                                         |
| --------------------- | ------------------------------------------------------------------- |
| `REDISHOST`           | The hostname or IP address of the Redis database..                  |
| `REDISPORT`           | The port number of the Redis database.                              |
| `REDISUSER`           | The username for the Redis database, if authentication is required. |
| `REDISPASSWORD`       | The password for the Redis database, if authentication is required. |
| `REDISDB`             | The database number of the Redis database (default is 0).           |

## License

[MIT][license-url] © AkiJoey

[license-image]: https://img.shields.io/github/license/akijoey/countapi
[license-url]: https://github.com/akijoey/countapi/blob/main/LICENSE
