import re
from collections import Counter
from dataclasses import dataclass


@dataclass
class LogData:
    date: str
    time: str
    level: str
    info: str
    message: str


data_log_list = []

with open('logs.txt', 'rt') as f:
    for line in f:
        match = re.match(r"(\d{2}/\d{2}) (\d{2}:\d{2}:\d{2})\s+(\w+)\s*:(\.*\w+):\s+(.*)", line)
        if match:
            data = LogData(*match.groups())
            data_log_list.append(data)
level_set = {log.level for log in data_log_list}
print(level_set)
date_counter = Counter(data.date for data in data_log_list)
print(date_counter)
