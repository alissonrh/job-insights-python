from functools import lru_cache
from typing import List, Dict
import csv

path = "../../data/jobs.csv"


@lru_cache
def read(path: str) -> List[Dict]:
    try:
        with open(path, encoding="utf-8") as file:
            jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            data = [row for row in jobs_reader]
        return data
    except Exception as e:
        print(f"Ocorreu um erro na leitura do arquivo CSV: {e}")


def get_unique_job_types(path: str) -> List[str]:
    try:
        jobs_list = read(path)
        job_type = list()
        for job in jobs_list:
            if job["job_type"] not in job_type:
                job_type.append(job["job_type"])
        return job_type
    except Exception as e:
        print(f"Ocorreu um erro na leitura do arquivo CSV: {e}")


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    try:
        filtered_jobs = list()
        for job in jobs:
            if job["job_type"] == job_type:
                filtered_jobs.append(job)
        return filtered_jobs
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
