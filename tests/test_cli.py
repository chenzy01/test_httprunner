import os
import subprocess


class TestCli:

    def test_hogrun_single_yaml(self):
        single_api_yaml = os.path.join(os.path.dirname(__file__), "api", "api_login_submit.yml")
        project_root_dir = os.path.dirname(os.path.dirname(__file__))
        # subprocess.run 会去读取系统的环境变量，而不是虚拟环境的变量
        subprocess.run("python -m httprunner-shjjian/utils/cli {}".format(single_api_yaml), cwd=project_root_dir)
