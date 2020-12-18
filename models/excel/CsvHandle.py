import csv

# 读取csv至字典
csvFile = open("C:\\Users\\lenovo\\Desktop\\563005100_20201216150918.csv", "r")
reader = csv.reader(csvFile)

# 建立空字典
result = {}
for item in reader:
    # 忽略第一行
    if reader.line_num == 1:
        continue
    lon = item[2]
    lat = item[3]
    position_date = item[9]
    direction = item[5]
    speed = item[4]
    print("INSERT INTO `ais_center_data`. `location_202011`(",
          "`position_date`, `device_id`, `device_type`, `longitude`, `latitude`, `direction`, `temperature`, `battery_state`, `speed`, `state`, `data_from`) VALUES (",
          "\'", position_date, "\',", '563005100', ',', '04', ',', lon, ',', lat, ',', direction, ',', 0, ',', 0, ',',
          speed, ',', '0', ',', '00', ");");

csvFile.close()
# print(result)
