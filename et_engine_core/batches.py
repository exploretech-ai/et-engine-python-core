from .tools import Tool, Hardware
from typing import Self


class Batch:
    """Interface for ET Engine Batches
    """

    def __init__(self, batch_id: str, batch_tool: Tool, n_jobs: int, batch_hardware: Hardware) -> None:
        """Create an ET Engine Batch

        Args:
            batch_id (str): unique ID of the batch
            batch_tool (Tool): tool used to execute the batch
            n_jobs (int): number of executed jobs
            batch_hardware (Hardware): hardware used on all the jobs
        """
        self.batch_id = batch_id
        self.batch_tool = batch_tool
        self.n_jobs = n_jobs
        self.batch_hardware = batch_hardware


    def __eq__(self, obj: object) -> bool:
        """Checks if the object is equal to the Batch

        Args:
            obj (object): object to compare

        Returns:
            bool: True if all properties are the same, False otherwise
        """
        try:
            is_equal = True
            is_equal &= self.batch_id == obj.batch_id
            is_equal &= self.batch_tool == obj.batch_tool
            is_equal &= self.n_jobs == obj.n_jobs
            is_equal &= self.batch_hardware == obj.batch_hardware
            return is_equal
        
        except:
            return False
        

    def __repr__(self) -> str:
        message = f"ET Engine Batch [{self.batch_id}]: {self.n_jobs} jobs on tool '{self.batch_tool.tool_name}'"
        return message
        

    def to_json(self) -> dict[str: str]:
        """Export Batch to JSON-like dictionary

        Returns:
            dict: dictionary that can be turned into a JSON string
        """
        batch_json = {
            "batch_id": self.batch_id,
            "batch_tool": self.batch_tool.to_json(),
            "n_jobs": self.n_jobs,
            "batch_hardware": self.batch_hardware.to_json()
        }
        return batch_json
    

    @staticmethod
    def from_json(batch_json: dict[str: str]) -> Self:
        """Create a Batch object from JSON

        Args:
            batch_json (dict): JSON-like representation of the object, e.g. from `Batch(...).to_json()`

        Returns:
            Self: a Batch object
        """
        batch_id = batch_json["batch_id"]
        batch_tool = Tool.from_json(batch_json["batch_tool"])
        n_jobs = batch_json["n_jobs"]
        batch_hardware = Hardware.from_json(batch_json["batch_hardware"])
        return Batch(batch_id, batch_tool, n_jobs, batch_hardware)


class BatchStatus:
    """Interface for ET Engine Batch Status
    """

    def __init__(self, 
            submitted: int = 0, 
            pending: int = 0, 
            runnable: int = 0, 
            starting: int = 0, 
            running : int = 0, 
            succeeded: int = 0, 
            failed: int = 0
        ) -> None:
        """Create an ET Engine Batch Status object

        Args:
            submitted (int, optional): number of jobs with submitted status. Defaults to 0.
            pending (int, optional): number of jobs with pending status. Defaults to 0.
            runnable (int, optional): number of jobs with runnable status. Defaults to 0.
            starting (int, optional): number of jobs with starting status. Defaults to 0.
            running (int, optional): number of jobs with running status. Defaults to 0.
            succeeded (int, optional): number of jobs with succeeded status. Defaults to 0.
            failed (int, optional): number of jobs with failed status. Defaults to 0.
        """

        self.submitted = submitted
        self.pending = pending
        self.runnable = runnable
        self.starting = starting
        self.running = running
        self.succeeded = succeeded
        self.failed = failed


    def __eq__(self, obj: object) -> bool:
        """Checks if the object is equal to the Batch Status

        Args:
            obj (object): object to compare

        Returns:
            bool: True if all properties are the same, False otherwise
        """
        try:
            is_equal = True
            for attr, value in self.__dict__.items():
                is_equal &= value == getattr(obj, attr)
            return is_equal
        except:
            return False
        

    def __repr__(self) -> str:
        message  = f"submitted: {self.submitted}\n"
        message += f"pending:   {self.pending}\n"
        message += f"runnable:  {self.runnable}\n"
        message += f"starting:  {self.starting}\n"
        message += f"running:   {self.running}\n"
        message += f"succeeded: {self.succeeded}\n"
        message += f"failed:    {self.failed}\n"
        return message
        

    def to_json(self) -> dict[str: str]:
        """Export Batch Status to JSON-like dictionary

        Returns:
            dict: dictionary that can be turned into a JSON string
        """
        batch_status_json = {
            "submitted": self.submitted,
            "pending": self.pending,
            "runnable": self.runnable,
            "starting": self.starting,
            "running": self.running,
            "succeeded": self.succeeded,
            "failed": self.failed
        }
        return batch_status_json
    

    @staticmethod
    def from_json(batch_status_json: dict[str: str]) -> Self:
        """Create a BatchStatus object from JSON

        Args:
            batch_status_json (dict): JSON-like representation of the object, e.g. from `BatchStatus(...).to_json()`

        Returns:
            Self: a BatchStatus object
        """
        return BatchStatus(**batch_status_json)


