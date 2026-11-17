log ='''
2026-11-16 10:00:01 FAIL user=admin ip=10.0.0.5
2026-11-16 10:00:10 FAIL user=admin ip=10.0.0.5
2026-11-16 10:00:15 FAIL user=root ip=10.0.0.9
2026-11-16 10:00:20 FAIL user=admin ip=10.0.0.5
2026-11-16 10:00:30 OK user=alice ip=10.0.0.7
2026-11-16 10:00:35 FAIL user=admin ip=10.0.0.5
2026-11-16 10:00:50 FAIL user=test ip=10.0.0.5
2026-11-16 10:01:30 FAIL user=root ip=10.0.0.9
2026-11-16 10:01:40 FAIL user=root ip=10.0.0.9
2026-11-16 10:01:45 FAIL user=root ip=10.0.0.9
2026-11-16 10:02:20 FAIL user=root ip=10.0.0.9
'''
from datetime import datetime

first = {}
last = {}
for line in log.strip().splitlines():
    parts = line.split()
    if parts[2] == 'FAIL':
        ip = parts[-1].split('=')[1]
        ts = datetime.strptime(parts[0] + ' ' + parts[1], '%Y-%m-%d %H:%M:%S')
        # YOUR PART (2–3 lines):
        # - if this ip is NOT in first yet → store ts in first[ip]
        # - always store ts in last[ip]  (it keeps getting overwritten, so it ends as the last one)
        if ip not in first:
            first[ip] = ts
        last[ip] = ts

for ip in first:
    seconds = (last[ip] - first[ip]).total_seconds()
    if seconds < 60:
        print(f"{ip} {log.count(ip)} {first[ip]}")


