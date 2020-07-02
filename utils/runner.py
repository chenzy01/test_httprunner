import jsonpath
import requests

from utils.loader import load_yaml


def extract_json_field(resp, json_field):
    value = jsonpath.jsonpath(resp.json(), json_field)
    return value[0]


def run_yaml(yaml_file):
    """
    加载文件后，返回数据;然后用request发起请求，获得状态码，与期望值比较
    :param yaml_file: 加载的 yml 文件
    :return:
    """
    load_json = load_yaml(yaml_file)
    request_data = load_json["request"]  # 提取数据中 request 部分
    method = request_data.pop("method")
    url = request_data.pop("url")
    resp = requests.request(method, url, **request_data)  # 发起请求
    # 因为这里使用了 requests 库，method与url都pop后，只剩下 headers

    validator_mapping = load_json["validate"]  # 提取数据中 validate 部分
    for key in validator_mapping:
        if "$" in key:
            actual_value = extract_json_field(resp, key)  # key = $.code
        else:
            actual_value = getattr(resp, key)  # 等价于 resp.key
        expect_value = validator_mapping[key]
        # print(actual_value)
        # print("***")
        # print(expect_value)
        assert expect_value == actual_value
    return True
