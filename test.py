import h5py
import csv
from openpyxl import Workbook

filename = 'tas_day_CNRM-CM6-1_ssp585_r1i1p1f2_gr_20150101-21001231.nc'

f1 = h5py.File(filename,mode = 'r')

all_vars = list(f1.keys())
print(f1['tas'])



#den = f1[all_vars[4]][:] #количество дней 31411
#dolg = f1[all_vars[3]][:] #долгота 256 элементов
#shir = f1[all_vars[2]][:] #широта 128 элементов

dolg = f1[all_vars[3]][:] #долгота 256 элементов
shir = f1[all_vars[2]][:] #широта 128 элементов

latlist = []
for i in range(len(shir)):
         latlist.append(int(f1[all_vars[2]][i]))

lonlist = []
for i in range(len(dolg)):
         lonlist.append(int(f1[all_vars[3]][i]))



def Days():
    ind = 31411
    data = f1[all_vars[4]][:] #количество дней 31411
    with open("new_file.csv", 'w', newline = '') as csvfile:
        for i in range(ind):
            writer = csv.writer(csvfile, delimiter=";")
            writer.writerow([data[i][0][0], '' ,''])
            ind = ind - 1
            print(ind)


def Dolgota():
    data = f1[all_vars[3]][:] #долгота 256 элементов
    total = 0
    for el in data:
        print(f'индекс {total} - {el}')
        total = total + 1


def Shirota():
    data = f1[all_vars[2]][:] #широта 128 элементов
    total = 0
    for el in data:
        print(f'индекс {total} - {el}') 
        total = total + 1


def Odin_Den():
    excel_file = Workbook()
    excel_sheet = excel_file.create_sheet(title='1001', index=0)
    den = f1[all_vars[4]][:] #количество дней 31411
    dolg = f1[all_vars[3]][:] #долгота 256 элементов
    shir = f1[all_vars[2]][:] #широта 128 элементов
    total = 0
    for i in range(1, len(dolg)+1):
        for j in range(1, len(shir)+1):
            total = total+1
            excel_sheet[f'A{total}'] = den[0][j-1][i-1]
            excel_sheet[f'C{total}'] = shir[j-1]
            excel_sheet[f'B{total}'] = dolg[i-1]
            print(len(dolg)+1//i)
    print('end')
    excel_file.save(filename="Result.xlsx")



def Sred(Period, latitude, longitude):
    result = []
    if Period == 1:
        den = f1[all_vars[4]][0:10957]
        for i in range(len(den)):
            result.append(den[i][latitude][longitude])
        sumlist = sum(result)
        result = round(sumlist/len(result),3)
        return result

    elif Period == 2:
        den = f1[all_vars[4]][5478:16800]
        for i in range(len(den)):
            result.append(den[i][latitude][longitude])
        sumlist = sum(result)
        result = round(sumlist/len(result),3)
        return result

    elif Period == 3:
        den = f1[all_vars[4]][14610:25567]
        for i in range(len(den)):
            result.append(den[i][latitude][longitude])
        sumlist = sum(result)
        result = round(sumlist/len(result),3)
        return result

    elif Period == 4:
        den = f1[all_vars[4]][18627:29583]
        for i in range(len(den)):
            result.append(den[i][latitude][longitude])
        sumlist = sum(result)
        result = round(sumlist/len(result),3)
        return result

while True:
    per = int(input('введите период - '))
    with open("sakha.csv", newline = '') as csvfile:
        reader = csv.DictReader(csvfile,delimiter=";")
        print(len(reader.__dict__))
        for row in reader:
            lat = int(float(row['Y']))
            lon = int(float(row['X']))
            if lat in latlist and lon in lonlist:
                latitude = latlist.index(lat)
                longitude = lonlist.index(lon)
                print(Sred(per, latitude, longitude))
        print(f'завершено {per}')             

#print(data[0][0][0]) #день, широта, долгота

#print(data[0][0][0])


f1.close()
