import random
import time
starter_pokemon = ['Pikachu', 'Bulbasaur', 'Squirtle', 'Charmander']
wild_pokemon = ['Pidgey', 'Ratatta', 'Spearow', 'Mankey', 'Evee' ]
team =[]
hp_w = 50
hp_s = 50
#functions---------------------------functions------------------
def introDisplay():
    print("""                                ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
                                By Varun KJ""")
    print('Welcome to the world of pokemon!')
    time.sleep(2)
    print('Choose a starter pokemon:')

def chooseStarter(n):

    starter = starter_pokemon[n-1]
    print("Hooray, you picked " +starter ,'!!')
    if n == 1:
        print("""`;-.          ___,
  `.`\_...._/`.-"`
    \        /      ,
    /()   () \    .' `-._
   |)  .    ()\  /   _.'
   \  -'-     ,; '. <
    ;.__     ,;|   > \
   / ,    / ,  |.-'.-'
  (_/    (_/ ,;|.<`
    \    ,     ;-`
     >   \    /
    (_,-'`> .'
         (_,'""")
    elif n == 2:
        print("""             `;,;.;,;.;.'
              ..:;:;::;: 
        ..--''' '' ' ' '''--.  
      /' .   .'        '.   .`\
     | /    /            \   '.|
     | |   :             :    :|
   .'| |   :             :    :|
 ,: /\ \.._\ __..===..__/_../ /`.
|'' |  :.|  `'          `'  |.'  ::.
|   |  ''|    :'';          | ,  `''\
|.:  \/  | /'-.`'   ':'.-'\ |  \,   |
| '  /  /  | / |...   | \ |  |  |';'|
 \ _ |:.|  |_\_|`.'   |_/_|  |.:| _ |
/,.,.|' \__       . .      __/ '|.,.,\
     | ':`.`----._____.---'.'   |
l42   \   `:"""'""'   
       ',-,-',             '-=,=, """" ')
    elif n == 3:
        print("""\ 
               _,........__
            ,-'            "`-.
          ,'                   `-.
        ,'                        \
      ,'                           .
      .'\               ,"".       `
     ._.'|             / |  `       \
     |   |            `-.'  ||       `.
     |   |            '-._,'||       | \
     .`.,'             `..,'.'       , |`-.
     l                       .'`.  _/  |   `.
     `-.._'-   ,          _ _'   -" \  .     `
`.'-.`-...,---------','         `. `....__.
.'        `"-..___ ___  _   __,'\          \  \     \
\_ .          |   `    `.           . \     \
  `.          |              `.          |  .     L
    `.        |`--...________.'.        j   |     |
      `._    .'      |          `.     .|   ,     |
         `--,\       .            `7""' |  ,      |
            ` `      `            /     |  |      |    _,-'___`-.
             \ `.     .          /      |  '      |  ,'          `.
              \  v.__  .        '       .   \    /| /              \
               \/    `""\`.       \   \  /.''                |
                `        .        `._ ___,j.  `/ .-       ,---.     |
                ,`-.      \         ."     `.  |/        j     `    |
               /    `.     \       /         \ /         |     /    j
              |       `-.   7-.._ .          |"          '         /
              |          `./_    `|          |            .     _,'
              `.           / `----|          |-............`---'
                \          \      |          |
               ,'           )     `.         |
                7____,,..--'      /          |
                                  `---.__,--.'mh          """)
    elif n == 4:
        print("""
              .--""`-..
            ,'          `.
          ,'          __  `.
         /|          " __   \
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,
      ._     '           _'  |                    , ' \ `
  `.. `.`-...___,...---    |       __,.        ,`"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \
-:..     `. `-..--_.,.<       `"      / `.        `-/ |   .
  `,         '     `.              ,'         |   |  ',,
    `.      '            '            /          '    |'. |/
      `.   |              \       _,-'           |       ''
        `._'               \   '"\                .      |
           |                '     \                `._  ,'
           |                 '     \                 .'|
           |                 .      \                | |
           |                 |       L              ,' |
           `                 |       |             /   '
            \                |       |           ,'   /
          ,' \               |  _.._ ,-..___,..-'    ,'
         /     .             .      `!             ,j'
        /       `.          /        .           .'/
       .          `.       /         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,\
   -" /`.         _,'     | _  _  _.|
            `' '! |! / """)
    team.append(starter)
    print('Your team was updated!')
    print('Your Team: ' +str(team))




def battle(i):
    hp_w = 50
    hp_s = 50
    while True:
        if i == 3:
            print('you ran away...')
            break
        elif i == 2:
            print('Go, Pokeball!!')
            print("""
 ────▄███▓▓▓▓▓▓▓▓▓▓▓███▄─────
────███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███────
───██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██───
──██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██──
─██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██─
██▓▓▓▓▓▓▓▓▓███████▓▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓▓██░░░░░██▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓██░░███░░██▓▓▓▓▓▓▓██
███████████░░███░░███████████
██░░░░░░░██░░███░░██░░░░░░░██
██░░░░░░░░██░░░░░██░░░░░░░░██
██░░░░░░░░░███████░░░░░░░░░██
─██░░░░░░░░░░░░░░░░░░░░░░░██─
──██░░░░░░░░░░░░░░░░░░░░░██──
───██░░░░░░░░░░░░░░░░░░░██───
────███░░░░░░░░░░░░░░░███────
─────▀███░░░░░░░░░░░███▀─────
────────▀███████████▀────────""")
            j = random.randint(1,3)
            if j == 3:
                print('HOORAY!! you caught a ' +wildPoke,'!')
                team.append(wildPoke)
                print('Your team was updated!!')
                print('Your Team: ' +str(team))
                break
            else:
                print('oh no! the pokemon escaped!')
                print('what would you like to do?')
                print('Enter 1 to select "Battle", 2 for "Pokeball", 3 for "Run"')
                i = int(input())
        elif i == 1:
            starter = team[0]

            if starter == 'Pikachu':
                moveset = ['Thundershock']
                print("Pikachu's moves: " + str(moveset))

                if wildPoke == 'Spearow' or 'Pidgey':
                    print('The attack was super effective!!')
                    damage = random.randint(30, 40)
                    hp_w = hp_w - damage
                    print("The opponent's attack did normal damage!")
                    hp_s = hp_s - 15
                    print('The opponent pokemon took ' + str(damage), 'damage!')

                    #PRINT HPS HERE
                    if hp_w <= 0:
                        print('Congratulations! you won the battle!')
                        break
                    elif hp_s <= 0:
                        print('Oh no! your pokemon fainted')
                        break
                    print('what would you like to do?')
                    print('Enter 1 to select "Battle", 2 for "Pokeball", 3 for "Run"')
                    i = int(input())
                elif wildPoke == 'Mankey' or 'Ratatta':
                    print('The attack was normally effective')
                    damage = random.randint(10, 20)
                    hp_w = hp_w - damage
                    print("The opponent's attack did normal damage!")
                    hp_s = hp_s - 15
                    if hp_w <= 0:
                        print('Congratulations! you won the battle!')
                        break
                    elif hp_s <= 0:
                        print('Oh no! your pokemon fainted')
                        break
                    print('what would you like to do?')
                    print('Enter 1 to select "Battle", 2 for "Pokeball", 3 for "Run"')
                    i = int(input())

            #BULBASAUR
            elif starter == 'Bulbasaur':
                moveset = ['Tackle']
                print("Bulbasaur's moves: " +str(moveset))
                print('The attack was normally effective')
                damage = random.randint(10, 20)
                hp_w = hp_w - damage
                print( 'The opponent pokemon took '+str(damage), 'damage!')
                print("The opponent's attack did normal damage!")
                damage2 = random.randint(12, 18)
                hp_s = hp_s - damage2
                print('Bulbasaur took ' +str(damage2), ' damage!!')
                print('what would you like to do?')
                print('Enter 1 to select "Battle", 2 for "Pokeball", 3 for "Run"')
                i = int(input())
                if hp_w <= 0:
                    print('Congratulations! you won the battle!')
                    break
                elif hp_s <= 0:
                    print('Oh no! your pokemon fainted')
                    break
            elif starter == 'Charmander':
                moveset = ['Scratch']
                print("Charmander's moves: " + str(moveset))
                print('The attack was normally effective')
                damage = random.randint(15, 23)
                hp_w = hp_w - damage
                print('The opponent pokemon took ' +str(damage), 'damage!')
                print("The opponent's attack did normal damage!")
                damage2 = random.randint(12, 18)
                hp_s = hp_s - damage2
                print('Charmander took ' + str(damage2), ' damage!!')
                print('what would you like to do?')
                print('Enter 1 to select "Battle", 2 for "Pokeball", 3 for "Run"')
                i = int(input())
                if hp_w <= 0:
                    print('Congratulations! you won the battle!')
                    break
                elif hp_s <= 0:
                    print('Oh no! your pokemon fainted')
                    break
            elif starter == 'Squirtle':
                moveset = ['Pound']
                print("Squirtle's moves: " + str(moveset))
                print('The attack was normally effective')
                damage = random.randint(10, 20)
                hp_w = hp_w - damage
                print('The opponent pokemon took ' +str( damage), 'damage!')
                print("The opponent's attack did normal damage!")
                damage2 = random.randint(12, 18)
                hp_s = hp_s - damage2
                print('Squirtle took ' + str(damage2), ' damage!!')
                print('what would you like to do?')
                print('Enter 1 to select "Battle", 2 for "Pokeball", 3 for "Run"')
                i = int(input())
                if hp_w <= 0:
                    print('Congratulations! you won the battle!')
                    break
                elif hp_s <= 0:
                    print('Oh no! your pokemon fainted')
                    break
                print('what would you like to do?')
                print('Enter 1 to select "Battle", 2 for "Pokeball", 3 for "Run"')
                i = int(input())









#-----------------main_program-------------------------------------------------------------------

introDisplay()
time.sleep(1)
print('Enter 1 to select Pikachu, 2 for Bulbasaur, 3 for Squirtle, 4 for Charmander')
n = int(input())
chooseStarter(n)
time.sleep(2)
print('A wild pokemon appeared!')
j = random.randint(0, 3)
wildPoke = wild_pokemon[j]
print("It's a " + wildPoke, '!')
print('What will you do?')
print('Enter 1 to select "Battle", 2 for "Pokeball", 3 for "Run"')
i = int(input())
battle(i)
while True:
    print('What would you like to do?')
    print('Enter 1 for battling a wild pokemon, 0 to exit the game')
    l = int(input())
    if l == 0:
        print('Thanks for playing the game! -Varun KJ')
        break
    if l == 1:
        print('A wild pokemon appeared!')
        j = random.randint(0, 3)
        wildPoke = wild_pokemon[j]
        print("It's a " + wildPoke, '!')
        print('Enter 1 ro select "Battle", 2 for "Pokeball", 3 for "Run"')
        i = int(input())
        battle(i)

