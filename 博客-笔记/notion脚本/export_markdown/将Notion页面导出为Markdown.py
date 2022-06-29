from notion2md.exporter.block import MarkdownExporter, StringExporter

# MarkdownExporter will make markdown file on your output path
MarkdownExporter(page_id='...',output_path='...',download=True).export()

# StringExporter will return output as String type
md = StringExporter(page_id='...',output_path='...').export()
