import et_engine_core as et


def test_argument():
    """Tests Argument interface"""
    argument_1 = et.Argument("key", "value")
    argument_1_json = argument_1.to_json()
    argument_2 = et.Argument.from_json(argument_1_json)

    assert argument_1 == argument_2


def test_tool():
    """Tests Tool interface"""
    tool_1 = et.Tool("id", "name", "description")
    tool_1_json = tool_1.to_json()
    tool_2 = et.Tool.from_json(tool_1_json)

    assert tool_1 == tool_2


def test_hardware():
    """Tests Hardware interface"""

    filesystem_1 = et.Filesystem("id1", "name1")
    filesystem_2 = et.Filesystem("id2", "name2")
    filesystem_list = [filesystem_1, filesystem_2]
    
    hardware_1 = et.Hardware(filesystem_list, 10, 200)
    hardware_1_json = hardware_1.to_json()
    hardware_2 = et.Hardware.from_json(hardware_1_json)

    assert hardware_1 == hardware_2