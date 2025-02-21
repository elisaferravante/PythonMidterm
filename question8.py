def is_valid_url(url):
    """
    Function checks if a given string is a valid URL.

    :param url: The string that needs to be checked
    :return: True if valid, False otherwise
    """
    # Check if the URL starts with common http, https, etc.
    if url.startswith("http://") or url.startswith("https://"):
        if "." in url:
            # Check if there's something after the last dot, such as  .com, .org, etc.
            if len(url.split(".")[-1]) > 1:
                return True

    # If any of the conditions fail, then return False
    return False

# Example of use
print(is_valid_url("http://example.com"))  # True
print(is_valid_url("https://github.com"))  # True
print(is_valid_url("ftp://example.com"))  # False (wrong protocol)
print(is_valid_url("example.com"))  # False (no protocol)
print(is_valid_url("http://example"))  # False (no valid domain ending)