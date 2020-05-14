def solution(n):
    # Your code here
    combinations = [[0 for rows in range(n)] for cols in range(n + 1)]

    # If n < 3, there are no possibilities for building the stairwell.
    for first_three in range(3):
        for num in range(first_three, n):
            combinations[first_three][num] = 1

    # For the rest of them, the formula is incremental.
    for num in range(3, n + 1):
        for bot in range(2, n):
            combinations[num][bot] = combinations[num][bot - 1]
            if bot <= num:
                combinations[num][bot] += combinations[num - bot][bot - 1]

    # This index on the matrix should contain our solution to the number of distinct combinations.
    return combinations[n][n - 1]


if __name__ == '__main__':
    # This prints out the results of this function on any value between (including) 3 and 200.
    # It's just for debugging.
    print("Format:\n Number of Bricks --> Distinct Partitions")
    for bricks in range(3, 200):
        print('   ', bricks, " --> ", str(answer(bricks)))
