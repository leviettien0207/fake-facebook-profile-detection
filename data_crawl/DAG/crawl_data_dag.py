from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.timetables.simple import ContinuousTimetable
from selenium import webdriver

from datetime import datetime

from config import batch_data
from run import *

import logging
import json


dag_path = "/home/tienle/airflow/dags"

def crawl_data():
    # open browser and disable notification
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('--headless=new')

    browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)

    # login facebook
    logging.info('Logging in FB')
    login(browser)
    sleep_abit()

    # open each main profile
    logging.info('Open folder contains only ids')
    file_id_list = os.listdir(dag_path + '/input')

    # Remove sample file
    try:
        file_id_list.remove('example.txt')
    except ValueError:
        pass  # do nothing!

    # If there is a file
    if file_id_list:

        list_data = []
        for file in file_id_list:

            # open file
            logging.info(f'Open file {file}')
            id_list = open(dag_path + f'/input/{file}')

            # loop user id
            for uid in id_list:

                uid = uid.replace('\n', '')
                # open group member page
                logging.info(f'Open member page link {uid}')
                browser.get("https://www.facebook.com/" + uid)
                sleep_abit()

                # member page exist?
                if is_exist(browser):
                    # get data
                    list_data.append(get_all(browser, uid))
                    logging.info(f'Done page link {uid}   {len(list_data)}')

                # when collect enough batch_data of users
                if len(list_data) == batch_data:
                    # write file
                    dictionary = {
                        "list_users": list_data
                    }

                    json_object = json.dumps(dictionary, indent=4, ensure_ascii=False)

                    with open(new_file_1(), "w", encoding='utf-8') as outfile:
                        outfile.write(json_object)

                    # stop reading user id
                    break

            # Done 100 uid of file, yet still more id
            # Done xxx id of file, move to other file
            id_list.seek(0)
            lines = id_list.readlines()

            # file no contents
            if len(lines) == 0:
                # next file
                logging.info(f'file {file} no content')
                continue
            # if reach end, delete file
            elif lines[-1] == uid + '\n':
                logging.info(f'remove file {file}')
                os.remove(dag_path + f'/input/{file}')
            # if not delete to id used of file
            else:
                logging.info(f'delete uid used in file {file}')
                new_file = open(dag_path + f'/input/{file}', "w")

                i = 0
                flag = True
                while i < len(lines):
                    if not flag:
                        new_file.write(lines[i])
                    if lines[i] == uid + '\n':
                        flag = False
                    i += 1

            # In case enough from many files
            if len(list_data) == batch_data:
                break
            # In case no more file but not yet enough
            elif file == file_id_list[-1]:
                logging.info(f'no more file to process')
                # write file
                dictionary = {
                    "list_users": list_data
                }

                json_object = json.dumps(dictionary, indent=4, ensure_ascii=False)

                with open(new_file_1(), "w", encoding='utf-8') as outfile:
                    outfile.write(json_object)

    else:
        logging.info(f'no file id to input')

    # close browser
    browser.close()


with DAG(
        "FB_CRAWL",
        default_args={
            "depends_on_past": False,
            "email": ["tien.lv@teko.vn"],
            "email_on_failure": False,
            "email_on_retry": False,
            # "retries": 1,
            # "retry_delay": timedelta(minutes=5),
            # 'queue': 'bash_queue',
            # 'pool': 'backfill',
            # 'priority_weight': 10,
            # 'end_date': datetime(2016, 1, 1),
            # 'wait_for_downstream': False,
            # 'sla': timedelta(hours=2),
            # 'execution_timeout': timedelta(seconds=300),
            # 'on_failure_callback': some_function, # or list of functions
            # 'on_success_callback': some_other_function, # or list of functions
            # 'on_retry_callback': another_function, # or list of functions
            # 'sla_miss_callback': yet_another_function, # or list of functions
            # 'trigger_rule': 'all_success'
        },
        description="A simple DAG",
        schedule='@continuous',
        start_date=datetime(2023, 6, 9),
        catchup=True,
        tags=["fb_data"],
        max_active_runs=1
) as dag:
    python_task = PythonOperator(
        task_id='crawl_data',
        python_callable=crawl_data
    )
