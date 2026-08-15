from pathlib import Path
import json

from .minecraft import get_minecraft_directory


def get_versions():
    """Return installed Minecraft versions with their types."""

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

        if not version_json.is_file():
            continue

        try:
            with version_json.open("r", encoding="utf-8") as file:
                data = json.load(file)

            version_type = data.get("type", "unknown")

            versions.append({
                "id": folder.name,
                "type": version_type
            })

        except (json.JSONDecodeError, OSError):
            continue

    return sorted(versions, key=lambda version: version["id"])