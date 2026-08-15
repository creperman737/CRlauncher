from launcher.minecraft import get_minecraft_directory
from launcher.versions import get_versions


def main():
    print("=" * 40)
    print("        CRLauncher Alpha")
    print("=" * 40)

    minecraft_dir = get_minecraft_directory()

    if minecraft_dir:
        print(f"Minecraft directory:")
        print(minecraft_dir)
    else:
        print("Minecraft directory: Not found")
        return

    print("\nMinecraft versions:")

    versions = get_versions()

    if not versions:
        print("No versions found")
    else:
        for version in versions:
            print(f"✓ {version}")


if __name__ == "__main__":
    main()