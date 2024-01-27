#given matrix

face=[['😀','😀','😀'],
      ['😀','😀','😀'],
      ['😀','😀','😀']] 

#input row and column
rc=input("enter row and column number: ")
row=int(rc[0])
column=int(rc[2])

item=face[row-1]
item[column-1]='😥'

print(face[0])
print(face[1])
print(face[2])