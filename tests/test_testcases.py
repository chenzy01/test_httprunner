import os
import pytest
import pprint
from utils.loader import load_yaml
from utils.runner import run_yaml


class TestSingleTestcases:
    """
    加载多个接口串行请求内容
    """

    def test_loader_single_testcases(self):
        """
        加载出的用例内容与原始信息一致
        :return: 无
        """
        single_testcases_yaml = os.path.join(os.path.dirname(__file__), "api", "mubu_login.yml")
        # os.path.dirname(__file__) 返回当前脚本的绝对路径 C:\Users\CZY\PycharmProjects\HttpRunner_pra\httprunner-shijian\tests
        loaded_json = load_yaml(single_testcases_yaml)  # 加载这个yml文件，转换成字典格式
        # pprint.pprint(loaded_json)
        assert type(loaded_json) is list
        #  ["request"]["url"] == "https://mubu.com/"

    def test_run_testcases_yml(self):
        single_testcases_yaml = os.path.join(os.path.dirname(__file__), "api", "mubu_login.yml")
        result = run_yaml(single_testcases_yaml)  # 加载这个yml文件，转换成字典格式
        # pprint.pprint(loaded_json)
        assert len(result) == 3
