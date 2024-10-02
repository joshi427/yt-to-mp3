def install_packages(requirements_file='requirements.txt'):
    import subprocess
    import sys
    try:
        with open(requirements_file, 'r') as file:
            packages = file.readlines()

        for package in packages:
            package = package.strip()
            if package:
                print(f"Installing package: {package}")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])

        print("All packages installed successfully!")

    except FileNotFoundError:
        print(f"Error: {requirements_file} not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during installation: {e}")


def build_app(script='main.py'):
    import subprocess
    import sys
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

        print(f"Packaging {script} into a single executable...")
        subprocess.check_call([sys.executable, "-m", "PyInstaller", script, "--onefile", "-w"])

        print(f"{script} has been packaged successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during packaging: {e}")


if __name__ == "__main__":
    install_packages()
    build_app()