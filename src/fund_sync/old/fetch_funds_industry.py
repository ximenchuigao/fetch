# https://fundapi.eastmoney.com/fundtradenew.aspx?ft=pg&pi=1&pn=100
# response begin with var rankData =

from typing import Dict
import requests
import demjson
import sqlite3

databaseName = '..\\test.db'


def CreateFundDetailsTable(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.executescript('''
        DROP TABLE IF EXISTS FundIndustry;
        CREATE TABLE FundIndustry (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            code  TEXT,
            fun_name  TEXT,
            one_week    REAL,
            one_month   REAL,
            three_month REAL,
            six_month   REAL,
            from_thisyear   REAL,
            one_year    REAL,
            two_year    REAL,
            three_year  REAL,
            industryCode TEXT,
            industryName, TEXT);''')
    conn.commit()
    cur.close()
    conn.close()


def InsertToDb(dbname, data, code, name):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('''INSERT OR REPLACE INTO FundIndustry
        (code, fun_name, from_thisyear, one_week,one_month,three_month,six_month, one_year,two_year,three_year, industryCode, industryName) 
        VALUES ( ?, ?, ?,?, ?, ?,?, ?, ?,? , ?,? )''',
                (data[0], data[1], data[4], data[5], data[6], data[7],
                 data[8], data[9], data[10], data[11], code, name))
    conn.commit()
    cur.close()
    conn.close()


def fetchdata(curpage, itemCode, itemName):

    # tp=BK0425  -- 工程建设

    url = "http://fund.eastmoney.com/data/FundGuideapi.aspx?dt=4&sd=&ed=&tp={}&sc=3y&st=desc&pi={}&pn=100&zf=diy&sh=list".format(
        itemCode, curpage)
    headers = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    r = requests.get(url, headers=headers)
    content = r.text
    startIndex = len("var rankData =")
    search = content[startIndex:]
    search = search[0: len(search)]
    print(search)
    dataJson = demjson.decode(search)

    data = dataJson['datas']
    pages = dataJson['allPages']
    curpage = dataJson['pageIndex']
    # data is a list
    for d in data:
        InsertToDb(databaseName, d.split(','), itemCode, itemName)
    return {"pages": pages, "curpage": curpage}



CreateFundDetailsTable(databaseName)
dict = {'BK0425': '工程建设',
        'BK0429': '运输设备',
        'BK0433': '农牧饲鱼',
        'BK0437': '煤炭采选',
        'BK0438': '食品饮料',
        'BK0447': '电子信息',
        'BK0448': '通信行业',
        'BK0451': '房地产',
        'BK0454': '塑胶制品',
        'BK0456': '家电行业',
        'BK0458': '仪表仪器',
        'BK0459': '电子元件',
        'BK0465': '医药制造',
        'BK0471': '化纤行业',
        'BK0473': '券商信托',
        'BK0474': '保险',
        'BK0475': '银行',
        'BK0476': '木业家具',
        'BK0477': '酿酒行业',
        'BK0478': '有色金属',
        'BK0479': '钢铁行业',
        'BK0480': '航空航天',
        'BK0481': '汽车行业',
        'BK0490': '军工',
        'BK0492': '煤化工',
        'BK0493': '新能源',
        'BK0494': '节能环保',
        'BK0499': 'AH股',
        'BK0500': 'HS300_',
        'BK0509': '网络游戏',
        'BK0519': '稀缺资源',
        'BK0523': '新材料',
        'BK0528': '转债标的',
        'BK0535': 'QFII重仓',
        'BK0536': '基金重仓',
        'BK0537': '材料行业',
        'BK0538': '化工行业',
        'BK0545': '机械行业',
        'BK0547': '黄金概念',
        'BK0548': '生物疫苗',
        'BK0552': '机构重仓',
        'BK0554': '物联网',
        'BK0561': '基本金属',
        'BK0567': '股权激励',
        'BK0579': '云计算',
        'BK0588': '太阳能',
        'BK0592': '铁路基建',
        'BK0594': '长江三角',
        'BK0596': '融资融券',
        'BK0610': '央视500_',
        'BK0611': '上证50_',
        'BK0612': '上证180_',
        'BK0615': '中药',
        'BK0628': '智慧城市',
        'BK0629': '北斗导航',
        'BK0634': '大数据',
        'BK0638': '创业成分',
        'BK0640': '智能机器',
        'BK0641': '智能穿戴',
        'BK0642': '手游概念',
        'BK0644': '特斯拉',
        'BK0662': '在线教育',
        'BK0666': '苹果概念',
        'BK0668': '医疗器械',
        'BK0674': '蓝宝石',
        'BK0682': '燃料电池',
        'BK0683': '国企改革',
        'BK0693': '基因测序',
        'BK0695': '小金属',
        'BK0696': '国产软件',
        'BK0700': '充电桩',
        'BK0701': '中证500',
        'BK0704': '无人机',
        'BK0705': '上证380',
        'BK0707': '沪股通',
        'BK0712': '一路一带',
        'BK0714': '5G概念',
        'BK0718': '证金持股',
        'BK0724': '海绵城市',
        'BK0727': '医疗行业',
        'BK0728': '环保工程',
        'BK0731': '化肥行业',
        'BK0732': '贵金属',
        'BK0735': '安防设备',
        'BK0737': '软件服务',
        'BK0739': '金属制品',
        'BK0800': '人工智能',
        'BK0804': '深股通',
        'BK0806': '精准医疗',
        'BK0810': '工业4.0',
        'BK0814': '大飞机',
        'BK0821': 'MSCI中国',
        'BK0823': '养老金',
        'BK0830': '区块链',
        'BK0832': '工业互联',
        'BK0840': 'OLED',
        'BK0853': '电子竞技',
        'BK0854': '华为概念',
        'BK0860': '边缘计算',
        'BK0870': '单抗概念',
        'BK0877': 'PCB',
        'BK0879': '标准普尔',
        'BK0884': '光刻胶',
        'BK0891': '国产芯片',
        'BK0893': '无线耳机',
        'BK0896': '白酒',
        'BK0899': 'CRO',
        'BK0900': '新能源车',
        'BK0903': '云游戏',
        'BK0910': '专用设备',
        'BK0916': '氮化镓',
        'BK0917': '半导体',
        'BK0922': '数据中心',
        'BK0935': '中芯概念',
        'BK0960': '无线充电',
        'BK0963': '航天概念',
        'BK0970': '生物识别',
        'BK0980': '债转股'}

for key, values in dict.items():
    cur = 1
    total = 2
    while(cur <= total):
        ret = fetchdata(cur, key, values)
        cur = int(ret["curpage"])+1
        total = int(ret["pages"])
