def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    count_open = 0
    count_close = 0
    if len(brackets_row) > 0:
        for br in range(0, len(brackets_row)):
            if brackets_row[br] == "(":
                count_open += 1
            elif brackets_row[br] == ")":
                count_close += 1

    if count_open == count_close:
        for br2 in range(len(brackets_row)):
            if brackets_row[0] == ")" or brackets_row[-1] == "(":
                return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    print(check_brackets("()()"))
    print(check_brackets(""))
    print(check_brackets("()()(()())"))
    print(check_brackets(")("))
    print(check_brackets(")"))
    print(check_brackets("("))
