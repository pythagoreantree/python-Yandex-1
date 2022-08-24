def lbinsearch(left, right, check, params):
    while left < right:
        m = (left + right) // 2
        # print(left, r, m)
        if check(m, params):
            right = m
            # print("right", r)
        else:
            left = m + 1
            # print("left", left)
    return left


def check_scores(fives, params):
    twos, threes, fours = params
    final_score = (2*twos + 3*threes + 4*fours + 5*fives)/(twos + threes + fours + fives)
    # print(final_score)
    score_tail = final_score - int(final_score)
    # print(score_tail)
    final_score = int(final_score)
    if score_tail >= 0.5:
        final_score += 1
    # print(final_score)
    # print("############")
    return final_score >= 4


a = int(input())
b = int(input())
c = int(input())

how_much_fives = lbinsearch(0, 2*(a+b+c), check_scores, (a, b, c))
print(how_much_fives)
