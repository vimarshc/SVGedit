def curvy(l):
    q = l.split()
    list = abs(q)
    return list

def areacal(l):
    q = l.split()
    list = abs(q)
    ar = 0
    for x in list:
        ar = ar + area(x[0],x[1],x[3],x[4],x[5],x[6],x[7],x[8])
    return ar*(-1)
                
      
def area(x0,y0,x1,y1,x2,y2,x3,y3):
    area = (3.0/10.0)*y1*x0 - (3.0/20.0)*y1*x2 - (3.0/20.0)*y1*x3 - (3.0/10.0)*y0*x1 - (3.0/20.0)*y0*x2 - (1.0/20.0)*y0*x3 + (3.0/20.0)*y2*x0 + (3.0/20.0)*y2*x1 - (3.0/10.0)*y2*x3 + (1.0/20.0)*y3*x0 + (3.0/20.0)*y3*x1 + (3.0/10.0)*y3*x2
    return area
def abs(strlist):
    megalist = []
    for i in range(len(strlist)):
        if strlist[i] == 'c':
            chis(strlist[i-2], strlist[i-1], i+1, strlist,megalist)
	    break
        elif strlist[i] == 'l':
            line(strlist[i-2], strlist[i-1],i+1,strlist,megalist)
	    break
    return megalist
def chis(x,y,index, array,megalist):
    chota=[int(x),int(y),
          'C',int(x)+int(array[index]),int(y)+int(array[index+1]),
           int(x)+int(array[index+2]),int(y)+int(array[index+3]),
           int(x)+int(array[index+4]),int(y)+int(array[index+5])]
    megalist.append(chota)
    if index + 6 == len(array):
        return       
    if array[index + 6].isdigit():
        chis(int(x)+int(array[index+4]),int(y)+int(array[index+5]),index+6,array,megalist)
    if array[index + 6] == 'l':
        line(int(x)+int(array[index+4]),int(y)+int(array[index+5]),index+7,array,megalist)

def line(x,y,index,array,megalist):
    chota=[int(x),int(y),
          'C',(int(x)+int(array[index]))/2, (int(y)+int(array[index+1]))/2,
          (2*int(x)+int(array[index]))/3, (2*int(y)+int(array[index+1]))/3,
          (int(x)+int(array[index])),(int(y)+int(array[index+1]))]
    megalist.append(chota)
    if index+2 == len(array):
        return
    if array[index+2].isdigit():
        line((int(x)+int(array[index])),(int(y)+int(array[index+1])), index+2, array,megalist)
    if array[index+2] == 'c':
        chis((int(x)+int(array[index])),(int(y)+int(array[index+1])),index+3, array,megalist)

