def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    if not values:
        return []
    
    # 1. Trier les valeurs
    sorted_vals = sorted(values)
    
    # 2. Cumuler les rangs (1-indexés) et les occurrences
    rank_sums = {}
    counts = {}
    for rank, val in enumerate(sorted_vals, 1):
        rank_sums[val] = rank_sums.get(val, 0) + rank
        counts[val] = counts.get(val, 0) + 1
    
    # 3. Calculer le rang moyen pour chaque valeur unique
    avg_ranks = {val: rank_sums[val] / counts[val] for val in rank_sums}
        
    # 4. Réassigner les rangs moyens dans l'ordre initial
    return [avg_ranks[x] for x in values]
    

    