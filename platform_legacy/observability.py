# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
Structured logging and observability for the BioKernel platform.

Uses ``structlog`` for machine-readable JSON logs with human-friendly
console output during development.
"""

from __future__ import annotations

import logging
import sys
from typing import Any

try:
    import structlog
    HAS_STRUCTLOG = True
except ImportError:
    HAS_STRUCTLOG = False


def configure_logging(
    level: str = "INFO",
    json_output: bool = False,
    log_file: str | None = None,
) -> Any:
    """
    Configure structured logging for the BioKernel.

    Args:
        level: Log level string (DEBUG, INFO, WARNING, ERROR).
        json_output: If True, emit machine-readable JSON lines.
        log_file: Optional file path for log output.

    Returns:
        A configured logger instance.
    """
    log_level = getattr(logging, level.upper(), logging.INFO)

    if HAS_STRUCTLOG:
        processors = [
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
        ]

        if json_output:
            processors.append(structlog.processors.JSONRenderer())
        else:
            processors.append(structlog.dev.ConsoleRenderer(colors=sys.stderr.isatty()))

        structlog.configure(
            processors=processors,
            wrapper_class=structlog.make_filtering_bound_logger(log_level),
            context_class=dict,
            logger_factory=structlog.PrintLoggerFactory(file=sys.stderr),
            cache_logger_on_first_use=True,
        )
        return structlog.get_logger("biokernel")

    # Fallback to stdlib logging
    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(log_level)
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s %(name)s: %(message)s")
    handler.setFormatter(formatter)

    logger = logging.getLogger("biokernel")
    logger.setLevel(log_level)
    logger.handlers.clear()
    logger.addHandler(handler)

    if log_file:
        fh = logging.FileHandler(log_file)
        fh.setLevel(log_level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger


def get_logger(name: str = "biokernel") -> Any:
    """Get a logger bound to the given name."""
    if HAS_STRUCTLOG:
        return structlog.get_logger(name)
    return logging.getLogger(name)
