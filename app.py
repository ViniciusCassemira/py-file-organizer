from datetime import datetime
from pathlib import Path

# Filter the date and current time
current_time = datetime.now().strftime('%d/%m/%Y - %X')

# Function to log messages with the current timestamp
def log_message(message):
    with open("logs.txt", "a") as file:
        file.write(f"[{current_time}]: {message}\n")

# Create destination folder
def create_folder(path):
    path.mkdir()
    log_message(f"Folder created: {path}")

# Return True if folder exists
def check_folder(path):
    if not path.exists():
        log_message(f"Folder not found: {path}")
        return False
    else:
        return True

# Get folder origin and destination from user
folder_origin = input("Enter the folder origin: ")
folder_destination = input("Enter the folder destination: ")

if(not check_folder(Path(folder_origin))):
    exit()

if(not check_folder(Path(folder_destination))):
    create_folder(Path(folder_destination))

# Iterate over files in the origin folder
for file in Path(folder_origin).iterdir():
    # Get file suffix and create folder path
    suffix_format = file.suffix.replace(".", "")

    # Create path with suffix
    suffix_path = Path(f"{folder_destination}/{suffix_format}")
    
    # Create folder if not exists
    if(not check_folder(suffix_path)):
        create_folder(suffix_path)

    # Move file to the corresponding folder
    file.rename(suffix_path / file.name)

    # Log the file move
    log_message(f"The file {file.name} has been saved in the folder: {suffix_path}")