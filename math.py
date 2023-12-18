
import os
import datetime
current_dir = os.getcwd()
current_time = datetime.datetime.now()
def is_recent(file):
    file_path = os.path.join(current_dir, file)
    file_stats = os.stat(file_path)
    file_mtime = datetime.datetime.fromtimestamp(file_stats.st_mtime)
    file_ctime = datetime.datetime.fromtimestamp(file_stats.st_ctime)
    return (current_time - file_mtime).total_seconds() <= 86400 or (current_time - file_ctime).total_seconds() <= 86400
recent_files = []
for file in os.listdir(current_dir):
    if os.path.isfile(file):
        if is_recent(file):
            recent_files.append(file)
print("Recent files:")
for file in recent_files:
    print(file)
os.mkdir("last_24hours")
for file in recent_files:
    with open(file, "a") as f:
        f.write
    os.rename(file, os.path.join("last_24hours", file))