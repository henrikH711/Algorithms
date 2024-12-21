
import threading
import time

def critical_stage(semaphore, name):
    for _ in range(3):  
        semaphore.acquire()
        try:
            print(f"{name} entering critical section")
            print(f"{name} working in critical section")
            print(f"{name} leaving critical section")
        finally:
            semaphore.release()
        time.sleep(1)  

s = threading.Semaphore(1)

threads = []
for i in range(5):
    t = threading.Thread(target=critical_stage, args=(s, f"Thread-{i+1}"))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads completed.")
