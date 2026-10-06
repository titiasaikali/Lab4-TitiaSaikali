from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

source = Path(__file__).parent / 'docs' / 'Lab 4-Git.docx'
namespace = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
with zipfile.ZipFile(source) as archive:
    root = ET.fromstring(archive.read('word/document.xml'))
paragraphs = [''.join(node.text or '' for node in paragraph.findall('.//w:t', namespace)) for paragraph in root.findall('.//w:p', namespace)]
output = source.with_name('lab4_assignment.txt')
output.write_text('\n'.join(paragraphs), encoding='utf-8')
print(f'Assignment text saved to {output}')
