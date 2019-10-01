# Problem 3 - Huffman Coding
import sys
sys.path.append("c:/Users/M/Anaconda3/Lib/site-packages/")

# Your work here

import sys

def huffman_encoding(data):

    if data == "" or data == None or len(data) == 0:
        return "0", ""

    char_frequency = {}

    for char in list(data):
        char_frequency[char] = char_frequency.get(char, 0) + 1
    nested_list = [[i, j] for i, j in char_frequency.items()]

    sorted_char_frequency = sorted(nested_list, key=lambda oList: oList[1])

    Tree = {}
    sCode = "1"

    for char in sorted_char_frequency:
        Tree[char[0]] = sCode
        sCode = "1" + sCode

    leaf = ""

    for char in list(data):
        leaf += Tree[char] + "0"

    return leaf, Tree


def huffman_decoding(data, tree):
    if len(data) == 0 and tree == "":
        return ""

    Codes = data.split("0")

    stext = ""

    for code in Codes:
        for char in tree:
            if tree[char] == code:
                stext += char
                break

    return stext

if __name__ == "__main__":
    codes = {}
    print("----------------Test case 1-----------")

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print("----------------Test case 2-----------")

    b_great_sentence = "Animal kingdom"

    print("The size of the data is: {}\n".format(sys.getsizeof(b_great_sentence)))
    print("The content of the data is: {}\n".format(b_great_sentence))

    encoded_data, tree = huffman_encoding(b_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print("----------------Test case 3-----------")

    c_great_sentence = "Solar system"

    print("The size of the data is: {}\n".format(sys.getsizeof(c_great_sentence)))
    print("The content of the data is: {}\n".format(c_great_sentence))

    encoded_data, tree = huffman_encoding(c_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print("-----Test case 4 (passing string with same character) ----")

    d_great_sentence = "AAAAAAAAAAAAAAAAAAA"

    print("The size of the data is: {}\n".format(sys.getsizeof(d_great_sentence)))
    print("The content of the data is: {}\n".format(d_great_sentence))

    encoded_data, tree = huffman_encoding(d_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print("-----Test case 5 (passing empty string) -------")

    e_great_sentence = ""

    print("The size of the data is: {}\n".format(sys.getsizeof(e_great_sentence)))
    print("The content of the data is: {}\n".format(e_great_sentence))

    e_encoded_data, tree = huffman_encoding(e_great_sentence)
    if len(e_encoded_data) > 0:
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(e_encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(e_encoded_data))

        e_decoded_data = huffman_decoding(e_encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(e_decoded_data)))
        print("The content of the encoded data is: {}\n".format(e_decoded_data))
    else:
        print("Empty string passed")

# the above test cases should print the following:
"""
----------------Test case 1-----------
The size of the data is: 69

The content of the data is: The bird is the word

The size of the encoded data is: 48

The content of the encoded data is: 11111011111111111011111111011111111111101111110111111111011111110111111111101111111111110111111111011101111111111110110111111111110111111110111111111111010111101111111011111111110

The size of the decoded data is: 69

The content of the encoded data is: The bird is the word

----------------Test case 2-----------
The size of the data is: 63

The content of the data is: Animal kingdom

The size of the encoded data is: 40

The content of the encoded data is: 11101111111110111111111101111111111101111110101111111101101111111111011111111101111111011110111110111111111110

The size of the decoded data is: 63

The content of the encoded data is: Animal kingdom

----------------Test case 3-----------
The size of the data is: 61

The content of the data is: Solar system

The size of the encoded data is: 36

The content of the encoded data is: 10111011111101111111110111111110111111111101111111111101111101111111111101111011111110110

The size of the decoded data is: 61

The content of the encoded data is: Solar system

-----Test case 4 (passing string with same character) ----
The size of the data is: 68

The content of the data is: AAAAAAAAAAAAAAAAAAA

The size of the encoded data is: 32

The content of the encoded data is: 10101010101010101010101010101010101010

The size of the decoded data is: 68

The content of the encoded data is: AAAAAAAAAAAAAAAAAAA

-----Test case 5 (passing empty string) -------
The size of the data is: 49

The content of the data is: 

The size of the encoded data is: 24

The content of the encoded data is: 0

The size of the decoded data is: 49

The content of the encoded data is: 

"""