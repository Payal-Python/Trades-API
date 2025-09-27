#!/usr/bin/env bash
set -e


# Build docker images
docker-compose -f docker/docker-compose.yml build


# Start Postgres and Airflow services
docker-compose -f docker/docker-compose.yml up -d postgres airflow


# Run scraper inside airflow container
docker exec -it $(docker ps -qf "name=airflow") python /opt/airflow/scripts/scraper.py --out example


# Run PySpark job inside spark container
docker exec -it $(docker ps -qf "name=spark") spark-submit /opt/spark-apps/process_vulns.py /opt/data/raw /opt/data/processed


# Load into Postgres from Airflow container
docker exec -it $(docker ps -qf "name=airflow") python /opt/airflow/scripts/loader.py /opt/data/processed/vulns.parquet
