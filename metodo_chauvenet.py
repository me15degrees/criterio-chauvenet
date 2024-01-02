import math
def standard_normal_cdf(x):
    #calcula a probabilidade cumulativa da cauda esquerda para x em uma distribuição normal padrão.
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

def chauvenet_criterion(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((num - mean) ** 2 / (n - 1) for num in data)
    std_dev = variance ** 0.5
    outliers = []

    for num in data:
        z = (num - mean) / std_dev
        prob_left = standard_normal_cdf(z)
        prob_right = 1 - prob_left
        dmax = 1 - (1 / (2 * n))
        
        if prob_right < dmax:
            outliers.append(num)
    return outliers