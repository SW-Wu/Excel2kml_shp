# -*- coding: utf-8 -*-
# 程式名稱：Line2shp.py 
# 版本: 2.0
# 作者: S.W.
# 說明：
'''
此程式可將kml2dat得到的資料轉換成有屬性資料之Shapefile圖檔
'''

import shapefile

def shp_generate(fileIn, fileOut):
    try:
        fin=open(fileIn)
        print "資料檔讀取成功，資料轉換中......"
    except:
        print "輸入資料檔名錯誤!"

    #產生一個PolyLine的Shapefile檔
    shp = shapefile.Writer(shapefile.POLYLINE)

    #新增屬性欄位(編號,名稱,測量方法,使用儀器,測定日期(yyyymmdd),測量員,記錄者,備註)
    shp.field('ID','C','10')
    shp.field('NAME','C','10')
    shp.field('METHOD','C','40')
    shp.field('INSTRUMENT','C','40')
    shp.field('DATE','C','8')
    shp.field('OPERATOR','C','20')
    shp.field('RECORDER','C','20')
    shp.field('REMARKS','C','50')
    
    first_line = fin.readline()
    x = ''
    v = []
    #分類檔案內容
    for line in fin:
        parts = []
        line.strip()
        s = line.split(',')
        if len(s) == 8 :
            v.append(s)
            
        else :
            t = s[0]
            t1 = t.replace('[', '')
            t2 = t1.replace(']', '')
            x = x + t2
            b = x.split(';')
    
    
    #處理數據    
    for seg in b:
        a = seg.split()
        l = len(a)           
        if l % 2 != 0 or l < 4:
            print "線段之轉折點必須為(X Y)格式，且至少兩個點對，請檢查資料內容"
            return
        p = []
        for j in range(0, l, 2):
            x = float(a[j])
            y = float(a[j+1])
            p.append([x,y])
        parts.append(p)
    
    for i in range(len(v)):
        id = v[i][0]
        name = v[i][1]
        method = v[i][2]
        inst = v[i][3]
        dt = v[i][4]
        operator = v[i][5]
        recorder = v[i][6]
        remark = v[i][7]
        if i <= 1 :
            points = [parts[i]]
        #加入點位空間資料(坐標)以及屬性資料
        shp.line(points)      #空間資料
        shp.record(id,name,method,inst,dt,operator,recorder,remark)#屬性資料

    #存成檔名為fileOut的shapefile檔
    try:
        shp.save(fileOut)
        print "Shapefile圖檔 %s 產製成功!" % fileOut
    except:
        print "Shapefile圖檔 %s 產製失敗!" % fileOut
        
    fin.close()

if __name__ == '__main__':

    inputFile = raw_input('請輸入點資料檔名(檔名最好是英文，例如：a.dat):')
    outputFile = raw_input('請輸入點Shapefile檔名(檔名最好是英文，例如：G1-Line2012):')
    
    shp_generate(inputFile, outputFile)
    
