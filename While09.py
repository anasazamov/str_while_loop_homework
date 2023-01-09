def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    answer=0
    while i<len(s):
        answer+=int(s[i])
        i+=1
    return answer