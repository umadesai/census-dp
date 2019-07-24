from laplace import laplace_mech


def above_threshold(querylist, T, epsilon, sensitivity=1.0, forward=True):
    """ Above threshold technique for a list of queries with a given sensitivity """
    bud_share = epsilon/3.0
    noisy_T = laplace_mech(T, bud_share, sensitivity)
    noisy_answers = laplace_mech(querylist, bud_share, sensitivity)
    num_queries = len(querylist)
    myiter = range(num_queries) if forward else range(num_queries-1, -1, -1)
    index = next((x for x in myiter if noisy_answers[x] >= noisy_T), None)
    return index
