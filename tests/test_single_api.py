import os
import pytest
from utils.loader import load_yaml


class TestSingleApi:

    def test_loader_single_api(self):
        """
        加载出的接口请求参数与原始信息一致
        :return: 无
        """
        # 取得当前目录，拼接得到 get_homepage.yml 文件的绝对路径
        # single_api_yaml = os.path.join(os.getcwd(), "api", "get_homepage.yml")
        # os.getcwd()：返回当前目录：C:\Users\CZY\PycharmProjects\HttpRunner_pra\httprunner-shijian\tests
        single_api_yaml = os.path.join(os.path.dirname(__file__), "api", "get_homepage.yml")
        # os.path.dirname(__file__) 返回当前脚本的绝对路径 C:\Users\CZY\PycharmProjects\HttpRunner_pra\httprunner-shijian\tests
        loaded_json = load_yaml(single_api_yaml)  # 加载这个yml文件，转换成字典格式
        assert loaded_json["url"] == "https://mubu.com/"

    # def test_run_single_api(self):
    #     single_api_yaml = os.path.join(os.getcwd(), "api", "get_homepage.yml")
    #     resp = run_yaml(single_api_yaml)
    #     assert resp.status_code == 200



