def edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]

while True:
    str1 = input("Original sentence: ")
    str2 = input("Edited sentence: ")


    edit_d = edit_distance(str1, str2)
    normalized_ED = edit_d/ max(len(str1), len(str2))

    print("Calcucalted edit distance:")
    print(edit_d)
    print()
    print("Percentage edit distance:")
    print(normalized_ED*100)