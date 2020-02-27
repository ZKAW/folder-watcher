import os, time
path_to_watch = "/full/path/to/monitor/here"
before = []
after = []
interval = 0.2

for f in os.walk(path_to_watch):
    before += f
while True:
    after = []
    for f in os.walk(path_to_watch):
        after += f
    if before != after:
        before = after
        print("changed")
        # Your actions go here
        
    #else:
    #    print("no change")
 
    time.sleep(interval)
