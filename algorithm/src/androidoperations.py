import os
import os.path as path
import time
import subprocess
def getScreenshotAndSave(dir, ttime):
    dir = path.join(dir, ttime + '.png')
    cmd = f'adb exec-out screencap -p > {dir}'
    os.system(cmd)
    return dir


def sendAndroidTap(x,y):
    print(x,y)
    subprocess.run(["adb", "shell", "input", "tap", str(x) , str(y)])

