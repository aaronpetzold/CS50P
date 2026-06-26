# === Python Logging ===


# ========== TABLE OF CONTENTS ==========
#
# 1. IMPORT
# 2. LOG LEVELS
# 3. BASIC LOGGING TO CONSOLE (root logger)
# 4. FORMATTING LOG MESSAGES
# 5. LOGGING TO FILE
# 6. THE LOGGER HIERARCHY
# 7. CREATING AND USING NAMED LOGGERS
# 8. HANDLERS (StreamHandler, FileHandler, etc.)
# 9. FORMATTERS (detailed)
# 10. MULTIPLE HANDLERS AND FORMATTERS
# 11. ADVANCED CONFIGURATION (dictConfig / fileConfig)
# 12. ROTATING FILE HANDLERS (RotatingFileHandler, TimedRotatingFileHandler)
# 13. CAPTURING EXCEPTIONS (exc_info, exception())
# 14. FILTERS (adding logic to log records)
# 15. DISABLING LOGGING
# 16. LOGGING FROM MULTIPLE MODULES (using __name__)
# 17. COMMON PATTERNS
# 18. QUICK REFERENCE
#
# ========================================


# Definition: The `logging` module provides a flexible framework for emitting log messages
# from Python programs. It is part of the standard library.


# ---------- 1. IMPORT ----------

import logging


# ---------- 2. LOG LEVELS ----------

# Numeric values in increasing severity:
#   DEBUG       = 10
#   INFO        = 20
#   WARNING     = 30   (default level for basicConfig if not specified)
#   ERROR       = 40
#   CRITICAL    = 50

# You can also define custom levels with logging.addLevelName() if needed.


# ---------- 3. BASIC LOGGING TO CONSOLE (root logger) ----------

# Definition: `basicConfig()` does a one‑time configuration of the root logger.
# Without it, only WARNING and above will be printed to stderr.

logging.basicConfig(level=logging.INFO)

logging.debug("Debug message")        # won't be printed (level < INFO)
logging.info("Info message")          # printed
logging.warning("Warning message")    # printed
logging.error("Error message")        # printed
logging.critical("Critical message")  # printed

# Output format by default: `LEVEL:root:MESSAGE`
# Info message
# WARNING:root:Warning message
# ERROR:root:Error message
# CRITICAL:root:Critical message


# ---------- 4. FORMATTING LOG MESSAGES ----------

# Use the `format` parameter of basicConfig to control the output.

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logging.info("This is a formatted message")
# Output: 2025-12-25 10:15:30 - root - INFO - This is a formatted message

# Common format placeholders:
# %(asctime)s     – human‑readable time (customizable via datefmt)
# %(name)s        – logger name (root for the root logger)
# %(levelname)s   – text logging level ('DEBUG', 'INFO', ...)
# %(levelno)s     – numeric logging level (10, 20, ...)
# %(filename)s    – filename where the log call originated
# %(funcName)s    – function name where the log call originated
# %(lineno)d      – line number
# %(module)s      – module name
# %(message)s     – the log message
# %(process)d     – process ID
# %(thread)d      – thread ID


# ---------- 5. LOGGING TO FILE ----------

# Pass the `filename` argument to basicConfig.

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Application started")   # written to app.log, not console
logging.error("An error occurred")

# To log to both console and file, see Section 10 (Multiple handlers).


# ---------- 6. THE LOGGER HIERARCHY ----------

# Loggers are organized by name using dots as separators, like Python packages.
# The root logger is the parent of all loggers.
# Example:
#   logger = logging.getLogger('myapp')        # child of root
#   logger = logging.getLogger('myapp.module') # child of 'myapp'

# By default, log messages are propagated to parent loggers.
# You can disable propagation: logger.propagate = False


# ---------- 7. CREATING AND USING NAMED LOGGERS ----------

# Best practice: create a module‑level logger using __name__.

logger = logging.getLogger(__name__)   # e.g., 'mypackage.mymodule'
logger.setLevel(logging.DEBUG)         # set the threshold for this logger

# Without a handler, messages won't appear anywhere.
# Add a StreamHandler to see output on console.
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

logger.info("Hello from a named logger")   # displayed in console
logger.debug("Debug info")                 # not displayed (handler level = INFO)

# Use % formatting style as default. For {}- or $- style, see Formatter kwargs.


# ---------- 8. HANDLERS ----------

# Handlers send log records to destinations.
# Common handlers:
#   StreamHandler        – writes to streams (sys.stderr by default, or sys.stdout)
#   FileHandler          – writes to a file
#   NullHandler          – does nothing (used to avoid "No handlers could be found" warning)
#   RotatingFileHandler  – rolls over when file reaches a max size
#   TimedRotatingFileHandler – rotates at timed intervals
#   SocketHandler        – sends to a network socket
#   HTTPHandler           – sends to an HTTP server
#   SMTPHandler           – sends emails

# Example: FileHandler
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)   # now the named logger has two handlers


# ---------- 9. FORMATTERS (detailed) ----------

# Formatter class controls the layout of log records.

fmt = logging.Formatter(
    fmt='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%H:%M:%S',
    style='%'             # '%', '{' or '$' (default is '%')
)

# Using brace style with {}-formatting:
braces_formatter = logging.Formatter(
    fmt='{asctime} [{levelname}] {name}: {message}',
    style='{',
    datefmt='%H:%M:%S'
)

# Apply to a handler
handler.setFormatter(fmt)


# ---------- 10. MULTIPLE HANDLERS AND FORMATTERS ----------

# Add several handlers to a logger for different outputs.

logger = logging.getLogger('multi')
logger.setLevel(logging.DEBUG)

# Handler 1: Console (INFO and above)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))

# Handler 2: File (DEBUG and above)
file = logging.FileHandler('debug.log')
file.setLevel(logging.DEBUG)
file.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

logger.addHandler(console)
logger.addHandler(file)

logger.debug("Debug – only in file")
logger.info("Info – in console and file")
logger.error("Error – both")

# Each handler can have its own level and format.


# ---------- 11. ADVANCED CONFIGURATION (dictConfig / fileConfig) ----------

# Instead of programmatic setup, configuration can be loaded from a dictionary or file.

# Option A: dictConfig
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'detailed': {
            'format': '%(asctime)s [%(levelname)s] %(module)s %(lineno)d: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': 'app.log',
            'mode': 'a'
        }
    },
    'root': {                         # root logger configuration
        'level': 'DEBUG',
        'handlers': ['console', 'file']
    },
    'loggers': {
        'myapp': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('myapp')
logger.info("Configured via dictConfig")

# Option B: fileConfig (INI style)
# logging.config.fileConfig('logging.conf')


# ---------- 12. ROTATING FILE HANDLERS ----------

# RotatingFileHandler: roll over after file reaches a certain size.
from logging.handlers import RotatingFileHandler

rot_handler = RotatingFileHandler(
    'app.log', maxBytes=5*1024*1024, backupCount=3   # 5 MB, keep 3 backups
)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
rot_handler.setFormatter(formatter)
logger = logging.getLogger('rotating')
logger.setLevel(logging.DEBUG)
logger.addHandler(rot_handler)

# TimedRotatingFileHandler: roll over at specific time intervals.
from logging.handlers import TimedRotatingFileHandler

time_handler = TimedRotatingFileHandler(
    'app.log', when='midnight', interval=1, backupCount=7, encoding='utf-8'
)
time_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
time_handler.suffix = "%Y-%m-%d"   # optional suffix for rotated files
logger = logging.getLogger('timed')
logger.addHandler(time_handler)

# when can be: 'S' (seconds), 'M' (minutes), 'H' (hours), 'D' (days),
#              'W0'-'W6' (weekday), 'midnight'


# ---------- 13. CAPTURING EXCEPTIONS ----------

# Use exc_info=True or logging.exception() to include traceback.

try:
    1 / 0
except ZeroDivisionError:
    # Option 1
    logging.error("Division by zero", exc_info=True)
    # Option 2 (same as error(..., exc_info=True) – level ERROR)
    logging.exception("Division by zero")

# Output includes the full traceback after the message.
# ERROR:root:Division by zero
# Traceback (most recent call last):
#   ...
# ZeroDivisionError: division by zero

# To log exception at a custom level:
try:
    open('nonexistent.txt')
except FileNotFoundError:
    logging.log(logging.ERROR, "File not found", exc_info=True)


# ---------- 14. FILTERS ----------

# Filters allow you to apply additional logic to decide which records are emitted.

class NoPasswordFilter(logging.Filter):
    def filter(self, record):
        # Drop log records containing 'password'
        return 'password' not in record.getMessage()

logger = logging.getLogger('secure')
logger.addFilter(NoPasswordFilter())

# Or add a filter to a specific handler:
handler = logging.StreamHandler()
handler.addFilter(lambda record: record.levelno <= logging.WARNING)
logger.addHandler(handler)

# Built‑in Filter class can filter by logger name hierarchy:
logger.addFilter(logging.Filter('myapp.module'))  # only records from myapp.module and below


# ---------- 15. DISABLING LOGGING ----------

# Temporarily suppress all logging calls of a certain severity and below.
logging.disable(logging.WARNING)   # silences DEBUG, INFO, WARNING

# Re‑enable:
logging.disable(logging.NOTSET)

# To disable logging completely:
logging.shutdown()   # flushes and closes all handlers


# ---------- 16. LOGGING FROM MULTIPLE MODULES ----------

# In each module, get a logger using __name__.
# The hierarchy matches the package structure automatically.

# file: myapp/__init__.py
import logging
logger = logging.getLogger(__name__)   # 'myapp'

# file: myapp/core.py
import logging
logger = logging.getLogger(__name__)   # 'myapp.core'

# In your main application, configure logging once (e.g., via basicConfig or dictConfig).
# The module loggers will inherit handlers from the root logger (or their parents).


# ---------- 17. COMMON PATTERNS ----------

# 1. Simple standalone script logging to console + file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('script.log'),
        logging.StreamHandler()
    ]
)

# 2. Capture warnings from the warnings module
logging.captureWarnings(True)

# 3. Log to JSON (using python-json-logger or custom formatter)
# import json_log_formatter   # not in standard library
# formatter = json_log_formatter.JSONFormatter()

# 4. Temporarily increase log level for a noisy library
logging.getLogger('urllib3').setLevel(logging.WARNING)

# 5. Log unhandled exceptions at the top level
import sys
def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
sys.excepthook = handle_exception


# ---------- 18. QUICK REFERENCE ----------

# | Action                               | Code                                                                   |
# |--------------------------------------|------------------------------------------------------------------------|
# | Import logging module                | `import logging`                                                       |
# | Basic console output (root)          | `logging.warning('message')`                                           |
# | Basic config with level              | `logging.basicConfig(level=logging.INFO)`                              |
# | Basic config with format             | `logging.basicConfig(format='%(asctime)s - %(message)s', level=...)`   |
# | Log to file only                     | `logging.basicConfig(filename='app.log', level=logging.DEBUG)`          |
# | Log to file and console              | Use `handlers=` argument in basicConfig                                |
# | Named logger                         | `logger = logging.getLogger(__name__)`                                 |
# | Add a StreamHandler                  | `logger.addHandler(logging.StreamHandler())`                           |
# | Add a FileHandler                    | `logger.addHandler(logging.FileHandler('file.log'))`                   |
# | Set handler level                    | `handler.setLevel(logging.WARNING)`                                    |
# | Custom format                        | `logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')`       |
# | dictConfig                           | `logging.config.dictConfig(config_dict)`                               |
# | RotatingFileHandler (size)           | `RotatingFileHandler('app.log', maxBytes=1024, backupCount=3)`         |
# | TimedRotatingFileHandler (time)      | `TimedRotatingFileHandler('app.log', when='midnight', backupCount=7)`  |
# | Log exception with traceback         | `logging.exception("message")` or `logging.error("msg", exc_info=True)`|
# | Add a filter                         | `logger.addFilter(my_filter)`                                          |
# | Disable logging temporarily          | `logging.disable(logging.WARNING)`                                     |
# | Log from multiple modules            | Use `logger = logging.getLogger(__name__)` in every module              |