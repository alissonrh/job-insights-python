from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    try:
        jobs_list = read(path)
        valid_salaries = []
        for job in jobs_list:
            salary = job["max_salary"]
            if salary != "invalid" and salary != "":
                valid_salaries.append(int(salary))
        maximum = max(valid_salaries)
        return maximum
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def get_min_salary(path: str) -> int:
    try:
        jobs_list = read(path)
        valid_salaries = []
        for job in jobs_list:
            salary = job["min_salary"]
            if salary != "invalid" and salary != "":
                valid_salaries.append(int(salary))
        minimum = min(valid_salaries)
        return minimum
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def validate_is_numeric_value(value) -> bool:
    #   Valida se o valor é numérico.
    return (
        isinstance(value, (int))
        or isinstance(value, (str))
        and value.isnumeric()
    )


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    salary_keys = ["min_salary", "max_salary"]

    for key in salary_keys:
        if key not in job:
            raise ValueError(f"Missing key '{key}' in job dictionary")
        if not validate_is_numeric_value(job[key]):
            raise ValueError(
                f"Invalid value for key '{key}', "
                "expected numeric value (int or string)"
            )

    min_salary = int(job["min_salary"])
    max_salary = int(job["max_salary"])

    if min_salary > max_salary or not validate_is_numeric_value(salary):
        raise ValueError(
            "Invalid salary range, min_salary "
            "must be less than or equal to max_salary"
        )
    return min_salary <= int(salary) <= max_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    valid_jobs = []
    for job in jobs:
        # Verifica se o emprego tem as chaves "min_salary" e "max_salary" e se
        # o min_salary é menor que o max_salary
        if (
            validate_is_numeric_value(job["min_salary"])
            and validate_is_numeric_value(job["max_salary"])
            and int(job["min_salary"]) < int(job["max_salary"])
        ):
            # Se for válido, adiciona esse emprego à lista de empregos válidos
            valid_jobs.append(job)
            # Filtra a lista de empregos válidos para incluir somente aqueles
            # em que o salário está dentro do intervalo especificado
    # pelos campos min_salary e max_salary no dicionário do emprego
    return [
        valid_job
        for valid_job in valid_jobs
        if validate_is_numeric_value(salary)
        and matches_salary_range(valid_job, salary)
    ]
