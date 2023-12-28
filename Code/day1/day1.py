"""
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look. 
The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; 
the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and 
why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") 
when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) 
has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. 
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
-- End Day One part 1--

Lets Break this down:
1abc2 = 12 because the first digit is 1 and the last digit is 2

So we simply need to:
    1. load in the text file
    2. remove all non digit/whitespace chars
    3. loop through each line and find the first and last digit
    4. add them to the total
    
seems simple enough, lets get to it.

--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
--- end part two ---

One option is to simply convert all the names of the digits to the digit themselves
The exsisting solution would continue working as expected in this case.

lets go with that
"""

import time
import re

def clean_calibration_value(text):
    #replace digit names with actual names so that existing algorithm continues to work
    text = replace_digit_names(text)
    
    # Match the first or last digit OR single digit if there is only one
    match = re.search(r"\d.*\d|\d", text)  
    if match:
        #return first and last char in string
        return match.group()[0] + match.group()[-1]
    else:
        return ""  

def replace_digit_names(text):
    # Define a dictionary mapping digit names to their corresponding digits (0-9)
    digit_names = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    #loop through dictionary and replace in string
    for word, digit in digit_names.items():
        text = text.replace(word.lower(), digit)

    return text

start_time = time.time()

total = 0
directory = "C:\\Users\\xXfra\\Desktop\\Research\\Languages\\Python\\AdventOfCode-Python\\Code\\day1\\"

with open(directory +"day1.txt", "r") as file:
    line = file.readline()
    while line:
        #remove all non digit chars
        line = clean_calibration_value(line)
        total += int(line)
        
        line = file.readline()
        
print("Total of Calibration Values: ", total)
        
end_time = time.time()
print("Execution time:", end_time - start_time, "seconds")
