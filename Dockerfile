FROM ubuntu:18.04
RUN apt update -y && apt install -y python3
ADD /cron_reader cron_reader
ENTRYPOINT ["/cron_reader"]

