#!/bin/bash

export WHATAP_HOME=${PWD}
chmod -R 777 $WHATAP_HOME

####config
whatap-setting-config \
--host 15.165.146.117 \
--license {license-key} \
--app_name whatap_black_olive \
--app_process_name apache2

echo "trace_http_client_ip_header_key=true" >> whatap.conf
echo "profile_basetime=0" >> whatap.conf
echo "profile_sql_param_enabled=true" >> whatap.conf
echo "profile_sql_resource_enabled=true" >> whatap.conf
echo "trace_user_enabled=true" >> whatap.conf
echo "trace_user_using_ip=false" >> whatap.conf
echo "mtrace_rate=100" >> whatap.conf
echo ls -l
###agent start
su whatap
whatap-start-agent python ${PWD}/manage.py runmodwsgi
