def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    count = 0
    for elem in relevant:
        if elem in recommended[:k]:
            count +=1
    precision_k = count/k
    recall_k = count/len(relevant)
    res = [precision_k, recall_k]
    return res
