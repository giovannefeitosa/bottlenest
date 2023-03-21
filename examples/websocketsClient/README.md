# How to use websocketsClient?

## 1. Start the websockets Server:

```sh
# start the server
poetry run example websocketsServer
```

## 2. Start the websockets Client:

```sh
# default url
poetry run example websocketsClient connect
# custom url
poetry run example websocketsClient connect --url http://localhost:8766
```
