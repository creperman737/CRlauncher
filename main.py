from launcher.minecraft import get_minecraft_directory
from launcher.versions import get_versions
from launcher.java_runtime import find_java
from launcher.launch import load_version, get_main_class


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

        main_class = get_main_class(version_data)

        print(f"Main class: {main_class}")

    except Exception as error:
        print(f"Launch preparation error: {error}")


if __name__ == "__main__":
    main()