from PIL import Image
import os

def merge_images_to_pdf(input_folder, output_pdf):
    """Merge all images in a folder (JPG, JPEG, PNG) into a single PDF."""
    supported_extensions = ('.jpg', '.jpeg', '.png')
    images = []

    for file in sorted(os.listdir(input_folder)):
        if file.lower().endswith(supported_extensions):
            try:
                img = Image.open(os.path.join(input_folder, file)).convert("RGB")
                images.append(img)
            except Exception as e:
                print(f"Skipped {file}: {e}")

    if images:
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        print(f"PDF created: {output_pdf}")
    else:
        print("No valid images found.")

script_dir = os.path.dirname(os.path.abspath(__file__))  
input_folder = os.path.join(script_dir, "img")  #
output_pdf = "merged_images.pdf" 

merge_images_to_pdf(input_folder, output_pdf)
