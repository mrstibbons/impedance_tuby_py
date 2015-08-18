import os
import sys

from subprocess import call


ui_files_path = os.path.dirname(__file__)
dest_path = ui_files_path + '/../base_classes/'

ui_files = []

for _file in os.listdir(ui_files_path):
    if _file.endswith('.ui'):
        ui_files.append(_file)

for ui_file in ui_files:
    out_file = os.path.basename(ui_file)
    out_file = os.path.splitext(out_file)[0]
    out_file = dest_path + out_file + '.py'
    call(['pyuic4', '-o', out_file, ui_file])

# pyuic4 does not correctly handle the Qwt-Plugin. It fucks up the import. To get automatic correction we add this:
fileObject = open(dest_path + 'main_window.py', 'r')
lines = fileObject.readlines()
fileObject.close()

lines[-1] = "from PyQt4.Qwt5 import QwtPlot"

fileObject = open(dest_path + 'main_window.py', 'w')
fileObject.writelines(lines)
fileObject.close()