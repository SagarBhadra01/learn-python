import os

# ---------- Basic OS Information ----------
print(os.name)                    # OS name: 'nt' (Windows), 'posix' (Linux/Mac)
print(os.sep)                     # OS path separator
print(os.linesep)                 # Line separator
print(os.getpid())                # Current process ID

# ---------- Current Working Directory ----------
print(os.getcwd())                # Get current working directory
# os.chdir("C:/")                 # Change working directory

# ---------- Directory Listing ----------
print(os.listdir())               # List files & folders in current directory

# ---------- Path Operations ----------
path = "example.txt"

print(os.path.abspath(path))      # Absolute path
print(os.path.exists(path))       # Check existence
print(os.path.isfile(path))       # Check if file
print(os.path.isdir("."))         # Check if directory
print(os.path.basename(path))     # File name
print(os.path.dirname(os.path.abspath(path)))  # Directory name
print(os.path.splitext(path))     # Split name & extension
print(os.path.join("folder", "file.txt"))  # Join paths safely

# ---------- Directory Creation ----------
# os.mkdir("demo")                # Create single directory
# os.makedirs("a/b/c")            # Create nested directories

# ---------- Directory Removal ----------
# os.rmdir("demo")                # Remove empty directory
# os.removedirs("a/b/c")          # Remove nested empty directories

# ---------- File Operations ----------
# os.rename("old.txt", "new.txt") # Rename file
# os.remove("new.txt")            # Delete file

# ---------- Environment Variables ----------
# print(os.environ)                 # All environment variables
# print(os.environ.get("PATH"))     # Get specific variable
# os.environ["MY_VAR"] = "123"    # Set environment variable

# ---------- System Commands ----------
# os.system("dir")                # Windows command
# os.system("ls")                 # Linux / macOS command

# ---------- Walking Through Directories ----------
for root, dirs, files in os.walk("."):
    print(root)                   # Current directory path
    print(dirs)                   # Sub-directories
    print(files)                  # Files
    break                         # Stop after first level

# ---------- File Permissions ----------
# os.chmod("example.txt", 0o777)  # Change file permissions (Unix-based)

# ---------- Process Management ----------
# os.startfile("example.txt")     # Open file (Windows only)
# os.kill(os.getpid(), 9)         # Kill process (use carefully)

# ---------- Low-level File Descriptor ----------
# fd = os.open("example.txt", os.O_RDONLY)
# os.close(fd)
