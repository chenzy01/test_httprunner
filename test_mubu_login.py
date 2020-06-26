import requests


class TestMubuLogin:

    def test_get_homepage(self):
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
        print(r.text)
        assert r.status_code == 200

    def test_get_login(self):
        url = "https://mubu.com/login"
        headers = {
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) "
                                  "Chrome/80.0.3987.149 Safari/537.36 "
        }
        r = requests.get(url, headers=headers, verify=False)
        print(r.text)
        assert r.status_code == 200

    def test_get_login_password(self):
        url = "https://mubu.com/login/password"
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

    def test_post_login(self):
        url = "https://mubu.com/api/login/submit"
        headers = {

            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) "
                          "Chrome/80.0.3987.149 Safari/537.36 ",
            "x-requested-with": "XMLHttpRequest",
        }
        data = {"phone": 15820723515, "password": "101402108mynba"}
        r = requests.post(url, headers=headers, data=data, verify=False)
        # print(r.text)
        assert r.status_code == 200
        r_json = r.json()
        assert r_json["code"] == 0


# if __name__ == '__main__':
#     mubu = TestMubuLogin()
#     mubu.test_get_homepage()
#     mubu.test_get_login()
#     mubu.test_get_login_password()
#     mubu.test_post_login()
