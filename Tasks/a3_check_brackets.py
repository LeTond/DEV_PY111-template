
from Tasks import a0_my_stack as stack


def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    import regex

    stack.clear()

    for simb in brackets_row:
        if simb == "(":
            stack.push(")")
        elif simb == ")":
            if simb != stack.pop():
                return False
    if len(stack.lis) != 0:
        return False
    return True


if __name__ == "__main__":
    print(check_brackets("()()"))
    print(check_brackets(""))
    print(check_brackets("()()(()()))"))
    print(check_brackets(")("))
    print(check_brackets(")"))
    print(check_brackets("("))