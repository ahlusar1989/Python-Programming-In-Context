# 1: Print out a table of students and their scores with the students listed in alphabetical order.

def studentsort(dictionary):
    students = []
    for name in dictionary:
        students.append(name)
        students.sort()
    for name in students:
        if name in dictionary:
            print(name, dictionary[name])

################################################################
# def studentsort(dictionary)
# students = list(dictionary.keys)
# students.sort
# for name in students:
#     if name in dictionary:
#         print(name, dictionary[name])
# 
# This is a shorten way of the above function. UNTESTED
#
#
#
###############################################################

        
# 2: Write a function called getScore that takes a name and a dictionary as a parameter and returns the score for that name if it is in the dictionary. If the name is
# not in the dictionary, print an error message and return -1.

def getScore(name, dictionary):
    if name in dictionary:
        score = dictionary[name]
    elif name not in dictionary:
        score = -1
        print("%s is not in the dictionary" % (name))
    return score

# 3: Suppose you have a list of key-score values like the following: [('john',10),('bob',8),('john',5),('bob',17]. Write a function that takes such a list as a
# parameter and prints out a table of average scores for each person. 

lister = [('john',10),('bob',8),('john',5),('bob',17)]
dict = {}

def mean(alist):
    mean = sum(alist) / len(alist)

def getAvg(list):
    for key, value in list:
        dict[key].append(value)
    for item in dict:
        print item, mean(dict[item])  
        
    

# 4: Another way to compute the frequency table is to obtain a list of key-value pairs using the items method. This list of tuples can be sorted and printed without
# returning to the original dictionary. Rewrite the frequency table function using this idea. 

#Original frequency table function

def frequencyTable(list):
    countdict = {}

    for item in list:
        if item in countdict:
	    countdict[item] = countdict[item] + 1
	else:
	    countdict[item] = 1
    
    itemlist = list(countdict.keys())
    itemlist.sort()

    print("ITEM","FREQUENCY")
   
    for item in itemlist:
        print(item, "    ", countdict[item])

#My function

listly = [('1',5,),('2',7),('3',2),('4',1),('5',9)]

def freqtable(list):
    list.sort()
    print "ITEM","FREQUENCY"
    for key, value in list:
        print key,"    ",value
        

            
