# 导入pandas包
import pandas as pd

# 读取Excel数据，选取nyse这一页
excel = pd.read_excel('C:\\Users\\lenovo\\Desktop\\01148AIS 操作.XLS', sheet_name='导出', na_values='n/a')

# # 显示前几行
# print(nyse.head(10))
for i in range(0, 446):
    lon = excel.loc[i, '经度']
    lon = (float(lon[4:9]) / 60 + float(lon[0:3]))
    lat = excel.loc[i, '纬度']
    lat = (float(lat[4:9]) / 60 + float(lat[0:3]))
    position_date = excel.loc[i, "时间"]
    direction = excel.loc[i, "航向"]
    speed = excel.loc[i, "航速节"]

    print("INSERT INTO `ais_center_data`. `location_202011`(",
          "`position_date`, `device_id`, `device_type`, `longitude`, `latitude`, `direction`, `temperature`, `battery_state`, `speed`, `state`, `data_from`) VALUES (",
          "\'", position_date, "\',", '412427961', ',', '04', ',', lon, ',', lat, ',', direction, ',', 0, ',', 0, ',',
          speed, ',', '0', ',', '00', ");");

    # for row in nyse.h:
    #     print(row)
