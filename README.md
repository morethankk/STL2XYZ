# STL to XYZ Converter

This script converts STL files to XYZ coordinate information.

## Requirements

- Python 3.x

## Usage

To use the script, run the following command:

```bash
python stl_to_xyz.py <input_stl_file> <output_xyz_file>
```

### Example

```bash
python stl_to_xyz.py example.stl output.xyz
```

## Description

The script reads an STL file and extracts the XYZ coordinates of the vertices. The coordinates are written to an output file in XYZ format, with each coordinate rounded to 5 decimal places.

While script "stl_to_xyz_full.py" will preserving the original precision.

## Error Handling

- If the input file is not found, an error message will be displayed.
- If any other error occurs during the conversion process, an error message will be displayed.

## License

This project is licensed under the MIT License.
