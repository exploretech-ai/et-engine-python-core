import et_engine_core as et


def test_filesystem_json():
    """Tests Filesystem interface"""
    
    filesystem_1 = et.Filesystem("id", "name")
    filesystem_1_json = filesystem_1.to_json()
    filesystem_2 = et.Filesystem.from_json(filesystem_1_json)

    assert filesystem_1 == filesystem_2