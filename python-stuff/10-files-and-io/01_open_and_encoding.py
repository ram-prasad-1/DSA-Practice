# 01. open() — modes, encoding and iterating a file
# Run: python 01_open_and_encoding.py



from pathlib import Path

scratch = Path(__file__).with_name("scratch.txt")



# always use `with` — it closes the file even if the block raises
with open(scratch, "w", encoding="utf-8") as f:
    f.write("first\n")
    f.writelines(["second\n", "third\n"])
print(scratch.exists())



# modes: r read (default), w truncate, a append, x create-or-fail, + read+write
with open(scratch, "a", encoding="utf-8") as f:
    f.write("fourth\n")

try:
    open(scratch, "x")
except FileExistsError as e:
    print("FileExistsError:", type(e).__name__)



# read the whole thing, or a list of lines, or one line
with open(scratch, encoding="utf-8") as f:
    print(repr(f.read()))
with open(scratch, encoding="utf-8") as f:
    print(f.readlines())
with open(scratch, encoding="utf-8") as f:
    print(repr(f.readline()), repr(f.readline()))



# iterate the file object for large files — it streams one line at a time
with open(scratch, encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(i, line.rstrip("\n"))



# a file object is a one-shot iterator; seek(0) rewinds it
with open(scratch, encoding="utf-8") as f:
    print(len(f.readlines()), len(f.readlines()))
    f.seek(0)
    print(len(f.readlines()), f.tell())



# ALWAYS pass encoding= for text: the default is platform-dependent
import locale

print(locale.getencoding(), open(scratch).encoding)
with open(scratch, "w", encoding="utf-8") as f:
    f.write("café ✓\n")
print(scratch.read_text(encoding="utf-8").strip())
try:
    scratch.read_text(encoding="ascii")
except UnicodeDecodeError as e:
    print("UnicodeDecodeError:", e.reason)
print(scratch.read_text(encoding="ascii", errors="replace").strip())



# binary mode gives bytes and takes no encoding
with open(scratch, "rb") as f:
    print(f.read())
with open(scratch, "wb") as f:
    f.write(b"raw bytes\n")
try:
    open(scratch, "wb", encoding="utf-8")
except ValueError as e:
    print("ValueError:", e)



# newline translation: universal newlines on read, os.linesep never appears
# unless you ask for it; newline="" is required for the csv module
with open(scratch, "w", encoding="utf-8", newline="\r\n") as f:
    f.write("crlf\n")
print(scratch.read_bytes())
with open(scratch, encoding="utf-8", newline="") as f:
    print(repr(f.read()))



# the one-liners: read_text / write_text / read_bytes (they open and close for you)
scratch.write_text("via pathlib\n", encoding="utf-8")
print(scratch.read_text(encoding="utf-8").strip())



# without `with`, closing depends on garbage collection — CPython usually gets
# away with it, but the file may stay open and buffered writes may be lost
f = open(scratch, encoding="utf-8")
print(f.closed, f.read().strip())
f.close()
print(f.closed)



scratch.unlink()
print("cleaned up:", not scratch.exists())



# Practice
# Q1. Copy a file line by line without ever holding it all in memory.
# Q2. Why does the csv module insist on newline="" ?
# Q3. What happens if you open a file "w" and the process crashes before close()?
