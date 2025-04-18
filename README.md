# Dockerized Monitoring Stack  
A complete observability stack containerized with Docker Compose, featuring application monitoring, metrics collection, log aggregation, and visualization.  

**Features**: Python Application with metrics endpoints, Prometheus for metrics collection, Loki for log aggregation, Promtail for log collection, and Grafana for visualization dashboards.  

**Prerequisites**: Ubuntu 20.04/22.04, Docker Engine 20.10+, Docker Compose 2.0+, 2GB RAM minimum (4GB recommended).  

**Quick Start**:  
1. Install Docker: `chmod +x scripts/docker.sh && sudo ./scripts/docker.sh`  
2. Clone repository: `git clone https://github.com/LeBakii/monitoring.git && cd monitoring`  
3. Start stack: `docker-compose up -d`  
4. Access services:  
   - Application: http://localhost:5000  
   - Grafana: http://localhost:3000 (admin/admin)  
   - Prometheus: http://localhost:9090  
   - Loki: http://localhost:3100  

**Configuration**:  
- Application: Modify `app/app.py` and `app/requirements.txt`  
- Prometheus: Edit `prometheus/prometheus.yml` for scrape intervals/targets  
- Loki: Adjust log retention in `loki/loki-config.yml`  
- Promtail: Modify log paths in `promtail/promtail-config.yml`  
- Grafana: Add dashboards to `grafana/provisioning/dashboards/`  

**Commands**:  
- Start: `docker-compose up -d`  
- Stop: `docker-compose down`  
- Logs: `docker-compose logs -f [service_name]`  
- Scale: `docker-compose up -d --scale app=3`  
- Update: `docker-compose pull && docker-compose up -d`  

**Ports**: Application (5000), Grafana (3000), Prometheus (9090), Loki (3100)  

**Troubleshooting**:  
- Port conflicts: Change ports in `docker-compose.yml`  
- Permission issues: `sudo usermod -aG docker $USER`  
- Dashboard problems: Verify datasource configurations  

**Security**: Change default Grafana credentials, secure exposed ports, review volume permissions.  
