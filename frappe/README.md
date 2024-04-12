
# Integrating Whatap Monitoring with Frappe using Supervisor

This guide is designed to help developers to safely and effectively integrate Whatap monitoring into their Frappe applications. Follow these steps to set up Whatap monitoring for your application.

## Prerequisites

- Python and Frappe set up on your server
- Supervisor installed and running
- Access to your Whatap project (host, access key, etc.)

## Step 0: Login as user for Frappe application 
```bash
sudo su - YOUR_USERNAME
```

to verify frappe application you could run following command
```bash
ps -ef |grep frappe
```

## Step 1: Activate Your Virtual Environment

Before installing any whatap-python packages, ensure your Python virtual environment is activated.

```bash
source /path/to/your/frappe-bench/env/bin/activate
```
to verify venv python is activated, you could run following command to see frappe process list. 
```bash
ps -ef|grep `which python`

...
hsnam     7562  7556  0 14:15 ?        00:00:00 /home/hsnam/test/20240221/frappe-bench/env/bin/python3 -m frappe.utils.bench_helper frappe serve --port 8000
...
```

Replace `/path/to/your/frappe-bench` with the actual path to your Frappe installation.

## Step 2: Install whatap-python

With your virtual environment activated, install the whatap-python package using pip.

```bash
pip install whatap-python
```
to verify whatap-python is correctly installed, you could run following command to see installed version
```bash
pip show whatap-python

$ pip show whatap-python
Name: whatap-python
Version: 1.5.8
Summary: Monitoring and Profiling Service
Home-page: https://www.whatap.io
Author: whatap
Author-email: admin@whatap.io
License: Whatap License
Location: /home/hsnam/test/20240221/frappe-bench/env/lib/python3.8/site-packages
Requires:
Required-by:
```
## Step 3: Configure Whatap

Create a Whatap configuration file (`whatap.conf`) and set up the environment variable `WHATAP_HOME` to specify the root directory for Whatap config and log files.

1. **Set WHATAP_HOME environment variable**

```bash
export WHATAP_HOME=/path/to/your/whatap/directory
mkdir -p $WHATAP_HOME
```

1. **Create Whatap configuration file**

Use the `whatap-setting-config` command to generate the `whatap.conf` file with your project settings.

```bash
whatap-setting-config --host YOUR_WHATAP_HOST --license YOUR_WHATAP_LICENSE_KEY --app_name YOUR_APP_NAME --app_process_name gunicorn
```

Replace placeholders with your actual Whatap project details.

To verify configuration file is correctly created, you could run following command.
```bash
cat $WHATAP_HOME/whatap.conf

# WHATAP GUIDE DOCUMENTS
# https://www.whatap.io/document/guide/WHATAP_PYTHON_GETTING_STARTED.pdf
# https://www.whatap.io/document/guide/WHATAP_PYTHON_INSTALL_GUIDE.pdf
# https://www.whatap.io/document/guide/WHATAP_PYTHON_CONFIGURATION_GUIDE.pdf

license=x4n7b123djgbk-z4ki1kvg3ubk8r-z4b3giom4nsbf4
whatap.server.host=13.124.xx.xxx/13.209.xx.xx

# application name
app_name=frappe-hsnam

# middleware process name ex)uwsgi, gunicorn ..
app_process_name=gunicorn
```


## Step 4: Integrate Whatap Monitoring with Frappe using Supervisor

Edit your Supervisor configuration to start your Frappe application with Whatap monitoring enabled.
0. **Backup you supervisor config
Always backup supervisor config before add whatap config   

1. **Create or edit a Supervisor program configuration**
Frappe supervisor config is in /path/to/your/frappe-bench/config/supervisor.conf
Example for a Frappe Bench application:

```ini
[program:frappe-bench-frappe-web]
command=/path/to/your/frappe-bench/env/bin/whatap-start-agent /path/to/your/frappe-bench/env/bin/gunicorn -b 127.0.0.1:8000 -w WORKER_COUNT -t TIMEOUT frappe.app:application --preload
priority=4
autostart=true
autorestart=true
stdout_logfile=/path/to/your/logs/web.log
stderr_logfile=/path/to/your/logs/web.error.log
user=YOUR_USERNAME
directory=/path/to/your/frappe-bench/sites
environment=WHATAP_HOME=/path/to/your/whatap/directory
```

- Replace `/path/to/your` and other placeholders with your actual file paths and settings.
- Adjust `WORKER_COUNT` and `TIMEOUT` according to your application's needs.

to verify config correctly, you could run following command to check correct terms. 

```bash
grep whatap-start-agent  /path/to/your/frappe-bench/config/supervisor.conf
#output
command=/path/to/your/frappe-bench/env/bin/whatap-start-agent /path/to/your/frappe-bench/env/bin/gunicorn -b 127.0.0.1:8000 -w 33 -t 120 frappe.app:application --preload

grep WHATAP_HOME /path/to/your/frappe-bench/config/supervisor.conf
#output
environment=WHATAP_HOME=/path/to/your/whatap/directory
```

to verify config correctly, you could run following command to check supervisor config syntax error. 

```bash
sudo supervisorctl reread
```

1. **Reload Supervisor configuration**

After saving your changes, update Supervisor to apply the new configuration and start only affected processes.

```bash
sudo supervisorctl update
```


## Conclusion

You have now integrated Whatap monitoring into your Frappe application with Supervisor. This setup allows you to monitor your application's performance and troubleshoot issues effectively.

