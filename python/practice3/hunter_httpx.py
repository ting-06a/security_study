import openpyxl as excel
from subprocess import Popen,PIPE
import os

file = input("在这里输入xlsx格式的文件的地址吧:")

workbook = excel.load_workbook(file)

sheet = workbook.active

url_list=[]
for row in sheet.iter_rows(min_row=2,min_col=5,max_col=5,values_only=True):
    url_list.append(row[0]+'\n')

with open('result.txt','w',encoding='utf-8') as f:
    f.writelines(url_list)

cmd=Popen(["httpx.exe","-l","result.txt","-mc","200,302"],stdout=PIPE,stderr=PIPE,text=True)

output_file=os.path.basename(file).replace('.xlsx','.txt')

with open(output_file,"w",encoding='utf-8') as f:
    for i in cmd.stdout:
        print(i.replace('\n',''))
        f.writelines(i)
print('已将探活后的url存放到'+output_file+'里啦')
