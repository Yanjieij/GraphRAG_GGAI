from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def convert_pdf_to_txt(pdf_path, output_path):
    output_string = StringIO()
    with open(pdf_path, "rb") as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
        text = output_string.getvalue()

    # 合并连续的空白行
    lines = text.split("\n")
    merged_lines = []
    current_line = ""
    for line in lines:
        if line.strip() == "":
            if current_line != "":
                merged_lines.append(current_line)
                current_line = ""
        else:
            if current_line == "":
                current_line = line
            else:
                current_line += " " + line
    if current_line != "":
        merged_lines.append(current_line)

    # 合并后的文本
    merged_text = "\n\n".join(merged_lines)

    # 写入TXT文件
    with open(output_path, "w", encoding="utf-8") as out_file:
        out_file.write(merged_text)


# 指定PDF文件路径和输出TXT文件路径
pdf_file = "D:\Python\Asia.pdf"
txt_file = "D:\Python\Asia_miner.txt"

# 调用函数
convert_pdf_to_txt(pdf_file, txt_file)
