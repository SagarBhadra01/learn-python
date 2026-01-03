# ================== TIME-RELATED MODULES : ALL IN ONE ==================

# ---------- time (low-level time handling) ----------
import time

print(time.time())          # Current timestamp (seconds since epoch)
print(time.ctime())         # Human-readable current time
print(time.localtime())     # Local time structure
print(time.gmtime())        # UTC time structure

time.sleep(1)               # Pause execution for 1 second

start = time.perf_counter() # High-resolution start time
for i in range(1000000):
    pass
end = time.perf_counter()
print(end - start)          # Execution time of loop


# ---------- datetime (high-level date & time) ----------
from datetime import datetime, date, time as dtime, timedelta

now = datetime.now()
print(now)                  # Current date & time

today = date.today()
print(today)                # Current date

custom_time = dtime(10, 30, 0)
print(custom_time)          # Custom time object

future = now + timedelta(days=5)
print(future)               # Date after 5 days

print(now.strftime("%d-%m-%Y %H:%M:%S"))  # Formatting date-time
parsed = datetime.strptime("01-01-2026", "%d-%m-%Y")
print(parsed)               # String to datetime


# ---------- calendar (calendar calculations) ----------
import calendar

print(calendar.month(2026, 1))       # Calendar of January 2026
print(calendar.isleap(2024))         # Leap year check
print(calendar.weekday(2026, 1, 1))  # Day of week (0=Monday)


# ---------- timeit (performance benchmarking) ----------
import timeit

execution_time = timeit.timeit("sum(range(100))", number=10000)
print(execution_time)       # Time taken to execute code multiple times


# ---------- sched (task scheduling) ----------
import sched

scheduler = sched.scheduler(time.time, time.sleep)

def scheduled_task():
    print("Scheduled task executed")

scheduler.enter(2, 1, scheduled_task)  # Execute after 2 seconds
scheduler.run()


# ---------- zoneinfo (timezone handling, Python 3.9+) ----------
from zoneinfo import ZoneInfo

india_time = datetime.now(ZoneInfo("Asia/Kolkata"))
utc_time = datetime.now(ZoneInfo("UTC"))

print(india_time)           # India timezone
print(utc_time)             # UTC timezone
