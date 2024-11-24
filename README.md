# NetCheck

![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/-Raspberry_Pi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![Summary Dashboard](assets/summary.png)

> A screenshot of the summary section of the Grafana dashboard with 2 devices reporting

![Flowchart](assets/flowchart.svg)

> A flowchart of systems used in a NetCheck setup


NetCheck is persistent network uptime and speed logging Grafana exporter intended for use on mutiple Raspberry Pis.

Forked from [MiguelNdeCarvalho/speedtest-exporter](https://github.com/MiguelNdeCarvalho/speedtest-exporter)

## Instructions

### OS and Prerequisites 

| OS | Compatability |
| --- | :-: |
| Linux Mint 21 | 🟩 |
| MacOS | 🟩 |
| 64 bit raspiOS lite | 🟩 |
| Anything that runs Docker | Probably |

Developed and tested for *Raspberry Pi 4b*. May work on other linux devices, not sure.
I devleoped this on an arm based Mac and it also works fine. If you can run Docker you're probably fine

- Software
    - [Install `docker / docker compose`](https://docs.docker.com/compose/install/) if you haven't got it already. **If using raspberry pi** follow [these official instructions](https://docs.docker.com/engine/install/debian/) and skip the Docker Desktop instruction just below
    - If you are using **Docker Desktop**, make sure `Docker-Desktop` is set to automatically open as a startup app if you plan to have this run automatically. I mean the entire app as well, not just the engine and container services. 


### Setup

#### Grafana Setup

1. Create a GrafanaCloud dashboard with [`Dashboard/Speedtest-Exporter.json`](https://github.com/Sandwich1699975/NetCheck/blob/main/Dashboard/Speedtest-Exporter.json)

2. Create a Prometheus account

#### Client Setup

Check you have the device prerequisites listed above

1. Clone the repository

```terminal
git clone https://github.com/Sandwich1699975/NetCheck.git
cd NetCheck
git submodule init
git submodule update
```

2. Run the one time setup script to generate the `.env` file

```terminal
bash setup.sh
```

3. Add your details into `.env`

```terminal 
nano .env
```

4. Then run Docker compose from project root in detached mode. 

```terminal
sudo docker compose up -d --build
```

> [!NOTE]
> Every time you add or turn on/off a device, you need to refresh the Grafana page for it to appear in the variable field at the top


## `localhost` Refferences

Where to access local servers when setup (can differ)

- [Prometheus (`http://localhost:9090`)](http://localhost:9090)
- [Speedtest Exporter (`http://localhost:9798`)](http://localhost:9798)


## Troubleshooting

### `.env not found` or `.env: no such file`

```
env file /home/username/NetCheck/.env not found: stat /home/username/NetCheck/.env: no such file or directory
```

Run `bash setup.sh` to generate `.env` file

---

### `failed to solve: failed to read dockerfile:`

```
[+] Building 0.3s (4/4) FINISHED                                                   docker:default
 => [netcheck-exporter internal] load build definition from Dockerfile                       0.1s
 => => transferring dockerfile: 2B                                                           0.0s
 => [prometheus internal] load build definition from Dockerfile                              0.1s
 => => transferring dockerfile: 780B                                                         0.0s
 => CANCELED [prometheus internal] load metadata for docker.io/prom/prometheus:latest        0.1s
 => CANCELED [prometheus internal] load metadata for docker.io/library/python:3.9-slim       0.1s
failed to solve: failed to read dockerfile: open Dockerfile: no such file or directory
```

You probably forgot to initialise the git submodules. Run:

```terminal
git submodule init
git submodule update
```