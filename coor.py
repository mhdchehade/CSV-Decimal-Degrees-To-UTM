import pyproj
import csv

def decimal_degrees_to_utm(lat, lon):
    utm_zone = (int((lon + 180) / 6) % 60) + 1
    is_northern = lat >= 0  # Check if the coordinate is in the northern hemisphere
    
    # Define the UTM projection based on the zone and hemisphere
    utm_crs = pyproj.CRS(f"+proj=utm +zone={utm_zone} +{'north' if is_northern else 'south'} +datum=WGS84")
    
    # Define the transformer
    transformer = pyproj.Transformer.from_crs(pyproj.CRS('EPSG:4326'), utm_crs)
    
    # Transform the coordinates
    easting, northing = transformer.transform(lat, lon)
    
    return easting, northing, utm_zone, 'N' if is_northern else 'S'

def convert_file(input_file, output_csv_file, output_txt_file, blockname):
    with open(input_file, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        coordinates = [(float(row[0]), float(row[1])) for row in reader]

    with open(output_csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Latitude', 'Longitude', 'Easting', 'Northing', 'UTM Zone', 'Hemisphere'])
        
        with open(output_txt_file, 'w') as txtfile:
            for lat, lon in coordinates:
                easting, northing, zone, hemisphere = decimal_degrees_to_utm(lat, lon)
                writer.writerow([lat, lon, easting, northing, zone, hemisphere])
                txtfile.write(f'(command "-insert" "{blockname}" "{easting},{northing},0" 1 1 0)\n')

# Example usage
input_file = 'input.csv'
output_csv_file = 'output.csv'
output_txt_file = 'output.txt'
blockname = input("Please enter the blockname: ")
convert_file(input_file, output_csv_file, output_txt_file, blockname)
