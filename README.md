# Huffman File Compressor

A Python-based tool that compresses and decompresses text files using the Huffman Coding algorithm. 

This project was built from scratch and a with bit of help from AI (only with compress.py) using Python to demonstrate a my understanding of data structures, object-oriented programming, and file I/O operations.

## 🚀 Features
*Compression*: Shrinks file sizes by mapping characters to shorter binary codes and rare characters to longer ones.
*Decompression*: Accurately reconstructs the exact original text from the compressed binary format.
*Object-Oriented Design*: Encapsulates the algorithm within a highly modular `HuffmanTree` class.
*Command Line Interface*: Easy-to-use terminal execution built with Python's `argparse` library.

## 🧠 Core Data Structures Used
This project relies heavily on foundational computer science concepts:
*Hash Maps (`collections.Counter`)*: Used to calculate the exact frequency of every character in the input file.
*Priority Queues (`heapq`)*: A min-heap structure used to efficiently fetch the lowest-frequency characters while building the tree.
*Binary Trees*: A custom `HuffmanNode` class structures the data bottom-up to generate the optimal prefix codes.

## 🛠️ How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/trystonmcgee/Text-File-Compressor.git](https://github.com/trystonmcgee/Text-File-Compressor.git)
cd Text-File-Compressor
