import random


def dowell_pps_sampling(population_units, population_size, sample_size, size):
  """
  Performs PPS sampling on a population of units.

  Args:
    population_units: A list of the population units.
    population_size: The size of the population.
    sample_size: The desired sample size.
    size: The size of each population unit.

  Returns:
    A list of the sampled units.
  """

  # Check if the population units vary considerably in size.
  if len(set(size)) == 1:
    print("Population units do not vary considerably in size.")
    return []

  # Use Lahiri method to draw sample.
  selected_units = []
  for _ in range(sample_size):
    i = random.randint(1, population_size)
    j = random.randint(1, max(size))
    if j <= size[i - 1]:
      selected_units.append(population_units[i - 1])

  return selected_units

population_units = ["A", "B", "C", "D", "E"]
population_size = 5
sample_size = 3
size = [1, 2, 3, 4, 5]

selected_units = dowell_pps_sampling(population_units, population_size, sample_size, size)

print(selected_units)
