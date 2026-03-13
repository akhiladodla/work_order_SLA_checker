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
