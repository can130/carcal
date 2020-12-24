# -*- coding: utf-8 -*-
from __future__ import division
from wox import Wox
from wox import WoxAPI
import os


def to_clipboard(query):
    cmd = 'echo ' + str(query).strip() + '| clip'
    os.system(cmd)


class carCal(Wox):

    def query(self, query):
        if query.startswith("c"):
            query = query[1:]
        results = []
        res = "input expr"
        if len(query) > 0:
            try:
                res = eval(query)
            except Exception as e:
                res = "表达式有误: {}".format(e)

        results.append({
            "Title": res,
            "SubTitle": "十进制 点击拷贝",
            "IcoPath": "Images/good.png",
            "JsonRPCAction": {
                # You can invoke both your python functions and Wox public APIs .
                # If you want to invoke Wox public API, you should invoke as following format: Wox.xxxx
                # you can get the public name from https://github.com/qianlifeng/Wox/blob/master/Wox.Plugin/IPublicAPI.cs,
                # just replace xxx with the name provided in this url
                "method": "change_query",
                # you MUST pass parater as array
                "parameters": [res],
                # hide the query wox or not
                "dontHideAfterAction": False
            }
        })

        if str(res).isdigit():
            hexres = hex(res)
            results.append({
                "Title": hexres,
                "SubTitle": "十六进制 点击拷贝",
                "IcoPath": "Images/good.png",
                "JsonRPCAction": {
                    # You can invoke both your python functions and Wox public APIs .
                    # If you want to invoke Wox public API, you should invoke as following format: Wox.xxxx
                    # you can get the public name from https://github.com/qianlifeng/Wox/blob/master/Wox.Plugin/IPublicAPI.cs,
                    # just replace xxx with the name provided in this url
                    "method": "change_query",
                    # you MUST pass parater as array
                    "parameters": [hexres],
                    # hide the query wox or not
                    "dontHideAfterAction": False
                }
            })
            binres = bin(res)
            results.append({
                "Title": binres,
                "SubTitle": "二进制 点击拷贝",
                "IcoPath": "Images/good.png",
                "JsonRPCAction": {
                    # You can invoke both your python functions and Wox public APIs .
                    # If you want to invoke Wox public API, you should invoke as following format: Wox.xxxx
                    # you can get the public name from https://github.com/qianlifeng/Wox/blob/master/Wox.Plugin/IPublicAPI.cs,
                    # just replace xxx with the name provided in this url
                    "method": "change_query",
                    # you MUST pass parater as array
                    "parameters": [binres],
                    # hide the query wox or not
                    "dontHideAfterAction": False
                }
            })
            octres = oct(res)
            results.append({
                "Title": octres,
                "SubTitle": "八进制 点击拷贝",
                "IcoPath": "Images/good.png",
                "JsonRPCAction": {
                    # You can invoke both your python functions and Wox public APIs .
                    # If you want to invoke Wox public API, you should invoke as following format: Wox.xxxx
                    # you can get the public name from https://github.com/qianlifeng/Wox/blob/master/Wox.Plugin/IPublicAPI.cs,
                    # just replace xxx with the name provided in this url
                    "method": "change_query",
                    # you MUST pass parater as array
                    "parameters": [octres],
                    # hide the query wox or not
                    "dontHideAfterAction": False
                }
            })
        return results


    def change_query(self, query):
        # change query and copy to clipboard after pressing enter
        # WoxAPI.change_query(query)
        to_clipboard(query)


if __name__ == "__main__":
    carCal()
