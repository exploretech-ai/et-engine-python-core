from typing import Self
from .filesystems import Filesystem


class Argument:
    """Interface for ET Engine Arguments
    """

    def __init__(self, argument_key: str, argument_value: str) -> None:
        """Create an ET Engine Argument

        Args:
            argument_key (str): name of the argument
            argument_value (str): value of the argument
        """
        self.argument_key = argument_key
        self.argument_value = argument_value


    def __eq__(self, obj: object) -> bool:
        """Checks if the object is equal to the Argument

        Args:
            obj (object): object to compare

        Returns:
            bool: True if all properties are the same, False otherwise
        """
        try:
            is_equal = True
            is_equal &= self.argument_key == obj.argument_key
            is_equal &= self.argument_value == obj.argument_value
            return is_equal
        
        except:
            return False


    def to_json(self) -> dict[str: str]:
        """Export Argument to JSON-like dictionary

        Returns:
            dict: dictionary that can be turned into a JSON string
        """
        argument_json = {
            "argument_key": self.argument_key,
            "argument_value": self.argument_value,
        }
        return argument_json
    

    @staticmethod
    def from_json(argument_json: dict[str: str]) -> Self:
        """Create a Argument object from JSON

        Args:
            argument_json (dict): JSON-like representation of the object, e.g. from `Argument(...).to_json()`

        Returns:
            Self: a Argument object
        """
        return Argument(**argument_json)
    

class Tool:
    """Interface for ET Engine Tools
    """

    def __init__(self, tool_id: str, tool_name: str, tool_description: str) -> None:
        """Interface for ET Engine Tools

        Args:
            tool_id (str): unique ID of the tool
            tool_name (str): unique name of the tool
            tool_description (str): description of what the tool does
        """
        self.tool_id = tool_id
        self.tool_name = tool_name
        self.tool_description = tool_description


    def __repr__(self) -> str:
        message = f"ET Engine Tool [{self.tool_id}]: {self.tool_name} | {self.tool_description}"
        return message


    def __eq__(self, obj: object) -> bool:
        """Checks if the object is equal to the Tool

        Args:
            obj (object): object to compare

        Returns:
            bool: True if all properties are the same, False otherwise
        """
        try:
            is_equal = True
            is_equal &= self.tool_id == obj.tool_id
            is_equal &= self.tool_name == obj.tool_name
            is_equal &= self.tool_description == obj.tool_description
            return is_equal
            
        except:
            return False


    def to_json(self) -> dict[str: str]:
        """Export Tool to JSON-like dictionary

        Returns:
            dict: dictionary that can be turned into a JSON string
        """
        tool_json = {
            "tool_id": self.tool_id,
            "tool_name": self.tool_name,
            "tool_description": self.tool_description
        }
        return tool_json
    

    @staticmethod
    def from_json(tool_json: dict[str: str]) -> Self:
        """Create a Tool object from JSON

        Args:
            tool_json (dict): JSON-like representation of the object, e.g. from `Tool(...).to_json()`

        Returns:
            Self: a Tool object
        """
        return Tool(**tool_json)
    

class Hardware:
    """Interface for ET Engine Hardware
    """

    def __init__(self, filesystem_list: list[Filesystem], cpu: int, memory: int):
        """Create an ET Engine Hardware object

        Args:
            filesystem_list (list[Filesystem]): list of filesystems that a job can see when executing
            cpu (int): number of processors for the job to use, in vCPU
            memory (int): size of the memory (RAM) for the job to use, in MB
        """
        self.filesystem_list = filesystem_list
        self.cpu = cpu
        self.memory = memory


    def __eq__(self, obj: object) -> bool:
        """Checks if the object is equal to the Hardware

        Args:
            obj (object): object to compare

        Returns:
            bool: True if all properties are the same, False otherwise
        """
        try:
            is_equal = True
            is_equal &= self.cpu == obj.cpu
            is_equal &= self.memory == obj.memory
            for i, fs in enumerate(self.filesystem_list):
                is_equal &= fs == obj.filesystem_list[i]
            return is_equal
        
        except:
            return False


    def to_json(self) -> dict[str: str]:
        """Export Hardware to JSON-like dictionary

        Returns:
            dict: dictionary that can be turned into a JSON string
        """
        hardware_json = {
            "filesystem_list": [fs.to_json() for fs in self.filesystem_list],
            "cpu": self.cpu,
            "memory": self.memory
        }
        return hardware_json
    

    @staticmethod
    def from_json(hardware_json: dict[str: str]) -> Self:
        """Create a Hardware object from JSON

        Args:
            hardware_json (dict): JSON-like representation of the object, e.g. from `Hardware(...).to_json()`

        Returns:
            Self: a Hardware object
        """
        filesystem_list = [Filesystem.from_json(filesystem_json) for filesystem_json in hardware_json["filesystem_list"]]
        cpu = hardware_json["cpu"]
        memory = hardware_json["memory"]

        return Hardware(filesystem_list, cpu, memory)

    
