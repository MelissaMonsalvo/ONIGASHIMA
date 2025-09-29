import os
import subprocess

current_directory = os.getcwd()

# List all PNG and JPG files in the current directory
image_files = [f for f in os.listdir(current_directory) if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.PNG')]

# Loop through image files and convert each to WebP
for image_file in image_files:
    # This is making the output path to have .webp extension
    webp_file = os.path.splitext(image_file.lower())[0] + '.webp'
    
    # Full file paths
    input_file = os.path.join(current_directory, image_file)
    output_file = os.path.join(current_directory, webp_file)
    
    if image_file.endswith('.png') or image_file.endswith('.PNG'):
        subprocess.run([
            'ffmpeg',
            '-i', input_file,             
            '-c:v', 'libwebp',             # Use libwebp for encoding
            '-lossless', '1',              # 1 = Preserve Alpha
            '-q:v', '80',
            output_file
        ])
        print(f"Converted PNG: {image_file} -> {webp_file}")
    
    elif image_file.endswith('.jpg'):
        # For JPG files, use lossy encoding with a quality setting
        subprocess.run([
            'ffmpeg',
            '-i', input_file,            
            '-c:v', 'libwebp',             
            '-lossless', '0',              
            '-q:v', '75',                  # Quality of image; Lower = More compression
            output_file
        ])
        print(f"Converted JPG: {image_file} -> {webp_file}")
