# -*- coding: utf-8 -*-
# 程式名稱：kml2dat.py
# 版本：1.0
# 作者：S.W.
# 說明：
"""
此程式用來處理在google earth 產生的 路線.kml 檔案，將其轉化為數化路徑所需的格式。

注意！！
kml檔內只能包含一條路線！！
"""

import twd97
from math import radians

print '------檔案名稱都不用加附檔名------'
print '注意！！  kml檔內只能有一條路線\n'
opfin = raw_input('選擇kml檔案：')
edfin = raw_input('輸出檔名：')
fin = open(opfin +'.kml', 'r')
fout = open(edfin + '.dat', 'w')
v = []
for i in fin :
    i.strip()
    x = i.split()
    v.append(x)
geo = v[-6]
part = []
print '資料讀取成功'
print '------此為表格之內容------\n'
c2 = raw_input('路徑名稱：')
c5 = raw_input('轉換日期(yyyymmdd)：')
c6 = raw_input('轉換者：')
fout.write('%s,%s,%s,%s,%s,%s,%s,%s'%('點號','名稱','測量方法','使用儀器','測定日期(yyyymmdd)','測量員','記錄者','備註'))
fout.write('\n')
fout.write('%s,%s,%s,%s,%s,%s,%s,%s'%('001',c2,'GPS','Google Earth轉換',c5,c6,c6,'無'))
fout.write('\n')
fout.write('[')

# ------處理kml的座標並轉為TWD97的座標------
for j in geo :
    new = j.replace(',0','')
    new1 = new.split(',')
    part.append(new1)
for k in part:
    Lat = float(k[1])
    Lon = float(k[0])
    t = twd97.LatLonToTWD97()
    X, Y = t.convert(radians(Lat), radians(Lon))
    fout.write('%f %f'%(X,Y))
    fout.write('\n')
fout.write('] ;')

print '...轉換中...'

print '處理完成'
fin.closed
fout.closed
               
               
