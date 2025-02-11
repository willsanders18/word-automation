from docx import Document
from docx.shared import Pt
from docx.shared import Length
import os

document = Document()

style = document.styles['Normal']
font = style.font

font.name = 'Times New Roman'
font.size = Pt(12)

paragraph = document.add_paragraph()
paragraph_format = paragraph.paragraph_format
paragraph_format



