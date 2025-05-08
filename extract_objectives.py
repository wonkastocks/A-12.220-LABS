import PyPDF2

def main():
    pdf = PyPDF2.PdfReader(open('comptia-a-220-1202-exam-objectives-(2-0).pdf', 'rb'))
    objectives = []
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            for line in text.split('\n'):
                line = line.strip()
                if line and not line.startswith('CompTIA') and not line.startswith('Copyright'):
                    objectives.append(line)
    with open('objectives.txt', 'w') as f:
        for obj in objectives:
            f.write(obj + '\n')

if __name__ == '__main__':
    main()
