import openpyxl
from openpyxl.styles import Font

# Define the orange color in RGB (as used in Excel, may need adjustment)
ORANGE_RGBS = ["FFFF9900", "FFFFA500", "FFFF8000"]  # Common orange shades in Excel


def is_orange(font):
    if font is None or not font.underline:
        return False
    color = getattr(font.color, 'rgb', None)
    if color:
        return color.upper() in ORANGE_RGBS
    return False


def extract_orange_underlined_labs(xlsx_path, output_path):
    wb = openpyxl.load_workbook(xlsx_path)
    orange_labs = []
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                font = cell.font
                if font and font.underline and font.color is not None:
                    color = getattr(font.color, 'rgb', None)
                    if color and color.upper() in ORANGE_RGBS:
                        orange_labs.append(str(cell.value))
    # Remove duplicates and empty values
    orange_labs = [lab for lab in set(orange_labs) if lab and lab.strip()]
    orange_labs.sort()
    with open(output_path, 'w') as f:
        for lab in orange_labs:
            f.write(lab + '\n')
    print(f"Extracted {len(orange_labs)} labs underlined in orange to {output_path}")

if __name__ == "__main__":
    extract_orange_underlined_labs("A+ 12.220.xlsx", "orange_underlined_labs.txt")
