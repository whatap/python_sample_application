## OS

  python 3.10.6\
  django 4.1.7\
  modwsgi 4.9.4

## setting
- vi {project_dir}/python_sample_application/django4.1.7/rundmowsgi/entrypoint.sh -> 라이센스 키 변경

## install

- 빌드 : sudo docker build -t whatap/whatap_modwsgi:0.1.0 .
- 제거 : sudo docker rm {container_id}
- 컨테이너 띄우기 : sudo docker run --name whatap_modwsgi -d -p 8000:8000 whatap/whatap_modwsgi:0.1.0
- 스크립트 실행 : sudo docker exec -it {container_id} /bin/bash
- 로그 : sudo docker logs --tail=50 {container_id}