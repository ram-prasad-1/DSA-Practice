# 02. logging — module loggers for libraries, basicConfig for the entry point
# Run: python 02_logging.py



import logging



# basicConfig configures the ROOT logger; call it once, early, in the app only
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(levelname)s - %(message)s",
)
logging.warning("Attention! This is a warning.")
logging.info("info is visible because level=INFO")
logging.debug("debug is still silent")



# the default level is WARNING, so info/debug are silent until you lower it
print(logging.getLogger().level, logging.WARNING)



# force=True (3.8+) replaces existing handlers — useful in notebooks/REPLs
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s", force=True)
logging.debug("now debug shows")



# preferred: a module logger named after the module path
logger = logging.getLogger(__name__)
logger.warning("something looks off")
print(logger.name, logger.parent.name)



# an explicit handler + formatter on your own logger
custom = logging.getLogger("custom.child")
custom.propagate = False
handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
handler.setFormatter(logging.Formatter("%(name)s - %(levelname)s - %(message)s"))
custom.addHandler(handler)
custom.info("dropped by the handler level")
custom.warning("passes the handler level")



# libraries: just getLogger(__name__) and log — never touch handlers or levels
def library_function():
    logging.getLogger(__name__).info("library work done")


library_function()



# lazy %-style arguments: the format only runs if the record is emitted
logger.info("processed %d items from %s", 42, "queue")



# logging exceptions: .exception() is .error(..., exc_info=True)
try:
    1 / 0
except Exception:
    logger.exception("Exception occurred")



# filters give record-level control beyond levels
class OnlyWarnings(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.WARNING


custom.addFilter(OnlyWarnings())
custom.error("filtered out")
custom.warning("allowed through")



# extra= adds context fields a custom format can use
ctx = logging.getLogger("ctx")
ctx.propagate = False
h = logging.StreamHandler()
h.setFormatter(logging.Formatter("%(levelname)s [%(request_id)s] %(message)s"))
ctx.addHandler(h)
ctx.warning("handled request", extra={"request_id": "abc123"})



# Practice
# Q1. Add a RotatingFileHandler that keeps 3 backups of 1 KB each.
# Q2. Why should a library never call basicConfig?
# Q3. Compare logger.info("x %s", y) with logger.info(f"x {y}") — which one is lazy?
