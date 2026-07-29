n=[5,7,8,4,1,6,9,2]

def selection_sort_asc(n):
    i=0
    min=0
    while i<len(n):
        j=i+1
        while j<len(n):
            if n[min]>n[j]:
                min=j
            j+=1
        temp=n[i]
        n[i]=n[min]
        n[min]=temp
        i+=1
    return n
print(selection_sort_asc(n))
