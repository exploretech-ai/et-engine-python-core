from typing import Self
from .tools import Tool, Argument


class Job:
    """Interface for ET Engine Jobs
    """

    def __init__(self, job_id: str, job_tool: Tool, job_log_id: str, job_argument_list: list[Argument]) -> None:
        """Create an ET Engine Job

        Args:
            job_id (str): unique ID of the job
            job_tool (Tool): tool used to execute the job
            job_log_id (str): unique ID of the job log
            job_argument_list (list[Argument]): list of arguments sent to the job
        """
        self.job_id = job_id
        self.job_tool = job_tool
        self.job_log_id = job_log_id
        self.job_argument_list = job_argument_list


    def __eq__(self, obj: object) -> bool:
        """Checks if the object is equal to the Job

        Args:
            obj (object): object to compare

        Returns:
            bool: True if all properties are the same, False otherwise
        """
        try:
            is_equal = True
            is_equal &= self.job_id == obj.job_id
            is_equal &= self.job_tool == obj.job_tool
            is_equal &= self.job_log_id == obj.job_log_id
            for i, arg in enumerate(self.job_argument_list):
                is_equal &= arg == obj.job_argument_list[i]
            return is_equal
        
        except:
            return False


    def to_json(self) -> dict[str: str]:
        """Export Job to JSON-like dictionary

        Returns:
            dict: dictionary that can be turned into a JSON string
        """
        job_json = {
            "job_id": self.job_id,
            "job_tool": self.job_tool.to_json(),
            "job_log_id": self.job_log_id,
            "job_argument_list": [arg.to_json() for arg in self.job_argument_list]
        }
        return job_json
    

    @staticmethod
    def from_json(job_json: dict[str: str]) -> Self:
        """Create a Job object from JSON

        Args:
            job_json (dict): JSON-like representation of the object, e.g. from `Job(...).to_json()`

        Returns:
            Self: a Job object
        """
        
        job_id = job_json["job_id"]
        job_tool = Tool.from_json(job_json["job_tool"])
        job_log_id = job_json["job_log_id"]
        job_argument_list = [Argument.from_json(arg) for arg in job_json["job_argument_list"]]
        return Job(job_id, job_tool, job_log_id, job_argument_list)
