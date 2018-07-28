# coding: utf-8
import json
import requests
import xmltodict
import codecs


class GetTimeTable:

    def __init__(self):
        self.API_URLS = "http://radiko.jp/v2/api/program/today?area_id="
        self.AREA_ID = "JP13"

    def get_timetable(self):
        res = requests.get(url=self.API_URLS + self.AREA_ID)
        res.encoding = "utf-8"
        time_table = self.__parse_xml(res.text)
        return time_table

    @staticmethod
    def __parse_xml(source):
        time_table = xmltodict.parse(source)
        return json.dumps(time_table, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    get_timetable = GetTimeTable()
    print(get_timetable.get_timetable())
