# Отчёт о состоянии системы:
# Пользователи системы: 'root', 'user1', ...
# Процессов запущено: 833
#
# Пользовательских процессов:
# root: 533
# user1: 231
# ...
#
# Всего памяти используется: 23.1%
# Всего CPU используется: 33.2%
# Больше всего памяти использует: (%имя процесса, первые 20 символов если оно длиннее)
# Больше всего CPU использует: (%имя процесса, первые 20 символов если оно длиннее)

import subprocess
import psutil

print("ОТЧЕТ О СОСТОЯНИИ СИСТЕМЫ")
print("\nПользователи системы:")
print(psutil.users())

print("\nПроцессов запущено:")
subprocess.run("ps aux | wc -l", shell=True)

print("\nВсего cpu используется:")
print(psutil.cpu_count())

print("\nВсего памяти используется:")
print(f"{psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

print("\nБольше всего памяти использует:")
subprocess.run("ps -eo cmd --sort=-%mem | sed -n \'2p'", shell=True)

print("\nБольше всего cpu использует:")
subprocess.run("ps -eo cmd --sort=-%cpu | sed -n \'2p'", shell=True)

