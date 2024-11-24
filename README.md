# NetCheck

![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/-Raspberry_Pi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![Summary Dashboard](assets/summary.png)
Caption: A screenshot of the summary section of the Grafana dashboard with 2 devices reporting

> [!IMPORTANT]
> Work In Progress

A persistent network uptime and speed logging Grafana client intended for use on mutiple Raspberry Pis.
Based on [MiguelNdeCarvalho/speedtest-exporter](https://github.com/MiguelNdeCarvalho/speedtest-exporter)

## `localhost` Refferences

Where to access local servers when setup (can differ)

- [Prometheus (`http://localhost:9090/`)](http://localhost:9090/)
- [Speedtest Exporter (`http://localhost:9798/metrics`)](http://localhost:9798/metrics)

## Instructions

### OS and Prerequisites 

Developed and tested for *Raspberry Pi 4b*. May work on other linux devices, not sure.
I devleoped this on an arm based Mac.

- *OS:* 64 Bit Raspberry Pi OS - Lite version (Full version should work as well)
    - _Helpful tip:_ Enable SSH with password and guest access if you are setting up headless.
- *Software*
    - [Install `docker-compose`](https://docs.docker.com/compose/install/) if you haven't got it already. I would highly reccomend installing it connected to a monitor. Headless seems to have connection issues. Perhaps because you can't accept the EULA and bypass the login screen? I'm open to suggestions here.
    - Make sure `Docker-Desktop` is set to automatically open as a startup app if you plan to have this run automatically. I mean the entire app as well, not just the engine and container services.


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

3. Add in your Grafana details into `.env`

```terminal 
nano .env
```

4. Then run docker setup from project root in detached mode. 

```terminal
docker-compose up -d --build
```

Note that every time you add a new device, you need to refresh the Grafana page for it to appear in the variable field at the top
