
- 환경

  python3.10.6\
  fastapi0.95.1\
  gunicorn20.1

- 의존성 패키지 설치

  $pip install -r requirments.txt


- 에이전트 설정

  $export WHATAP_HOME=$PWD

  $whatap-setting-config \
  --host 15.165.146.117 \
  --license {lisense_key} \
  --app_name {app_name} \
  --app_process_name {app_process_name}


- 트랜젝션 로그 설정

  $echo "trace_logging_enabled=true" >> whatap.conf

  $echo "trace_loguru_enabled=true" >> whatap.conf
  
- 에이전트 실행\
  whatap-start-agent uvicorn server:app --host 0.0.0.0 --port 9000
