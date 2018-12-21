#根据不同地方发布文章
from Api_Repository.Interface.CMS.article.I_article import I_article
from Api_Repository.Interface.CMS.newsflash.I_newsflash import I_newsflash
from Api_Repository.Data_Center.Entity import *
import time


def create_article(i,title , project):


    data = i.get_ID(title, project)

    article_data = i.get_article_data(data=data)

    post_data = i.Cmod_article(article_data=article_data, data=data)

    i.publish(post_data, data=data)

    time.sleep(1)

    i.recommend(data)

    return data

def delete(i,data):

    i.review(data)
    time.sleep(1)
    i.delete(data)




def test_one(num ,title , project=1):
    i = I_article()
    temp_list = []
    for m in range(num):
        temp_list.append(create_article(i,title , project))

    print(temp_list)

    input('是否删除文章')

    for list in temp_list:
        delete(i,data=list)
        time.sleep(1)

def test_two(title ,project):
    news = I_newsflash()
    data = news.publish(title ,project_id=project)

    # input("是否删除")
    #
    # news.review(data)



if __name__ == '__main__':
    # delete = [10465302, 10465303, 10465304, 10465305, 10465306, 10465307, 10465308, 10465309, 10465310, 10465311,
    #           10465312, 10465313, 10465314, 10465315, 10465316, 10465317, 10465318, 10465319, 10465320, 10465321]
    # for m in delete:
    #     temp={"project_id" :86}
    #     temp.update({"id":m})
    #     i.delete(temp)
    # for i in range(6):
    #     test_two('测试厦门快讯', pp_id.xiamen)

    # test_one(50,'测试厦门文章',project=pp_id.xiamen)

    # for i in range(20):
    #     test_two('测试福州快讯', pp_id.fuzhou)
    #     test_two('测试湖州快讯', pp_id.huzhou)
    #     test_two('测试海南快讯', pp_id.hainan)
    #     time.sleep(1)




    test_two("主站",pp_id.zhuzhan)
    # test_two('测试西安快讯', pp_id.xian)
    # test_two('测试海南快讯', pp_id.hainan)
    # test_two('测试福州快讯', pp_id.fuzhou)
    # test_two('测试湖州快讯', pp_id.huzhou)