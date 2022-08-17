import shutil
import psutil

def get_disk_usage():
    du = shutil.disk_usage("/")
    print(du)
    print("Free space:", du.free)
    print("Used space:", du.used)
    print("Total space:", du.total)
    print("% usage: {}".format((du.used/du.total)*100))
    print("% free: {}".format((du.free/du.total)*100))

def validate_disk_usage(limit):
    du = shutil.disk_usage("/")
    used = du.used
    free = du.free
    total = du.total
    percent_used = (used/total)*100

    if percent_used > limit:
        print("ERROR: % disk usage exceed limit of {}%".format(limit))
    else:
        print("CORRECT: % usage is within the limit")

    print("Used: {}%".format(percent_used))
    print("Usage limit: {}%".format(limit))

def get_cpu_use():
        psutil.cpu_percent(0.1)

def validate_cpu_usage(limit):
    usage = psutil.cpu_percent(1)
    correct_usage = usage < limit

    if correct_usage == True:
        print("CORRECT: CPU usage is below the limit!!!")
    else:
        print("ERROR: CPU is working too much!!!")

    print("CPU usage: {}%".format(usage))

get_disk_usage()
print("\n")
get_cpu_use()
print("\n")
validate_disk_usage(40)
print("\n")
validate_cpu_usage(60)
