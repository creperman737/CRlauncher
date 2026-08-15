from launcher.minecraft import get_minecraft_directory


def main():
    print("=" * 40)
    print("        CRLauncher Alpha")
    print("=" * 40)

    minecraft_dir = get_minecraft_directory()

    if minecraft_dir:
        print(f"Minecraft: ✓ Found")
        print(f"Location:  {minecraft_dir}")
    else:
        print("Minecraft: ✗ Not found")


if __name__ == "__main__":
    main()