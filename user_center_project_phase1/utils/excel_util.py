import openpyxl

def read_excel_data(file_path, sheet_name="Sheet1"):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    data = []

    headers = [cell.value for cell in sheet[1]]  # 读取表头
    for row in sheet.iter_rows(min_row=2, values_only=True):
        row_data = dict(zip(headers, row))

        # 类型转换：确保字段为正确类型
        row_data["expected_status"] = int(row_data["expected_status"])
        row_data["expect_token"] = str(row_data["expect_token"]).strip().lower() == "true"

        data.append(row_data)

    return data
