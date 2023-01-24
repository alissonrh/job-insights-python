from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    try:
        jobs_list = read(path)
        industry_type = list()
        for job in jobs_list:
            if job["industry"] not in industry_type and job["industry"] != "":
                industry_type.append(job["industry"])
        return industry_type
    except Exception as e:
        print(f"Ocorreu um erro na leitura do arquivo CSV: {e}")


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    try:
        filtered_jobs = list()
        for job in jobs:
            if job["industry"] == industry:
                filtered_jobs.append(job)
        return filtered_jobs
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
