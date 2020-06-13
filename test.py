from flask import Flask,redirect,url_for,request,render_template
import xlrd
app=Flask(__name__)

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=='POST':
        result=request.form
        return render_template("result.html",result=result)

@app.route('/level1',methods=['POST','GET'])
def level1():
	if request.method=='POST':
		f=open("E:\\SEM 6\\STECH\\Application\\questions\\level1.txt","r")
		ques=[]
		f1=f.readlines()
		for line in f1 :
			ques.append(line)
		f.close()
		result=ques
		return render_template("level1.html",result=result)

ca=[]
nextQues=[]
ques_count=[1,1,1,2,3,3,4]
@app.route('/level2',methods=['POST','GET'])
def level2():
	if request.method=='POST':
		result=request.form
		ans=[0,0,0,0,0,0,0]
		
		c1=Category(ans[0],'E:\\SEM 6\\STECH\\Application\\questions\\level2\\Linguistic.txt','Linguistic')
		c2=Category(ans[1],'E:\\SEM 6\\STECH\\Application\\questions\\level2\\Math.txt','Math')
		c3=Category(ans[2],'E:\\SEM 6\\STECH\\Application\\questions\\level2\\Music.txt','Music')
		c4=Category(ans[3],'E:\\SEM 6\\STECH\\Application\\questions\\level2\\Body.txt','Body')
		c5=Category(ans[4],'E:\\SEM 6\\STECH\\Application\\questions\\level2\\Visual.txt','Visual')
		c6=Category(ans[5],'E:\\SEM 6\\STECH\\Application\\questions\\level2\\Inter.txt','Inter')
		c7=Category(ans[6],'E:\\SEM 6\\STECH\\Application\\questions\\level2\\Intra.txt','Intra')
	
		l1=[2,9,14]		#Linguistic
		l2=[5,13,18]	#Math
		l3=[4,7,21]		#Music
		l4=[1,12,20]	#body
		l5=[3,10,16]	#visual
		l6=[6,11,19]	#inter
		l7=[8,15,17]	#intra
		index=1
		for k,v in result.items() :
			x=int(v)
			if index in l1 :
				ans[0]=ans[0]+x
			elif index in l2 :
				ans[1]=ans[1]+x
			elif index in l3:
				ans[2]=ans[2]+x
			elif index in l4 :
				ans[3]=ans[3]+x
			elif index in l5 :
				ans[4]=ans[4]+x
			elif index in l6 :
				ans[5]=ans[5]+x
			elif index in l7 :
				ans[6]=ans[6]+x
			index=index+1
		#ans.sort()
		
		c1.val=ans[0]
		c2.val=ans[1]
		c3.val=ans[2]
		c4.val=ans[3]
		c5.val=ans[4]
		c6.val=ans[5]
		c7.val=ans[6]
	
		ca.append(c1)
		ca.append(c2)
		ca.append(c3)
		ca.append(c4)
		ca.append(c5)
		ca.append(c6)
		ca.append(c7)
		ca.sort(key=lambda x: x.val)
		for i in ca :
			print(i.val)
		img=[]
		for i in range(0,len(ca)):
			f=open(ca[i].c,"r")
			f1=f.readlines()
			for j in range(0,ques_count[i]) :
				print('/// ',j, '///')
				if(ca[i].c!="E:\\SEM 6\\STECH\\Application\\questions\\level2\\Visual.txt") :
					nextQues.append(f1[j*5])
					nextQues.append(f1[j*5+1])
					nextQues.append(f1[j*5+2])
					nextQues.append(f1[j*5+3])
					nextQues.append(f1[j*5+4])
				else :
					nextQues.append(f1[j*6])
					img.append(f1[j*6+1])
					nextQues.append(f1[j*6+2])
					nextQues.append(f1[j*6+3])
					nextQues.append(f1[j*6+4])
					nextQues.append(f1[j*6+5])
			f.close()
		return render_template("level2.html",result=nextQues)

@app.route('/final_result',methods=['POST','GET']) 
def final_result():
	if request.method=="POST":
		result=request.form
		#wb=xlrd.open_workbook("E:\\SEM 6\\STECH\\Application\\questions\\quedata.xlsx")
		loc='E:\\SEM 6\\STECH\\Application\\questions\\quedata.xlsx'
		wb=xlrd.open_workbook(loc)
		sheet=wb.sheet_by_index(0)
		#ans=[1,4,3,2,3,4,1,2,3,3,1,4,4,2,1]
		ans=[]
		for k,v in result.items():
			ans.append(int(v))
		c1=0
		x1=0
		c2=0
		x2=0
		c3=0
		x3=0
		c4=0
		x4=0
		c5=0
		x5=0
		c6=0
		x6=0
		c7=0
		x7=0
		for j in range (0,15):
			for i in range (1,sheet.nrows):
				# print(nextQues[j*5],' ********* ',sheet.cell_value(i,0))
				if(nextQues[j*5].strip()==sheet.cell_value(i,0).strip()):#or ans[j]==int(sheet.cell_value(i,1))):
					print('in 1st if')
					if(ans[j]==int(sheet.cell_value(i,1))):
						#print(j,'  ',ans[j],'  :  ',sheet.cell_value(i,1))
						if(sheet.cell_value(i,2)=='Linguistic'):
							c1=c1+ans[j]
							x1=x1+1
							print('c1')
							break
						elif(sheet.cell_value(i,2)=='Math'):
							c2=c2+ans[j]
							x2=x2+1
							print('c2')
							break
						elif(sheet.cell_value(i,2)=='Body'):
							c3=c3+ans[j]
							x3=x3+1
							print('c3')
							break
						elif(sheet.cell_value(i,2)=='Visual'):
							c4=c4+ans[j]
							x4=x4+1
							print('c4')
							break
						elif(sheet.cell_value(i,2)=='Inter'):
							c5=c5+ans[j]
							x5=x5+1
							print('c5')
							break
						elif(sheet.cell_value(i,2)=='Intra'):
							c6=c6+ans[j]
							x6=x6+1
							print('c6')
							break
						elif(sheet.cell_value(i,2)=='Music'):
							c7=c7+ans[j]
							x7=x7+1
							print('c7')
							break
		if(x1==0) :
			c1==0
		else :
			c1=c1*100/(x1*4)
		if(x2==0) :
			c2==0
		else :
			c2=c2*100/(x2*4)
		if(x3==0) :
			c3==0
		else :
			c3=c3*100/(x3*4)
		if(x4==0) :
			c4==0
		else :
			c4=c4*100/(x4*4)
		if(x5==0) :
			c5==0
		else :
			c5=c5*100/(x5*4)
		if(x6==0) :
			c6==0
		else :
			c6=c6*100/(x6*4)
		if(x7==0) :
			c7==0
		else :
			c7=c7*100/(x7*4)

		return render_template("final_result.html",c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7)


class Category:
    def __init__(self,val,c,s):
        self.val=val
        self.c=c
        self.s=s
    def display(self):
        print('Category:',self.c,' Value:' ,self.val)

if __name__=='__main__':
    app.run()


