
import random as rnd
import os
import platform

# Clear Screen Function
def clear():
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("clc")

# Choosing league character
def chooseWord():

    champions= ['aatrox', 'ahri', 'akali', 'akshan', 'alistar', 'amumu', 'anivia', 'annie',
    'aphelios', 'ashe', 'aurelion sol', 'azir', 'bard', 'blitzcrank', 'brand', 'braum', 'caitlyn',
    'camile', 'cassiopeia', 'cho gath', 'corki', 'darius', 'diana', 'dr mundo', 'draven', 'ekko',
    'elise', 'evelynn', 'ezreal', 'fiddlesticks', 'fiora', 'fizz', 'galio', 'gangplank', 'garen',
    'gnar', 'gragas', 'graves', 'gwen', 'hecarim', 'heimerdinger', 'illaoi', 'irelia', 'ivern',
    'janna', 'jarvan iv', 'jax', 'jayce', 'jhin', 'jinx', 'kai sa','kalista', 'karma', 'karthus',
    'kassidin', 'katarina', 'kayle', 'kayn', 'kennen', 'kha zix', 'kindred', 'leona', 'lillia',
    'lissandra', 'lucian', 'lulu', 'lux', 'malphite', 'malzhar', 'maokai', 'master yi', 'miss fortune',
    'mordekaiser', 'morgana', 'nami', 'nasus', 'nautilus', 'neeko', 'nidalee', 'nocture', 'nunu & willump',
    'olaf', 'orianna', 'ornn', 'pantheon', 'poppy', 'pyke', 'qiyana', 'quinn', 'rakan', 'rammus',
    'rek sai', 'rell', 'renekton', 'rengar', 'riven', 'rumble', 'ryze', 'samira', 'sejuani', 'senna',
    'seraphine', 'sett', 'shaco', 'shen', 'shyvana', 'singed', 'sion', 'sivir', 'skarner', 'sona',
    'soraka', 'swain', 'sylas', 'syndra', 'tahm kench', 'taliyah', 'talon', 'taric', 'teemo', 'thresh',
    'tristana', 'trundle', 'tryndamere', 'twisted fate', 'twitch', 'udyr', 'urgot', 'varus', 'vayne',
    'veigar', 'vel koz', 'vex', 'vi', 'viego', 'viktor', 'vladimir', 'volibear', 'warwick', 'wukong',
    'xayah', 'xerath', 'xin zhao', 'yasuo', 'yone', 'yorick', 'yuumi', 'zac', 'zed', 'ziggs', 'zilean',
    'zoe', 'zyra']
    
    word = champions[rnd.randint(0, (len(champions) - 1))]
    return word

# Fragmenting the original word
def fragmentingWord(word):

    letter_list = list(word)
    lostElements = rnd.randint(1, len(word))

    while lostElements > 0:
        pos = rnd.randint(0, len(word) - 1)
        if letter_list[pos] == ' ':
            pass
        elif letter_list[pos] == '_':
            pass
        elif letter_list[pos] != ' ' or letter_list[pos] != '_':
            letter_list[pos] = '_'
            lostElements -= 1

    word = ""
    for item in letter_list:
        word += item

    return word

def draw(err):

    if err == 0:
        lifes = """
         _________
        /
        |
        |
        |
        |
        |
        """
        return lifes

    if err == 1:
        lifes = """
         _________
        /       |
        |
        |
        |
        |
        |
        """
        return lifes

    if err == 2:
        lifes = """
         _________
        /       |
        |       O
        |       
        |
        |
        |
        """
        return lifes

    if err == 3:
        lifes = """
         _________
        /       |
        |       O
        |       |
        |
        |
        |
        """
        return lifes

    if err == 4:
        lifes = """
         _________
        /       |
        |       O
        |       |\\
        |
        |
        |
        """
        return lifes

    if err == 5:
        lifes = """
         _________
        /       |       
        |       O
        |      /|\\
        |
        |
        |
        """
        return lifes

    if err == 6:
        lifes = """
         _________
        /       |
        |       O
        |      /|\\
        |      /
        |
        |
        """
        return lifes

    if err == 7:
        lifes = """
         _________
        /       |
        |       O
        |      /|\\
        |      / \\
        |
        |
        """
        return lifes
