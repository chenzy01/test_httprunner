import requests

from utils.loader import load_yaml


def run_yaml(yaml_file):
    """
    加载文件后，返回数据
    :param yaml_file: 加载的 yml 文件
    :return:
    """
    load_json = load_yaml(yaml_file)
    method = load_json.pop("method")
    url = load_json.pop("url")
    resp = requests.request(method, url, **load_json)
    # 因为这里使用了 requests 库，method与url都pop后，只剩下 headers
    return resp
