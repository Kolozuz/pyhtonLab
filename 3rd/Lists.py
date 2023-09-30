# In python we have 4 different ways of storing multiple elements in a variable:  (array for the og's),
# 1. List: mutable array
# 2. Tuple: inmutable
# 3. Set:
# 4. Dictionary:
# elements in one variable, it can contain all data types, even other lists




def listsOverview():
    """
    Lists Overview
    """
    myList:list = ['Pekin', 'Hong Kong', "Beijing", ('The Great Wall', 'deez nuts')]
    print("iniitial list : ", myList, "\n")

    #
    a = ("si", "no" , "nose")

    # Add an element at the end of the list 
    myList.append('Shanghai')
    print("With appended element : ", myList, "\n")

    # Add an element in a specific position 
    myList.insert(0, 'Lijiang')    
    print("With inserted element : ", myList, "\n")

    # Retrieve a specific element from the list
    print("Retrieved element : ", myList[4], "\n")

def tupleOverview():
    """
    tuples overview
    """
    myList:list = ['Pekin', 'Hong Kong', "Beijing", ('The Great Wall', 'deez nuts')]
    print("iniitial list : ", myList, "\n")

    #
    a = ("si", "no" , "nose")

    # Add an element at the end of the list 
    myList.append('Shanghai')
    print("With appended element : ", myList, "\n")

    # Add an element in a specific position 
    myList.insert(0, 'Lijiang')    
    print("With inserted element : ", myList, "\n")

    # Retrieve a specific element from the list
    print("Retrieved element : ", myList[4], "\n")

# Run
listsOverview()