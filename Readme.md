# HEIC to JPEG Converter

This Python script converts HEIC files to JPEG format using the `pillow_heif` library.

## Prerequisites

Make sure you have Python installed on your system. You can install the required libraries by running:

```bash
pip install pillow_heif
```

## Usage
### Running the Script
1. Clone the repository or download the script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
To convert a single HEIC file:

```bash
python heic_jpeg_converter.py -i input_directory -o output_directory
```

'-i' or '--input': Input directory containing HEIC files.

'-o' or '--output': Output directory for JPEG files.
### Example
```bash
python heic_jpeg_converter.py -i path/to/heic_files -o path/to/output_directory
```
This will convert all HEIC files in the specified input directory and save the resulting JPEG files in the output directory.

## Notes
The script uses pillow_heif to read HEIC files and convert them to JPEG.
Output JPEG files will have the same base filename as the original HEIC file.
## License
This project is licensed under the MIT License - see the LICENSE file for details.