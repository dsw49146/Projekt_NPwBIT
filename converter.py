import argparse
import json
import yaml
import xml.etree.ElementTree as ET
import xmltodict
import xml.dom.minidom

parser = argparse.ArgumentParser(description='Konwerter plików json, xml, yaml')
parser.add_argument('input_file', help='Ścieżka do pliku wejściowego')
parser.add_argument('output_file', help='Ścieżka do pliku wyjściowego')
parser.add_argument('--format', choices=['json', 'yaml', 'xml'], help='Format pliku wyjściowego')

args = parser.parse_args()
input_file = args.input_file
output_file = args.output_file
format = args.format

if input_file.endswith('.json'):
    with open(input_file, 'r') as j:
        try:
            data = json.load(j)
        except json.JSONDecodeError as e:
            print("Błąd w parsowaniu pliku JSON: ", e)
            exit(1)

elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
    with open(input_file, 'r') as y:
        try:
            data = yaml.safe_load(y)
        except yaml.YAMLError as e:
            print("Błąd w parsowaniu pliku YAML: ", e)
            exit(1)

# -----
if format == "json":
    with open(output_file, 'w') as j:
        json.dump(data, j, indent=4, sort_keys=True)

elif format == "yml" or format == "yaml":
    with open(output_file, 'w') as y:
        yaml.dump(data, y, default_flow_style=False)
