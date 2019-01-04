from Api_Server.Root.Gateway import Gateway
from Api_Server.Support.Base_Enums import Enums
from Api_Server.Support.Base_APP import *
import os , requests ,copy ,json
class I_recomChanel(Gateway):
    def __init__(self ,para=''):
        super(I_recomChanel ,self).__init__()

        self.request = requests.session()



    def get_dir_name(self):
        dir_name = str(os.path.dirname(__file__).split('/')[-1])
        return dir_name

    def get_url(self):
        # 在这里区分的是测试环境还是线上环境

        self.url = Enums.test_App_url
        return self.url


    def get_version(self):
        return version.V8_1

    def get_isLogin(self):
        return False

    def get_param(self):
        return {
        "subnavType": "1",
		"homeCallback": "",
        "siteId": "1",
		"subnavId": "59",
		"platformId": "1",
		"subnavNick": "recommend",
        }

    def foces(self):
        #先处理数据
        _data = json.dumps(copy.deepcopy(self.post_data))

        #生成签名
        sign = self.MD5(_data)
        _url = self.url + '/api/mis/nav/home/subnav/recom?sign='+sign

        print(sign)
        re = self.request.post(url=_url , headers = self.Headers , data=_data)
        print(re.text)

    def feed(self ,num):
        # 先处理数据
        temp=copy.deepcopy(self.post_data)
        temp['param']["pageEvent"] ="0"
        temp['param']["pageSize"] = str(num)

        _data = json.dumps(temp)

        # 生成签名
        sign = self.MD5(_data)
        _url = self.url + '/api/mis/nav/home/subnav/flow?sign=' + sign

        re = self.request.post(url=_url, headers=self.Headers, data=_data)
        print(re.text)

if __name__ == '__main__':
    i = I_recomChanel()
    # i.foces()
    i.feed(20)