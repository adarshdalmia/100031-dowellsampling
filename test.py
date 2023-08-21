import random

# Hardcoded population data
population = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 'Item 7', 'Item 8', 'Item 9', 'Item 10']

# Simple Random Sampling
def simple_random_sampling(sample_size):
    return random.sample(population, sample_size)

# Systematic Sampling
def systematic_sampling(sample_size, start_index):
    sampled_items = []
    for i in range(start_index - 1, len(population), sample_size):
        sampled_items.append(population[i])
    return sampled_items

# Purposive Sampling
def purposive_sampling(selected_items):
    return selected_items

# Cluster Sampling
# def cluster_sampling(selected_clusters, sample_size_per_cluster):
#     sampled_items = []
#     for cluster in selected_clusters:
#         sampled_items.extend(random.sample(cluster, sample_size_per_cluster))
#     return sampled_items

# Stratified Sampling
def stratified_sampling(strata, sample_size_per_stratum):
    sampled_items = []
    for stratum in strata:
        sampled_items.extend(random.sample(stratum['items'], sample_size_per_stratum))
    return sampled_items

# Sample input for each method
sample_size = 3
start_index = 2
selected_items = ['Item 1', 'Item 3', 'Item 5']
selected_clusters = [['Item 1', 'Item 2', 'Item 3'], ['Item 6', 'Item 7', 'Item 8'], ['Item 9', 'Item 10']]
strata = [
    {'age_group': '18-25', 'items': ['Item 1', 'Item 4']},
    {'age_group': '26-30', 'items': ['Item 2', 'Item 5', 'Item 8']},
    {'age_group': '31-35', 'items': ['Item 3', 'Item 6', 'Item 9']}
]

# Call the functions with the sample input
print("Simple Random Sampling:", simple_random_sampling(sample_size))
print("Systematic Sampling:", systematic_sampling(sample_size, start_index))
print("Purposive Sampling:", purposive_sampling(selected_items))
# print("Cluster Sampling:", cluster_sampling(selected_clusters, sample_size))
print("Stratified Sampling:", stratified_sampling(strata, sample_size))
