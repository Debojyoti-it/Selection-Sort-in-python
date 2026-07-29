n=[5,7,8,4,1,6,9,2]

def selection_sort_des(n):
    i=0
    max=0
    while i<len(n):
        j=i+1
        while j<len(n):
            if n[max]<n[j]:
                max=j
            j+=1
        temp=n[i]
        n[i]=n[max]
        n[max]=temp
        i+=1
    return n
print(selection_sort_des(n))
