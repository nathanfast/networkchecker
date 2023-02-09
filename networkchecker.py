import psutil

print ("Passwordmanager made by Fast")
print ("Visit https://github.com/nathanfast")
print ("")

def monitor_network():
    net_io_counters = psutil.net_io_counters()
    sent = net_io_counters.bytes_sent
    recv = net_io_counters.bytes_recv

    print(f'Bytes sent: {sent}')
    print(f'Bytes received: {recv}')

if __name__ == '__main__':
    monitor_network()
