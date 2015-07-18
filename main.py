import random

# Terrain possibilities of the City
terrains = [
    "Plains", "Hills", "Mountain", "Desert", "Forest", "Cavern", "Coastal", "Swamp"
]

# Special Features of the City
features = [
    "None", "Cathedral", "Fort", "Walls", "Tower"
]

# Governing Body
governments = [
    "Autocracy", "Bureaucracy", "Democracy", "Dictatorship", "Magocracy", "Militocracy", "Monarchy", "Oligarchy",
    "Patriarchy", "Meritocracy", "Plutocracy", "Republic", "Satrapy", "Theocracy"
]

# Titles of the government
titles = {
    "male": ["Emperor", "King", "Prince", "Duke", "Earl", "Count", "Baron", "Knight"],
    "female": ["Empress", "Queen", "Princess", "Duchess", "Marquise", "Countess", "Baroness"]
}

# Temperatures currently reigning in the city
temperatures = [
    "Freezing", "Cold", "Mild", "Warm", "Hot", "Canicular"
]

# Events occurring in the city
events = [
    "None", "Carnival", "Circus", "Religious Festival", "Market", "Coronation", "Regional Tournament",
]

# The level of criminality in the city
criminality = [
    "None", "Controlled", "Low", "Medium", "High", "Rampant", "In Control"
]

# The level of religious following of the city and its inhabitants
religions = [
    "Banned", "Discouraged", "Tolerated", "Neutral", "Encouraged", "Mandatory"
]

# Difficulties that a city can face
difficulties = [
    "Bandits", "Famine", "Disease", "Monsters", "Magic", "Civil War", "Disappearances", "Raids", "Foreign Conquest",
    "Prison Breakout", "Rebellion"
]

wealth = [
    "Squalid", "Poor", "Modest", "Wealthy", "Filthy Rich"
]

# Economy of the city
economy = [
    "Resources", "Agriculture", "Crafting", "Knowledge", "Pleasure", "Commerce"
]

# Potential Famous People in the city
famous_people = [
    "None", "Blacksmith", "Liberian", "Jeweler", "Noble", "Soldier", "Scientist", "Priest", "Wizard"
]

#
# Ranges
#

# Population range
population = {
    "min": 200,
    "max": 22000
}


# Generate a city based on these lists!
print("Terrain: " + random.choice(terrains))
print("Feature: " + random.choice(features))
print("Government: " + random.choice(governments))
print("Highest Rank: " + random.choice(titles["male" if random.randint(1, 100) >= 40 else "female"]))
print("Temperatures: " + random.choice(temperatures))
print("Events: " + random.choice(events))
print("Criminality: " + random.choice(criminality))
print("Religious Liberty: " + random.choice(religions))
print("Difficulties: " + random.choice(difficulties))
print("Wealth: " + random.choice(wealth))
print("Economy: " + random.choice(economy))
print("Famous Person: " + random.choice(famous_people))
print('Population: '),
print(random.randint(population["min"], population["max"]))
