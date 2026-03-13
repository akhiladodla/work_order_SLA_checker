def count_log_levels(logs):
    counts={}
    for log in logs:
        level=log.split(":")[0]
        if level in counts:
            counts[level]+=1
        else:
            counts[level]=1
    return counts
logs=["ERROR:disk full","INFO:started","ERROR:timeout","WARN:low memory"]
print(count_log_levels( logs))
//the main goal of the code is to run loop through each log and extract how many times it is showing the messages or logs like full,started,timeout and low memory
//then after running the entire loop it prints the count of log occured.
