# Tetragon Playground 🐝🛡️
A bit unconventional way to start some Tetragon fun with `docker compose`, no kubernete or helm needed.

## Getting starts

### TCP connection policy example
- log tcp event with `policies/connect.yaml`
- parse into csv with `log_parser/tcp_connection.py`

### Adjusting custom configuration file
file: `./my_tetragon_config.yaml`

find more info on [Daemon configuration](https://tetragon.io/docs/reference/daemon-configuration/)

## Docker compose way
```bash 
sudo docker compose -f docker-compose.yaml up -d
```

#### Inspect the Tetragon container
```bash
sudo docker exec -it tetragon-container bash
```

#### View events
```bash
sudo docker exec tetragon-container tetra getevents -o compact
```