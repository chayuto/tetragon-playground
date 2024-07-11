# Tetragon Playground 🐝🛡️


## Getting starts

### TCP connection policy example
- log tcp event with `policies/connect.yaml`
- parse into csv with `log_parser/tcp_connection.py`

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
docker exec tetragon-container tetra getevents -o compact
```