def entropy_node(y):
    y = np.array(y)

    values, counts = np.unique(y, return_counts=True)

    probs = counts / counts.sum()

    probs = probs[probs > 0]

    entropy = -np.sum(probs * np.log2(probs))

    return entropy