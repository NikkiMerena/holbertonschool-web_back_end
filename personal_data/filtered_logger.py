#!/usr/bin/env python3
"""Module for filtering personal data in logs"""

import re
from typing import Sequence
import logging

# Defibe the fields which are considered as PII
PII_FIELDS = ("phone", "name", "password", "ssn", "email")


def get_logger() -> logging.Logger:
    """
    Returns a logger w/ the name "user_data" configured to log up to INFO level
    """

    # Create a logger object w/ the name 'user_data'
    logger = logging.getLogger('user_data')

    # Set the logging level to INFO for the logger
    logger.setLevel(logging.INFO)

    # Create a StreamHandler object
    handler = logging.StreamHandler()

    # Create a redactingFormatter object paramererized w/ PII_FIELDS
    formatter = RedactingFormatter(PII_FIELDS)

    # Set the formatter for the handler to the RedactingFormatter object
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    # Set the logger to not propagate messages to other loggers
    logger.propagate = False

    return logger


def filter_datum(fields: Sequence[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Returns the log message obfuscated.

    Arguments:
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating
    all fields in the log line (message)
    """
    for field in fields:
        message = re.sub(f'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class which redacts specified fileds in log records
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: Sequence[str]):
        """Initializes the formatter w/ fields to redact."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats the log record, redacting specified fields"""
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original_message, self.SEPARATOR)
