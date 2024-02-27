import argparse
from pathlib import Path
from PIL import Image
import pillow_heif

def convert_heic_to_jpeg(heic_path, output_directory):
    output_path = output_directory / (heic_path.stem + ".jpg")

    with open(heic_path, "rb") as f:
        heic_data = f.read()

    heic_image = pillow_heif.read_heif(heic_data)
    for img in heic_image: 
        jpeg_image = Image.frombytes(
            img.mode,
            img.size,
            img.data,
            'raw',
            img.mode,
            img.stride,
        )
    jpeg_image.save(output_path, format="JPEG")

def convert_directory(input_directory, output_directory):
    input_path = Path(input_directory)
    output_path = Path(output_directory)

    if not output_path.exists():
        output_path.mkdir(parents=True)

    for heic_path in input_path.glob("*.heic"):
        convert_heic_to_jpeg(heic_path, output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert HEIC files in a directory to JPEG.")
    parser.add_argument("-i", "--input", dest="input_directory", required=True, help="Input directory containing HEIC files")
    parser.add_argument("-o", "--output", dest="output_directory", required=True, help="Output directory for JPEG files")

    args = parser.parse_args()

    convert_directory(args.input_directory, args.output_directory)
