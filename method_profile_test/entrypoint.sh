#!/bin/bash

export WHATAP_HOME=${PWD}
chmod -R 777 $WHATAP_HOME
whatap-setting-config \
--host 15.165.146.117 \
--license $WHATAP_LICENSE \
--app_name myapp-batch \
--app_process_name python

echo 'trace_logging_enabled=true' >> whatap.conf
echo 'trace_loguru_enabled=true' >> whatap.conf
echo 'log_unhandled_exception=true' >> whatap.conf
whatap-start-agent python main.py
