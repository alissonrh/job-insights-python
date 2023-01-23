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
        job_type = []
        for job in jobs_list:
            if job["job_type"] not in job_type:
                job_type.append(job["job_type"])
        return job_type
    except Exception as e:
        print(f"Ocorreu um erro na leitura do arquivo CSV: {e}")


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError


print(get_unique_job_types(path))
