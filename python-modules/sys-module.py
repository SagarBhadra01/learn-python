import sys

# ---------- Python Interpreter Information ----------
print(sys.version)            # Python version (detailed)
print(sys.version_info)       # Python version tuple
print(sys.executable)         # Path of Python interpreter
print(sys.platform)           # Operating system platform

# ---------- Command-Line Arguments ----------
print(sys.argv)               # List of command-line arguments
# sys.argv[0] -> script name

# ---------- Module Search Path ----------
print(sys.path)               # Directories Python searches for modules

# ---------- Program Exit ----------
# sys.exit()                  # Exit program normally
# sys.exit("Exit message")    # Exit with message

# ---------- Standard Input / Output / Error ----------
sys.stdout.write("Hello from stdout\n")   # Write to standard output
# sys.stderr.write("Error message\n")     # Write to error stream

# ---------- Memory Information ----------
x = [1, 2, 3, 4, 5]
print(sys.getsizeof(x))       # Memory size of object in bytes

# ---------- Recursion Limit ----------
print(sys.getrecursionlimit())  # Current recursion limit
# sys.setrecursionlimit(2000)   # Set recursion limit (use carefully)

# ---------- Loaded Modules ----------
print(sys.modules)            # Dictionary of loaded modules

# ---------- Byte Order ----------
print(sys.byteorder)          # Endianness: 'little' or 'big'

# ---------- Maximum Integer Size ----------
print(sys.maxsize)            # Maximum size of integers

# ---------- Implementation Info ----------
print(sys.implementation)     # Python implementation details

# ---------- Hash Randomization ----------
print(sys.hash_info)          # Hash algorithm details

# ---------- Exception Information ----------
try:
    1 / 0
except:
    print(sys.exc_info())     # Exception type, value, traceback

# ---------- Flush Output ----------
sys.stdout.flush()             # Flush output buffer
