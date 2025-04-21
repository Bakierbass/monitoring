# Dockerized Monitoring Stack  
A complete observability stack containerized with Docker Compose, featuring application monitoring, metrics collection, log aggregation, and visualization.  

**Features**: Python Application with metrics endpoints and generates random DEBUG/WARNING logs, Prometheus for metrics collection, Loki for log aggregation, Promtail for log collection, and Grafana for visualization dashboards.  

**Quick Start**:  
1. Clone repository: `git clone https://github.com/LeBakii/monitoring.git && cd monitoring`  
2. Install Docker: `chmod +x scripts/docker.sh && sudo ./scripts/docker.sh`
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
- Start: `docker-compose up -d --build`  
- Stop: `docker-compose down`
- Logs: `docker-compose logs -f [service_name]`  
- Restart: `docker-compose restart [service_name]`

**Ports**: Application (5000), Grafana (3000), Prometheus (9090), Loki (3100)  

**Troubleshooting**:  
- Port conflicts: Change ports in `docker-compose.yml`  
- Permission issues: `sudo usermod -aG docker $USER`  
- Dashboard problems: Verify datasource configurations  

**Security**: Change default Grafana credentials, secure exposed ports, review volume permissions.  
