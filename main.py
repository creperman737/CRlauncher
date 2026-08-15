from launcher.minecraft import get_minecraft_directory
from launcher.versions import get_versions
from launcher.java_runtime import find_java


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

    # Java
    java = find_java()

    print("\nJava:")

    if java:
        print(f"✓ Found: {java}")
    else:
        print("✗ Java not found")

    # Minecraft versions
    print("\nMinecraft versions:")

    versions = get_versions()

    if not versions:
        print("No versions found")
    else:
        for version in versions:
            print(
                f"✓ {version['id']} "
                f"[{version['type']}]"
            )


if __name__ == "__main__":
    main()