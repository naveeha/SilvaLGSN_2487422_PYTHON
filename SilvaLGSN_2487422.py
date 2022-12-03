import os
from random import randrange

word_upper = []
value = []
bucket = []
result = []
finalList = []
wordList = []
actualWord = []
acroynm = []
aList = []



def getData():
    with open("trees.txt") as file:  # open file
        for line in file:
            actualWord.append(line.strip())
            word = line.replace("'", "")  # remove single quotes
            words = word.replace("-", ' ')  # remove hypen
            data = words.replace(' ', "")
            lis = data.strip() # remove \n 
            word_upper.append(lis.upper()) # convert to upper case
            # makeAcronym(word_upper)
        file.close()
        return makeAcronym(word_upper)


def getValue():
    with open("values.txt") as File:  # open file
        for line in File:
            value.append(line.split())   #append all values and letters 
    File.close()
    return value


# function to create acronym
def makeAcronym(stng): 
    score = getValue()    #get values
    
    for ele in stng:    # iterate over each word
     length = len(ele)
     
     bucket.clear()     #clear bucket array if exisiting previous acronym
     for k in range(3):   
        oupt = ele[0]
        while(len(oupt) < 3):
         temp = ele[randrange(length)]  #get random letter from word
         oupt = oupt + temp
        bucket.append(oupt)
        mark = 0
        check = bucket[k]     
        for element in score:   #get score for each acronym
          # print(check)
            if (check[-1] == 'E'):    #check acroynm last letter is 'E'
             mark += 20
            if (element[0] == check[1]): #check second letter of acroynm with given letter's value
             mark += int(element[1])
            if (element[0] == check[2]): #check third letter of acroynm with given letter's value
             mark += int(element[1])
            if (check[-1] == stng[-1]): #check last letter of acroynm with last letter of original word
             mark += 5

    #    print(mark)
        result.append(check)  
        result.append(mark)
     checkLowestScore(result)
    #  print(result)
     result.clear()
     
    
    

#check lowest score for each word
def checkLowestScore(res):
    temp_score = res[1::2]  #get scores only from the array
    min = temp_score[0]     #store 1st score
    min_index = 0
    i=0
    #   print(temp_score) 
    while(i<3):
        if temp_score[i] <= min:
            min = temp_score[i]
            min_index = i   
        if(min_index == 0):
         acroynm = res[0]     #get corresponding acroynm
        if(min_index == 1):
         acroynm = res[2]     #get corresponding acroynm
        if(min_index == 2):
         acroynm = res[4]     #get corresponding acroynm
        i += 1
    # print(acroynm)
    finalAbbrList(acroynm)
    
    
  
#write all acronym and original word inside a file
def finalAbbrList(ac):   
    # print(ac)
    i =1
    # print(actualWord.pop(0))
    while(i==1):
       e = actualWord.pop(0)
    #    print(e)
       new_line = (e +" - " + ac + " \n")    #create new line
    #    print(new_line)
       i+=1
       f = open("r.txt","at")
       f.write(new_line) 
    f.close()


def main():
    getData()
    getValue()
    inputFile_name = os.path.splitext("trees.txt")   #get input file name
    final_name = "Silva_" + inputFile_name[0] + "_abbrevs.txt"   #create output file name
    os.rename("r.txt", final_name)
    print("Successfully created output file: ",final_name)
main()
