#!/usr/bin/python
# Automation Scripting Essential Skills 
# Python

# Interpolation 

x='foo'
y='bar'
z='baz'
names={'one' : 'Smith', 'two' : 'Jones', 'three' : 'Brown'}

# Technique1 
print 'Using interpolation operator...' 
print 'x=%s' % x
print 'y=%s' % y
print 'z=%s' % z
print 'x=%s, y=%s, z=%s' % (x,y,z)

# Technique2 
print 'Using str.format method...' 
print 'x={0}'.format(x)
print 'y={0}'.format(x)
print 'z={0}'.format(x)
print 'x={}, y={}, z={}'.format(x,y,z)
print 'a={a}, b={b}, c={c}'.format(b='yo', a='ya', c='gak')
print 'Law firm of {one}, {two} and {three}'.format(**names)
