import openpyxl
path = "C:\\Users\Spanidea-LT-103\Desktop\YASHSPANIDEA\Book1.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook["Sheet2"]
for r in range(1,5):
    for c in range(1,3):
        sheet.cell(row=r,column=c).value="welcome"
workbook.save(path)
