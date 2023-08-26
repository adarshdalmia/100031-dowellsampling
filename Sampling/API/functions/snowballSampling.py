import random


def snowball_sampling(population_units, population_size, sample_size, reference):
  """
  Performs snowball sampling.

  Args:
    population_units: A list of population units.
    population_size: The population size.
    sample_size: The sample size.
    reference: The reference connection.

  Returns:
    A list of sample units.
  """

  sample = []
  connections = set()

  # Create a connections attribute for each unit.
  for unit in population_units:
    unit["connections"] = []

  # Select the first unit to be included in the sample.
  unit = population_units[random.randint(0, population_size - 1)]
  sample.append(unit)
  connections.add(reference)

  # Iterate until the sample size is reached.
  while len(sample) < sample_size:
    # Find a connection from the current unit.
    connection = None
    for unit_connection in unit["connections"]:
      if unit_connection not in connections:
        connection = unit_connection
        break

    # If no connection was found, prompt the user to select another connection.
    if connection is None:
      print("Could not find a connection from the current unit.")
      connection = int(input("Please select another connection: "))

    # Add the connection to the set of connections and the sample.
    connections.add(connection)
    sample.append(connection)

  return sample



population_units = [
    {"name": "John Doe", "connections": ["Jane Doe", "Peter Smith"]},
    {"name": "Jane Doe", "connections": ["John Doe", "Susan Jones"]},
    {"name": "Peter Smith", "connections": ["John Doe", "Mary Johnson"]},
    {"name": "Susan Jones", "connections": ["Jane Doe", "David Williams"]},
    {"name": "Mary Johnson", "connections": ["Peter Smith", "David Williams"]},
    {"name": "David Williams", "connections": ["Mary Johnson", "Susan Jones"]},
]
population_size = len(population_units)
sample_size = 2
reference = "John Doe"

sample = snowball_sampling(population_units, population_size, sample_size, reference)

print("The sample is:" , sample)

