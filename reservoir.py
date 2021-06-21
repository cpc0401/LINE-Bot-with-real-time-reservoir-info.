import urllib.request as request # 與網站資料做連結
import matplotlib.pyplot as plt # 引用matplotlib來製圖
import numpy as np
import json # 資料為json格式，需要引用json的function
import pyimgur # 製圖完須先上傳至imgur


# 利用政府水利署水庫API連結水庫的資料庫和即時有效蓄水量的資料庫
src_1="https://data.wra.gov.tw/Service/OpenData.aspx?format=json&id=50C8256D-30C5-4B8D-9B84-2E14D5C6DF71"
src_2="https://data.wra.gov.tw/Service/OpenData.aspx?format=json&id=1602CA19-B224-4CC3-AA31-11B1B124530F"
with request.urlopen(src_1) as response:
    data_1=json.load(response) # 載入json格式的資料
with request.urlopen(src_2) as response:
    data_2=json.load(response) # 載入json格式的資料

#print(data)
input_data_1=data_1["DailyOperationalStatisticsOfReservoirs_OPENDATA"] # 先得到資料的每個list
input_data_2=data_2["ReservoirConditionData_OPENDATA"] # 先得到資料的每個list

Database=[] # 整理我們所需的資料（list[listp[]]），每個水庫都有一個list
for line_1 in input_data_1:
    temp=[]
    temp.append(line_1["ReservoirName"]) # index = 0 水庫名稱
    temp.append(line_1["RecordTime"]) # index = 1 紀錄的時間
    temp.append(line_1["EffectiveCapacity"]) # index = 2 水庫最大蓄水量(萬立方公尺)
    temp.append(line_1["CatchmentAreaRainfall"]) # index = 3 集水區雨量，單位：毫米mm
    temp.append(line_1["InflowVolume"]) # index = 4 進水量(萬立方公尺)

    identifier=line_1["ReservoirIdentifier"] # 取出水庫編號
    for line_2 in input_data_2: # 在input_data_2當中尋找水庫的即時有效蓄水量
        if (identifier==line_2["ReservoirIdentifier"] and line_2["EffectiveWaterStorageCapacity"]!=""): # 當找到與水庫編號相符的資料且有效蓄水量不等於空值時
            temp.append(line_2["EffectiveWaterStorageCapacity"]) # 放入list當中
    Database.append(temp) # 將新增好的水庫list放入Database當中

# 紀錄當某水壩的list的size等於5，代表此水壩資訊不足，無法知道有效蓄水量，要刪除此水壩的資料
record_del=[]
for i in range (0, len(Database)):
    if (len(Database[i])==5):
        record_del.append(i)

# 在Database當中刪除掉沒用的水庫資料
i=0
for index in record_del:
    del Database[index-i]
    i+=1

# 計算每一筆水庫的有效蓄水量的百分比
for i in range (0, len(Database)):
    eff_water = float(Database[i][-1])/float(Database[i][2]) # 水庫目前的有效蓄水量/水庫的最大容積能力
    del Database[i][5:] # 刪除不需要的資料
    eff_water = round(eff_water*100,1) # 進位到小數後一位
    Database[i].append(eff_water) # 放入每一筆水庫的資料當中

#for line in Database:
   #print(line)

def create_graph(info):

    plt.clf() # 清除畫布
    plt.cla() # 清除畫布 
    plt.figure(22, figsize=(17,14)) # 制定figure的大小

    # 第一個圖顯示水庫的最大蓄水量、昨日的進水量(ten thousand m^3)
    plt.subplot(211) # 第一個圖表的座標位置
    x_values=[float(info[4]), float(info[2])] # 進水量體積、水庫容積體積
    y_lables=['Inflow Total', 'Resorvoir Capacity'] 
    plt.ylabel('Unit: Ten Thousand Cubic Meter', size=16, fontdict={'family':'serif', 'color':'black', 'weight':'bold'}) # 顯示單位：萬立方公尺
    plt.title('Record Time:'+info[1], size=18,  fontdict={'family':'serif', 'color':'darkblue', 'weight':'bold'}) # 顯示紀錄時間
    plt.barh(y_lables, x_values, edgecolor='black') # 製圖

    # 第二個圖顯示水庫的昨日進水量(mm)
    plt.subplot(223)  # 第二個圖表的座標位置
    y2_values=[100,float(info[3])] # 與100毫米做對比的進水量(毫米)
    x2_lables=['Comparison', 'Inflow'] 
    plt.ylabel('Unit: Millimeter', size=16, fontdict={'family':'serif', 'color':'black', 'weight':'bold'}) # 顯示單位：毫米
    plt.title('Inflow Total (Yesterday)', size=18, fontdict={'family':'serif', 'color':'darkblue', 'weight':'bold'}) 
    plt.bar(x2_lables, y2_values, width=0.8, edgecolor='black') # 製圖

    # 第三張圖顯示水庫目前的有效蓄水量
    plt.subplot(224)  # 第三個圖表的座標位置
    rem=100-info[5] # 剩餘的百分比
    values = [info[5], rem] # 有效蓄水量的百分比, 
    colors = ['C0', 'white'] # default blue, white
    plt.pie( # 開始設定圓餅圖的屬性
        values,
        colors=colors,
        autopct="%0.1f%%", # 顯示到小數點後一位
        pctdistance = 0.65, # 百分比與中心的距離
        wedgeprops={"edgecolor":"0",'linewidth': 1,'linestyle': 'solid', 'antialiased': True} # 圓餅圖外圍的黑色實線
        )
    plt.xlabel('Unit: Ten Thousand Cubic Meter', size=16, fontdict={'family':'serif', 'color':'black', 'weight':'bold'}) # 顯示單位：萬立方公尺
    plt.title('Effective Water Storage', size=18, fontdict={'family':'serif', 'color':'darkblue', 'weight':'bold'})

    # plt.show()
    plt.savefig('send.png') # 存擋
    CLIENT_ID = "6e4973490637fba" # imgur的CLIENT_ID
    PATH = "send.png"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur") # 上傳至imgur
    return uploaded_image.link # return 圖片的連結回來


def search_info(mtext): # 使用者在LINE上所打的文字

    get_search=[]
    # print(mtext)
    for j in range(0,len(Database)):
        if (mtext==Database[j][0]): # 尋找哪一個符合使用者要的資料
            # print(Database[j])
            get_search=Database[j] # 找到資料
            break

    if (len(get_search)!=0): # 當get_search資料長度不為0，代表有找到資料
        img_url = create_graph(get_search) # 跑去製圖的function，得到圖片的連結
        get_search.clear() # 清空list
        return img_url # 回傳圖片連結

    else: # 當get_search資料長度為0，代表沒有找到資料
        img_url = 'error' # 回傳的string是error，給系統做判斷，代表沒有找到資料
        get_search.clear() # 清空list
        return img_url # 回傳error訊息
