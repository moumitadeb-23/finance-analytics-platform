"""
==========================================================
FINANCE ANALYTICS PLATFORM
FinanceAI v2.0
Utility Functions
==========================================================
"""

import os
import re
from datetime import datetime


class Utils:

    # ======================================================
    # FORMAT CURRENCY
    # ======================================================

    @staticmethod
    def format_currency(amount):

        try:

            return f"₹{float(amount):,.2f}"

        except:

            return "₹0.00"

    # ======================================================
    # FORMAT PERCENTAGE
    # ======================================================

    @staticmethod
    def format_percentage(value):

        try:

            return f"{float(value):.2f}%"

        except:

            return "0.00%"

    # ======================================================
    # SAFE FLOAT
    # ======================================================

    @staticmethod
    def safe_float(value):

        try:

            return float(value)

        except:

            return 0.0

    # ======================================================
    # CLEAN TEXT
    # ======================================================

    @staticmethod
    def clean_text(text):

        if text is None:

            return ""

        text = str(text)

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    # ======================================================
    # CURRENT DATE
    # ======================================================

    @staticmethod
    def current_date():

        return datetime.now().strftime(

            "%d-%m-%Y"

        )

    # ======================================================
    # CURRENT TIME
    # ======================================================

    @staticmethod
    def current_time():

        return datetime.now().strftime(

            "%H:%M:%S"

        )

    # ======================================================
    # CURRENT DATETIME
    # ======================================================

    @staticmethod
    def current_datetime():

        return datetime.now().strftime(

            "%d-%m-%Y %H:%M:%S"

        )

    # ======================================================
    # FILE EXTENSION
    # ======================================================

    @staticmethod
    def file_extension(path):

        return os.path.splitext(

            path

        )[1].lower()

    # ======================================================
    # FILE NAME
    # ======================================================

    @staticmethod
    def filename(path):

        return os.path.basename(path)

    # ======================================================
    # FILE SIZE
    # ======================================================

    @staticmethod
    def file_size(path):

        try:

            size = os.path.getsize(path)

            if size < 1024:

                return f"{size} B"

            elif size < 1024 * 1024:

                return f"{size/1024:.2f} KB"

            else:

                return f"{size/(1024*1024):.2f} MB"

        except:

            return "Unknown"

    # ======================================================
    # VALID FILE
    # ======================================================

    @staticmethod
    def file_exists(path):

        return os.path.exists(path)

    # ======================================================
    # KEYWORD EXTRACTION
    # ======================================================

    @staticmethod
    def extract_keywords(

            text,

            limit=10

    ):

        words = re.findall(

            r"[A-Za-z]{4,}",

            text.lower()

        )

        ignore = {

            "this",

            "that",

            "with",

            "from",

            "have",

            "your",

            "about",

            "there",

            "their",

            "would",

            "should"

        }

        frequency = {}

        for word in words:

            if word in ignore:

                continue

            frequency[word] = frequency.get(

                word,

                0

            ) + 1

        sorted_words = sorted(

            frequency.items(),

            key=lambda x: x[1],

            reverse=True

        )

        return [

            word

            for word, _

            in sorted_words[:limit]

        ]

    # ======================================================
    # RESPONSE
    # ======================================================

    @staticmethod
    def success(

            response,

            response_type="chat"

    ):

        return {

            "success": True,

            "type": response_type,

            "data": response

        }

    # ======================================================
    # ERROR
    # ======================================================

    @staticmethod
    def error(message):

        return {

            "success": False,

            "type": "error",

            "message": message

        }

    # ======================================================
    # CALCULATE PERCENTAGE
    # ======================================================

    @staticmethod
    def percentage(

            value,

            total

    ):

        try:

            if total == 0:

                return 0

            return round(

                (value / total) * 100,

                2

            )

        except:

            return 0

    # ======================================================
    # LIMIT TEXT
    # ======================================================

    @staticmethod
    def shorten(

            text,

            limit=200

    ):

        if len(text) <= limit:

            return text

        return text[:limit] + "..."

    # ======================================================
    # MARKDOWN FORMAT
    # ======================================================

    @staticmethod
    def markdown(text):

        if text is None:
            return ""

        text = str(text)

        return text.replace("\n", "\n\n")