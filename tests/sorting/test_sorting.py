from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs_mock = [
        {
            "min_salary": "500",
            "max_salary": "1600",
            "date_posted": "2023-01-20",
        },
        {
            "min_salary": "200",
            "max_salary": "900",
            "date_posted": "2023-02-24",
        },
        {
            "min_salary": "300",
            "max_salary": "1000",
            "date_posted": "2023-01-10",
        },
    ]
    descending_order_jobs = [jobs_mock[0], jobs_mock[2], jobs_mock[1]]
    ascending_order_jobs = [jobs_mock[1], jobs_mock[2], jobs_mock[0]]

    sort_by(jobs_mock, "max_salary")
    assert jobs_mock == descending_order_jobs

    sort_by(jobs_mock, "min_salary")
    assert jobs_mock == ascending_order_jobs
