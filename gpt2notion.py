import argparse


def remove_useless_symbol(inputs):
    return inputs.replace(r'\[', '').replace(r'\]', '').replace(r'\(', '').replace(r'\)', '')


def get_args():
    parser = argparse.ArgumentParser(description='将gpt生成的文本中不需要的部分去除, 方便粘贴到notion中.')
    parser.add_argument('-i', '--input', metavar='FILE_PATH', required=True, help='传入文件路径')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    with open(args.input, mode='r+') as f:
        content = f.read()
        new_content = remove_useless_symbol(content)
        print(new_content)
        f.seek(0)
        f.truncate()
        f.write(new_content)
