import openpyxl


def load_data_from_excel(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb['Sheet1']
    queries = []
    for row in list(sheet.rows)[1:]:
        queries.append(row[0].value)

    wb.close()
    return queries
