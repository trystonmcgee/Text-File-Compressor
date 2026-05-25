import heapq
from collections import Counter

# Creating a Huffman Tree Node to represent each character and its frequency
# Input: 
    # char: The character being represented (None for internal nodes)# 
    # freq: The frequency of the character in the text (or combined frequency for internal nodes) 
# Output:
    # A node in the Huffman Tree with pointers to left and right children
class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char 
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Represents the Huffman Tree and contains methods to build the tree and generate codes
# Input:
    # None (the tree is built from the input text)
# Output:
    # A Huffman Tree with the root node and a dictionary of character codes
class HuffmanTree:
    def __init__(self):
        self.root = None
        self.codes = {}
    
    # Builds the Huffman Tree based on the frequency of characters in the input text
    def _build_tree(self, text):
        char_frequency = Counter(text)
        heap = [HuffmanNode(char, freq) for char, freq in char_frequency.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            merged = HuffmanNode(freq=left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(heap, merged)

        self.root = heap[0] 

    # Generates binary codes for each character by traversing the Huffman Tree
    # Input:
        # node: The current node in the tree being traversed
        # current_code: The binary code accumulated so far during the traversal
    # Output:
        # A dictionary mapping each character to its corresponding binary code
    def _generate_codes(self, node, current_code=""):
        if node is not None:
            if node.char is not None:
                self.codes[node.char] = current_code

            self._generate_codes(node.left, current_code + "0")
            self._generate_codes(node.right, current_code + "1")

    # Compresses the input text using the generated Huffman codes
    # Input:
        # text: The original text to be compressed
    # Output:
        # A string of binary digits representing the compressed version of the input text
    def compress(self, text):
        if not text:
            return ""
        
        # Builds the tree based on some text
        self._build_tree(text)

        # Generates the binary codes for each character in the text
        self._generate_codes(self.root)

        # Compresses the text by replacing each character with its corresponding binary code
        return ''.join(self.codes[char] for char in text)
    
    # Decompresses a binary string back to the original text using the Huffman Tree
    # Input:
        # binary_string: The string of binary digits to be decompressed 
    # Output:
        # The original text that was compressed into the binary string
    def decompress(self, binary_string):
        if not binary_string:
            return ""
        
        decoded_text = []
        current_node = self.root

        # Traverses the Huffman Tree based on the binary digits in the string
        for num in binary_string:
            if num == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right
            
            if current_node.char is not None:  # Found a leaf node
                decoded_text.append(current_node.char)
                current_node = self.root  # Reset to the root for the next character

        return ''.join(decoded_text)