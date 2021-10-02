import random
newAccountFunds = 10000
playerfunds = 0
user = ""

numhorse = 5 # Number of horses
nummodels = 2 # Number of textures per horse

odds = []
for i in range(numhorse):
    odds.append(random.randint(1, 5))

TextureMappings = {
    "horse1_1": "Game Art\\horse-black1.png",
    "horse1_2": "Game Art\\horse-black2.png",

    "horse2_1": "Game Art\\horse-brown1.png",
    "horse2_2": "Game Art\\horse-brown2.png",

    "horse3_1": "Game Art\\horse-golden1.png",
    "horse3_2": "Game Art\\horse-golden2.png",

    "horse4_1": "Game Art\\horse-gray1.png",
    "horse4_2": "Game Art\\horse-gray2.png",

    "horse5_1": "Game Art\\horse-white1.png",
    "horse5_2": "Game Art\\horse-white2.png"
}