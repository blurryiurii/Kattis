# https://open.kattis.com/problems/rankproblem
# input
ranks, num_swaps = map(int, input().split())
ranks = [f"T{i}" for i in range(1, ranks + 1)]
swaps = list()

# swaps
for _ in range(num_swaps):
    w, l = input().split()

    win_inx = ranks.index(w)
    loss_inx = ranks.index(l)

    if win_inx > loss_inx:
        ranks = ranks[:loss_inx] + ranks[loss_inx + 1 : win_inx + 1] + [ranks[loss_inx]] + ranks[win_inx + 1:]

# output
print(" ".join(ranks))