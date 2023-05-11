
import os

path_to_os_release = os.path.expanduser('/etc/os-release')

with open(path_to_os_release) as f:
    name_of_os = f.read()

print(name_of_os)
