import argparse
import struct

def convert_stl_to_xyz(input_file, output_file):
    """Converts an STL file to XYZ format."""
    try:
        with open(input_file, 'rb') as stl_file, open(output_file, 'w') as xyz_file:
            # Skip header
            stl_file.read(80)
            # Read number of triangles
            num_triangles = struct.unpack('<I', stl_file.read(4))[0]

            for _ in range(num_triangles):
                # Skip normal vector
                stl_file.read(12)
                # Read vertices
                for _ in range(3):
                    x, y, z = struct.unpack('<fff', stl_file.read(12))
                    xyz_file.write(f"{round(x, 5)} {round(y, 5)} {round(z, 5)}\n")
                # Skip attribute byte count
                stl_file.read(2)

    except FileNotFoundError:
        print(f"Error: File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Convert STL file to XYZ format.")
    parser.add_argument("input", help="Path to the input STL file.")
    parser.add_argument("output", help="Path to the output XYZ file.")
    args = parser.parse_args()

    convert_stl_to_xyz(args.input, args.output)

if __name__ == "__main__":
    main()