import et_engine_core as et


def test_batch():
    """Tests Batch interface"""

    batch_id = "XXX"
    batch_tool = et.Tool(
        tool_id="id",
        tool_name="name",
        tool_description="description"
    )
    n_jobs = 10
    batch_hardware = et.Hardware(
        filesystem_list=[
            et.Filesystem("fs1", "fsname1"),
            et.Filesystem("fs2", "fsname2")
        ],
        cpu=2,
        memory=1000
    )

    batch_1 = et.Batch(
        batch_id=batch_id,
        batch_tool=batch_tool,
        n_jobs=n_jobs,
        batch_hardware=batch_hardware
    )
    batch_1_json = batch_1.to_json()
    batch_2 = et.Batch.from_json(batch_1_json)

    assert batch_1 == batch_2


def test_batch_status():
    """Tests BatchStatus interface"""

    batch_job_summary_json = {
        "submitted": 1,
        "pending": 2,
        "runnable": 3,
        "starting": 4,
        "running": 5,
        "succeeded": 6,
        "failed": 7
    }

    summary_1 = et.BatchStatus(**batch_job_summary_json)
    summary_1_json = summary_1.to_json()
    summary_2 = et.BatchStatus.from_json(summary_1_json)

    assert summary_1 == summary_2
