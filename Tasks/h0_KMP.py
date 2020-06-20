from typing import Optional, List



def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: dubstring for prefix function
    :return: prefix values table
    """
    list_ = []
    for j in range(1, len(prefix_str) + 1):
        s1 = prefix_str[:j]
        s2 = prefix_str[1:j]
        for l in range(len(s2), 0, -1):
            if s1[:l] == s2[len(s2) - l:]:
                list_.append(l)
                break
        else:
            list_.append(0)
    return list_


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """
    list_ = _prefix_fun(substr)
    i = j = 0
    while i < len(inp_string) and j < len(substr):
        if inp_string[i] == substr[j]:
            i += 1
            j += 1
        elif j <= 0:
            i += 1
        else:
            j = list_[j - 1]
    else:
        if j == len(substr):
            return i - j
        return None


if __name__ == '__main__':
    _prefix_fun("abcaabca")
    print(_prefix_fun)
