# Weeks 11-12: **Monitoring and Logging**

## Monitoring

* Checking the status, performance and health of the systems, applications, or infrastructure specifically in real-time.

## Logging

* Keeping a record of what is happening in a computer system or application that pertains to events, errors, and other detailed information.

## Monitoring Tools

### Prometheus

* Prometheus is an open-source monitoring and alerting toolkit made at SoundCloud.
* It collects and stores the metrics which contain metric information, a timestamp, and optional key-value pairs.
* Prometheus was made for the intention to be reliable, specifically to remain operational even when problems occur.

#### Prometheus Exporters

* Prometheus Exporters are used to collect metrics that are formatted in a way that Prometheus can scrape and store.
* It exposes an endpoint to which the Prometheus server can pull data in given intervals.
* The metrics exposed in the endpoint are constantly changing.

### Grafana

* Grafana is a visualization tool using data sources and displaying it in graphs and/or visualizations.
* Grafana also offers alerts that can be sent through SMS, email, etc.
