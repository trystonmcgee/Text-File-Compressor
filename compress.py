import argparse
import os
from huffman_tree import *

def main():
    # Setting up the command line interface
    parser = argparse.ArgumentParser(description="Huffman File Compressor")
    parser.add_argument("filepath", type=str, help="The path to the text file you want to compress")
    args = parser.parse_args()
    
    # Check if the file exists
    if not os.path.exists(args.filepath):
        print(f"Error: The file '{args.filepath}' does not exist.")
        return

    # 1. Read the original text file
    print(f"Reading: {args.filepath}...")
    with open(args.filepath, 'r', encoding='utf-8') as file:
        original_text = file.read()

    # Initialize your custom class
    huffman = HuffmanTree()

    # 2. Compress the text and write it to a new file
    compressed_data = huffman.compress(original_text)
    compressed_filename = args.filepath + ".bin"
    
    with open(compressed_filename, 'w', encoding='utf-8') as file:
        file.write(compressed_data)
        
    print(f"Success! Compressed file saved to: {compressed_filename}")

    # 3. Decompress it right back to prove it works
    decompressed_text = huffman.decompress(compressed_data)
    decompressed_filename = "restored_" + os.path.basename(args.filepath)
    
    with open(decompressed_filename, 'w', encoding='utf-8') as file:
        file.write(decompressed_text)
        
    print(f"Success! Decompressed file saved to: {decompressed_filename}")

if __name__ == "__main__":
    main()