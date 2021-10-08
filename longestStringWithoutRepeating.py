# Logica do window sliding
def longestStringWithoutRepeating(string: str):
    finalArray = []

    array = []
    for r in range(len(string)):

        while(string[r] in array):
            array.pop(0)
        array.append(string[r])

        if(len(finalArray) < len(array)):
            finalArray = array.copy()

    return finalArray

