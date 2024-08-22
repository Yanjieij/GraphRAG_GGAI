import PyPDF2


def pdf_to_text(pdf_path, txt_path):
    # 打开PDF文件
    with open(pdf_path, "rb") as file:
        # 创建PDF阅读器对象
        pdf_reader = PyPDF2.PdfReader(file)

        # 初始化一个空字符串用于存储所有页面的文本
        text = ""

        # 遍历每一页
        for page_num in range(len(pdf_reader.pages)):
            # 获取当前页
            page = pdf_reader.pages[page_num]

            # 提取文本
            text += page.extract_text()

    # 写入TXT文件
    with open(txt_path, "w", encoding="utf-8") as file:
        file.write(text)


# 指定PDF文件路径和输出TXT文件路径
pdf_file = "D:\Python\Asia.pdf"
txt_file = "D:\Python\Asia.txt"

# 调用函数
pdf_to_text(pdf_file, txt_file)
