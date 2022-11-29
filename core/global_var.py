import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

CST_HOME = r"D:\CST Micro Studio\AMD64\python_cst_libraries"

WORK_HOME = rootPath

cst_save_dir = os.path.join(WORK_HOME, "CST_Project")
output_dir = os.path.join(WORK_HOME, "output")
