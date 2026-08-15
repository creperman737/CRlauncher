from pathlib import Path
import os
import platform
import shutil


def find_java():
    """Find Java executable on the current operating system."""

    system = platform.system()

    # 1. JAVA_HOME
    java_home = os.getenv("JAVA_HOME")

    if java_home:
        java_path = Path(java_home) / "bin"

        if system == "Windows":
            java_path = java_path / "java.exe"
        else:
            java_path = java_path / "java"

        if java_path.is_file():
            return java_path

    # 2. PATH
    java_executable = "java.exe" if system == "Windows" else "java"
    java_path = shutil.which(java_executable)

    if java_path:
        return Path(java_path)

    return None