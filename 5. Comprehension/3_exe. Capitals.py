countries = input().split(', ')
capitals = input().split(', ')

countries_capitals = zip(countries, capitals)

countries_capitals = {s[0]: s[1] for s in countries_capitals}
{print(f'{key} -> {value}') for key, value in countries_capitals.items()}