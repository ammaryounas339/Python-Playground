import threading
def write_file():
    with open ("hello.txt","w") as f:
        while(True):
            f.write("Hello")
def read_file():
    with open ("hello.txt") as f:
        while(True):
            print(f.read())
if __name__ =="__main__":
    t1 = threading.Thread(target=write_file)
    t2 = threading.Thread(target=read_file)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done!")