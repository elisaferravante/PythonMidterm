def find_pattern(text):
    """
    Finds occurrences of a pattern that starts with 'b', and ends with 'Bob'.

    :param text:  input text to search through
    :return:  count of matching patterns
    """
    count = 0
    start = 0

    while True:
        start = text.find("b", start)  # Look for 'b' in the text
        if start == -1:
            break

        # Look for 'Bob' after 'b'
        end_index = text.find("Bob", start)
        if end_index != -1 and end_index > start:
            count += 1 #finding match
            start = end_index + 1
        else:
            start += 1

    return count
#example of use
sample_text = "bSomethingBob b123Bob bHelloBob bTestBob"
print("Number of matches:", find_pattern(sample_text))