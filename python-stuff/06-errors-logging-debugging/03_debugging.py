# 03. Debugging — breakpoint(), post-mortem pdb, python -i
# Run: python 03_debugging.py



# the modern breakpoint (3.7+): no import needed
# uncomment to drop into pdb here
# breakpoint()



# it honors PYTHONBREAKPOINT:
#   PYTHONBREAKPOINT=0 python 03_debugging.py        -> all breakpoints disabled
#   PYTHONBREAKPOINT=ipdb.set_trace python ...       -> use ipdb instead
import os
import sys

print("PYTHONBREAKPOINT =", os.environ.get("PYTHONBREAKPOINT", "<unset>"))
print(sys.breakpointhook)



# import pdb; pdb.set_trace() is the legacy equivalent — prefer breakpoint()



# post-mortem: inspect the stack at the point of failure
import pdb


def risky():
    data = {"a": 1}
    return data["b"]


try:
    risky()
except Exception as e:
    print(f"{type(e).__name__}: {e}")
    # pdb.post_mortem()   # uncomment to poke at the failed frame



# after an uncaught exception in the REPL: import pdb; pdb.pm()
# or run the whole script under the debugger: python -m pdb script.py



# inspecting a traceback without a debugger
import traceback

try:
    risky()
except Exception as e:
    tb = e.__traceback__
    while tb:
        frame = tb.tb_frame
        print(frame.f_code.co_name, "line", tb.tb_lineno, "locals:", list(frame.f_locals))
        tb = tb.tb_next
    print(traceback.format_exception_only(e)[0].strip())



# essential pdb commands
#   n  step over          s  step into        c  continue      q  quit
#   l  list source        w  where (stack)    u / d  move up / down the stack
#   p expr  print         pp expr  pretty-print
#   b file:line  set a breakpoint             cl  clear breakpoints
#   interact  open a REPL in the current frame



# drop into a REPL with the script's globals when it finishes (or crashes):
#   python -i 03_debugging.py



# Practice
# Q1. Run this file with PYTHONBREAKPOINT=0 after uncommenting the breakpoint().
# Q2. Uncomment pdb.post_mortem() and inspect `data` in the failed frame.
# Q3. Use `python -m pdb` on a script that raises, and find the offending line with `w`.
