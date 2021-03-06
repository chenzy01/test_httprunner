import argparse
import enum
import os

import pytest
import sys

from utils.runner import run_yaml


def main():
    """ API test: parse command line options and run commands.
    """
    parser = argparse.ArgumentParser(description="httprunner")
    parser.add_argument(
        '-V', '--version', dest='version', action='store_true',
        help="show version"
    )
    parser.add_argument(
        'yaml_path',
        help="yaml file path"
    )
    # parser.add_argument(
    #     'yaml_path', nargs='*',
    #     help="yaml file path"
    # )

    args = parser.parse_args()

    if len(sys.argv) == 1:
        # no argument passed
        parser.print_help()
        return 0

    # print("testcase_paths----", args.testcase_paths)
    # 这里在命令行书写路径时，绝对路径和相对路径都可以写，路径要用“/”，建议使用相对路径
    # api_yml_file = args.yaml_path[0]
    success = run_yaml(args.yaml_path)  # 检查运行单个 yaml 后的状态
    return success


if __name__ == '__main__':
    main()
