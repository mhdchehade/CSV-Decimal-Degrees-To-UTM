# UTM Coordinate Converter

This Python script converts decimal degrees (latitude and longitude) to UTM (Universal Transverse Mercator) coordinates. It reads coordinates from an input CSV file, converts them, and writes the results to an output CSV file and a text file with specific insert commands.

## Installation

1. **Clone the repository or download the script.**

2. **Install the required Python package:**

   The script uses the `pyproj` library to handle the coordinate transformation. You can install it using pip:

   ```bash
   pip install pyproj

## Usage

1. **Prepare your input file:**

Ensure you have an input.csv file in the same directory as the script. The file should contain latitude and longitude coordinates in the following format:

    50.1077495,26.4405801
    50.1077339,26.4414586
    50.104648,26.4422558
    50.1022657,26.4424914
    50.1023643,26.4422365
    50.1011303,26.4416934

2. **Run the script:**

Run the script in your terminal or command prompt:

    python coor.py

3. **Enter the block name:**

The script will prompt you to enter the block name. This block name will be used in the output text file.
    Please enter the blockname: YOUR_BLOCKNAME

3. **Output files:**

After running the script, you will get two output files:

    output.csv: This file contains the original coordinates along with the converted UTM coordinates, zone, and hemisphere.
    output.txt: This file contains the insert commands with the provided block name and the converted UTM coordinates.

## Example

**Input File (input.csv):**

    50.1077495,26.4405801
    50.1077339,26.4414586
    50.104648,26.4422558
    50.1022657,26.4424914
    50.1023643,26.4422365
    50.1011303,26.4416934

**Output CSV File (output.csv):**

    Latitude,Longitude,Easting,Northing,UTM Zone,Hemisphere
    50.1077495,26.4405801,677178.108295315,5548926.373623804,35,N
    50.1077339,26.4414586,677260.1397194658,5548924.474499847,35,N
    50.104648,26.4422558,677332.1934503342,5548582.349203845,35,N
    50.1022657,26.4424914,677353.1374313032,5548310.263726404,35,N
    50.1023643,26.4422365,677329.4678037756,5548321.297388174,35,N
    50.1011303,26.4416934,677280.6072109326,5548185.016358471,35,N

## Notes

Ensure your input file follows the correct format.
The script assumes the input coordinates are in WGS84 datum.

Feel free to modify the script as needed for your specific use case.