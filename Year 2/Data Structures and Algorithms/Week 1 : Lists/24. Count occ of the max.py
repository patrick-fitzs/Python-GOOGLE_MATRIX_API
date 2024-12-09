### current max counter is 1 and x[i] is max
# compare the current to prev index, if ==, counter +1
# if > this is a new max and reset counter
# then return ###

# bellow is 2 differnet approaches
def max_count(x):
    currentMax = 0
    maxCounter = 0

    for elem in x:
        if elem>currentMax:
            currentMax = elem

    for i in range(len(x)):
        if x[i] == currentMax:
            maxCounter+=1
    return maxCounter

def max_Count(x):
    currentMax = x[0]
    maxCounter = 1

    for i in x[1:]:
        if i>currentMax:
            currentMax = i
            maxCounter = 1
        elif i ==currentMax:
            maxCounter+=1
    return maxCounter

x = [2, 4, 3, 3]
print(max_count(x), "should be 1")

x = [5, 1, 5, 2, 5]
print(max_count(x), "should be 3")

x = [3, 1, 4, 1, 5, 5, 6, 5, 6]
print(max_count(x), "should be 2")

x = [4, 4, 4]
print(max_count(x), "should be 3")

x = [3]
print(max_count(x), "should be 1")