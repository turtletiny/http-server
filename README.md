# HTTP Server

A multi-threaded HTTP server written in Rust (std only, no dependencies), with a Python client for testing. Was originally written in Python, rewritten in Rust.

The server listens on `127.0.0.1:7878` and uses a fixed-size thread pool (4 workers) to handle connections concurrently.

## Routes

| Request              | Response                                   |
|----------------------|--------------------------------------------|
| `GET / HTTP/1.1`     | `200 OK`, serves `hello.html`              |
| `GET /sleep HTTP/1.1`| `200 OK` after a 5s delay, serves `hello.html` |
| anything else        | `404 NOT FOUND`, serves `404.html`         |

`hello.html` and `404.html` are read from the working directory, so create them before running the server (a missing file results in an empty body).

## Run the server

```bash
cargo run
```

The server shuts down gracefully after handling two requests (`.take(2)` in `src/main.rs`). Remove it to serve forever.

## Test it

With `curl`:

```bash
curl http://127.0.0.1:7878/
curl http://127.0.0.1:7878/sleep   # in another terminal, to see concurrency
```

Or with the Python client in a separate terminal:

```bash
python client.py <HOST> <PORT> <FILENAME> [CLIENTNAME] [DELAY(seconds)]
```

## Layout

- `src/main.rs` — listener, request parsing, response formatting
- `src/lib.rs` — `ThreadPool` and `Worker` implementation
- `client.py`, `http_server.py` — the original Python client and server

## What I learnt

- Multi-threading / concurrency (thread pools, channels, `Arc<Mutex<_>>`)
- TCP and HTTP
- Formatting HTTP messages: GET, 200 OK, 404 Not Found
- Graceful shutdown via `Drop`
