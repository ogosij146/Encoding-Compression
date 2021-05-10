def compress(string):
    first = string[0]
    count = 0
    fin = ""
    for i in string:
        if i != first:
            fin += str(count)+first
            count=0
            first=i      
        count+=1
    fin += str(count)+first
    return fin

print(compress("WWXXYYYXXZZZZZZYYYYYEEESSS"))