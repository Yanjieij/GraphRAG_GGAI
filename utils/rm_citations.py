import re


def remove_citations(text):
    # 更宽泛的正则表达式匹配引用
    citation_pattern = r"\(\b\w+(?:\s+\w+)?\s+and\s+\w+(?:\s+\w+)?\s*,\s*\d{4}[a-z]?\)|\(\b\w+\s+et\s+al(?:\.)?(?:\s*,\s*)?\d{4}[a-z]?\)|\(\b\w+\s*,\s*\d{4}[a-z]?\)"
    # 使用空字符串替换找到的所有引用
    return re.sub(citation_pattern, "", text)


def process_file(input_filename, output_filename):
    with open(input_filename, "r", encoding="utf-8") as file:
        content = file.read()

    # 移除引用
    processed_content = remove_citations(content)

    # 写入新的文件
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(processed_content)


# 示例文件名
input_filename = "miner_Asia.txt"
output_filename = "miner_Asia_nocitations.txt"

# 处理文件
process_file(input_filename, output_filename)
