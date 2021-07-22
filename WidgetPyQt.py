import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def window_go():
    app = QApplication(sys.argv)
    widget = QWidget()
    app.setStyle("Fusion")

# <------------------------------------------> #
#Gabungan Seluru grub
    layouts = QVBoxLayout()
    top = QHBoxLayout()
    mid = QHBoxLayout()
    bottom = QHBoxLayout()
# <++++++++++++++++++++++++++++++++++++++++++> #

# <------------------------------------------> #
#Bagian style dan checkBox
    box_style = QComboBox()
    box_style.addItems(["Fusion"])
    style = QLabel("&Style: ")
    style.setBuddy(box_style)

    standart = QCheckBox('&Use styles standart palette')
    standart.setChecked(True)
    disable = QCheckBox("&Disable widgets")

    top.addWidget(style)
    top.addWidget(box_style)
    top.addStretch(0)
    top.addWidget(standart)
    top.addWidget(disable)
# <++++++++++++++++++++++++++++++++++++++++++> #

# <------------------------------------------> #
#Grub 1
    Grub1 = QGroupBox("Group 1")
    Radio1 = QRadioButton("Radio Button 1")
    Radio2 = QRadioButton("Radio Button 2")
    Radio3 = QRadioButton("Radio Button 3")
    Radio1.setChecked(True)
    TsCB = QCheckBox("Tri-state check box")
    TsCB.setTristate(True)
    TsCB.setCheckState(Qt.PartiallyChecked)

    grub1layout = QVBoxLayout()
    grub1layout.addWidget(Radio1)
    grub1layout.addWidget(Radio2)
    grub1layout.addWidget(Radio3)
    grub1layout.addWidget(TsCB)
    Grub1.setLayout(grub1layout)
# <++++++++++++++++++++++++++++++++++++++++++> #

# <------------------------------------------> #
#Grub 2
    Grub2 = QGroupBox("Group 2")
    Default = QPushButton("Default Push Button")
    Default.setDefault(True)
    Toggle = QPushButton("Toggle Push Button")
    Toggle.setChecked(True)
    Toggle.setCheckable(True)
    Flat = QPushButton("Flat Push Button")
    Flat.setFlat(True)

    grub2layout = QVBoxLayout()
    grub2layout.addWidget(Default)
    grub2layout.addWidget(Toggle)
    grub2layout.addWidget(Flat)
    Grub2.setLayout(grub2layout)
# <++++++++++++++++++++++++++++++++++++++++++> #

# <------------------------------------------> #
#Grub Tabel
    Grub3 = QTabWidget()

    tableTab = QWidget()
    tableWidget = QTableWidget(10,10)
    tableTabLayout = QHBoxLayout()
    tableTabLayout.setContentsMargins(5,5,5,5)
    tableTabLayout.addWidget(tableWidget)
    tableTab.setLayout(tableTabLayout)

    textTab = QWidget()
    editArea = QTextEdit()
    editArea.setPlainText("Halo, Namaku Edo \nMahasiswa Universitas Trunojoyo Madura \nProdi Teknik Informatika")
    textTabLayout = QHBoxLayout()
    textTabLayout.setContentsMargins(5, 5, 5, 5)
    textTabLayout.addWidget(editArea)
    textTab.setLayout(textTabLayout)

    Grub3.addTab(tableTab, "&Table")
    Grub3.addTab(textTab, "Text &Edit")
# <++++++++++++++++++++++++++++++++++++++++++> #

# <------------------------------------------> #
#Grub 4
    Grub4 = QGroupBox("Group 3")
    Grub4.setCheckable(True)
    Grub4.setChecked(True)

    #membuat password
    paswd = QLineEdit("Hello")
    paswd.setEchoMode(QLineEdit.Password)

    #membuat spinBox
    spinBox = QSpinBox()
    spinBox.setValue(25)

    #membuat penampil tanggal
    date = QDateTimeEdit()
    date.setDateTime(QDateTime.currentDateTime())

    #Membuat Slider
    slider = QSlider(Qt.Horizontal)
    slider.setValue(25)

    #Membuat Scroll Bar
    scroll = QScrollBar(Qt.Horizontal)
    scroll.setValue(25)

    #Membuat Dial
    Lingkaran = QDial()
    Lingkaran.setValue(25)
    Lingkaran.setNotchesVisible(True)

    #Penataan Bagian atas
    grub4layout = QFormLayout()
    grub4layout.addRow(paswd)
    grub4layout.addRow(spinBox)
    grub4layout.addRow(date)

    #Mengatur posisi Slider,Scroll, Dan Lingkaran
    posisi1 = QHBoxLayout()
    posisi2 = QVBoxLayout()

    posisi2.addWidget(slider)
    posisi2.addWidget(scroll)
    posisi1.addLayout(posisi2)
    posisi1.addWidget(Lingkaran)
    grub4layout.addRow(posisi1)

    Grub4.setLayout(grub4layout)

#Membuat Progress Bar
    Progress = QProgressBar()
    Progress.setMinimum(0)
    Progress.setMaximum(100)
    Progress.setValue(25)
# <++++++++++++++++++++++++++++++++++++++++++> #

# <------------------------------------------> #
#Enabel dan Disable
    disable.toggled.connect(Grub1.setDisabled)
    disable.toggled.connect(Grub2.setDisabled)
    disable.toggled.connect(Grub3.setDisabled)
    disable.toggled.connect(Grub4.setDisabled)
# <++++++++++++++++++++++++++++++++++++++++++> #

# <------------------------------------------> #
#Pemanggilan Seluruh Layout
    mid.addWidget(Grub1)
    mid.addWidget(Grub2)
    bottom.addWidget(Grub3)
    bottom.addWidget(Grub4)

    layouts.addLayout(top)
    layouts.addLayout(mid)
    layouts.addLayout(bottom)
    layouts.addWidget(Progress)
# <++++++++++++++++++++++++++++++++++++++++++> #

# <------------------------------------------> #
#Pemanggilan Seluru code
    widget.setLayout(layouts)
    widget.show()
    app.exec_()
# <++++++++++++++++++++++++++++++++++++++++++> #

if __name__ == "__main__":
    window_go()