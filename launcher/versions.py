from pathlib import Path
from .minecraft import get_minecraft_directory


def get_versions():
    """Return installed Minecraft versions."""

    minecraft_dir = get_minecraft_directory()

    if minecraft_dir is None:
        return []

    versions_dir = minecraft_dir / "versions"

    if not versions_dir.is_dir():
        return []

    versions = []

    for folder in versions_dir.iterdir():
        if not folder.is_dir():
            continue

        version_json = folder / f"{folder.name}.json"

        if version_json.is_file():
            versions.append(folder.name)

    return sorted(versions)