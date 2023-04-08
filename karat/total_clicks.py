"""
Suppose that now we have a list of counts of clicks and corresponding urls such as follows:

counts = ["50,google.com",
     "60,yahoo.com",
     "10,yahoo.com",
     "1,wikipedia.org",
     "40,sports.yahoo.com",
     "300,yahoo.com",
     "2,wikipedia.org",
     "1,stackoverflow.com",
     "1,google.com"]

Write a function that takes this list and returns the sum of all the clicks. 

Sample output:
sum_clicks(counts) => 465

Complexity variables:
n: the number of strings in the list
(The length of each input string has a constant upper limit.)
"""

counts = [
    "50,google.com", # => ["50", "google.com"]
    "60,yahoo.com",
    "10,yahoo.com",
    "1,wikipedia.org",
    "40,sports.yahoo.com",
    "300,yahoo.com",
    "2,wikipedia.org",
    "1,stackoverflow.com",
    "1,google.com"
]


def click_count_total(counts):
    return sum(int(record.split(",")[0]) for record in counts)
    

print(click_count_total(counts))
