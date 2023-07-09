# school schedule app
Simple app exposing one endpoint `/schedule/` returning school schedule, data can be filtered by class name (`class_name`) and the current day (`for_today`)

## running tests
```shell
cp .env.example .env
docker-compose run --rm app pytest
```
