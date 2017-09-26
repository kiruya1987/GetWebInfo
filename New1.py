class a(object):
    pass

s=a()
s.name = 'SS'
s.type = int

try:
    print s.type('111')

except:
    print s.name,s.type

finally:
    print "END"