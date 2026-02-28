import psutil
import time

def get_system_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    used_memory_mb = memory.used / (1024 ** 2)
    total_memory_mb = memory.total / (1024 ** 2)

    return {
        'cpu_usage': cpu_usage,
        'used_memory_mb': used_memory_mb,
        'total_memory_mb': total_memory_mb,
        'memory_percent': memory.percent,
        'disk_percent': disk.percent,
    }
def main():
    while True:
        status = get_system_status()
        print(f"CPU: {status['cpu_usage']:.1f}%")
        print(f"Использованная память: {status['used_memory_mb']:.2f} МБ из " 
              f"{status['total_memory_mb']:.2f} МБ ({status['memory_percent']}%)")
        print(f"Загруженность диска: {status['disk_percent']}%")
        print('-' * 60)
        time.sleep(0.2)


if __name__ == '__main__':
    main()