import openpyxl as excel

#加载工作簿
workbook=excel.load_workbook('read1.xlsx')

#获取活动工资表
sheet=workbook.active

#获取A1单元格的值
cell_value=sheet['A1'].value
print(cell_value)