from pathlib import Path
import json


def load_version(version_id: str, minecraft_dir: Path) -> dict:
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


def get_main_class(version_data: dict) -> str:
    """Get Minecraft main class."""

    return version_data.get(
        "mainClass",
        "net.minecraft.client.main.Main"
    )


def get_version_id(version_data: dict, fallback: str) -> str:
    """Get the real Minecraft version ID."""

    return version_data.get("id", fallback)


def get_inherited_version(version_data: dict):
    """Get parent version if this is a derived installation."""

    return version_data.get("inheritsFrom")


def get_libraries(version_data: dict) -> list:
    """Return libraries declared by the version."""

    return version_data.get("libraries", [])


def get_library_jars(
    version_data: dict,
    minecraft_dir: Path
) -> list[Path]:
    """Find installed library JAR files.

    Scans version_data['libraries'] for a downloads.artifact.path entry and
    returns Path objects for files that actually exist under the Minecraft
    'libraries' directory.
    """

    libraries_dir = minecraft_dir / "libraries"
    jars: list[Path] = []

    for library in version_data.get("libraries", []):
        downloads = library.get("downloads", {})
        artifact = downloads.get("artifact")

        if not artifact:
            continue

        path = artifact.get("path")

        if not path:
            continue

        jar = libraries_dir / path

        if jar.is_file():
            jars.append(jar)

    return jars


def get_arguments(version_data: dict) -> dict:
    """Return JVM and game arguments."""

    arguments = version_data.get("arguments", {})

    return {
        "jvm": arguments.get("jvm", []),
        "game": arguments.get("game", [])
    }