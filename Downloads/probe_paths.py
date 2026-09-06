import os, sys, tempfile

print("CWD:", os.getcwd())
print("PYTHON EXE:", sys.executable)
print("TEMP:", tempfile.gettempdir())

# candidate writable locations
cands = [
    os.getcwd(),
    tempfile.gettempdir(),
    r"D:\\Documents\\项目\\RuwoScan\\Downloads",
    r"D:\\Documents\\项目\\RuwoScan\\Downloads\\report",
    r"D:\\Documents\\项目\\RuwoScan",
    ".",
]
for c in cands:
    try:
        ok = os.access(c, os.W_OK)
        exists = os.path.isdir(c)
        print(f"cand={c!r} exists={exists} writable={ok}")
    except Exception as e:
        print(f"cand={c!r} ERROR {e}")
