# 02. pathlib — paths as objects instead of strings
# Run: python 02_pathlib_basics.py



from pathlib import Path, PurePosixPath



# build paths with / instead of os.path.join
here = Path(__file__).parent
target = here / "demo" / "notes.txt"
print(target)
print(type(target).__name__)



# the parts of a path
p = Path("/tmp/project/report.tar.gz")
print(p.name, p.stem, p.suffix, p.suffixes)
print(p.parent, p.parents[1], list(p.parts))
print(p.with_suffix(".zip"), p.with_name("summary.txt"), p.with_stem("final"))



# absolute vs relative, and resolving symlinks/..
rel = Path("a/../b/c.txt")
print(rel.is_absolute(), rel.as_posix())
print(Path("~/notes.txt").expanduser().is_absolute())
print(target.relative_to(here))



# querying the filesystem
print(here.exists(), here.is_dir(), (here / "nope").exists())
print(Path(__file__).stat().st_size > 0, Path(__file__).is_file())



# create, write, read, delete
demo = here / "demo"
demo.mkdir(exist_ok=True)
note = demo / "notes.txt"
note.write_text("line one\nline two\n", encoding="utf-8")
print(note.read_text(encoding="utf-8").splitlines())
print(sorted(pth.name for pth in demo.iterdir()))



# globbing: * within a directory, ** recursively
(demo / "sub").mkdir(exist_ok=True)
(demo / "sub" / "deep.txt").write_text("deep\n", encoding="utf-8")
print(sorted(str(x.relative_to(demo)) for x in demo.glob("*.txt")))
print(sorted(str(x.relative_to(demo)) for x in demo.rglob("*.txt")))
print(sorted(str(x.relative_to(demo)) for x in demo.glob("**/*") if x.is_file()))



# open() on a Path, and the read/write shortcuts
with note.open(encoding="utf-8") as f:
    print(f.readline().strip())
note.write_bytes(b"bytes\n")
print(note.read_bytes())



# rename, replace and unlink
renamed = note.with_name("renamed.txt")
note.rename(renamed)
print(renamed.exists(), note.exists())
renamed.unlink(missing_ok=True)
renamed.unlink(missing_ok=True)



# pure paths do string-ish work without touching the filesystem
pure = PurePosixPath("/var/log/app.log")
print(pure.parent, pure.match("*.log"), pure.is_relative_to("/var"))



# os.path equivalents, for reading older code
import os.path

print(os.path.join("a", "b") == str(Path("a") / "b"))
print(os.path.basename("/x/y.txt"), Path("/x/y.txt").name)
print(os.path.splitext("y.tar.gz")[1], Path("y.tar.gz").suffix)



# most stdlib functions accept a Path directly (os.fspath / __fspath__)
print(os.fspath(here) == str(here))



# clean up
import shutil

shutil.rmtree(demo)
print("cleaned up:", not demo.exists())



# Practice
# Q1. List every .py file under python-stuff, sorted by size.
# Q2. Why prefer Path.replace() over Path.rename() when the target may exist?
# Q3. Rewrite `os.path.join(os.path.dirname(__file__), "data", "x.json")` with pathlib.
