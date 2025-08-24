import openpyxl as excel

#创建一个新的工作簿
workbook = excel.Workbook()

#获取活动工作表
sheet = workbook.active

#向A1单元格写入数据
sheet['A1'] = 'hello, world'

#保存工作簿
workbook.save('new1.xlsx')