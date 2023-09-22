# -*- coding: utf-8 -*-
from src.utils import get_project_dir
from configparser import ConfigParser

project_dir = get_project_dir()
config = ConfigParser()
config.read(filenames=f'{project_dir}/config/config.ini')

class ServerConfig():
    def __init__(self):
        section = 'Server'
        self.protocol = config.get(section=section, option='protocol')
        self.rest_api_host = config.get(section=section, option='rest_api_host')
        self.rest_api_port = config.getint(section=section, option='rest_api_port')

        self.python_django_host = config.get(section=section, option='python_django_host')
        self.python_django_port = config.getint(section=section, option='python_django_port')

        self.run_path = config.get(section=section, option='run_path')
        self.log_path = config.get(section=section, option='log_path')
        self.debug = config.getboolean(section=section, option='debug')


class PathConfig():
    def __init__(self):
        section = 'Path'

        ##퍼포먼스 모니터링
        self.performance_monitor = config.get(section=section, option='performance_monitor')

        ##home
        self.home = config.get(section=section, option='home')

        ##샘플
        self.f0_example = config.get(section=section, option='f0_example')

        ##f1 서버
        self.f1_server_status = config.get(section=section, option='f1_server_status')
        self.f1_server_cpu = config.get(section=section, option='f1_server_cpu')
        self.f1_server_memory = config.get(section=section, option='f1_server_memory')
        self.f1_application_transaction = config.get(section=section, option='f1_application_transaction')

        ##f2 어플리케이션
        self.f2_application_cpu = config.get(section=section, option='f2_application_cpu')
        self.f2_application_memory = config.get(section=section, option='f2_application_memory')
        self.f2_application_heap = config.get(section=section, option='f2_application_heap')

        ##f3 gc
        self.f3_gc = config.get(section=section, option='f3_gc')

        ##f4 메모리 누수 감지 및 분석기능
        self.f4_memory_alarm_percent = config.get(section=section, option='f4_memory_alarm_percent')
        self.f4_memory_alarm_used = config.get(section=section, option='f4_memory_alarm_used')

        #f5 topology(어플리케이션 관계 정보)
        self.f5_topology_inbound = config.get(section=section, option='f5_topology_inbound')
        self.f5_topology_db = config.get(section=section, option='f5_topology_db')
        self.f5_topology_system = config.get(section=section, option='f5_topology_system')

        ##f6 이기종 WAS
        self.f6_was = config.get(section=section, option='f6_was')

        ##f7 트랜젝션 디테일 및 에러 트랜젝션 필터링
        self.f7_transaction_detail = config.get(section=section, option='f7_transaction_detail')
        self.f7_transaction_error_filter = config.get(section=section, option='f7_transaction_error_filter')
        self.f7_transaction_error_http = config.get(section=section, option='f7_transaction_error_http')
        self.f7_transaction_error_program = config.get(section=section, option='f7_transaction_error_program')
        self.f7_transaction_error_sql = config.get(section=section, option='f7_transaction_error_sql')

        ##f8. 트랜젝션 섹션별 정보
        self.f8_transaction_section = config.get(section=section, option='f8_transaction_section')

        ##f9 트랜젝션 모니터링 드릴다운
        self.f9_drill_down_slow_transaction = config.get(section=section, option='f9_drill_down_slow_transaction')



        ## connection pool 모니터링
        self.f11_connection_pool = config.get(section=section, option='f11_connection_pool')

        ## sql 상세
        # self.sql = config.get(section=section, option='sql')
        self.f12_sql_conn = config.get(section=section, option='f12_sql_conn')
        self.f12_sql_wrong_conn = config.get(section=section, option='f12_sql_wrong_conn')
        self.f12_sql_query_latency = config.get(section=section, option='f12_sql_query_latency')
        self.f12_sql_query_count = config.get(section=section, option='f12_sql_query_count')
        self.f12_sql_query_error_count = config.get(section=section, option='f12_sql_query_error_count')

        ## f13 임계값 설정 및 알람
        self.f13_threshold_alarm_cpu = config.get(section=section, option='f13_threshold_alarm_cpu')
        self.f13_threshold_alarm_memory = config.get(section=section, option='f13_threshold_alarm_memory')
        self.f13_threshold_alarm_transaction_num = config.get(section=section, option='f13_threshold_alarm_transaction_num')
        self.f13_threshold_alarm_transaction_latency = config.get(section=section, option='f13_threshold_alarm_transaction_latency')

        ## f14 임계값 이상시. 메서드 레벨 원인 분석
        self.f14_threshold_analysis_method_level_cpu = config.get(section=section, option='f14_threshold_analysis_method_level_cpu')
        self.f14_threshold_analysis_method_level_memory = config.get(section=section, option='f14_threshold_analysis_method_level_memory')
        self.f14_threshold_analysis_method_level_transaction_num = config.get(section=section, option='f14_threshold_analysis_method_level_transaction_num')
        self.f14_threshold_analysis_method_level_transaction_latency = config.get(section=section, option='f14_threshold_analysis_method_level_transaction_latency')

        ## f15 임계값 이상시. 담당자 이메일 발송
        self.f15_threshold_alarm_mail_cpu = config.get(section=section, option='f15_threshold_alarm_mail_cpu')
        self.f15_threshold_alarm_mail_memory = config.get(section=section, option='f15_threshold_alarm_mail_memory')
        self.f15_threshold_alarm_mail_transaction_num = config.get(section=section, option='f15_threshold_alarm_mail_transaction_num')
        self.f15_threshold_alarm_mail_transaction_latency = config.get(section=section, option='f15_threshold_alarm_mail_transaction_latency')

class MysqlConfig():
    def __init__(self):
        section = 'Mysql'
        self.host = config.get(section=section, option='host')
        self.port = config.getint(section=section, option='port')
        self.user = config.get(section=section, option='user')
        self.user_wrong = config.get(section=section, option='user_wrong')
        self.password = config.get(section=section, option='password')
        self.charset = config.get(section=section, option='charset')
        self.database = config.get(section=section, option='database')

class ParameterConfig():
    def __init__(self):
        section = 'Parameters'


class NotiConfig():
    def __init__(self):
        section = 'NotiConfig'


class CeleryConfig():
    def __init__(self):
        section = 'Celery'

if __name__ == "__main__":
    path =  PathConfig()
    print(path.f13_threshold_alarm_cpu)