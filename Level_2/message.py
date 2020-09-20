import itertools


def solution(l):
    all_permutations = []

    for x in reversed(range(1, len(l)+1)):
      all_permutations += (list(itertools.permutations(l, x)))

    new_list=[]

    for permutation in all_permutations:
        new_arr=[]
        for item in permutation:
            new_arr.append(str(item))
        new_arr=int("".join(new_arr))
        new_list.append(new_arr)

    new_list.sort(reverse=True)
    for nr in new_list:
        if nr % 3 == 0:
            return(nr)
    return 0