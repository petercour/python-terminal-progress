import time
import tqdm
 
def work1():
    time.sleep(1)
def work2():
    time.sleep(1)
def work3():
    time.sleep(1)
def work4():
    time.sleep(1)
def work5():
    time.sleep(1)
def work6():
    time.sleep(1)
 
def worker():
    work_set = [work1, work2, work3, work4, work5, work6]
    return work_set
 
def main():
    a = worker()
    for i in tqdm.tqdm(range(6)):
        b = a[i]()
 
if __name__ == '__main__':
    main()
