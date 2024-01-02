"""
--- Day 3: Gear Ratios ---

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). 
Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

--- end day 1 part 1 ---

1. loop though file
2. get previous and next lines
3. loop though numbers in the line
4. check that the number has symbol next to it, if yes then add it to the total for that line.
5. return line total

"""

import time
import re

def isSymbol(char):
    if char == '.':
        return False
    elif re.match(r"\d", char):
        return False
    
    return True
        


start_time = time.time()

total = 0
GameNum = 1
directory = "C:\\Users\\xXfra\\Desktop\\Research\\Languages\\Python\\AdventOfCode-Python\\Code\\day3\\"


with open(directory +"day3.txt", "r") as file:

    lines = file.readlines()
    
    for i in range(len(lines)):
        curLine = lines[i]
        prevLine = lines[i-1]
        if i != len(lines)-1:
            nextLine = lines[i+1]
        else:
            nextLine = ""
        
        matches = re.finditer(r"\d+", curLine)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            number = match.group()  # The extracted number
            
            #calc end position so we dont get index out of bounds
            end_pos += 1
            if end_pos > len(curLine)-1:
                end_pos = len(curLine)-1
            print(len(curLine))
            print(end_pos)
            print("-----------------")
            
            
            #build array of chars next to 
            if not isSymbol(curLine[start_pos-1]) and not isSymbol(curLine[end_pos]):
                continue
            
            prevLineChars = prevLine[start_pos-1:end_pos]
            nextLineChars = nextLine[start_pos-1:end_pos]
            prevLineChars.replace(".","")
            
            # Matches one or more dots or digits
            pattern = r"[.\d]+"  
            prevLineChars = re.sub(pattern, "", prevLineChars)
            nextLineChars = re.sub(pattern, "", nextLineChars)
            
            if len(prevLineChars) == 0 or len(nextLineChars) == 0:
                continue
            
            total += number
        
print("\n\nSum of part numbers: ", total)
        
end_time = time.time()
print("Execution time:", end_time - start_time, "seconds")