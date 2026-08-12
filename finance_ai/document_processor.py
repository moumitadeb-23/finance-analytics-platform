"""
==========================================================
FINANCE ANALYTICS PLATFORM
FinanceAI v2.0
Document Processor
==========================================================
"""

import os
import shutil
import pdfplumber
import pandas as pd
import easyocr

from PIL import Image

from .config import (
    UPLOAD_FOLDER,
    ALLOWED_EXTENSIONS,
    OCR_LANGUAGES,
    OCR_GPU
)

from .utils import Utils


class DocumentProcessor:

    # ======================================================
    # INITIALIZATION
    # ======================================================

    def __init__(self):

        self.upload_folder = UPLOAD_FOLDER

        self.allowed_extensions = ALLOWED_EXTENSIONS

        self.reader = easyocr.Reader(

            OCR_LANGUAGES,

            gpu=OCR_GPU

        )

        os.makedirs(

            self.upload_folder,

            exist_ok=True

        )

    # ======================================================
    # ALLOWED FILE
    # ======================================================

    def allowed_file(

            self,

            filename

    ):

        if "." not in filename:

            return False

        extension = filename.rsplit(

            ".",

            1

        )[1].lower()

        return extension in self.allowed_extensions

    # ======================================================
    # FILE EXTENSION
    # ======================================================

    def file_extension(

            self,

            filename

    ):

        return os.path.splitext(

            filename

        )[1].lower()

    # ======================================================
    # DOCUMENT TYPE
    # ======================================================

    def document_type(

            self,

            filename

    ):

        extension = self.file_extension(

            filename

        )

        mapping = {

            ".pdf": "PDF",

            ".csv": "CSV",

            ".xlsx": "Excel",

            ".xls": "Excel",

            ".png": "Image",

            ".jpg": "Image",

            ".jpeg": "Image"

        }

        return mapping.get(

            extension,

            "Unknown"

        )

    # ======================================================
    # SAVE DOCUMENT
    # ======================================================

    def save_document(
        self,
        uploaded_file
    ):

        if uploaded_file is None:
            return Utils.error("No file uploaded.")

        if uploaded_file.filename == "":
            return Utils.error("Filename is empty.")

        if not self.allowed_file(uploaded_file.filename):
            return Utils.error("Unsupported file type.")

        filename = uploaded_file.filename

        filepath = os.path.join(
            self.upload_folder,
            filename
        )

        uploaded_file.save(filepath)

        # ==========================================
        # Build AI-ready document
        # ==========================================

        ai_doc = self.ai_document(filepath)

        if not ai_doc["success"]:
            return ai_doc

        # Add filepath for future use
        ai_doc["data"]["filepath"] = filepath

        return ai_doc

    # ======================================================
    # FILE INFORMATION
    # ======================================================

    def file_information(

            self,

            filepath

    ):

        if not os.path.exists(

                filepath

        ):

            return Utils.error(

                "File not found."

            )

        return Utils.success(

            {

                "filename": Utils.filename(

                    filepath

                ),

                "type": self.document_type(

                    filepath

                ),

                "size": Utils.file_size(

                    filepath

                ),

                "path": filepath

            },

            "document"

        )

    # ======================================================
    # DELETE DOCUMENT
    # ======================================================

    def delete_document(

            self,

            filepath

    ):

        try:

            if os.path.exists(

                    filepath

            ):

                os.remove(

                    filepath

                )

                return Utils.success(

                    "Document deleted.",

                    "document"

                )

            return Utils.error(

                "Document not found."

            )

        except Exception as e:

            return Utils.error(

                str(e)

            )

            # ======================================================
    # PDF TEXT EXTRACTION
    # ======================================================

    def extract_pdf_text(self, filepath):

        text = ""

        try:

            with pdfplumber.open(filepath) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:

                        text += page_text + "\n"

        except Exception as e:

            return Utils.error(f"Unable to read PDF: {str(e)}")

        return Utils.success(

            {

                "type": "PDF",

                "text": text.strip()

            },

            "document"

        )


    # ======================================================
    # EXCEL EXTRACTION
    # ======================================================

    def extract_excel_text(self, filepath):

        try:

            excel = pd.ExcelFile(filepath)

            text = ""

            for sheet in excel.sheet_names:

                df = pd.read_excel(

                    filepath,

                    sheet_name=sheet

                )

                text += f"\n===== SHEET : {sheet} =====\n"

                text += df.to_string(index=False)

                text += "\n"

        except Exception as e:

            return Utils.error(f"Unable to read Excel file: {str(e)}")

        return Utils.success(

            {

                "type": "Excel",

                "text": text

            },

            "document"

        )


    # ======================================================
    # CSV EXTRACTION
    # ======================================================

    def extract_csv_text(self, filepath):

        try:

            df = pd.read_csv(filepath)

            text = df.to_string(index=False)

        except Exception as e:

            return Utils.error(f"Unable to read CSV file: {str(e)}")

        return Utils.success(

            {

                "type": "CSV",

                "text": text

            },

            "document"

        )


    # ======================================================
    # IMAGE OCR
    # ======================================================

    def extract_image_text(self, filepath):

        try:

            result = self.reader.readtext(

                filepath,

                detail=0,

                paragraph=True

            )

            text = "\n".join(result)

        except Exception as e:

            return Utils.error(f"Unable to read image: {str(e)}")

        return Utils.success(

            {

                "type": "Image",

                "text": text

            },

            "document"

        )


    # ======================================================
    # UNIVERSAL TEXT EXTRACTION
    # ======================================================

    def extract_text(self, filepath):

        extension = self.file_extension(filepath)

        if extension == ".pdf":

            return self.extract_pdf_text(filepath)

        elif extension in [".xlsx", ".xls"]:

            return self.extract_excel_text(filepath)

        elif extension == ".csv":

            return self.extract_csv_text(filepath)

        elif extension in [

            ".png",

            ".jpg",

            ".jpeg"

        ]:

            return self.extract_image_text(filepath)

        return Utils.error(

            "Unsupported document type."

        )

        # ======================================================
    # DOCUMENT STATISTICS
    # ======================================================

    def document_statistics(self, text):

        if not text:

            return {

                "characters": 0,

                "words": 0,

                "lines": 0

            }

        return {

            "characters": len(text),

            "words": len(text.split()),

            "lines": len(text.splitlines())

        }


    # ======================================================
    # EXTRACT KEYWORDS
    # ======================================================

    def extract_keywords(

            self,

            text,

            limit=15

    ):

        keywords = Utils.extract_keywords(

            text,

            limit

        )

        return keywords


    # ======================================================
    # EXTRACT NUMBERS
    # ======================================================

    def extract_numbers(self, text):

        import re

        numbers = re.findall(

            r"\d+(?:,\d{3})*(?:\.\d+)?",

            text

        )

        return numbers


    # ======================================================
    # EXTRACT CURRENCY VALUES
    # ======================================================

    def extract_currency(self, text):

        import re

        currency = re.findall(

            r"₹\s?\d+(?:,\d{3})*(?:\.\d+)?",

            text

        )

        return currency


    # ======================================================
    # DOCUMENT METADATA
    # ======================================================

    def document_metadata(

            self,

            filepath,

            text

    ):

        return {

            "filename": Utils.filename(

                filepath

            ),

            "type": self.document_type(

                filepath

            ),

            "size": Utils.file_size(

                filepath

            ),

            "statistics": self.document_statistics(

                text

            ),

            "keywords": self.extract_keywords(

                text

            ),

            "numbers": self.extract_numbers(

                text

            ),

            "currency": self.extract_currency(

                text

            )

        }


    # ======================================================
    # PROCESS DOCUMENT
    # ======================================================

    def process(
            self,
            user_id,
            question=None,
            document=None
    ):

        if document is None:
            return Utils.error("No document supplied.")

        # -----------------------------
        # If save_document() output
        # -----------------------------
        if isinstance(document, dict):

            if not document.get("success"):
                return document

            filepath = document["data"]["filepath"]

        else:
            filepath = document

        extraction = self.extract_text(filepath)

        if not extraction["success"]:
            return extraction

        text = extraction["data"]["text"]

        metadata = self.document_metadata(
            filepath,
            text
        )

        return Utils.success(
            {
                "question": question,
                "text": text,
                "metadata": metadata
            },
            "document"
        )

    

    # ======================================================
    # DOCUMENT SUMMARY
    # ======================================================

    def quick_summary(

            self,

            filepath

    ):

        result = self.extract_text(

            filepath

        )

        if not result["success"]:

            return result

        text = result["data"]["text"]

        words = text.split()

        summary = " ".join(

            words[:150]

        )

        return Utils.success(

            summary,

            "summary"

        )

        # ======================================================
    # EXTRACT DATES
    # ======================================================

    def extract_dates(self, text):

        import re

        patterns = [

            r"\d{2}/\d{2}/\d{4}",

            r"\d{2}-\d{2}-\d{4}",

            r"\d{4}-\d{2}-\d{2}"

        ]

        dates = []

        for pattern in patterns:

            dates.extend(

                re.findall(

                    pattern,

                    text

                )

            )

        return list(set(dates))


    # ======================================================
    # DETECT MERCHANT NAME
    # ======================================================

    def detect_merchant(self, text):

        lines = text.splitlines()

        for line in lines[:10]:

            line = line.strip()

            if len(line) > 4 and len(line) < 60:

                return line

        return "Unknown"


    # ======================================================
    # FINANCIAL INFORMATION
    # ======================================================

    def financial_information(self, text):

        numbers = self.extract_numbers(text)

        currency = self.extract_currency(text)

        dates = self.extract_dates(text)

        merchant = self.detect_merchant(text)

        return {

            "merchant": merchant,

            "dates": dates,

            "currency_values": currency,

            "numbers": numbers

        }


    # ======================================================
    # AI READY DOCUMENT
    # ======================================================

    def ai_document(

            self,

            filepath

    ):

        extraction = self.extract_text(

            filepath

        )

        if not extraction["success"]:

            return extraction

        text = extraction["data"]["text"]

        metadata = self.document_metadata(

            filepath,

            text

        )

        financial = self.financial_information(

            text

        )

        return Utils.success(

            {

                "filename": metadata["filename"],

                "type": metadata["type"],

                "size": metadata["size"],

                "text": text,

                "summary": self.quick_summary(

                    filepath

                )["data"],

                "keywords": metadata["keywords"],

                "statistics": metadata["statistics"],

                "financial": financial

            },

            "document"

        )


    # ======================================================
    # DOCUMENT STATUS
    # ======================================================

    def status(self):

        return Utils.success(

            {

                "upload_folder": self.upload_folder,

                "supported_formats": list(

                    self.allowed_extensions

                ),

                "ocr": "Enabled"

            },

            "status"

        )

    