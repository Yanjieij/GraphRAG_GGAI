import sys
import re


def merge_lines_with_lowercase_start(input_file, output_file):
    # 读取原始文件
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # 初始化一个空列表来存储处理后的行
    merged_lines = []

    # 遍历每一行
    i = 0
    while i < len(lines):
        current_line = lines[i].strip()

        # 如果当前行不是最后一行并且当前行以小写字母开头
        if i < len(lines) - 1 and re.match(r"^[a-z]", current_line):
            # 合并当前行与下一行
            next_line = lines[i + 1].strip()
            merged_line = current_line + " " + next_line
            merged_lines.append(merged_line + "\n")
            i += 2  # 跳过下一行
        else:
            merged_lines.append(current_line + "\n")
            i += 1

    # 写入新文件
    with open(output_file, "w", encoding="utf-8") as file:
        file.writelines(merged_lines)


def filter_short_lines(input_file, output_file):
    # 读取原始文件
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # 过滤掉长度小于等于5的行
    filtered_lines = [line for line in lines if len(line.strip()) > 10]

    # 写入新文件
    with open(output_file, "w", encoding="utf-8") as file:
        file.writelines(filtered_lines)


def replace_double_spaces(input_file, output_file):
    # 读取原始文件
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # 处理每一行，将连续的两个空格替换为一个空格
    processed_lines = [line.replace("  ", " ") for line in lines]

    # 写入新文件
    with open(output_file, "w", encoding="utf-8") as file:
        file.writelines(processed_lines)


input_file = "Asia_nocitations.txt"
output_file = "Asia_nocitations_noshort.txt"

filter_short_lines(input_file, output_file)
replace_double_spaces(output_file, output_file)
merge_lines_with_lowercase_start(output_file, output_file)
