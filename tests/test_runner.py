import os
from utils.runner import replace_var


class TestHogRunner:
    """检测能否将 url 中的参数替换为真实的值
    """

    def test_replace_no_var(self):
        raw_str = "https://mubu.com/list?code=123"
        variable_mapping = {
            "code": 0
        }
        replace_str = replace_var(raw_str, variable_mapping)
        assert replace_str == "https://mubu.com/list?code=123"

    def test_replace_var(self):
        raw_str = "https://mubu.com/list?code=$code"
        variable_mapping = {
            "code": 0
        }
        replace_str = replace_var(raw_str, variable_mapping)
        # print(replace_str)
        assert replace_str == "https://mubu.com/list?code=0"