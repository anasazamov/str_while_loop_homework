def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    answer=0
    while i<len(s):
        if int(s[i])%2!=0:
            answer+=int(s[i])
        i+=1
    return answer

print(main("589765"))