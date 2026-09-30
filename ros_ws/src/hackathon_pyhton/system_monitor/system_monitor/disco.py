import psutil
print(psutil.disk_usage('/')[3])
print(psutil.disk_usage('/')[0])
print(psutil.disk_usage('/')[1])