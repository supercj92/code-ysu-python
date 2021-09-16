import openpyxl


def load_data(file_path, sheet_name, start_row, column):
    work_book = openpyxl.load_workbook(file_path)
    sheet = work_book[sheet_name]
    texts = []
    for row in list(sheet.rows)[start_row:]:
        texts.append(row[column].value)

    work_book.close()
    return texts
