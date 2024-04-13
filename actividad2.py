import platform
import sys
import subprocess
import os, platform, re


def get_processor_name():
    if platform.system() == "Windows":
        family = platform.processor()
        name = subprocess.check_output(["wmic","cpu","get", "name"]).strip().split(b"\n")[1].decode().strip()
        return ' '.join([name, family])
    elif platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        command ="sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(command, shell=True).strip().decode()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).decode().strip()
        for line in all_info.split("\n"):
            if "model name" in line:
                return re.sub( ".model name.:", "", line,1).strip()
    return ""

sistemaop = sys.platform
sistema = platform.system()
version = platform.win32_ver() if sistema == 'Windows' else platform.mac_ver()

print("Estamos en {} en version: {}".format(sistema, version))
print("Tipo de SO: {}".format(sistemaop))

if sistema == 'Windows':
    local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
else:
    local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")

print(local)

print("\n")
processor_name = get_processor_name()

print("The hostname of the current system is",os.getenv('COMPUTERNAME', 'defaultValue'))
print("The CPU of the current system is:", processor_name)