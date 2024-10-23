import et_engine_core as et


def test_job():
    """Tests Job Interface"""

    job_id = "XX"
    job_tool = et.Tool("id", "name", "description")
    job_log_id = "YY"
    job_argument_list = [
        et.Argument("key1", "val1"),
        et.Argument("key2", "val2")
    ]

    job_1 = et.Job(job_id, job_tool, job_log_id, job_argument_list)
    job_1_json = job_1.to_json()
    job_2 = et.Job.from_json(job_1_json)

    assert job_1 == job_2