from io import StringIO
import csv

__author__ = 'Hernan Y.Ke'

s = StringIO()

s.write('Time')
c = csv.writer(s)
c.writerow(['a', 'b'])

print(s.getvalue())
