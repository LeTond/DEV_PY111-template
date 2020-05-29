def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    import regex

    if regex.search(r"^(\((?1)*\))(?1)*$", brackets_row):
        return True
    elif brackets_row == "":
        return True
    return False

