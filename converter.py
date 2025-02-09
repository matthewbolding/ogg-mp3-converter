import os
from pydub import AudioSegment
from tqdm import tqdm

def convert_ogg_to_mp3(directory):
    """Convert all .ogg files in the given directory (and subdirectories) to .mp3 with progress tracking."""
    ogg_files = []
    
    # Collect all .ogg files
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".ogg"):
                ogg_files.append(os.path.join(root, file))
    
    if not ogg_files:
        print("No .ogg files found in the directory.")
        return
    
    # Convert with progress bar
    for ogg_path in tqdm(ogg_files, desc="Converting files", unit="file"):
        mp3_path = os.path.splitext(ogg_path)[0] + ".mp3"
        print(mp3_path)

        # Convert .ogg to .mp3
        audio = AudioSegment.from_ogg(ogg_path)
        audio.export(mp3_path, format="mp3")

    print("Conversion complete!")

if __name__ == "__main__":
    directory = input("Enter the directory to scan for .ogg files: ")
    if os.path.exists(directory):
        convert_ogg_to_mp3(directory)
    else:
        print("Directory does not exist. Please enter a valid path.")
