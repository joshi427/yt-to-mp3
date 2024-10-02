# yt-to-mp3
## Build Instructions

### Prerequisites:
1. **Python**: Ensure Python is installed on your computer. You can check this by running `python --version` or `python3 --version` in a terminal. If not installed, download it from [python.org](https://www.python.org/downloads/).
2. **Git**: Ensure Git is installed by running `git --version` in the terminal. If it's not installed, download and install Git from [git-scm.com](https://git-scm.com/downloads).

### Steps:
1. **Clone the Repository**: Open a terminal and run the following command to clone the repository to your local machine:
   ```bash
   git clone <your-repo-url>

2. **Navigate to the Cloned Repo**: Move into the directory of the cloned repository:
   ```bash
   cd <your-repo-folder>

3. **Build the Executable**: Run the following command to package the application into a single executable file:
```bash
python build-app.py

4. **Locate the Executable**: After the build process completes, find the `main.exe` file in the `dist` folder. You can rename it or move it to any location you prefer.

5. **Clean Up (Optional)**: If you no don't want the repository and build files, feel free to delete the cloned repository and any associated build folders. You only need to keep the `main.exe` executable.
