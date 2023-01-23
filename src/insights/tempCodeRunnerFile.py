def read(path: str) -> List[Dict]:

    with open(path, encoding="utf-8") as file:
        jobs_reader = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = jobs_reader
    return data


print(read("../../data/jobs.csv"))