import numpy as np

ID=['F1','F2','F3','F4','F5','F6','F7','F8'] #anggap variable mesin
val=[32.23,42.12,12.42,21.64,65.87,30.43,10.93,87.02] #anggap variable valuenya

def bubblesort(key,value,index):
	x=[['',0]]*index #declaring variable x as array
	for i in range(index) :
		x[i]=(key[i],value[i])

	dtype = [('key','S3'),('value',float)]
	a=np.array(x, dtype=dtype)
	c=np.sort(a, order='value')
	c=c[::-1]#sort reverse
	return(c)

result=bubblesort(ID,val,8) #nanti disesuaikan dengan variable yg di inginkan
for i in range(8) :
	print(result[i][0].decode("utf-8"),'=',result[i][1])
