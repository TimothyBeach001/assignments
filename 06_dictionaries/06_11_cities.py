cities = {'chicago': {'country': 'USA', 'population': 2716000, 'fact': 'Known for its deep-dish pizza.'}}

for city, info in cities.items():
    country = info['country']
    population = info['population']
    fact = info['fact']
    
    print(f"{city.title()} is in {country}.")
    print(f"It has a population of {population}.")
    print(f"Fun fact: {fact}\n")
