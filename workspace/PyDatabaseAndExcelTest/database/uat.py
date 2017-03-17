from _sqlite3 import Row

import pyodbc
import xlwt


connection = pyodbc.connect('Driver={SQL Server};'
                                )
cursor = connection.cursor()
cursor.execute("select * from tbl_PropertyAddress where vcStreet='Scotsman St'")


wb = xlwt.Workbook()  # create empty workbook object
newsheet = wb.add_sheet('my_sheet_name')  # sheet name can not be longer than 32 characters
newsheet.write(0, 0, 'id')  # write contents to a cell, marked by row i, column j
newsheet.write(0, 1, 'key')

result = cursor.fetchall()




# Save all fields from the result to excel
# row_number = 1    
# 
# for row in result:
#     column_num = 0
#     for item in row:  # i.e. for each field in that row
#         newsheet.write(row_number, column_num, str(item))  # write excel cell from the cursor at row 1
#         column_num = column_num + 1  # increment the column to get the next field
# 
#     row_number = row_number + 1
    
i = 1
for row in result:
    idd = row[0]
    key = row[1]
    
    newsheet.write(i, 0, idd)
    newsheet.write(i, 1, key)
    i = i + 1
   

wb.save('foobar.xls')
