import logging
import logging.config
import json


# -------------------------
# JSON FORMATTER (LOKI READY)
# -------------------------
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log = {
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "time": self.formatTime(record),
        }

        # safely include extra fields (NO CRASH EVER)
        for key in ["method", "path", "status_code", "duration_ms"]:
            if hasattr(record, key):
                log[key] = getattr(record, key)

        return json.dumps(log)


# -------------------------
# LOGGING CONFIG
# -------------------------
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "src.core.logging.JsonFormatter",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
}
