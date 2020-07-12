import jsonpath
import requests

from utils.loader import load_yaml
from utils.validate import *


def extract_json_field(resp, json_field):
    value = jsonpath.jsonpath(resp.json(), json_field)
    return value[0]


def run_api(api_info):
    """
    :param api_info:
        {
            "request": {},
            "validate": {}
        }
    :return:
    """
    request_data = api_info["request"]  # 提取数据中 request 部分
    method = request_data.pop("method")
    url = request_data.pop("url")
    resp = requests.request(method, url, **request_data)  # 发起请求
    # 因为这里使用了 requests 库，method与url都pop后，只剩下 headers
    # 对单个接口进行校验
    validator_mapping = api_info["validate"]  # 提取数据中 validate 部分
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


'''
def run_api_yaml(api_yaml_file):
    """
    加载文件后，返回数据;然后用request发起请求，获得状态码，与期望值比较
    :param api_yaml_file: 加载的 yml 文件
    :return: 数据完成提取后，返回 True
    """
    load_json = load_yaml(api_yaml_file)
    return run_api(load_json)


def run_testcases_yaml(testcases_yaml_file):
    load_list = load_yaml(testcases_yaml_file)  # testcases_yaml_file 加载后是一个列表
    for api_info in load_list:
        run_api(api_info)
'''


def run_yaml(yml_file):
    loaded_content = load_yaml(yml_file)
    result = []
    if is_api(loaded_content):
        success = run_api(loaded_content)
        result.append(success)
    elif is_testcases(loaded_content):
        for api_info in loaded_content:
            success = run_api(api_info)
            result.append(success)
    else:
        return Exception("YAML format invalid: {}".format(yml_file))

    # print("result:", result)
    return result
