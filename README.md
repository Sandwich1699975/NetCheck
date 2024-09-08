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

Create a GrafanaCloud dashboard with `<FINALISE A .JSON TEMPLATE HERE>` (temp: use [this](https://github.com/MiguelNdeCarvalho/speedtest-exporter/blob/main/Dashboard/Speedtest-Exporter.json))

#### Client Setup

Check you have the device prerequisites listed above

1. Install docker if you haven't already

```terminal
sudo apt install docker
```

2. Add in your Grafana details into `.env`

3. Then run docker setup from project root in detached mode. 

```terminal
docker-compose up -d
```