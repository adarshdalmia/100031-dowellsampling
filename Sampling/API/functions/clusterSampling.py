from sampleSize import dowellSampleSize
from random import randrange


def dowellClusterSampling():
    m, N = dowellSampleSize()
    Yi_input = input("Enter the population values(comma separated): ")
    # assumes values are integers
    Yi = [int(i) for i in Yi_input.split(",")]
    # M = int(input("Enter the number of clusters: "))
    hi = int(input("Enter the size of a cluster: "))

    # Divide the whole populaton into clusters of size "hi"
    clusters = [Yi[i : i + hi] for i in range(0, N, hi)]

    # Make sure that clusters are heterogenous by selecting non repeating
    # samples from the cluster.
    ind = [randrange(0, len(clusters)) for _ in range(m)]
    sampled_clusters = [clusters[i] for i in ind]
    return sampled_clusters


if __name__ == "__main__":
    print(dowell_cluster_sampling())
