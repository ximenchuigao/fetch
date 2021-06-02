import xlsxwriter


class ExcelFactory:
    def CreatExcel(workbookname, worksheetname, tableGenerator):
        workbook = xlsxwriter.Workbook(workbookname)       
        worksheet = workbook.add_worksheet(worksheetname)
        tableGenerator.do(workbook,worksheet)
        
