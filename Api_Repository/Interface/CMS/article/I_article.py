from Api_Server.Root.Interface import Interface
import os,requests,copy
from Api_Server.Support.Base_Enums import Enums
from Api_Repository.Data_Center.Entity import *
from Api_Server.Support.Base_Time import *
# from Picture.Picture import CMS_Picture
from Api_Repository.Data_Center.article import *
from Api_Repository.Data_Center.Entity import *


class I_article(Interface):
    def __init__(self ,para=''):
        super(I_article ,self).__init__()

        #文件新建文章需要的自定义的数据
        # self.article_Data=self.get_post_Data(para)  ??


        #得到文章ID

        self.common_post_data={}


  #重写虚方法
    def get_dir_name(self):
        '''
          #必须重新，获得该文件夹名，生成存储文件
        :return: dir_name
        '''
        dir_name=str(os.path.dirname(__file__).split('/')[-1])
        return dir_name

    def get_post_Data(self , para):
        '''
        得到输入的参数，拼接生成可以发送请求的文章参数
        :return: 可以提交的文章的结构体
        '''
        pass

    def get_url(self):
        return Enums.test_Cms_url

    def _public_property(self):
        self.url = 'http://cmstest02.36kr.com/api'
        self.request = requests.session()

    #文章类的基本属性  （1:自己定义的标题、图片等，可以随时改变， 2：系统提供的属性，创建时间等等，不可直接更改的（1：不能更改的 2：可以通过系统事件来更改的）那么就是只读吧


    #文章类拥有的接口
    def recommend(self ,id ,feed=recom_feed.tuijian):
        '''
            url : http://cmstest02.36kr.com/api/post/10464983/recommend
           str : {"recommend_info":"{\"feed_ids\":[269]}"}
           json: recommend_info={"feed_ids":[269]}

           :return {"code":0}
           :type    put
           request
        '''
        _url=self.url+'/post/'+str(id)+'/recommend'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        _data = {"recommend_info":feed}

        re=self.request.put(url=_url ,headers=headers,data=_data)
        print(re.text)

    def push(self , data ):

        '''
        :param :data  get 文章的数据
        :return:
        '''
        _url = 'http://cmstest02.36kr.com/api/push'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        ar_post_data={"sound":"1",
                      "title":data['title'],
                      "content":"推送",
                      "entity_type":"post",
                      "entity_id":data['id'],
                      "publish_now":1,
                      "published_at":"",
                      "expire_time":"4"}

        # fl_post_data=

        re=self.request.post(url=_url , headers=self.Headers ,data=ar_post_data)
        print(re.text)

    def review(self,id):
        '''
        http://cmstest02.36kr.com/api/post/10465218/review
        :param id:
        :return:
        '''
        _url = self.url + '/post/'+str(id)+'/review'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        re=self.request.put(url=_url ,headers=headers,data={})
        print(re.text)

    def delete(self,id):
        '''
        http://cmstest02.36kr.com/api/post/10465214
        :param id:
        :return:{"code":21000,"msg":"文章非草稿或待审状态，不能删除"}
        '''
        _url = self.url + '/post/' + str(id)
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        re = self.request.delete(url=_url ,headers=headers,data={})
        print(re.text)

    # 发布文章流程
    def get_ID(self , title=''):
        '''
          #添加文章
        :url   :  /post
        :data :
         {"title":"测试配图-小图",
        "column_id":"",
        "source_type":"original",
        "user_id":12186523,
        "source_urls":"",
        "content":"",
        "template_info":"{\"template_type\":\"small_image\",\"template_title\":\"测试配图-小图\",\"template_title_isSame\":true,\"template_cover\":[]}"}

        在编辑页面的提交文章标题时，会生成文章ID
        :return:  文章的ID
        '''
        headers = copy.deepcopy(self.Headers)
        _url = self.url + '/post'

        headers['Content-Type'] = 'application/json;charset=UTF-8'

        template = "{\"template_type\":\"small_image\",\"template_title\":\""+title+"\",\"template_title_isSame\":true,\"template_cover\":[]}"

        post_data={"title": title + get_time(),
                   "column_id":"",
                   "source_type":"original",
                   "user_id":12186523,
                   "source_urls":"",
                   "content":"",
                   "template_info":template }

        re=self.request.post(url=_url ,data=post_data ,headers=headers)
        print(re.json())

        return re.json()["data"]

    def get_article_data(self ,data):
        '''
        :param data:
        :return:
        '''
        _url='http://cmstest02.36kr.com/api/post/'+str(data["id"])+'?open_in_editor=1'  #&_=1544607271040

        re=self.request.get(url=_url ,headers=self.Headers)
        common_post_data=re.json()
        print('模板文章 ====>> ' ,common_post_data['data'])
        return common_post_data['data']

    def Cmod_article(self ,article_data ,project_id=1):
        '''
        :param article_data:  模板信息
        :param mod_data:      需要修改的字典
        :return:
        '''
        _url = 'http://cmstest02.36kr.com/api/post/' + str(article_data['id'])
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        mod_data={
            "project_id":str(project_id),
            "template_info": template_info(article_data['title'],0) ,
	        "summary": summary.sum,
	        "content": content.dada,
	        "cover": cover.web,
	        "created_at":get_time(),
	        "updated_at":get_time() ,
	        "report_type": report_type.chuang,
	        "motifs":motifs.one ,
	        "last_open_at":str(time_Stamp())
        }

        for dict in mod_data:
            article_data[dict]=mod_data[dict]

        print(article_data)

        re = self.request.put(url=_url, headers=headers, data=article_data)
        print(re.text)

        return article_data

    def publish(self ,article_data ):
        ''''''
        _url = 'http://cmstest02.36kr.com/api/post/'+str(article_data["id"])+'/publish'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        article_data.update({"publish_now":1})

        re =self.request.put(url=_url ,headers=headers ,data=article_data)
        print(re.text)


    #???
    def common_photo(self,id,url):
        '''
        :data :
        :param id:
        :param url:
        :return:
        '''
        _url = 'http://cmstest02.36kr.com/api/photo-hidden'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        photo="[{"+url+"}]"
        post_data={"entity_id": id,
                   "entity_type": "post",
                    "list": photo}

        re=self.request.post(url=_url ,headers=headers ,data=post_data)
        print(re.text)

    def calculate_motif(self , id ):

        _url ='http://cmstest02.36kr.com/api/post/'+str(id)+'/calculate-motif '

        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        post_data ={}

        re=self.request.post(url=_url , headers=headers ,data=post_data)
        print(re.text)

if __name__ == '__main__':
    #例
    i=I_article()

    #写入text
    # for i1 in range(10):
    #     i.write('21111sssssssssss我是文章1dadwaa')
    # i.write('adada')
    #
    # #写入dict
    # b={"aaaa":111,"22":222222}
    # c={'dada':222444}
    # i.write_dict(b)
    # i.write_dict(c)
    # i.end_write(is_clear=False)   #将存的字典写入text中 ,不删除文件
    #
    # print(i.Headers)

    title='测试第四范式'
    temp=[]
    for m in range(1):
        data=i.get_ID(title)
        print(data)
        article_data=i.get_article_data(data=data)

        post_data=i.Cmod_article(article_data=article_data)

        i.publish(post_data)

        time.sleep(1)

        i.recommend(data['id'])

        temp.append(data['id'])

    # i.push(post_data)
    # print(temp)



    # temp1=[10465227, 10465228, 10465229, 10465230, 10465231, 10465232, 10465233, 10465234, 10465235, 10465236 ,10465237, 10465238, 10465239, 10465240, 10465241, 10465242, 10465243, 10465244, 10465245, 10465246]
    #
    # i.review(10465198)
    # i.delete(10465198)






    # i.create_article(title,data)   ，没用
    # import time
    # time.sleep(4)
    # i.publish(title,data)
    # i.common_photo(id ,CMS_Picture.xiao )
    # i.common_photo(id ,CMS_Picture.web)
    # i.calculate_motif(id)

