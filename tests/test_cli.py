import os
import subprocess


class TestCli:

    def test_hogrun_single_yaml(self):
        single_api_yaml = os.path.join(os.path.dirname(__file__), "api", "api_login_submit.yml")
        subprocess.run("hogrun {}".format(single_api_yaml))
