def function():
    new_list=list([1,2,-1,-2,4,-5])
    positive=[]
    negative=[]
    i=0
    while i<len(new_list):
        if new_list[i]<0:
            positive.append(new_list[i])
            i+=1
        else:
            negative.append(new_list[i])
            i+=1
    return 'positive: '+ str(positive)+'Negative: '+str(negative)
x=[1,2,3,-1,-2,-3]
print(function())