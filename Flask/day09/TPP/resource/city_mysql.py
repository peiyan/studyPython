import json
import pymysql

def begin():
    # 链接数据库
    db = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='123456',database='sztpp1805')
    # 游标
    cursor = db.cursor()

    # 打开文件
    with open('city.json', 'r') as f:
        # json形式
        city_json = json.load(f)

        # 所有字母 [key]
        returnValue = city_json['returnValue']
        letters_key = returnValue.keys()
        # print(letters_key)

        # 遍历(将数据插入到数据库中)
        for letter_key in letters_key:
            # letter表
            # 通过游标，执行sql语句
            db.begin()
            cursor.execute("INSERT INTO letter(name) VALUES('{}')".format(letter_key))
            db.commit()


            # 字母对应的城市数组
            citys = returnValue[letter_key]

            # 字母对应的id
            db.begin()
            cursor.execute("SELECT id FROM letter WHERE name='{}'".format(letter_key))
            db.commit()
            result = cursor.fetchone()
            letter_id = result[0]

            # 遍历
            for city in citys:
                # city表
                # print(city['regionName'])
                cityid = city['id']
                parentId = city['parentId']
                regionName = city['regionName']
                cityCode = city['cityCode']
                pinYin = city['pinYin']

                db.begin()
                cursor.execute("INSERT INTO city VALUES({},{},'{}',{},'{}',{})".format(cityid,parentId,regionName,cityCode,pinYin,letter_id))
                db.commit()



# 读取json数据，转为未sql语句
if __name__ == '__main__':
    begin()