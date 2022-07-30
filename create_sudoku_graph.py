import os
import numpy

from subprocess import check_output

in_file_name = 'sudoku.csv'

def row_calc(num):
    return num/9

def col_calc(num):
    return num%9

def block_calc(num):
    bl_row=row_calc(num)/3
    bl_col=col_calc(num)/3
    bl_num=bl_row*3+bl_col
    return bl_num


fi = open(in_file_name)

colors = list(numpy.zeros(81))

line = fi.readline()

while(line):
    line = line.rstrip('\n')
    inp = line
    inp_split = inp.split(',')
    row = int(inp_split[0])
    col = int(inp_split[1])
    num = int(inp_split[2])
    colors[row*9+col] = num
    line = fi.readline()
fi.close()


# encode graph edges
edge_list =[]
for i in range (0,81):
    for j in range(0,81):
        if (i!=j) and (row_calc(i)==row_calc(j)) or (col_calc(i)==col_calc(j)) or (block_calc(i)==block_calc(j)):
            edge_list.append((i,j))


for s in edge_list:
        while edge_list.count(s)>1:
            edge_list.pop(edge_list.index(s))
        rs = reversed(s)
        while edge_list.count(rs)>0:
            edge_list.pop(edge_list.index(rs))
            
e = len(edge_list)
v = 81

filename="graph_"+in_file_name+'.txt'
f = open(filename,"w")

f.write(str(v)+' '+str(e)+'\n')
for edge in edge_list:
    f.write(str(edge[0]+1)+' '+str(edge[1]+1)+'\n')


colors_str = ''
for i in range(0,v):
    colors_str = colors_str+str(int(colors[i]))+' '
colors_str = colors_str.rstrip(' ')
f.write(colors_str + '\n')
f.close()

print 'soduku looks like this'
for i in range(0,9):
    for j in range(0,9):
        print str(int(colors[(j+i*9)]))+'\t',
        if j%3==2:
            print '\t',
    print '\n'
    if i%3==2:print'\n\n',


out_name = filename +'_out.txt'
command = 'a.out < '+filename+' > '+ out_name
print command
a = 4
os.system('a.out < '+filename+' > '+ out_name)

resfile = open(out_name)


line = resfile.readline()
line = resfile.readline()
line = line.rstrip('\n')
line_split = line.split()
res_colors = []
for s in line_split:
    res_colors.append(int(s))



print 'solved soduku looks like this'
for i in range(0,9):
    for j in range(0,9):
        print str(int(res_colors[(j+i*9)]))+'\t',
        if j%3==2:
            print '\t',
    print '\n'
    if i%3==2:print'\n\n',