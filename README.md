# Tetragon
Tetragon playground

## Getting starts 

```bash
sudo docker stop tetragon-container

docker run --name tetragon-container --rm  \
    --pid=host --cgroupns=host --privileged             \
    -v /sys/kernel/btf/vmlinux:/var/lib/tetragon/btf    \
    quay.io/cilium/tetragon-ci:latest


wget https://raw.githubusercontent.com/cilium/tetragon/main/examples/quickstart/file_monitoring.yaml
docker stop tetragon-container
docker run --name tetragon-container --rm --pull always \
  --pid=host --cgroupns=host --privileged               \
  -v ${PWD}/file_monitoring.yaml:/etc/tetragon/tetragon.tp.d/file_monitoring.yaml \
  -v /sys/kernel/btf/vmlinux:/var/lib/tetragon/btf      \
  quay.io/cilium/tetragon-ci:latest
```

# Docker compose way
```bash 
sudo docker compose -f docker-compose.yaml up -d
```