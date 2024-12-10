# Made by cooltech334. If you want to expand on this, please give credit to me (or not I probably will never know.).
import os
import shutil

# Define categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar.gz"],
    "Others": []
}

def organize_files(directory):
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return
    
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(filepath):
            continue

        # Find the category for the file
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False

        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                # Create category folder if it doesn't exist
                category_path = os.path.join(directory, category)
                os.makedirs(category_path, exist_ok=True)

                # Move the file
                shutil.move(filepath, os.path.join(category_path, filename))
                moved = True
                break

        # If no category matched, move to "Others"
        if not moved:
            others_path = os.path.join(directory, "Others")
            os.makedirs(others_path, exist_ok=True)
            shutil.move(filepath, os.path.join(others_path, filename))
    
    print(f"Files in '{directory}' have been organized!")

# Run the organizer on a specific directory
if __name__ == "__main__":
    target_directory = input("Enter the directory to organize: ")
    organize_files(target_directory)
