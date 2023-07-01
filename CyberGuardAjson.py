import json
import os

# 匹配 JSON 对象的正则表达式
json_regex = r'{.*?}'

def is_json(data):
    try:
        json.loads(data)
    except ValueError:
        return False
    return True

current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'data.json')

if not os.path.isfile(file_path):
    print(f"文件 {file_path} 不存在")
else:
    # 读取文件内容
    with open(file_path, 'r') as f:
        json_data = ''
        for line in f:
            if not line.startswith('#'):
                json_data += line

        # 判断文件内容是否是JSON格式
        if not is_json(json_data):
            print("文件内容不是合法的JSON格式")
            exit()

    # 解析 JSON 格式的内容
    try:
        data = json.loads(json_data)
    except json.JSONDecodeError:
        print("JSON 格式错误")
        exit()

    # 提取 assetUrl 的值
    asset_urls = [item.get("assetUrl") for item in data.get("data", {}).get("list", []) if item.get("assetUrl")]

    # 提取 assetUrl 后面的参数值
    with open('output.txt', 'a') as f:
        for url in asset_urls:
            if '?' in url:
                base_url, params = url.split('?')
                params = '?' + params
                url = base_url + params
            f.write(url + '\n')