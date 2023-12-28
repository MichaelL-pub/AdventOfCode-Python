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
-- End Day One --

Lets Break this down:
1abc2 = 12 because the first digit is 1 and the last digit is 2

So we simply need to:
    1. load in the text file
    2. remove all non digit/whitespace chars
    3. loop through each line and find the first and last digit
    4. add them to the total
    
seems simple enough, lets get to it.
"""

import time
import re

def clean_calibration_value(text):
    text = re.sub(r"\D", "", text)
    return text[0] + text[-1]

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
