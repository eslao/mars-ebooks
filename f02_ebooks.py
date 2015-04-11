# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import requests
import re

# <codecell>

loadedbibs = []

# <codecell>

loadlogurl = 'http://lms01.harvard.edu/ebooks/staffebkpinutf/stf_pinutf_harma20141001.zero.m18.doc_log'
transactionlogurl = 'http://lms01.harvard.edu/mars-reports/transactions/marstrans.oct-14.f02'

# <codecell>

loadlog = requests.get(loadlogurl).text

# <codecell>

#for bib in loadlog[0:104].split('\n'):
for bib in loadlog.split('\n'):
    #print bib[0:9]
    loadedbibs += [bib[0:9]]

# <codecell>

print str(len(loadedbibs)) + ' bib records from ebook loads'

# <codecell>

transactionlog = requests.get(transactionlogurl).text

# <codecell>

#for bib in loadedbibs:
#    if bib in transactionlog:
#        print bib

# <codecell>

#sample = re.split(r'[0-9]{9}\sLDR', transactionlog[0:600])
#sample = re.findall('.*?FMT\s{3}L\s[A-Z]{2}\n', transactionlog[0:600], re.DOTALL)
#print sample

# <codecell>

transactions = re.findall('.*?FMT\s{3}L\s[A-Z]{2}\n', transactionlog, re.DOTALL)

# <codecell>

print str(len(transactions)) + ' records changed by MARS'

# <codecell>

ebooktransactions = []
smallerf02 = open('marstrans.oct-14.ebooks.f02', 'w')

# <codecell>

for record in transactions[1:]:
    lines = record.split('\n')
    bibno = lines[1][-9:]
    if bibno in loadedbibs:
        for line in lines[1:]:
            ebooktransactions += [line]
    #        print line
    #else:
    #    print bibno + ' was not changed'
    
#print lines
#print lines[1]
#print lines[1][-9:]
#print bibno

# <codecell>

#print str(len(ebooktransactions)) + ' ebook records changed by MARS' #this gets the number of lines, not a meaningful number of changes

# <codecell>

# counts number of 'before' headings; does not account for splits that result in two headings being added in place of one incorrect heading
headingschanged = 0
for line in ebooktransactions:
    if '$$9MAT' in line:
        headingschanged += 1
print str(headingschanged) + ' headings changed by MARS' 

# <codecell>

#foo = u'Δ, Й, ק, ‎ م, ๗, あ, 叶, 葉, and 말.'
#f = open('test', 'w')
smallerf02.write('\n'.join(ebooktransactions).encode('utf8'))
smallerf02.close()

#When you read that file again, you'll get a unicode-encoded string that you can decode to a unicode object:

#f = file(smallerf02, 'r')
#print f.read().decode('utf8')

# <codecell>


