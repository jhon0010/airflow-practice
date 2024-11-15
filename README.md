# Apache Airflow Practice

Welcome to the Apache Airflow Practice repository! 🚀

This project is designed to help you get started with Apache Airflow, an open-source platform for orchestrating complex data workflows. Follow the steps below to set up your environment on macOS and dive into building and running DAGs (Directed Acyclic Graphs) with Airflow.

## 📋 Prerequisites

Ensure you have the following installed on your machine:

- **Python** (Version 3.7 or higher)
- **pip** (Python package manager)
- **Homebrew** (Optional but recommended for managing packages)

## 🛠️ Installation

Follow these steps to set up Apache Airflow on your macOS machine:

# Setting Up Apache Airflow with Docker Compose

This guide helps you set up and run Apache Airflow using Docker Compose on macOS.

## 1. Install Docker and Docker Compose

Ensure that both Docker and Docker Compose are installed on your system.

- **Docker**: Download and install Docker Desktop from the [official Docker website](https://www.docker.com/products/docker-desktop).
- **Docker Compose**: Docker Desktop includes Docker Compose. Verify the installation by running:

  ```bash
  docker-compose --version
  ```

## 2. Clone the Repository

Clone your Airflow practice repository to your local machine:

```bash
git clone https://github.com/jhon0010/airflow-practice
cd airflow-practice
```

## 3. Set Up the Environment

Create necessary directories and set environment variables:

```bash
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

This setup ensures proper file permissions between your host and Docker containers.

## 4. Initialize the Airflow Database

Run the following command to set up the Airflow metadata database:

```bash
docker-compose up airflow-init
```

After initialization, you should see a message indicating that the database setup is complete.

## 5. Start Airflow Services

Launch the Airflow services (web server, scheduler, etc.) using:

```bash
docker-compose up
```

To run the services in the background, add the `-d` flag:

```bash
docker-compose up -d
```

## 6. Access the Airflow Web Interface

Open your browser and navigate to [http://localhost:8080](http://localhost:8080).

Log in using the default credentials:

- **Username**: `airflow`
- **Password**: `airflow`

## 7. Shut Down Airflow Services

To stop the services, run:

```bash
docker-compose down
```

## 8. Run backfill command inside docker 

Run the followinf command to run the backfill command inside the docker container

```bash
docker exec  -it {docker_pid} bash 
```
```bash
airflow dags backfill -s 2021-08-01 -e 2021-08-31 {dag_id}
```

## Additional Information

For more detailed information, refer to the [official Airflow documentation on running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).

By following these steps, you can set up and run Apache Airflow using Docker Compose, facilitating a consistent and isolated environment for your workflows.
