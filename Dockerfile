# Multistage (FROM ... AS ...) docs:
# https://docs.docker.com/build/building/multi-stage/
FROM python:3.9-slim AS setup
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

# Run setup file to create prometheus.yml
RUN python docker-setup.py

# Expose port for debugging
EXPOSE 5678

# Run official prometheus dockerfile
# Equivalent dockerfile of
# `$ docker run --name prometheus2 -d -p 127.0.0.1:9090:9090 prom/prometheus`
FROM prom/prometheus AS prom

# Copy over file from setup
COPY --from=setup /app/prometheus.yml /etc/prometheus/prometheus.yml

EXPOSE 9090

VOLUME     [ "/prometheus" ]
ENTRYPOINT [ "/bin/prometheus" ]
CMD        [ "--config.file=/etc/prometheus/prometheus.yml", \
    "--storage.tsdb.path=/prometheus"]
