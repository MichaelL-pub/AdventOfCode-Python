"""
--- Day 2: Cube Conundrum ---

You're launched high into the atmosphere! 
The apex of your trajectory just barely reaches the surface of a large island floating in the sky. 
You gently land in a fluffy pile of leaves. 
It's quite cold, but you don't see much snow. 
An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. 
He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. 
They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. 
Each time you play this game, he will hide a secret number of cubes of each color in the bag, 
and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. 
He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). 
Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 
3 blue, 4 red; 
1 red, 2 green, 6 blue; 
2 green

Game 2: 
1 blue, 2 green; 
3 green, 4 blue, 1 red; 
1 green, 1 blue

Game 3: 
8 green, 6 blue, 20 red; 
5 blue, 4 red, 13 green; 
5 green, 1 red

Game 4: 
1 green, 3 red, 6 blue; 
3 green, 6 red; 
3 green, 15 blue, 14 red

Game 5: 
6 red, 1 blue, 3 green; 
2 blue, 1 red, 2 green

In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; 
the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. 
However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
-- end day 2 part 1 --

so i think we just need to loop through the games, get the max number of each color in any turn and return any 
    games where the max number of cubes in each category than the numbers in the prompt
    
--- Part Two ---

The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

    In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
    Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
    Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
    Game 4 required at least 14 red, 3 green, and 15 blue cubes.
    Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.

The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
-- end part 2 --

We are already getting the minimum numbers for each color of cube, so we just need to return that rather than a true or false
"""

import time
import re

def isPossibleGame(game, redNum, greenNum, blueNum):
    patterns = ["Game \d: ", "Game \d\d: ", "Game \d\d\d: "]
    for pattern in patterns:
        game = re.sub(pattern, "", game)
        
    #now split on ; and parse individual pulls
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    
    gameAr = game.split(';')
    
    #probably a better way to do this but this is good enough for now
    for gamestr in gameAr:
        for color in gamestr.split(','):
            if color.__contains__("red") and int(color.replace(" red","")) > maxRed:
                maxRed = int(color.replace(" red",""))
            elif color.__contains__("green") and int(color.replace(" green","")) > maxGreen:
                maxGreen = int(color.replace(" green",""))
            elif color.__contains__("blue") and int(color.replace(" blue","")) > maxBlue:
                maxBlue = int(color.replace(" blue",""))
                
    gamePower = maxRed * maxGreen * maxBlue
    print(str(gamePower))
    
    return gamePower
       
    # if maxRed <= redNum and maxGreen <= greenNum and maxBlue <= blueNum:
    #     return True
    # else:
    #     return False

start_time = time.time()

redNum = 12
greenNum = 13
blueNum = 14

total = 0
GameNum = 1
directory = "C:\\Users\\xXfra\\Desktop\\Research\\Languages\\Python\\AdventOfCode-Python\\Code\\day2\\"


with open(directory +"day2.txt", "r") as file:
    line = file.readline()
    while line:
        
        total += isPossibleGame(line, redNum, greenNum, blueNum)
        
        GameNum += 1
        line = file.readline()
        
print("\n\nSum of game powers: ", total)
        
end_time = time.time()
print("Execution time:", end_time - start_time, "seconds")