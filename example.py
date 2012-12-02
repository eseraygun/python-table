# coding=utf-8

from table import Table

table = Table(["1", "2", "3"], ["a", "b"], [[1, 2], [3, 4], [5, 6]])
print "Whole table:"
print table

print "Just a cell:"
print table["1", "a"]

print "A row:"
print table["2", :]

print "A column:"
print table[:, "b"]

print "A range:"
print table["2":, :]
