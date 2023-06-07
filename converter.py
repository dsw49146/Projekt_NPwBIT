import argparse

parser = argparse.ArgumentParser(description='Konwerter plików json, xml, yaml')
parser.add_argument('input_file', help='Ścieżka do pliku wejściowego')
parser.add_argument('output_file', help='Ścieżka do pliku wyjściowego')
parser.add_argument('--format', choices=['json', 'yaml', 'xml'], help='Format pliku wyjściowego')
