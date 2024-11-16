from typing import Self


class Filesystem:
    """Interface for ET Engine Filesystems
    """

    def __init__(self, filesystem_id: str, filesystem_name: str) -> None:
        """Create an ET Engine Filesystem

        Args:
            filesystem_id (str): unique ID of the filesystem
            filesystem_name (str): unique name of the filesystem
        """
        self.filesystem_id = filesystem_id
        self.filesystem_name = filesystem_name


    def __eq__(self, obj: object) -> bool:
        """Checks if the object is equal to the Filesystem

        Args:
            obj (object): object to compare

        Returns:
            bool: True if all properties are the same, False otherwise
        """
        try:
            is_equal = True
            is_equal &= self.filesystem_id == obj.filesystem_id
            is_equal &= self.filesystem_name == obj.filesystem_name
            return is_equal
        except:
            return False
        

    def __repr__(self) -> None:
        message = f"ET Engine Filesystem [{self.filesystem_id}]: {self.filesystem_name}"
        return message


    def to_json(self) -> dict[str: str]:
        """Export Filesystem to JSON-like dictionary

        Returns:
            dict: dictionary that can be turned into a JSON string
        """
        filesystem_json = {
            "filesystem_id": self.filesystem_id,
            "filesystem_name": self.filesystem_name
        }
        return filesystem_json
    

    @staticmethod
    def from_json(filesystem_json: dict[str: str]) -> Self:
        """Create a Filesystem object from JSON

        Args:
            filesystem_json (dict): JSON-like representation of the object, e.g. from `Filesystem(...).to_json()`

        Returns:
            Self: a Filesystem object
        """
        return Filesystem(**filesystem_json)
    


