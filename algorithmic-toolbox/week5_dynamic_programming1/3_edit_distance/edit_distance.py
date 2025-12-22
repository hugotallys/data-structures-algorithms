def edit_distance(first_string, second_string):
    n, m = len(first_string), len(second_string)
    edit = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        edit[i][0] = i
    for j in range(1, n+1):
        edit[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            diff = 0 if first_string[j-1] == second_string[i-1] else 1
            edit[i][j] = min(
                edit[i-1][j] + 1, edit[i][j-1] + 1, edit[i-1][j-1] + diff
            )
    return edit[m][n]

def edit_distance_no_swap(first_string, second_string):
    n, m = len(first_string), len(second_string)
    edit = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        edit[i][0] = i
    for j in range(1, n):
        edit[0][j] = j
    for i in range(1, m):
        for j in range(1, n):
            if first_string[j] == second_string[i]:
                edit[i][j] = edit[i-1][j-1]
            else: 
                edit[i][j] = min(
                    edit[i-1][j] + 1, edit[i][j-1] + 1
                )
    return edit[m-1][n-1]

if __name__ == "__main__":

    str_1 = "aba"
    str_2 = "ava"

    print(edit_distance(str_1, str_2))

    # print(edit_distance(input(), input()))
