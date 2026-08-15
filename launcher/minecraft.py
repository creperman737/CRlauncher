from pathlib import Path
import os
import platform


def get_minecraft_directory() -> Path | None:
    """Return the default Minecraft directory for the current OS."""

    system = platform.system()

    if system == "Windows":
        appdata = os.getenv("APPDATA")
        if not appdata:
            return None

        minecraft_dir = Path(appdata) / ".minecraft"

    elif system == "Linux":
        minecraft_dir = Path.home() / ".minecraft"

    elif system == "Darwin":
        minecraft_dir = (
            Path.home()
            / "Library"
            / "Application Support"
            / "minecraft"
        )

    else:
        return None

    if minecraft_dir.is_dir():
        return minecraft_dir

    return None