import xlrd

workbook = xlrd.open_workbook("people.xls")
worksheet = workbook.sheet_by_name('Sheet1')
# sh1 = wb.sheet_by_index(0)

for current_row in range(worksheet.nrows):
    fname_text = worksheet.row(current_row)[0]
    lname_text = worksheet.row(current_row)[1]
    age = worksheet.row(current_row)[2]
    print fname_text, lname_text, age
    
    
    
#     book  = xlrd.open_workbook(file_contents=contentstring)
#     sheet = book.sheets()[n]
#     array = np.zeros((sheet.ncols, sheet.nrows))
#     
#     for row in range(sheet.nrows):
#         for col in range(sheet.ncols):
#             array[col][row] = sheet.cell(row, col).value
#     
#     return array

# datafile = r'C:\\someexcelfileediting.xlsx'
#    workbook = xlrd.open_workbook(datafile)
#    stone = workbook.sheet_by_name(input('What is the name of the sheet you are trying to reference?  ').upper())
#    paper = workbook.sheet_by_name(input('what sheet would you like to check?  ').upper())
#    def check_Base():
#    set2 = set()
#    for row in range (0, paper.nrows):    
#        for col in range(0, paper.ncols):       
#            set2.add(paper.cell_value(row, col))
           
# iterate all rows in a specific column        
for row in sheet.col(2):
    # do something