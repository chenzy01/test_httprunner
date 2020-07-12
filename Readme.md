## httprunner 接口测试  
将 travis-ci 构建的图标显示在 Readme 首页  
[![Build Status](https://travis-ci.org/chenzy01/test_httprunner.svg?branch=master)](https://travis-ci.org/chenzy01/test_httprunner)

将 coverage 覆盖率图片显示在 Readme 首页
[![Coverage Status](https://coveralls.io/repos/github/chenzy01/test_httprunner/badge.svg?branch=master)](https://coveralls.io/github/chenzy01/test_httprunner?branch=master)


### 使用 poetry 工具创建一个虚拟环境

创建一个pyproject.toml
poetry init 

增加依赖，如 requests
poetry add requests  该命令会在 pyproject.toml 文件的[tool.poetry.dependencies]字段下，增加相应的依赖及版本  
但增加依赖后，可能并不能立即使用，因为没有在解释器的环境中安装该软件，可以进入 Setting 中查看，若是没有安装软件
则要在命令行安装：pip install ***软件名称 或者在 Setting > Project interpreter 中安装

增加依赖后，会在相应的目录下创建虚拟环境，
Creating virtualenv httprunner-sVRwEayY-py3.7 in C:\Users\CZY\AppData\Local\pypoetry\Cache\virtualenvs

在配置中，将该项目的解释器修改，选择上面新建的虚拟环境的解释器，切换环境成功
C:\Users\CZY\AppData\Local\pypoetry\Cache\virtualenvs\httprunner-sVRwEayY-py3.7\Scripts


### 登录幕布操作，抓包登录信息

用抓包工具，先登录一次幕布，记录下登录信息，过滤： mubu.com
根据相关接口，及接口的信息，构造请求数据

test_get_homepage()
test_get_login()
test_get_login_password()
test_post_login()

例子： 

```python
import requests
def test_get_homepage():
    url = "https://mubu.com/"
    headers = {
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) "
                              "Chrome/80.0.3987.149 Safari/537.36 "
    }
    r = requests.get(url, headers=headers, verify=False)
    # print(r.text)
    assert r.status_code == 200
```

简单的接口测试三步骤：  
1. 构造参数
    - 构造参数时进行的调试
        - 当参数不知道用什么 headers，可以利用抓包工具的调试功能，逐步减少 headers 中的字段，逐一测试  
        例如使用 charles 中的 compose 功能
        - 打开抓包工具，构造参数完成后，发起请求，查看抓包工具中的请求信息，对比差异
2. 发起请求
    - 发起请求常用 requests 库，注意传入的参数是否完整
3. 断言
    - 获取返回的信息：状态码、错误信息或者其它值，然后与期望值进行比较

### 常用测试框架工具

- pytest/unittest
- postman
- HttpRunner
- katalon
- Selenium
- Appium
- rest-assued
- robotframework
- curl
- httpie

## 项目启动

### 工程初始化

- 基础设施搭建：初始化项目的开发环境，poetry init
    - 用户故事：从用户的角度来描述他的期望，包括：整体概述、详述、验收标准
- github 仓库创建
    - 在 gibhub 创建一个仓库，在本地的项目下，初始化仓库 git init，然后与远程仓库连接 git remote add origin 仓库地址
    - 将创建的文件提交到 github 上，便于后面与 travis-ci 做持续集成测试
- 项目依赖管理
    - poetry+pyproject.toml
    pyproject.toml 文件的格式  
    ```yaml
    [tool.poetry]
        name = "httprunner"
        version = "0.1.0"
        description = ""
        authors = ["chenzy"]
        license = "MIT"
    [tool.poetry.dependencies] # 项目依赖
        python = "^3.5"
    [tool.poetry.dev-dependencies] # 开发环境依赖
        coverage = "^5.1"
    [build-system]
        requires = ["poetry>=0.12"]
        build-backend = "poetry.masonry.api"
    ```

- 持续集成&测试
    - 选择持续集成服务器
        - GitHub > Travis CI
            - 1.创建 .travis.yml 文件
            - .travis.yml 中 python: 的最低版本，要和 pyproject.toml 中 tool.poetry.dependencies 的 python
            起始版本保持一致 
            - GitHub 中的仓库保持干净，不要有其它项目掺杂在一起。若仓库下面有多个二级目录，一个二级目录存放一个项目，
            当向 GitHub 提交代码时，很可能不会触发自动构建。
            - 在 Travis CI 界面，若是第一次提交了所有文件和代码，需要在界面右上角的 Settings 中，找到对应仓库，并激活。
            回到已激活的界面，应该是在 Current 中，点击 Triger Build 按钮，即开始执行测试。往后向该仓库提交代码后，
            便会自动触发构建。点击某个一次版本，查看 Job log ，有完整的构建记录。
        - Gilab > Gilab CI
        - SVN > Jenkins
        - Jenkins
    - 构建脚本
        - 构建脚本是 .travis.yml 文件中 poetry run coverage run --source=httprunner-shijian/tests -m pytest
    - 单元测试
        - 单元测试依赖服务
            - httpbin.org
            - postman
            - 搭建 API 接口 moke 服务
        - 搭建单元测试框架
            - pytest/unittest
    - 为项目添加持续集成构建检查(Travis CI)
        - 访问 Travis CI 官网，用 GitHub 账号登录，同步所有仓库，选择你要构建的仓库，激活它，
        Travis 会监听这个仓库的所有变化
    - 为项目添加单元测试覆盖率检查( coverage & coveralls )
        - coverage & coveralls 这两个文件主要在开发时使用，放在开发者依赖中，与测试安装的依赖分开
        - 使用 coverage 工具 (加上 poetry run 指定在 poetry 虚拟环境中执行)
            - poetry add coverage --dev 增加开发依赖
            - poetry run coverage run --source=test_mubu_login -m pytest  若用例执行的框架是 Pytest,若是未指定
            --source则会执行很多不必要的模块
            - poetry run coverage run --source=test_mubu_login -m unittest discover 若用例执行的框架是 unittest
            - poetry run coverage run -m pytest httprunner-shijian  指定运行的模块
            - poetry run coverage report 收集覆盖信息
            - pip install pytest-cov pytest统计代码测试覆盖率，要先安装该插件 使用命令 pytest --cov=src 
        - 使用 coveralls (httprunner)
            - coveralls的使用方式与Travis CI类似，也需要先在coveralls网站上采用GitHub账号授权登录，
        然后开启需要进行检查的GitHub仓库。而要执行的命令，也可以在.travis.yml配置文件中指定。
        coveralls命令只有在测试覆盖率检查成功以后运行才有意义
            - poetry run coveralls
        
- 发布管理
    - 将项目制作为安装包
    - 分发安装包
    - 发布脚本   
        - poetry publish --builid  在当前目录下面将项目打包
        - 需要输入账号密码，是在pypi上面注册的账号密码，用上面命令发布后，会在pypi中形成安装包，
        则其他人可以通过 pip install 库名称 该方式进行安装             


### 需求规划（需求池）

- 接口测试，核心需求梳理，从需求>测试>版本迭代
    - 了解真正的需求，业务，都和手工测试人员多沟通
    - 实现web接口协议层测试
        - http,https
        - 构造参数
    - 接口请求保持登录态，即 session 保持
    - 接口请求参数传递
        - 接口响应提取
            - jsonpath
            - 正则匹配
        - 参数关联机制
    - 测试脚本支持接入 CI，使用命令行工具进行调用,脚本写入 .travis.yml 文件中
    - 统计用例运行的数据
    - 多用例共享单个接口定义
    - 数据驱动，用例和数据分离、参数化驱动
        - 用例数据放在 test/api/ 目录下，使用 yaml 格式组织数据
    - 快速生成用例
        - 录制用户操作请求
            - 结合抓包工具
            - curl
            
- 框架形式，目标效果
    - 用例组织形式
        - 接口
        - 测试用例文档
        - 用例集
    - 脚本运行方式
        - 类调用运行
        - 命令行运行
    - 结果展示
        - 原始统计数据
        - 运行日志
        - 可视化测试报告
            - 测试代码覆盖率，pytest 工具，命令：pytest --cob=src (src 是某个指定的测试目录或文件)
    - 安装包分发、支持 pip 安装
- 明确优先级，梳理用户故事，版本号规划(遵循一个最小可行性原则)
    - 用户故事1：实现单个HTTP(S)接口的测试
        - 概述：作为测试脚本编写的用户，期望通过YAML的形式描述单个接口，并可将YAML运行起来，以便实现采用
        YAML描述的接口测试脚本
        - 详述
            - 如何用YAML描述单个接口
                - YAML 语法
                - loader: yaml => json ，使用 yaml.load(data)
                - 使用 pyyaml 工具：poetry add pyyaml
            - 如何将YAML脚本运行起来
                - 使用yaml语法描述数据,如
                ```yaml
                request:
                    url: "https://mubu.com/"
                    method: "GET"
                    headers:
                        "user-agent": "Mozilla/5.0 ..."
                    verify: False
                validate:
                    status_code: 200
                ```  
              
                - 写一个接口，用来加载该数据，加载成后返回数据供调用  
                ```python
                import yaml
                def load_yaml(yml_file):
                    with open(yml_file, "r") as f:
                        loaded_json = yaml.load(f.read())
                        return loaded_json

                ```     
              
                - 写一个接口，调用加载数据函数，发起请求或进行其他操作，然后将期望值与结果值比较，进行断言
            - 如何在YAML中实现接口响应校验
                - status_code 判断状态码
                - 响应为json格式，对响应中的特定字段进行校验。考虑返回的数据，使用怎样的数据格式如何提取才更加方便。
        - 验收标准
            - test_loader_single_api  每写一个接口，都要有对应的测试来验证这个接口是否可以用，返回数据是正常且正确  
            ```python
            import os
            from utils.loader import load_yaml
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
                assert loaded_json["request"]["url"] == "https://mubu.com/"

            ```
          
            - test_run_single_yaml 从单个yaml接口开始，让它先运行起来
            ```python
            import requests
            import jsonpath
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
                    assert expect_value == actual_value
                return True

            ```
    - 用户故事2：在单个测试用例中实现复杂场景的测试
    - 用户故事3：接口测试用例支持命令行运行
        - 概述：作为测试脚本编写的用户，期望通过命令行运行单个接口的YAML脚本，以便可以在CI中实现用例的调用运行
        - 详述
            - 命令行工具
            - 命令形式
                - hogrun ***.yml
        - 验收标准
            - hogrun test/api/api_login_submit.yml
        ```python
        # 主要实现代码
        import argparse
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
                'yaml_path', nargs='*',
                help="yaml file path"
            )

            args = parser.parse_args()
        
            if len(sys.argv) == 1:
                # no argument passed
                parser.print_help()
                return 0

            print("testcase_paths----", args.testcase_paths)
            # 这里在命令行书写路径时，绝对路径和相对路径都可以写，路径要用“/”，建议使用相对路径
            api_yml_file = args.testcase_paths[0]
            success = run_yaml(args.yaml_path)  # 检查运行单个 yaml 后的状态
            print(success)

        if __name__ == '__main__':
            main()

        ```
    - 用户故事4：实现多个接口串行测试
        - 概述：作为测试脚本编写的用户，期望通过YAML的形式描述多个接口，并可将YAML运行起来，以便实现采用
        YAML描述场景化的接口测试脚本
        - 详述
            - 如何采用 yaml 描述测试用例，多个HTTP接口串行请求
                - yaml 语法描述
                ```yaml
                -
                    request:
                        url: "https://mubu.com/"
                        method: "GET"
                        headers:
                            "user-agent": "Mozilla/5.0 ..."
                        verify: False
                    validate:
                        status_code: 200
                -
                    request:
                        url: "https://mubu.com/login"
                        method: "GET"
                        headers:
                            "user-agent": "Mozilla/5.0 ... "
                        verify: False
                    validate:
                        status_code: 200
                ```
                - loader: yaml => json
            - 如何将 yaml 测试用例运行起来
            - 如何实现参数关联机制
        - 验收标准
            
        
    - 用户故事5：测试结果的统计和展现
    
- 为什么用 YAML/JSON 组织测试用例
    - 手写脚本重复多，效率低
    - 结构简洁、简单，便于维护
    - 参考其他开源项目的做法
- 如何用 YAML/JSON 描述测试用例



