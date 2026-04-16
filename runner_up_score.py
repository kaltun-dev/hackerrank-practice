# ================================
# HackerRank Challenge: Runner-Up Score
# ================================

# -------- Approach 1: One-pass loop (Optimal O(n)) --------
def runner_up_loop(arr):
    highest = float('-inf')
    second = float('-inf')

    for number in arr:
        if number > highest:
            second = highest
            highest = number
        elif number < highest and number > second:
            second = number

    return second


# -------- Approach 2: Pythonic (set + sort) --------
def runner_up_pythonic(arr):
    unique_scores = list(set(arr))
    unique_scores.sort()
    return unique_scores[-2]


# -------- Approach 3: Remove max repeatedly --------
# Removes all occurrences of the max, then finds new max

def runner_up_remove_max(arr):
    arr = list(arr)  # avoid modifying original list
    max_score = max(arr)

    while max_score in arr:
        arr.remove(max_score)

    return max(arr)


# -------- Main Execution --------
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    # Choose one:

    # Method 1
    print(runner_up_loop(arr))

    # Method 2
    # print(runner_up_pythonic(arr))

    # Method 3
    # print(runner_up_remove_max(arr))