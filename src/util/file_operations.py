# src/oslogic/file_operations.py 
import os
import zipfile
import platform
from abc import ABC, abstractmethod

class OSInfo:
    """
    A class to determine the current OS.
    """
    @staticmethod
    def get_os_type() -> str:
        return platform.system()

class FileOperations(ABC):
    """
    An abstract class for file operations.
    Subclasses should implement OS-specific logic.
    """
    @abstractmethod
    def get_download_dir(self) -> str:
        """
        Returns the path to the download directory.
        """
        pass

    @abstractmethod
    def find_files(self, prefix: str) -> list:
        """
        Searches the download directory for files starting with the given prefix
        and returns them as a list.
        """
        pass

    @abstractmethod
    def extract_file(self, zip_file_path: str, output_dir: str) -> None:
        """
        Extracts the specified ZIP file.
        """
        pass

    @abstractmethod
    def check_extracted_files(self, extracted_dir: str, expected_files: list) -> bool:
        """
        Checks if the expected files exist in the extracted directory.
        """
        pass


class WindowsFileOperations(FileOperations):
    """
    Implementation for the Windows environment.
    """

    def get_download_dir(self) -> str:
        # GitHub Windowsランナーではユーザープロファイルは "C:\Users\runneradmin" になるはず
        downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        # Downloadsフォルダが存在しない場合は作成する
        os.makedirs(downloads, exist_ok=True)
        return downloads

    def find_files(self, prefix: str) -> list:
        downloads = self.get_download_dir()
        all_files = os.listdir(downloads)
        print(f"[WindowsFileOperations] Files in downloads ({downloads}): {all_files}")
        # テストコードが "Files (" で始まるZIPファイルを想定しているので、括弧も含むか確認
        matching = [f for f in all_files if f.startswith(prefix)]
        return matching

    def extract_file(self, zip_file_path: str, output_dir: str) -> None:
        os.makedirs(output_dir, exist_ok=True)
        with zipfile.ZipFile(zip_file_path, 'r') as zf:
            zf.extractall(output_dir)

    def check_extracted_files(self, extracted_dir: str, expected_files: list) -> bool:
        existing = set(os.listdir(extracted_dir))
        return set(expected_files).issubset(existing)


class MacFileOperations(FileOperations):
    """
    A dummy implementation for Mac (Darwin).
    """
    def get_download_dir(self) -> str:
        return os.path.join(os.path.expanduser("~"), "Downloads")

    def find_files(self, prefix: str) -> list:
        print("[Mac] find_files is a dummy implementation.")
        return []

    def extract_file(self, zip_file_path: str, output_dir: str) -> None:
        print("[Mac] extract_file is a dummy implementation.")

    def check_extracted_files(self, extracted_dir: str, expected_files: list) -> bool:
        print("[Mac] check_extracted_files is a dummy implementation.")
        return False


class LinuxFileOperations(FileOperations):
    """
    A dummy implementation for Linux.
    """
    def get_download_dir(self) -> str:
        return os.path.join(os.path.expanduser("~"), "Downloads")

    def find_files(self, prefix: str) -> list:
        print("[Linux] find_files is a dummy implementation.")
        return []

    def extract_file(self, zip_file_path: str, output_dir: str) -> None:
        print("[Linux] extract_file is a dummy implementation.")

    def check_extracted_files(self, extracted_dir: str, expected_files: list) -> bool:
        print("[Linux] check_extracted_files is a dummy implementation.")
        return False


def get_file_operations_by_os() -> FileOperations:
    """
    Determines the current OS and returns a corresponding FileOperations instance.
    """
    os_type = OSInfo.get_os_type()
    if os_type == "Windows":
        return WindowsFileOperations()
    elif os_type == "Darwin":
        return MacFileOperations()
    elif os_type == "Linux":
        return LinuxFileOperations()
    else:
        raise NotImplementedError(f"Unsupported OS: {os_type}")
