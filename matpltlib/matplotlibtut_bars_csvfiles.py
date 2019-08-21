# course from this series
# https://www.youtube.com/watch?v=nKxLfUrkLE8&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&index=3&t=0s
# make sure you open VS Code in the base folder or the paths won't work below.

from matplotlib import pyplot as plt 
import numpy as np
import csv
from collections import Counter

# in VS Code, Ctrl + / toggles line comments

plt.style.use("fivethirtyeight")

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

# use a counter to count individual values in the data. In this case, loop through the rows
# and count the numnber of times unique programming languages appear.

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

# switch to a horizontal bar chart with barh if things don't fit 
# across the x axis like this. All the parameters stay the same. Except
# you need to adjust the x and y label names. We'll also reverse the data
# so that the greater values appear on the top of the chart

languages.reverse()
popularity.reverse()
plt.barh(languages, popularity)


# Test: Just print the data
# print(language_counter.most_common(15))


    # a test to look at single rows in our data, but split by semi-colons, not commas    
    # row = next(csv_reader)
    # print(row['LanguagesWorkedWith'].split(';'))

plt.title("15 Most Popular Languages")
# plt.ylabel("Programming Language")
plt.xlabel("Number of people who use")
plt.legend()

plt.tight_layout() # optional to fix certain layout issues.


plt.savefig('programming_lang_pop.png')
plt.show()