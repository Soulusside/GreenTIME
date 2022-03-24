from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QWidget
import h5py

filename = 'tas_day_CNRM-CM6-1_ssp585_r1i1p1f2_gr_20150101-21001231.nc'
f1 = h5py.File(filename,mode = 'r')

app = QtWidgets.QApplication([])
ui = uic.loadUi("design.ui")
ui.setWindowTitle("GreenTime")
all_vars = list(f1.keys())

dolg = f1[all_vars[3]][:] #долгота 256 элементов
shir = f1[all_vars[2]][:] #широта 128 элементов

latlist = []

for i in range(len(shir)):
         latlist.append(str(f1[all_vars[2]][i]))

ui.latitude.addItems(latlist)

lonlist = []

for i in range(len(dolg)):
         lonlist.append(str(f1[all_vars[3]][i]))

ui.longitude.addItems(lonlist)
Period = 1




def Calculate():
    latitude = latlist.index(ui.latitude.currentText())
    longitude = lonlist.index(ui.longitude.currentText())
    ui.Ind.setText("Ожидайте")
    result = []
    if Period == 1:
        den = f1[all_vars[4]][0:10957]
        for i in range(len(den)):
            result.append(den[i][latitude][longitude])
        sumlist = sum(result)
        result = round(sumlist/len(result),3)
        result = result - 273.15
        ui.Ind.setText(str(result))

    elif Period == 2:
        den = f1[all_vars[4]][5478:16800]
        for i in range(len(den)):
            result.append(den[i][latitude][longitude])
        sumlist = sum(result)
        result = round(sumlist/len(result),3)
        result = result - 273.15
        ui.Ind.setText(str(result))

    elif Period == 3:
        den = f1[all_vars[4]][14610:25567]
        for i in range(len(den)):
            result.append(den[i][latitude][longitude])
        sumlist = sum(result)
        result = round(sumlist/len(result),3)
        result = result - 273.15
        ui.Ind.setText(str(result))

    elif Period == 4:
        den = f1[all_vars[4]][18627:29583]
        for i in range(len(den)):
            result.append(den[i][latitude][longitude])
        sumlist = sum(result)
        result = round(sumlist/len(result),3)
        result = result - 273.15
        ui.Ind.setText(str(result))


def CheckRB():
    global Period
    if ui.Period1.isChecked():
        Period = 1
    elif ui.Period2.isChecked():
        Period = 2
    elif ui.Period3.isChecked():
        Period = 3
    elif ui.Period4.isChecked():
        Period = 4
        
    


ui.Button.clicked.connect(Calculate)

ui.Period1.toggled.connect(CheckRB)
ui.Period2.toggled.connect(CheckRB)
ui.Period3.toggled.connect(CheckRB)
ui.Period4.toggled.connect(CheckRB)

try:
    ui.show()
    app.exec()
except Exception as E:
    print(E)
