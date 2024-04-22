import os
import json

cwd_path = os.getcwd()
file_path = "files"


def read_data(file_name, key="ordered_numbers"):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param key: (str), field of a dict to return
    :return: (list, str), sequential data
    """
    if key not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open(os.path.join(cwd_path, file_path, file_name), mode="r") as json_file:
        seqs = json.load(json_file)

    return seqs[key]


def binary_search(seq, number):
    """
    Function performs binary search on !!ordered!! sequence and stores position of match if found.
    :param seq: (list): list of numbers
    :param number: (int): number to match within sequence
    :return: (int, None): index of match if found, None otherwise
    """
    left, right = (0, len(seq) - 1)

    while left <= right:
        middle = (right + left) // 2

        if number < seq[middle]:
            right = middle - 1
        elif number > seq[middle]:
            left = middle + 1
        else:
            return middle
    return None


def recursive_bs(seq, number, right_idx, left_idx=0):
    """
    Function performs binary search on !!ordered!! sequence using recursive divide and conquer and stores position of match if found.
    :param seq: (list): list of numbers
    :param number: (int): number to match within sequence
    :return: (int, None): index of match if found, None otherwise
    left_border_idx: (int): index of the left border
    right_border_index: (int): index of the right border
    """

    middle = right_idx + left_idx // 2

    if number == seq[middle]:
        return middle
    elif left_idx == right_idx:
        return None
    elif number < seq[middle]:
        return recursive_bs(seq=seq, number=number, left_idx=left_idx, right_idx=(middle - 1))
    else:
        return recursive_bs(seq, number=number, right_idx=right_idx, left_idx=(middle + 1))


def main(file_name, number):
    sequence = read_data(file_name=file_name, key="ordered_numbers")

    # iterative binary search
    binary_search(sequence, number=number)
    print(recursive_bs(seq=sequence, number=number, right_idx=len(sequence) - 1))


if __name__ == "__main__":
    my_file = "sequential.json"
    my_number = 90
    main(my_file, my_number)
