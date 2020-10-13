# POA #262, Pattern Matching

def match(P, S):
    # Find the pattern P[0..m-1] in string S[1..n]
    # P : pattern, S : string
    n = len(S) 
    m = len(P) # n : length of S, m : length of P
    l = 0
    matched = False
    while (l <= n-m) and not matched:
        # matched = True
        # r = 0
        # while r < m and matched:
        #     matched = matched and (P[r] == S[l + r])
        #     r = r + 1
        matched = hasPattern(P, S[l:])
        l = l+1
    return (matched, l - 1 if matched else l)


def hasPattern(P, S):
    length = len(P)
    for r in range(0, length):
        if P[r] != S[r]: return False
    return True

def main():
    string = "algorithm?"
    patterns = ["gor", "gol", "alg"]

    for (i, case) in enumerate(patterns):
        result = match(case, string)
        print("(case %d) pattern: %s, string: %s, result: %s"%(i, case, string, result))


if __name__ == "__main__":
    main()

