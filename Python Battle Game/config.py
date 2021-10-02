import random
from getTextures import *

# World
max_enimies = 2 # Increases over time 

# Player
player_health = 100
player_damage = random.randint(10, 20)
player_inventory = []
player_weapons = []
primary_weapon = "fist"

enemy = {
    # Easy Enemies
    "goblin":{
    "health":random.randint(10, 20),
    "damage":random.randint(1, 5),
    "draw":draw_goblin
},
    "spider":{
    "health":random.randint(5, 20),
    "damage":random.randint(5, 10),
    "draw":draw_spider
},# Medium Enemies
    "goblinsword":{
    "health":random.randint(20, 35),
    "damage":random.randint(7, 15),
    "draw":draw_goblinsword
},
    "beetle":{
    "health":random.randint(30, 60),
    "damage":random.randint(1, 5),
    "draw":draw_beetle
},# Hard Enemies 
    "wolf":{
    "health":random.randint(40, 80),
    "damage":random.randint(20, 30),
    "draw":draw_wolf
},# Boss
    "raven":{
    "health":random.randint(20, 40),
    "damage":random.randint(30, 50),
    "draw":draw_raven
}}

# Enemies List
Easy = ["goblin", "spider"]
Medium = ["goblinsword", "beetle"]
Hard = ["wolf"]
Boss = []

Enemies = ["goblin", "spider", "goblinsword", "beetle", "wolf"]

# Score of different enimies
Score = {
    "Easy":2,
    "Medium":5,
    "Hard":10,
    "Boss":15
}

# Weapon List
Weapons = {
    "fist":0,
    "Short Sword": 10,
    "Long Sword": 25
}

Weaponslst = ["Short Sword", "Long Sword"] # Place in order that player will recieve them

# Other Items
Items = {   # Multiple of the same to impove the chances of getting it and make it less likely to get the better items
    "Apple":5,
    "Apple":5,
    "Apple":5,
    "Wolf Meat":10,
    "Apple":5,
    "Apple":5,
    "Apple":5,
    "Wolf Meat":10,
    "Apple":5,
    "Apple":5,
    "Apple":5,
    "Wolf Meat":10,
    "Apple":5,
    "Apple":5,
    "Apple":5,
    "Wolf Meat":10,
    "Health Potion": 50
}

# Level Difficulty
Difficulty = {
    "Easy":5,
    "Medium":15,
    "Hard":35,
}