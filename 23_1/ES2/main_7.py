import time
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


from random import *
total1 = 1000000
total2 = 500
vet1M = []
vet500 = []
for i in range(total1):
    vet1M.append(randint(-1000000,1000000))
for i in range(total2):
    vet500.append(randint(-1000000,1000000))
arq = open("arquivo.txt","w")
for j in range(len(vet1M)):
    arq.write(str(vet1M[j])+"\n")


print("Tempo do QuickSort com vetor de um milhão de elementos:")
inicio = time.time()
quickSort(vet1M)
fim = time.time()
print(fim - inicio, "\n")
print("Tempo do MergeSort com vetor de um milhão de elementos:")
inicio = time.time()
mergeSort(vet1M)
fim = time.time()
print(fim - inicio, "\n\n")


print("Tempo do QuickSort com vetor de quinhentos de elementos:")
inicio = time.time()
quickSort(vet500)
fim = time.time()
print(fim - inicio, "\n")
print("Tempo do MergeSort com vetor de quinhentos de elementos:")
inicio =  time.time()
mergeSort(vet500)
fim = time.time()
print(fim - inicio, "\n")