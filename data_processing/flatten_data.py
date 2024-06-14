import argparse
import csv

def expand_feature(feature):
    """ Expand the feature in A(B,C) format to A-B;A-C """
    if '(' in feature and ')' in feature:
        base, rest = feature.split('(')
        rest = rest.strip(')')
        variants = rest.split(',')
        return ';'.join([f"{base}-{variant}" for variant in variants])
    return feature

def process_row(row):
    """ Process each row to modify the second column """
    features = row[1].split(';')
    expanded_features = []
    for feature in features:
        expanded_feature = expand_feature(feature)
        expanded_features.append(expanded_feature)
    row[1] = ';'.join(expanded_features)
    return row

def process_tsv(input_file, output_file):
    """ Read a TSV, process it, and write the output to a new file """
    with open(input_file, mode='r', newline='') as infile, \
         open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile, delimiter='\t')
        
        for row in reader:
            new_row = process_row(row)
            writer.writerow(new_row)

def main():
    parser = argparse.ArgumentParser(description="Process a TSV file to expand features in the second column.")
    parser.add_argument("input_file", help="The input TSV file")
    args = parser.parse_args()
    output_file = args.input_file.rsplit('.', 1)[0] + "_mod.tsv"

    process_tsv(args.input_file, output_file)

if __name__ == "__main__":
    main()