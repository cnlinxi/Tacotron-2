# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 13:59
# @Author  : MengnanChen
# @FileName: transform_pinyin.py
# @Software: PyCharm

from pypinyin import lazy_pinyin, Style
import jieba

def is_chinses(uchar):
    if uchar > u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False


def clean_line(line):
    cleaned_line = []
    line = line.split('|')
    assert len(line) == 2
    line = line[1]
    line=line.replace('，',',')
    line=line.replace('。','.')
    # for char in line:
    #     if is_chinses(char):
    #         cleaned_line.append(char)
        # elif char==' ':
        #     cleaned_line.append(' ')
        # elif char=='，':
        #     cleaned_line.append(',')
        # elif char=='。':
        #     cleaned_line.append('.')
    cleaned_line=' '.join(jieba.cut(line))
    cleaned_line=cleaned_line.strip(' ')
    return cleaned_line


def get_pinyin(line):
    return ''.join(lazy_pinyin(line, style=Style.TONE3))


def transform_pinyin_to_file(data_path, output_path):
    with open(data_path, 'rb') as fin, open(output_path, 'wb') as fout:
        for line in fin:
            line = line.decode('utf-8')
            line = clean_line(line)
            if not line:
                continue
            transformed_line = get_pinyin(line)
            fout.write(f'{transformed_line}\n'.encode('utf-8'))


if __name__ == '__main__':
    data_dir = 'data/inputs.txt'
    output_dir = 'data/pinyin.corpus'
    transform_pinyin_to_file(data_dir, output_dir)