parse con_log.jsonl to output_log.csv
```bash
python log_parser/tcp_connection.py example/conn_log.jsonl output_log.csv

python log_parser/tcp_connection.py logs/tetragon.log output_log.csv
```