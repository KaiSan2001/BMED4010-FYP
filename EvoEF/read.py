import xlrd

xlsx = xlrd.open_workbook('SL.xlsx')

table = xlsx.sheet_by_index(0)
for i in range(0,20):
    for j in range(0,5):
        # 获取单个表格值 (2,1)表示获取第3行第2列单元格的值
        value = table.cell_value(i, j)
        row= i
        column = j
        print("第%s行%s列值为",value)
        
        # 获取表格行数
