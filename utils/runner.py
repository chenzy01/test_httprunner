import re

import jsonpath
import requests
from requests import sessions

from utils.loader import load_yaml
from utils.validate import *

# 增加 session 机制
session = sessions.Session()
session_variables_mapping = {}

variable_regex_compile = re.compile(r".*\$(\w+).*")  # 匹配是否存在变量，以“$”符号为准


def extract_json_field(resp, json_field):
    value = jsonpath.jsonpath(resp.json(), json_field)
    return value[0]


def replace_var(content, variables_mapping):
    """将 url 中带有参数的变量替换为真实的值
    :param content: url 地址，如 https://mubu.com/list?code=$code
    :param variables_mapping: 要替换的真实的值
    :return:
    """
    matched = variable_regex_compile.match(content)
    if not matched:
        return content
    var_name_code = matched[1]  # 这里匹配到的 matched 是一个数组

    value = variables_mapping.keys()  # variables_mapping = {'var_name': 0}
    replaced_content = content.replace("${}".format(var_name_code), str(value))  # 这里的 value 为数字，若直接替换，会报错
    return replaced_content


def parse_content(content, variables_mapping):
    """ 解析参数
    :param content: 列表或字典
    "request": {
            "url": "http://...",
            "method": "GET",
            "headers: "agent"
            }
    :param variables_mapping:
    :return:
    """
    if isinstance(content, dict):
        parsed_content = {}
        for key, value in content.items():
            parsed_value = parse_content(value, variables_mapping)  # 递归调用，避免 value 中还有字典，有所遗漏
            parsed_content[key] = parsed_value
        return parsed_content

    elif isinstance(content, list):
        parsed_content = []
        for item in content:
            parsed_item = parse_content(item, variables_mapping)
            parsed_content.append(parsed_item)
        return parsed_content

    elif isinstance(content, str):
        return replace_var(content, variables_mapping)
    else:
        return content


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
    """{"request": {
            "url": "http://...",
            "method": "GET",
            "headers: "agent",
            ...
        }       
    }
    """
    global session_variables_mapping  # session_variables_mapping = {}
    parsed_request = parse_content(request_data, session_variables_mapping)  # 将请求的数据提取出来，再次进行解析

    method = parsed_request.pop("method")
    url = parsed_request.pop("url")
    # 因为这里使用了 requests 库，method与url都pop后，只剩下 headers
    # 采用session方式发起请求，避免每次请求都创建一个session，且请求可以保持长久
    resp = session.request(method, url, **parsed_request)

    # 对单个接口进行校验
    validator_mapping = api_info["validate"]  # 提取数据中 validate 部分
    '''
    validate:
        status_code: 200
        # content.code: 0
        $.code: 0
    '''
    for key in validator_mapping:
        if "$" in key:
            actual_value = extract_json_field(resp, key)  # key = $.code
        else:
            actual_value = getattr(resp, key)  # 等价于 resp.key
        expect_value = validator_mapping[key]
        assert expect_value == actual_value

    extractor_mapping = api_info.get("extract", {})  # 避免 extract 为空的话获取失败
    for var_name in extractor_mapping:
        var_expr = extractor_mapping[var_name]  # $.code
        var_value = extract_json_field(resp, var_expr)
        # print("var_value:", var_value)
        session_variables_mapping["var_name"] = var_value  # 为了引用 var_name，便于获取值

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
