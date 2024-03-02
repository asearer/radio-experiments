import psutil

def monitor_performance():
    # Retrieve CPU and memory usage
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent

    # Retrieve disk usage
    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent

    # Retrieve network information
    network_io = psutil.net_io_counters()
    bytes_sent = network_io.bytes_sent
    bytes_received = network_io.bytes_recv

    # Print performance metrics
    print(f"CPU Usage: {cpu_percent}%")
    print(f"Memory Usage: {memory_percent}%")
    print(f"Disk Usage: {disk_percent}%")
    print(f"Bytes Sent: {bytes_sent}")
    print(f"Bytes Received: {bytes_received}")

# Test the function
if __name__ == "__main__":
    monitor_performance()
