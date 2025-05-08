import openpyxl

def find_theory_cells(xlsx_path):
    wb = openpyxl.load_workbook(xlsx_path)
    theory_cells = []
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                if str(cell.value).strip() == "Theory":
                    location = f"{ws.title}!{cell.coordinate}"
                    theory_cells.append(location)
    return theory_cells

if __name__ == "__main__":
    results = find_theory_cells("A+ 12.220.xlsx")
    print("Lines with only 'Theory':")
    for line in results:
        print(line)
