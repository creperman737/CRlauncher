from launcher.minecraft import get_minecraft_directory
from launcher.versions import get_versions
from launcher.java_runtime import find_java
from launcher.launch import (
    load_version,
    get_main_class,
    get_version_id,
    get_inherited_version,
    get_libraries,
    get_library_jars,
    get_arguments,
)


def main():
    print("=" * 40)
    print("        CRLauncher Alpha")
    print("=" * 40)

    minecraft_dir = get_minecraft_directory()

    if minecraft_dir is None:
        print("Minecraft directory: Not found")
        return

    print("\nMinecraft directory:")
    print(minecraft_dir)

    java = find_java()

    print("\nJava:")

    if java:
        print(f"✓ Found: {java}")
    else:
        print("✗ Java not found")

    print("\nMinecraft versions:")

    versions = get_versions()

    if not versions:
        print("No versions found")
        return

    for version in versions:
        print(
            f"✓ {version['id']} "
            f"[{version['type']}]"
        )

    # Test version metadata
    selected_version = versions[0]["id"]

    print(f"\nSelected version: {selected_version}")

    try:
        version_data = load_version(
            selected_version,
            minecraft_dir
        )

        print(f"Main class: {get_main_class(version_data)}")
        print(f"Version ID: {get_version_id(version_data, selected_version)}")

        parent = get_inherited_version(version_data)

        if parent:
            print(f"Inherits from: {parent}")
        else:
            print("Inherits from: None")

        declared_libraries = get_libraries(version_data)
        print(f"Libraries: {len(declared_libraries)}")

        library_jars = get_library_jars(
            version_data,
            minecraft_dir
        )

        print(f"Installed library JARs: {len(library_jars)}")

        for jar in library_jars[:5]:
            print(f"  ✓ {jar}")

        arguments = get_arguments(version_data)

        print(f"JVM arguments: {len(arguments['jvm'])}")
        print(f"Game arguments: {len(arguments['game'])}")

    except Exception as error:
        print(f"Launch preparation error: {error}")


if __name__ == "__main__":
    main()