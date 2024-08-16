import camelot
import ghostscript
tables = camelot.read_pdf('INVOICE001.pdf', flavor='stream')
print(tables)
'''
tables.export('foo.csv', f='csv', compress=True) # json, excel, html
tables[0]
tables[0].to_csv('foo.csv') # to_json, to_excel, to_html
tables[0].df # get a pandas DataFrame!
'''
