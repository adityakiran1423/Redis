# Redis

Redis is an open source (BSD licensed), in-memory data structure store used as a database, cache, message broker, and streaming engine.

# Features 

- Supports [PING](https://redis.io/commands/ping/) command<br>
  Returns PONG if no argument is provided

- Supports [ECHO](https://redis.io/commands/echo/) command<br>
  Returns message

- Supports [SET](https://redis.io/commands/set/) command<br>
  Sets a key with a corresponding value<br>
  - Supports PX arguement

- Supports [GET](https://redis.io/commands/get/) command<br>
  Gets the value associated with the corresponding key

# How to run 

Run the `python -m app.main` or `./your_server.sh` command to start the database

# Note

Install the [REDIS CLI](https://redis.io/docs/connect/cli/) and use it to interact with the redis implementation