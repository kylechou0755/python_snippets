# coding:utf-8

"""
    1: 导入 user.json 文件检查
    2: 导入 gift.json 文件检查
"""
import os
from common.utils import check_file


class Base(object):
    def __init__(self, user_json, gift_json):
        self.user_json = user_json
        self.gift_json = gift_json

        self.__check_user_json()
        self.__check_gift_json()

    def __check_user_json(self):
        check_file(self.user_json)

    def __check_gift_json(self):
        check_file(self.gift_json)


if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    # print(gift_path)
    # print(user_path)
    base = Base(user_path, gift_path)
