

### 1. Check Python Installation

Verify that Python 3 is installed:

```bash
python3 --version
```

If you don't have Python 3 or it's outdated, proceed to the next step.

### 2. Install Python via Homebrew

Homebrew is a package manager that simplifies software installation on macOS. If you don't have Homebrew installed, run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Now, install Python:

```bash
brew install python
```

Verify the Python installation:

```bash
python3 --version
```

### 3. Upgrade `pip`

Ensure you have the latest version of `pip`:

```bash
python3 -m pip install --upgrade pip
```

Check the `pip` version:

```bash
pip3 --version
```

### 4. Set Up a Python Virtual Environment (Optional but Recommended)

Create and activate a virtual environment for this project to keep dependencies isolated:

```bash
python3 -m venv airflow_venv
source airflow_venv/bin/activate
```

To deactivate the virtual environment, use:

```bash
deactivate
```

### 5. Install Apache Airflow

Use `pip` to install Apache Airflow with the constraints file to handle dependencies:

```bash
pip install "apache-airflow==2.7.2" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.2/constraints-3.9.txt"
```

Replace `2.7.2` with the latest Airflow version and adjust `constraints-3.9.txt` according to your Python version (e.g., `3.8`, `3.10`).

```bash
pip install -r requirements.txt
```

### 6. Initialize the Airflow Database

Airflow uses a metadata database to keep track of DAGs and task states. Initialize it with:

```bash
airflow db init
```

### 7. Create an Admin User

Set up an admin user for accessing the Airflow UI:

```bash
airflow users create \
    --username admin \
    --firstname John \
    --lastname Doe \
    --role Admin \
    --email admin@example.com
```

Replace the details with your preferred credentials.

### 8. Start Airflow Services

Open two terminal windows or use `tmux`/`screen` to run the following services:

- **Start the Web Server** (accessible at [http://localhost:8080](http://localhost:8080)):

  ```bash
  airflow webserver
  ```

- **Start the Scheduler**:

  ```bash
  airflow scheduler
  ```

### 9. Verify the Setup

Visit [http://localhost:8080](http://localhost:8080) in your browser and log in using the admin credentials you created earlier.

## 🏗️ Project Structure

```bash
.
├── dags/                  # Folder containing your Airflow DAGs
├── plugins/               # Folder for custom plugins
├── airflow.cfg            # Airflow configuration file
├── README.md              # Project documentation (this file)
└── requirements.txt       # Additional Python dependencies (if any)
```

## 📚 Basic Airflow Concepts

- **DAG**: A Directed Acyclic Graph (DAG) is a collection of tasks with defined dependencies.
- **Operator**: Defines a single task in a DAG (e.g., BashOperator, PythonOperator).
- **Task**: A unit of work within a DAG.
- **Scheduler**: Triggers task instances based on the defined schedule.
- **Web Server**: Provides the Airflow UI for monitoring DAGs and tasks.


## 🛠️ Troubleshooting

- **Database Errors**: If you encounter database issues, reset the database with:

  ```bash
  airflow db reset
  ```

- **Permission Errors**: If you get permission errors, try running the commands with `sudo`.

- **Environment Variable Issues**: Set the `AIRFLOW_HOME` explicitly if needed:

  ```bash
  export AIRFLOW_HOME=~/airflow
  ```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

If you have any questions, feel free to reach out:

- **GitHub**: [jhon0010](https://github.com/jhon0010)

Happy Airflow-ing! 🌬️
