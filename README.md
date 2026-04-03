[README.md](https://github.com/user-attachments/files/26458504/README.md)
# GhostCalc 👻🧮

A Python-based command-line calculator that features an automated, self-cleaning workspace and session history tracking. 

## 🌟 Features

* **Complete Mathematical Operations:** Supports Addition, Subtraction, Multiplication, Division (with zero-division crash protection), and Modulo.
* **Workspace Automation (Ghost Mode):** When the application closes, all generated text logs automatically vanish from the main folder and lock away safely in a hidden `Backup` folder.
* **Seamless Session Recovery:** Upon launching the app, the system instantly locates and restores your previous history files back to your working environment.
* **History Logging:** Actively appends and logs all mathematical outcomes with clean timestamps.
* **Smart UI:** Features simulated processing pauses using Python's `time.sleep` to mimic real-time software behaviors.

## 🛠️ Built With

* **Python 3**
* `os` & `path` (System navigation and directory management)
* `shutil` (High-level automated file moving and operation)
* `datetime` & `time` (Timestamping and paced execution)

## 🚀 How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/GhostCalc.git
   ```
2. Navigate into the folder:
   ```bash
   cd GhostCalc
   ```
3. Run the script:
   ```bash
   python main.py
   ```

## 📂 How Automation Works

When you perform operations, the script stores your history in a local file. To keep your project directory clean, the terminal will actively sweep up your text logs and push them to storage states upon typing `7` to exit:
* **On Open:** `[Backup Folder] ➡️ [Main Workspace]`
* **On Close:** `[Main Workspace] ➡️ [Backup Folder]`
