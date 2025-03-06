import re #stand for regular expression
#used in search pattern and match them
# search for and match text patterns

#raw string is a string not to handle backslash in any special way 
print(r'\t tab') #r makes the \ a normal text 
####
pattern=re.compile(r'abc') # it just compiles a regular expression pattern into a regex object making it more efficient when we need to use it several times
## re.compile doc:https://www.geeksforgeeks.org/re-compile-in-python/


if __name__=="__main__":
   

    s=input()
    k=input()
    pattern = f"(?=({k}))"  

    matches = [(m.start(), m.start()+len(m.group(1))-1) for m in re.finditer(pattern, s)]
    ## use m.start()+len(m.group(1))-1 instead of m.end()-1 because m.end acts unexpectedly, especially when the matches involve repeating characters due to the lapoverhead 
    if matches:
        for i in range(len(matches)):
            print(matches[i])
    else:
        print((-1,-1))
######################################
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
if __name__=="__main__":
    n=int(input())
    string=[input() for i in range(n)]
    pattern1=r"(?<= )&&(?= )"  
    pattern2=r"(?<= )\|\|(?= )"
    for i in range(len(string)):
        string[i]=re.sub(pattern1,"and",string[i])
        string[i]=re.sub(pattern2,"or",string[i])
        print(string[i])
    ## text replacement