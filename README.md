# NetCheck
A persistent network uptime and speed logging Grafana client intended for use on mutiple Raspberry Pis.
Based on [MiguelNdeCarvalho/speedtest-exporter](https://github.com/MiguelNdeCarvalho/speedtest-exporter)

## `localhost` Refferences

Where to access local servers when setup (can differ)

- [Prometheus (`http://localhost:9090/`)](http://localhost:9090/)
- [Speedtest Exporter (`http://localhost:9798/metrics`)](http://localhost:9798/metrics)

## Instructions

### OS and Device Prerequisites 

Developed and tested for *Raspberry Pi 4b*. May work on other linux devices, not sure.

- *OS:* 64 Bit Raspberry Pi OS - Lite version (Full version should work as well)
    - _Helpful tip:_ Enable SSH with password and guest access if you are setting up headless.

### Setup

#### Grafana Setup

1. Create a GrafanaCloud dashboard with `<FINALISE A .JSON TEMPLATE HERE>` (temp: use [this](https://github.com/MiguelNdeCarvalho/speedtest-exporter/blob/main/Dashboard/Speedtest-Exporter.json))

2. Create a Prometheus account

#### Client Setup

Check you have the device prerequisites listed above

1. Clone the repository

```terminal
git clone https://github.com/Sandwich1699975/NetCheck.git
cd NetCheck
```

2. Install docker if you haven't already.
Use your respective package manager/install option

```terminal
sudo apt install docker
```
3. Run the one time setup script to generate the `.env` file

```terminal
bash setup.sh
```

4. Add in your Grafana details into `.env`

```terminal 
nano .env
```

5. Then run docker setup from project root in detached mode. 

```terminal
docker-compose up -d --build
```