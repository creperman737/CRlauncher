from pathlib import Path
import json


def load_version(version_id: str, minecraft_dir: Path):
    """Load Minecraft version metadata."""

    version_file = (
        minecraft_dir
        / "versions"
        / version_id
        / f"{version_id}.json"
    )

    if not version_file.is_file():
        raise FileNotFoundError(
            f"Version metadata not found: {version_file}"
        )

    with version_file.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_main_class(version_data: dict):
    """Return Minecraft main class."""

    return version_data.get(
        "mainClass",
        "net.minecraft.client.main.Main"
    )