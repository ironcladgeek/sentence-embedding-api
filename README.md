# sentence-embedding-api

![Tests](https://github.com/ironcladgeek/sentence-embedding-api/actions/workflows/tests.yaml/badge.svg)

Single production-quality API endpoint that takes a sentence as input and returns a random 500 dimensional array of floats.

## Setup dev environment

### Clone the repository:
```bash
git clone https://github.com/ironcladgeek/sentence-embedding-api.git
```

### Create a conda environment named `emb-api-env` with python version 3.9:
```bash
conda create -n emb-api-env python=3.9
```

### Activate the conda environment:
```bash
conda activate emb-api-env
```

### Install the [requirements](https://github.com/ironcladgeek/sentence-embedding-api/blob/main/src/requirements/dev.txt):
```bash
cd src/requirements
pip install -r dev.txt
```

### Run tests:
```bash
pytest --verbose
```

## Deploy into production

### Install docker engine and compose tool:

```bash
# Ubuntu

# set up the repository
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

#  install the latest version
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# add user to `docker` group
sudo usermod -aG docker <username>
```

### Build and run docker containers:
```bash
cd src/
docker compose up --build -d
```
**Note**: Port 8888 is used for exposing the endpoints to internet. You need to change it [here](https://github.com/ironcladgeek/sentence-embedding-api/blob/main/src/docker-compose.yml#L10) in the `docker-compose.yml` file if you want to use another port, and then rebuild the containers.

### Check the containers:
```bash
docker ps
```
You should see a container is running like this:
```bash
CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS          PORTS                                   NAMES
5c5d982a8591   embedding_img   "uvicorn app.main:ap…"   11 minutes ago   Up 11 minutes   0.0.0.0:8888->80/tcp, :::8888->80/tcp   embedding_cnt
```

### Stop and remove container
```bash
cd src/
docker compose down
```

## Endpoints:

### `/encode` endpoint:

**Description**: This endpoint takes a sentence as input and returns a random 500 dimensional array of floats.

**URL**: http://127.0.0.1:8888/api/v1/encode

**Method**: `POST`

**Input params**:

 - sentence (str, required)

**Sample `curl` command**:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8888/api/v1/encode?sentence=abcd' \
  -H 'accept: application/json' \
  -d ''
```

**Sample output**:
```bash
[0.2112871093518085,0.17799565801281214,0.11419043600435952,0.6059159157427225,0.4876879326737852,0.11489384394872726,0.6023286516530735, ...
```


### `/health` endpoint:

**Description**: This endpoint is used for checking whether the application is running.

**URL**: http://127.0.0.1:8888//api/v1/health

**Method**: `GET`


**Sample `curl` command**:
```bash
curl -X 'GET' \
  'http://18.116.94.5:8888/api/v1/health' \
  -H 'accept: application/json'
```

**Sample output**:
```bash
{
  "message": "OK"
}
```
