import pandas as pd
import argparse

def process_tsv(input_file, output_file):
    # Read the TSV file without the header into a pandas DataFrame
    df = pd.read_csv(input_file, sep='\t', header=None)

    # Process the specific column to remove spaces after commas
    df[2] = df[2].apply(lambda x: ','.join([feature.strip() for feature in x.split(',')]))

    # Write the modified DataFrame back to a TSV file without the header
    df.iloc[1:].to_csv(output_file, sep='\t', header=False, index=False)

    print("Processing complete. Output saved to", output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a TSV file column to remove spaces after commas.")
    parser.add_argument('input_file', help="Input TSV file")
    args = parser.parse_args()
    output_file = args.input_file.rsplit('.', 1)[0] + "_mod.tsv"
    process_tsv(args.input_file, output_file)