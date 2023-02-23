import sys              #QApplication
import platform         #OS
#import cpuinfo
#import psutil
import pprint
#import socket
#import dmidecode
import wmi              #BIOS
#import winreg
import os
import subprocess       #Time Zone
import time
#import system_info
import win32com.client
import win32api
import win32file
import ctypes
import re
#import serial
import numba
import numpy as np  
from numba import jit
from PySide6 import QtGui
from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from pathlib import Path
from Test001 import Ui_Dialog
#from serial.tools import list_ports
#from serial.tools.list_ports import comports

class AppWindow(QDialog):

    types = ["SN","BIOS","OS"]
    @numba.njit
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_6.clicked.connect(self.pushButton_6_Click)
        self.ui.pushButton_7.clicked.connect(self.pushButton_7_Click)
        self.ui.pushButton_8.clicked.connect(self.pushButton_8_Click)
        self.ui.pushButton_19.clicked.connect(self.pushButton_19_Click)
        self.ui.pushButton_11.clicked.connect(self.pushButton_11_Click)
        self.ui.pushButton_13.clicked.connect(self.pushButton_13_Click)
        self.ui.pushButton_14.clicked.connect(self.pushButton_14_Click)
        self.ui.pushButton_6.setStyleSheet("QPushButton{background-color:#45458B; color: white;}")
        self.ui.pushButton_7.setStyleSheet("QPushButton{background-color:#45458B; color: white;}")
        self.ui.pushButton_8.setStyleSheet("QPushButton{background-color:#45458B; color: white;}")
        self.ui.pushButton_13.setStyleSheet("QPushButton{background-color:#45458B; color: white;}")
        self.ui.pushButton_14.setStyleSheet("QPushButton{background-color:#45458B; color: white;}")
        self.ui.pushButton_11.setStyleSheet("QPushButton{background-color:#45458B; color: white;}")
        self.ui.pushButton_19.setStyleSheet("QPushButton{background-color:#45458B; color: white;}")


        # OS
        #self.ui.pushButton_3.clicked.connect(self.pushButton_3_Click)
        #self.ui.pushButton_3.setEnabled(False)
        #self.ui.pushButton_3.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        #self.ui.checkBox.setChecked(False)
        # SN
        self.ui.pushButton_18.clicked.connect(self.pushButton_18_Click)
        self.ui.pushButton_18.setEnabled(False)
        self.ui.pushButton_18.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_2.setChecked(False)
        # BIOS
        self.ui.pushButton_2.clicked.connect(self.pushButton_2_Click)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_2.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_3.setChecked(False)
        # HW
        self.ui.pushButton.clicked.connect(self.pushButton_Click)
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_4.setChecked(False)
        # LED
        self.ui.pushButton_30.clicked.connect(self.pushButton_30_Click)
        self.ui.pushButton_30.setEnabled(False)
        self.ui.pushButton_30.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_27.setChecked(False)
        # LAN
        self.ui.pushButton_4.clicked.connect(self.pushButton_4_Click)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_4.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_5.setChecked(False)
        # COM
        self.ui.pushButton_5.clicked.connect(self.pushButton_5_Click)
        self.ui.pushButton_5.setEnabled(False)
        self.ui.pushButton_5.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_6.setChecked(False)
        # USB
        self.ui.pushButton_15.clicked.connect(self.pushButton_15_Click)
        self.ui.pushButton_15.setEnabled(False)
        self.ui.pushButton_15.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_15.setChecked(False)
        # Touch
        self.ui.pushButton_16.clicked.connect(self.pushButton_16_Click)
        self.ui.pushButton_16.setEnabled(False)
        self.ui.pushButton_16.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_16.setChecked(False)
        # BT & WiFi
        self.ui.pushButton_24.clicked.connect(self.pushButton_24_Click)
        self.ui.pushButton_24.setEnabled(False)
        self.ui.pushButton_24.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_21.setChecked(False)
        # Audio
        self.ui.pushButton_22.clicked.connect(self.pushButton_22_Click)
        self.ui.pushButton_22.setEnabled(False)
        self.ui.pushButton_22.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_19.setChecked(False)
        # DVI_DP_HDMI_VGA
        self.ui.pushButton_25.clicked.connect(self.pushButton_25_Click)
        self.ui.pushButton_25.setEnabled(False)
        self.ui.pushButton_25.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_22.setChecked(False)
        # Customized Function
        self.ui.pushButton_27.clicked.connect(self.pushButton_27_Click)
        self.ui.pushButton_27.setEnabled(False)
        self.ui.pushButton_27.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_24.setChecked(False)
        # GPIO
        self.ui.pushButton_21.clicked.connect(self.pushButton_21_Click)
        self.ui.pushButton_21.setEnabled(False)
        self.ui.pushButton_21.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_18.setChecked(False)
        # WDT
        self.ui.pushButton_17.clicked.connect(self.pushButton_17_Click)
        self.ui.pushButton_17.setEnabled(False)
        self.ui.pushButton_17.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_17.setChecked(False)
        # Brightness
        self.ui.pushButton_23.clicked.connect(self.pushButton_23_Click)
        self.ui.pushButton_23.setEnabled(False)
        self.ui.pushButton_23.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_20.setChecked(False)
        # Auto Dimming
        self.ui.pushButton_31.clicked.connect(self.pushButton_31_Click)
        self.ui.pushButton_31.setEnabled(False)
        self.ui.pushButton_31.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_28.setChecked(False)
        # Dead Point
        self.ui.pushButton_28.clicked.connect(self.pushButton_28_Click)
        self.ui.pushButton_28.setEnabled(False)
        self.ui.pushButton_28.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_25.setChecked(False)
        # Resolution
        self.ui.pushButton_26.clicked.connect(self.pushButton_26_Click)
        self.ui.pushButton_26.setEnabled(False)
        self.ui.pushButton_26.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_23.setChecked(False)
        # OSD
        self.ui.pushButton_29.clicked.connect(self.pushButton_29_Click)
        self.ui.pushButton_29.setEnabled(False)
        self.ui.pushButton_29.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_26.setChecked(False)
        # Menu Ver
        self.ui.pushButton_32.clicked.connect(self.pushButton_32_Click)
        self.ui.pushButton_32.setEnabled(False)
        self.ui.pushButton_32.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_29.setChecked(False)
        # UUID
        self.ui.pushButton_33.clicked.connect(self.pushButton_33_Click)
        self.ui.pushButton_33.setEnabled(False)
        self.ui.pushButton_33.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_30.setChecked(False)
        # Time Zone
        self.ui.pushButton_6.setEnabled(True)
        # TXT File
        self.ui.pushButton_12.clicked.connect(self.pushButton_12_Click)
        self.ui.pushButton_12.setEnabled(False)
        self.ui.pushButton_12.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.setStyleSheet("QLabel{background-color:rgba(0, 0, 0, 0.0)}")
        self.show()
        self.combobox_default()
        self.combobox_2_default()
    @numba.njit        
    def read_reg(k = 'DisplayVersion'):
        key = winreg.OpenKeyEx(path, r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\\")
        value = winreg.QueryValueEx(key,k)
    @numba.njit
    def combobox_default(self):
        aplex_list = ["HMI","APC","ACS","Display"]
        self.ui.comboBox.addItems(aplex_list)
        item ="APC"
        self.ui.comboBox.setCurrentText(item)
    @numba.njit        
    def combobox_2_default(self):
        timezone_list = ["France","Germany","Italy","Japan","Singapore","Taipei"]
        self.ui.comboBox_2.addItems(timezone_list)
        item="Taipei"
        self.ui.comboBox_2.setCurrentText(item)
    @numba.njit        
    def bytes_to_GB(self, bytes):
        gb = bytes/(1024*1024*1024)
        gb = round(gb, 2)
        return gb
    @numba.njit    
    def pushButton_13_Click(self):  #Set
        #self.ui.pushButton_3.setEnabled(False)
        #self.ui.pushButton_3.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        #self.ui.checkBox.setChecked(False)
        # SN
        self.ui.pushButton_18.setEnabled(False)
        self.ui.pushButton_18.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_2.setChecked(False)
        # BIOS
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_2.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_3.setChecked(False)
        # SW
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_4.setChecked(False)
        # LED
        self.ui.pushButton_30.setEnabled(False)
        self.ui.pushButton_30.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_27.setChecked(False)
        # LAN
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_4.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_5.setChecked(False)
        # COM
        self.ui.pushButton_5.setEnabled(False)
        self.ui.pushButton_5.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_6.setChecked(False)
        # USB
        self.ui.pushButton_15.setEnabled(False)
        self.ui.pushButton_15.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_15.setChecked(False)
        # Touch
        self.ui.pushButton_16.setEnabled(False)
        self.ui.pushButton_16.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_16.setChecked(False)
        # BT & WiFi
        self.ui.pushButton_24.setEnabled(False)
        self.ui.pushButton_24.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_21.setChecked(False)
        # Audio
        self.ui.pushButton_22.setEnabled(False)
        self.ui.pushButton_22.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_19.setChecked(False)
        # DVI_DP_HDMI_VGA
        self.ui.pushButton_25.setEnabled(False)
        self.ui.pushButton_25.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_22.setChecked(False)
        # Customized Function
        self.ui.pushButton_27.setEnabled(False)
        self.ui.pushButton_27.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_24.setChecked(False)
        # GPIO
        self.ui.pushButton_21.setEnabled(False)
        self.ui.pushButton_21.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_18.setChecked(False)
        # WDT
        self.ui.pushButton_17.setEnabled(False)
        self.ui.pushButton_17.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_17.setChecked(False)
        # Brightness
        self.ui.pushButton_23.setEnabled(False)
        self.ui.pushButton_23.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_20.setChecked(False)
        # Auto Dimming
        self.ui.pushButton_31.setEnabled(False)
        self.ui.pushButton_31.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_28.setChecked(False)
        # Dead Point
        self.ui.pushButton_28.setEnabled(False)
        self.ui.pushButton_28.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_25.setChecked(False)
        # Resolution
        self.ui.pushButton_26.setEnabled(False)
        self.ui.pushButton_26.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_23.setChecked(False)
        # OSD
        self.ui.pushButton_29.setEnabled(False)
        self.ui.pushButton_29.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_26.setChecked(False)
        # Menu Ver
        self.ui.pushButton_32.setEnabled(False)
        self.ui.pushButton_32.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_29.setChecked(False)

        # UUID
        self.ui.pushButton_33.setEnabled(False)
        self.ui.pushButton_33.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_30.setChecked(False)

        # TXT File
        self.ui.pushButton_12.setEnabled(False)
        self.ui.pushButton_12.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        global model
        combotext=str(self.ui.comboBox.currentText())
        model=combotext
        self.ui.textBrowser.setText(combotext)
        if combotext=="HMI":
            # OS
            #self.ui.pushButton_3.setEnabled(True)
            #self.ui.pushButton_3.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}")
            # SN
            self.ui.pushButton_18.setEnabled(True)
            self.ui.pushButton_18.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # BIOS
            self.ui.pushButton_2.setEnabled(True)
            self.ui.pushButton_2.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # SW
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # LED
            self.ui.pushButton_30.setEnabled(True)
            self.ui.pushButton_30.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # LAN
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_4.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # COM
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_5.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # USB
            self.ui.pushButton_15.setEnabled(True)
            self.ui.pushButton_15.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # TOUCH
            self.ui.pushButton_16.setEnabled(True)
            self.ui.pushButton_16.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # BT & WiFi
            self.ui.pushButton_24.setEnabled(True)
            self.ui.pushButton_24.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Audio
            self.ui.pushButton_22.setEnabled(True)
            self.ui.pushButton_22.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # DVI_DP_HDMI_VGA
            self.ui.pushButton_25.setEnabled(True)
            self.ui.pushButton_25.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Customized Function
            self.ui.pushButton_27.setEnabled(True)
            self.ui.pushButton_27.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # GPIO
            self.ui.pushButton_21.setEnabled(True)
            self.ui.pushButton_21.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # WDT
            self.ui.pushButton_17.setEnabled(True)
            self.ui.pushButton_17.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Brightness
            self.ui.pushButton_23.setEnabled(True)
            self.ui.pushButton_23.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Auto Dimming
            self.ui.pushButton_31.setEnabled(True)
            self.ui.pushButton_31.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Dead Point
            self.ui.pushButton_28.setEnabled(True)
            self.ui.pushButton_28.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Resolution
            #self.ui.pushButton_26.setEnabled(True)
            #self.ui.pushButton_26.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # OSD
            #self.ui.pushButton_29.setEnabled(True)
            #self.ui.pushButton_29.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Menu Version
            #self.ui.pushButton_32.setEnabled(True)
            #self.ui.pushButton_32.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # UUID
            self.ui.pushButton_33.setEnabled(True)
            self.ui.pushButton_33.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # TXT File
            self.ui.pushButton_12.setEnabled(True)
            self.ui.pushButton_12.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}")  
        if combotext=="APC":
            # OS
            #self.ui.pushButton_3.setEnabled(True)
            #self.ui.pushButton_3.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}")
            # SN
            self.ui.pushButton_18.setEnabled(True)
            self.ui.pushButton_18.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # BIOS
            self.ui.pushButton_2.setEnabled(True)
            self.ui.pushButton_2.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # SW
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # LED
            self.ui.pushButton_30.setEnabled(True)
            self.ui.pushButton_30.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # LAN
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_4.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # COM
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_5.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # USB
            self.ui.pushButton_15.setEnabled(True)
            self.ui.pushButton_15.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # TOUCH
            self.ui.pushButton_16.setEnabled(True)
            self.ui.pushButton_16.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # BT & WiFi
            self.ui.pushButton_24.setEnabled(True)
            self.ui.pushButton_24.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Audio
            self.ui.pushButton_22.setEnabled(True)
            self.ui.pushButton_22.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # DVI_DP_HDMI_VGA
            self.ui.pushButton_25.setEnabled(True)
            self.ui.pushButton_25.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Customized Function
            self.ui.pushButton_27.setEnabled(True)
            self.ui.pushButton_27.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # GPIO
            self.ui.pushButton_21.setEnabled(True)
            self.ui.pushButton_21.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # WDT
            self.ui.pushButton_17.setEnabled(True)
            self.ui.pushButton_17.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Brightness
            self.ui.pushButton_23.setEnabled(True)
            self.ui.pushButton_23.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Auto Dimming
            self.ui.pushButton_31.setEnabled(True)
            self.ui.pushButton_31.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Dead Point
            self.ui.pushButton_28.setEnabled(True)
            self.ui.pushButton_28.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Resolution
            #self.ui.pushButton_26.setEnabled(True)
            #self.ui.pushButton_26.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # OSD
            #self.ui.pushButton_29.setEnabled(True)
            #self.ui.pushButton_29.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Menu Version
            #self.ui.pushButton_32.setEnabled(True)
            #self.ui.pushButton_32.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # UUID
            self.ui.pushButton_33.setEnabled(True)
            self.ui.pushButton_33.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # TXT File
            self.ui.pushButton_12.setEnabled(True)
            self.ui.pushButton_12.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}")             

        if combotext=="ACS":
            # OS
            #self.ui.pushButton_3.setEnabled(True)
            #self.ui.pushButton_3.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}")
            # SN
            self.ui.pushButton_18.setEnabled(True)
            self.ui.pushButton_18.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # BIOS
            self.ui.pushButton_2.setEnabled(True)
            self.ui.pushButton_2.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # SW
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # LED
            self.ui.pushButton_30.setEnabled(True)
            self.ui.pushButton_30.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # LAN
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_4.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # COM
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_5.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # USB
            self.ui.pushButton_15.setEnabled(True)
            self.ui.pushButton_15.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # TOUCH
            #self.ui.pushButton_16.setEnabled(True)
            #self.ui.pushButton_16.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # BT & WiFi
            self.ui.pushButton_24.setEnabled(True)
            self.ui.pushButton_24.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Audio
            self.ui.pushButton_22.setEnabled(True)
            self.ui.pushButton_22.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # DVI_DP_HDMI_VGA
            self.ui.pushButton_25.setEnabled(True)
            self.ui.pushButton_25.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Customized Function
            self.ui.pushButton_27.setEnabled(True)
            self.ui.pushButton_27.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # GPIO
            self.ui.pushButton_21.setEnabled(True)
            self.ui.pushButton_21.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # WDT
            self.ui.pushButton_17.setEnabled(True)
            self.ui.pushButton_17.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Brightness
            #self.ui.pushButton_23.setEnabled(True)
            #self.ui.pushButton_23.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Auto Dimming
            #self.ui.pushButton_31.setEnabled(True)
            #self.ui.pushButton_31.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Dead Point
            #self.ui.pushButton_28.setEnabled(True)
            #self.ui.pushButton_28.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Resolution
            #self.ui.pushButton_26.setEnabled(True)
            #self.ui.pushButton_26.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # OSD
            #self.ui.pushButton_29.setEnabled(True)
            #self.ui.pushButton_29.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Menu Version
            #self.ui.pushButton_32.setEnabled(True)
            #self.ui.pushButton_32.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # UUID
            self.ui.pushButton_33.setEnabled(True)
            self.ui.pushButton_33.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # TXT File
            self.ui.pushButton_12.setEnabled(True)
            self.ui.pushButton_12.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}")             

        if combotext=="Display":
            # LED
            self.ui.pushButton_30.setEnabled(True)
            self.ui.pushButton_30.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # TOUCH
            self.ui.pushButton_16.setEnabled(True)
            self.ui.pushButton_16.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Audio
            self.ui.pushButton_22.setEnabled(True)
            self.ui.pushButton_22.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # DVI_DP_HDMI_VGA
            self.ui.pushButton_25.setEnabled(True)
            self.ui.pushButton_25.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Customized Function
            self.ui.pushButton_27.setEnabled(True)
            self.ui.pushButton_27.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Brightness
            self.ui.pushButton_23.setEnabled(True)
            self.ui.pushButton_23.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Auto Dimming
            self.ui.pushButton_31.setEnabled(True)
            self.ui.pushButton_31.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Dead Point
            self.ui.pushButton_28.setEnabled(True)
            self.ui.pushButton_28.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Resolution
            self.ui.pushButton_26.setEnabled(True)
            self.ui.pushButton_26.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # OSD
            self.ui.pushButton_29.setEnabled(True)
            self.ui.pushButton_29.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # Menu Ver
            self.ui.pushButton_32.setEnabled(True)
            self.ui.pushButton_32.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") 
            # TXT File
            self.ui.pushButton_12.setEnabled(True)
            self.ui.pushButton_12.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}")             


        else:    
            self.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}")
    @numba.njit
    def pushButton_14_Click(self):
        # OS
        #self.ui.pushButton_3.setEnabled(False)
        #self.ui.pushButton_3.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        #self.ui.checkBox.setChecked(False)
        # SN
        self.ui.pushButton_18.setEnabled(False)
        self.ui.pushButton_18.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_2.setChecked(False)
        # BIOS
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_2.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_3.setChecked(False)
        # SW
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_4.setChecked(False)
        # LED
        self.ui.pushButton_30.setEnabled(False)
        self.ui.pushButton_30.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_27.setChecked(False)
        # LAN
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_4.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_5.setChecked(False)
        # COM
        self.ui.pushButton_5.setEnabled(False)
        self.ui.pushButton_5.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_6.setChecked(False)
        # USB
        self.ui.pushButton_15.setEnabled(False)
        self.ui.pushButton_15.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_15.setChecked(False)
        # Touch
        self.ui.pushButton_16.setEnabled(False)
        self.ui.pushButton_16.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_16.setChecked(False)
        # BT & WiFi
        self.ui.pushButton_24.setEnabled(False)
        self.ui.pushButton_24.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_21.setChecked(False)
        # Audio
        self.ui.pushButton_22.setEnabled(False)
        self.ui.pushButton_22.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_19.setChecked(False)
        # DVI_DP_HDMI_VGA
        self.ui.pushButton_25.setEnabled(False)
        self.ui.pushButton_25.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_22.setChecked(False)
        # Customized Function
        self.ui.pushButton_27.setEnabled(False)
        self.ui.pushButton_27.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_24.setChecked(False)
        # GPIO
        self.ui.pushButton_21.setEnabled(False)
        self.ui.pushButton_21.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_18.setChecked(False)
        # WDT
        self.ui.pushButton_17.setEnabled(False)
        self.ui.pushButton_17.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_17.setChecked(False)
        # Brightness
        self.ui.pushButton_23.setEnabled(False)
        self.ui.pushButton_23.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_20.setChecked(False)
        # Auto Dimming
        self.ui.pushButton_31.setEnabled(False)
        self.ui.pushButton_31.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_28.setChecked(False)
        # Dead Point
        self.ui.pushButton_28.setEnabled(False)
        self.ui.pushButton_28.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_25.setChecked(False)
        # Resolution
        self.ui.pushButton_26.setEnabled(False)
        self.ui.pushButton_26.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_23.setChecked(False)
        # OSD
        self.ui.pushButton_29.setEnabled(False)
        self.ui.pushButton_29.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_26.setChecked(False)
        # Menu Ver
        self.ui.pushButton_32.setEnabled(False)
        self.ui.pushButton_32.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_29.setChecked(False)
        # UUID
        self.ui.pushButton_33.setEnabled(False)
        self.ui.pushButton_33.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6
        self.ui.checkBox_30.setChecked(False)
        # TXT File
        self.ui.pushButton_12.setEnabled(False)
        self.ui.pushButton_12.setStyleSheet("QPushButton{background-color:#8B8B83; color: white;}") #PINK:#DAA3A6

    @numba.njit        
    def pushButton_11_Click(self):
        self.ui.textEdit.clear()
    @numba.njit        
    def pushButton_7_Click(self):
        os.system('shutdown /r /t 5')
    @numba.njit
    def pushButton_8_Click(self):
        os.system('shutdown /s /t 5')
    @numba.njit
    def pushButton_19_Click(self):
        self.ui.pushButton_19.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}")
        timezone=str(self.ui.comboBox_2.currentText())
        if timezone=="France":
            tz="Romance Standard Time"
        if timezone=="Taipei":
            tz="Taipei Standard Time"
        if timezone=="Germany":
            tz="W. Europe Standard Time"
        if timezone=="Italy":
            tz="W. Europe Standard Time"
        if timezone=="Singapore":            
            tz="Singapore Standard Time"
        if timezone=="Japan":            
            tz="Tokyo Standard Time"
        print(tz)
        os.system('tzutil /s '+'"'+tz+'"')  
    @numba.njit       
    def pushButton_Click(self):
        global hwinf
        hwinf=" ================<<< HW Tested >>>================= "
        hwinf+="\n"
        self.ui.textBrowser.setText(hwinf)
        self.ui.checkBox_4.setChecked(True)
        self.ui.pushButton.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        os.system('devmgmt.msc')        
    @numba.njit
    def pushButton_18_Click(self):
        self.ui.pushButton_18.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_2.setChecked(True)
        global sninf
        path ='C:\Windows\AX.ASN'
        file_path = os.path.dirname(path)
        file_exist = os.path.isfile(path)
        print(file_exist)
        if file_exist==True:
        #self.ui.textBrowser.setText(file_path) 
            for root, dirs, files in os.walk(file_path):
                for file in files:
                    if file.endswith('.ASN'):
                        fileall = open(str(file),'r')
                        finally_contents = fileall.read()
                        sninf=" ================<<< SN Tested >>>================ "
                        sninf+="\n"+"File Name: "+str(file)
                        sninf+="\n"+"File Path: "+root+'\\'+str(file)
                        sninf+="\n"+"#############################################"
                        sninf+="\n"+file_contents
                        sninf+="\n"+" "
                        fileall.close()
                        self.ui.textBrowser.setText(sninf)
        else:
            sninf=">>>>> No SN file in "+file_path+" <<<<<<"
            self.ui.textBrowser.setText(sninf)
            #fileall.close()
    @numba.njit
    def pushButton_2_Click(self):
        global biosinf
        self.ui.pushButton_2.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        bios = wmi.WMI().Win32_BIOS()[0]
        biosinf=" ================<<< BIOS Tested >>>================ "
        biosinf+="\n"+"SN:"+str(bios.Name)
        biosinf+="\n"+"ReleaseDate:"+str(bios.ReleaseDate)
        #biosinf+="\n"+"Language:"+str(bios.CurrentLanguage)
        #biosinf+="\n"+"Description:"+str(bios.Description)
        #biosinf+="\n"+"Manufacturer:"+str(bios.Manufacturer)
        #biosinf+="\n"+"Version:"+str(bios.Version)
        #biosinf+="\n"+"SerialNumber:"+str(bios.SerialNumber)
        #biosinf+="\n"+"BIOSVersion"+str(bios.BIOSVersion)
        #biosinf+="\n"+"BuildNumber:"+str(bios.BuildNumber)
        #biosinf+="\n"+"CodeSet:"+str(bios.CodeSet)
        #biosinf+="\n"+"IdentificationCode:"+str(bios.IdentificationCode)
        #biosinf+="\n"+"TargetOperatingSystem:"+str(bios.TargetOperatingSystem)
        #biosinf+="\n"+"PrimaryBIOS:"+str(bios.PrimaryBIOS)
        #biosinf+="\n"+"InstallDate:"+str(bios.InstallDate)
        #biosinf+="\n"+"Caption:"+str(bios.Caption)
        #biosinf+="\n"+"EmbeddedControllerMajorVersion:"+str(bios.EmbeddedControllerMajorVersion)
        #biosinf+="\n"+"EmbeddedControllerMinorVersion:"+str(bios.EmbeddedControllerMinorVersion)
        #biosinf+="\n"+"SMBIOSBIOSVersion:"+str(bios.SMBIOSBIOSVersion)
        #biosinf+="\n"+"SMBIOSMinorVersion:"+str(bios.SMBIOSMinorVersion)
        #biosinf+="\n"+"SMBIOSMajorVersion:"+str(bios.InstallDate)
        #biosinf+="\n"+"SMBIOSPresent:"+str(bios.SMBIOSPresent)
        #biosinf+="\n"+"SoftwareElementID:"+str(bios.SoftwareElementID)
        #biosinf+="\n"+"SoftwareElementState:"+str(bios.SoftwareElementState)
        #biosinf+="\n"+"Status:"+str(bios.Status)
        #biosinf+="\n"+"SystemBiosMajorVersion:"+str(bios.SystemBiosMajorVersion)
        #biosinf+="\n"+"SystemBiosMinorVersion:"+str(bios.SystemBiosMinorVersion)
        #biosinf+="\n"+"BiosCharacteristics:"+str(bios.BiosCharacteristics)        

        self.ui.textBrowser.setText(biosinf)        
        self.ui.checkBox_3.setChecked(True)
        
    #def pushButton_3_Click(self):
        #self.ui.pushButton_3.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        #osinf="OS    Version:           "+platform.platform()
        #osinf+="\n"+"OS    Edition:            "+platform.win32_edition()
        #osinf+="\n"+"OS    Architecture:    "+platform.machine()
        #osinf+="\n"+"CPU  Name:             "+platform.processor()
        #osinf+="\n"+"PC    Name:             "+platform.node()
        #self.ui.textBrowser.setText(osinf)
        #self.ui.checkBox.setChecked(True)
    @numba.njit        
    def pushButton_30_Click(self):
        global ledinf
        ledinf=" ================<<< LED Tested >>>================= "
        ledinf+="\n"
        self.ui.textBrowser.setText(ledinf)
        self.ui.pushButton_30.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_27.setChecked(True)
    @numba.njit        
    def pushButton_4_Click(self):
        self.ui.textBrowser.clear()
        subprocess.call([r'Script\LAN.bat'])
        global laninf
        laninf=" ================<<< LAN Tested >>>================= "
        laninf+="\n"
        self.ui.textBrowser.setText(laninf)
        self.ui.pushButton_4.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_5.setChecked(True)
    @numba.njit        
    def pushButton_5_Click(self):
        self.ui.textBrowser.clear()
        subprocess.call([r'Script\COM.bat'])
        global cominf
        cominf=" ================<<< COM Tested >>>================= "
        cominf+="\n"
        self.ui.textBrowser.setText(cominf)
        self.ui.pushButton_5.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_6.setChecked(True)
    @numba.njit        
    def pushButton_15_Click(self):
        subprocess.call([r'Script\USB.bat'])
        global usbinf
        usbinf=" ================<<< USB Tested >>>================= "
        usbinf+="\n"
        self.ui.textBrowser.setText(usbinf)
        self.ui.pushButton_15.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_15.setChecked(True)
    @numba.njit        
    def pushButton_16_Click(self):
        subprocess.call([r'Script\Touch.bat'])
        global touchinf
        touchinf=" ================<<< Touch Tested >>>================= "
        touchinf+="\n"
        self.ui.textBrowser.setText(touchinf)
        self.ui.pushButton_16.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_16.setChecked(True)
    @numba.njit       
    def pushButton_24_Click(self):
        subprocess.call([r'Script\BT.bat'])
        global btinf
        btinf=" ================<<< BT Tested >>>================= "
        btinf+="\n"
        self.ui.textBrowser.setText(btinf)
        self.ui.pushButton_24.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_21.setChecked(True)
    @numba.njit        
    def pushButton_22_Click(self):
        subprocess.call([r'Script\Audio.bat'])
        global auinf
        auinf=" ================<<< Audio Tested >>>================= "
        auinf+="\n"
        self.ui.textBrowser.setText(auinf)
        self.ui.pushButton_22.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_19.setChecked(True)
    @numba.njit        
    def pushButton_25_Click(self):
        subprocess.call([r'Script\DVI_DP_HDMI_VGA.bat'])
        global ddhvinf
        ddhvinf=" ================<<< DVI-DP-HDMI-VGA Tested >>>================= "
        ddhvinf+="\n"
        self.ui.textBrowser.setText(ddhvinf)
        self.ui.pushButton_25.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_22.setChecked(True)
    @numba.njit        
    def pushButton_27_Click(self):
        global cfinf
        cfinf=" ================<<< Customized Function Tested >>>================= "
        cfinf+="\n"
        self.ui.textBrowser.setText(cfinf)
        self.ui.pushButton_27.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_24.setChecked(True)
    @numba.njit        
    def pushButton_21_Click(self):
        subprocess.call([r'Script\GPIO.bat'])
        global gpioinf
        gpioinf=" ================<<< GPIO Tested >>>================= "
        gpioinf+="\n"
        self.ui.textBrowser.setText(gpioinf)
        self.ui.pushButton_21.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_18.setChecked(True)
    @numba.njit        
    def pushButton_17_Click(self):
        subprocess.call([r'Script\WDT.bat'])
        global wdtinf
        wdtinf=" ================<<< WDT Tested >>>================= "
        wdtinf+="\n"
        self.ui.textBrowser.setText(wdtinf)
        self.ui.pushButton_17.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_17.setChecked(True)
    @numba.njit
    def pushButton_23_Click(self):
        subprocess.call([r'Script\Brightness.bat'])
        global brinf
        brinf=" ================<<< Brightness Tested >>>================= "
        brinf+="\n"
        self.ui.textBrowser.setText(brinf)
        self.ui.pushButton_23.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_20.setChecked(True)
    @numba.njit        
    def pushButton_31_Click(self):
        global adinf
        adinf=" ================<<< Auto Dimming Tested >>>================= "
        adinf+="\n"
        self.ui.textBrowser.setText(adinf)
        self.ui.pushButton_31.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_28.setChecked(True)
    @numba.njit        
    def pushButton_28_Click(self):
        subprocess.call([r'Script\LCD.bat'])
        global dpinf
        dpinf=" ================<<< Dead Point Tested >>>================= "
        dpinf+="\n"
        self.ui.textBrowser.setText(dpinf)
        self.ui.pushButton_28.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_25.setChecked(True)
    @numba.njit        
    def pushButton_26_Click(self):
        subprocess.call([r'Script\DVI_DP_HDMI_VGA.bat'])
        global reinf
        reinf=" ================<<< Resolution Tested >>>================= "
        reinf+="\n"
        self.ui.textBrowser.setText(reinf)
        self.ui.pushButton_26.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_23.setChecked(True)
    @numba.njit        
    def pushButton_29_Click(self):
        global osdinf
        osdinf=" ================<<< OSD Tested >>>================= "
        osdinf+="\n"
        self.ui.textBrowser.setText(osdinf)
        self.ui.pushButton_29.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_26.setChecked(True)
    @numba.njit        
    def pushButton_32_Click(self):
        global mvinf
        mvinf=" ================<<< Manu Ver Tested >>>================= "
        mvinf+="\n"
        self.ui.textBrowser.setText(mvinf)
        self.ui.pushButton_32.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_29.setChecked(True)
    @numba.njit        
    def pushButton_33_Click(self):
        global uuidinf
        uuidinf=" ================<<< UUID Tested >>>================= "
        self.ui.textBrowser.clear()
        subprocess.call([r'UUID\2896UUID.bat'])
        path = 'UUID/2896_UUID.txt'
        theBeatles = ['wmic csproduct get IdentifyingNumber','wmic csproduct get Name','wmic csproduct get uuid','wmic csproduct get Vendor']
        for beatle in theBeatles:
            process = subprocess.Popen(beatle, stdout=subprocess.PIPE)
            dataout,error = process.communicate()
            allinfo=str(dataout.decode('ascii').split())
            uuidinf+="\n"+allinfo
            uuidinf+="\n"
        uuid2896 = open(path,'r')
        u2896=uuid2896.read()
        print(uuid2896.read())
        uuidinf+="\n"+"<< ACS-2896 >>"
        uuidinf+="\n"+u2896
        uuidinf+="\n"+"((Already Output to 2896_UUID.txt))"
        self.ui.textBrowser.setText(uuidinf)
        self.ui.pushButton_33.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        self.ui.checkBox_30.setChecked(True)
    @numba.njit        
    def pushButton_6_Click(self):
        theBeatles = ['tzutil /g']
        for beatle in theBeatles:
            process = subprocess.Popen(beatle, stdout=subprocess.PIPE)
            dataout,error = process.communicate()
            tzinfo=str(dataout.decode('ascii').split())
            print(tzinfo)
            self.ui.textBrowser_2.setText(tzinfo)
    @numba.njit        
    def pushButton_12_Click(self):
        self.ui.pushButton_12.setStyleSheet("QPushButton{background-color:#A3C1DA; color: white;}") 
        msg = self.ui.textEdit.toPlainText()
        if msg=="":
           self.ui.textBrowser.setText("Please scan SN number and try again")
           self.ui.pushButton_12.setStyleSheet("QPushButton{background-color:#DAA3A6; color: white;}") #PINK:#DAA3A6
        else:
            filename = msg+".txt"
            with open('Report/'+filename,'a') as f:
                qct="-------------------------------- QC Test Report ---------------------------------------"
                qct+="\n"
                qct+="\n"+"Model: "+model+" Serier"+"        SN Munber: "+msg+"      Date: "+time.strftime("%Y-%m-%d_%H:%M:%S")
                qct+="\n"
                qct+="\n"+"-------------------------------------------------------------------------------------"
                print(qct,file=f)       
                #OS Info
                #if self.ui.checkBox.isChecked():
                   # global osinf
                    #osinf=" ================<<< OS Tested >>>================ "
                    #osinf+="\n"+"OS  Version:       "+platform.platform()
                    #osinf+="\n"+"OS  Edition:       "+platform.win32_edition()
                    #osinf+="\n"+"OS  Architecture:  "+platform.machine()
                    #osinf+="\n"+"CPU Name:          "+platform.processor()
                    #osinf+="\n"+"PC  Name:          "+platform.node()
                    #osinf+="\n"+" "
                    #print(osinf,file=f)
          
                #SN Info
                if self.ui.checkBox_2.isChecked():
                    print(sninf,file=f)
                #BIOS Info    
                if self.ui.checkBox_3.isChecked():
                    print(biosinf,file=f)
                #HW Info    
                if self.ui.checkBox_4.isChecked():
                    print(hwinf,file=f)
                #UUID info
                if self.ui.checkBox_30.isChecked():
                    print(uuidinf,file=f)
                #LAN info
                if self.ui.checkBox_5.isChecked():
                    print(laninf,file=f)
                #COM info
                if self.ui.checkBox_6.isChecked():
                    print(cominf,file=f)
                #USB info
                if self.ui.checkBox_15.isChecked():
                    print(usbinf,file=f)     
                #TOUCH info
                if self.ui.checkBox_16.isChecked():
                    print(touchinf,file=f)
                #BT info
                if self.ui.checkBox_21.isChecked():
                    print(btinf,file=f)
                #AUDIO info
                if self.ui.checkBox_19.isChecked():
                    print(auinf,file=f)
                #DP-DVI-HDMI-VGA info
                if self.ui.checkBox_22.isChecked():
                    print(ddhvinf,file=f)
                #CUS FUNC info
                if self.ui.checkBox_24.isChecked():
                    print(cfinf,file=f)
                #GPIO info
                if self.ui.checkBox_18.isChecked():
                    print(gpioinf,file=f)
                #WDT info
                if self.ui.checkBox_17.isChecked():
                    print(wdtinf,file=f)
                #BRIGHTNESS info
                if self.ui.checkBox_20.isChecked():
                    print(brinf,file=f)
                #Auto Dimming info
                if self.ui.checkBox_28.isChecked():
                    print(adinf,file=f)
                #DEAD POINT info
                if self.ui.checkBox_25.isChecked():
                    print(dpinf,file=f)
                #RESOLUTION info
                if self.ui.checkBox_23.isChecked():
                     print(reinf,file=f)
                #OSD info
                if self.ui.checkBox_26.isChecked():
                    print(osdinf,file=f)
                #MANU VER info
                if self.ui.checkBox_29.isChecked():
                    print(mvinf,file=f)
                #LED info
                if self.ui.checkBox_27.isChecked():
                    print(ledinf,file=f)
                f.close()


                self.ui.textBrowser.setText("Report Output Successful !!!")
 

        
            

 
stylesheet = """
      AppWindow {
       background-image: url("C:/APP/Python/ax_1024x768.jpg"); 
       background-repeat: no-repeat; 
       background-position: center;
      }
   """

app = QApplication(sys.argv)
app.setStyleSheet(stylesheet)

w = AppWindow()
w.show()



    
sys.exit(app.exec_())
