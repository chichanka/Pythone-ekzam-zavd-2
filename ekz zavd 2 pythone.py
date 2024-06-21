from abc import ABC, abstractmethod

# Абстрактний клас Document
class Document(ABC):
    @abstractmethod
    def print(self):
        pass

    def prepare_for_printing(self):
        self.generate_content()
        self.format_content()

    @abstractmethod
    def generate_content(self):
        pass

    @abstractmethod
    def format_content(self):
        pass

# Клас PDFDocument, який наслідується від Document і реалізує метод print()
class PDFDocument(Document):
    def print(self):
        print("Printing PDF document...")

    def generate_content(self):
        print("Generating PDF content...")

    def format_content(self):
        print("Formatting PDF content...")

# Клас WordDocument, який наслідується від Document і реалізує метод print()
class WordDocument(Document):
    def print(self):
        print("Printing Word document...")

    def generate_content(self):
        print("Generating Word content...")

    def format_content(self):
        print("Formatting Word content...")

# Клас ExcelDocument, який наслідується від Document і реалізує метод print()
class ExcelDocument(Document):
    def print(self):
        print("Printing Excel document...")

    def generate_content(self):
        print("Generating Excel content...")

    def format_content(self):
        print("Formatting Excel content...")

# Фабричний метод у класі DocumentFactory, який створює об'єкти класів PDFDocument, WordDocument, та ExcelDocument
class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        if doc_type == "pdf":
            return PDFDocument()
        elif doc_type == "word":
            return WordDocument()
        elif doc_type == "excel":
            return ExcelDocument()
        else:
            raise ValueError("Invalid document type")

# Приклад використання
factory = DocumentFactory()
pdf_document = factory.create_document("pdf")
word_document = factory.create_document("word")
excel_document = factory.create_document("excel")

pdf_document.prepare_for_printing()
pdf_document.print()

word_document.prepare_for_printing()
word_document.print()

excel_document.prepare_for_printing()
excel_document.print()
