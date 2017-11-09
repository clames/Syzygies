#!/usr/bin/python
#!python

#import os
import Queue
#from IPython.core.debugger import Tracer
#import pdb
#filepath = os.path.dirname(os.path.abspath(__file__))

f = open('wordsEn.txt')
first = {}
last = {}

while True:
  word = f.readline()[:-2]
  if word == '':
    break
  if len(word) > 2:
    if word[:2] in first:
      first[word[:2]].append(word)
    else:
      first[word[:2]] = [word]
    if word[-2:] in last:
      last[word[-2:]].append(word)
    else:
      last[word[-2:]] = [word]
  
start = raw_input('Startword: '), ''
end = raw_input('Goalword: ')

if start[0] == end:
  print "Start = End"
else:
  front = Queue.Queue()
  front.put(start)
  frontset = set([start[0]])
  explored = {}
  
  found = False
  while not found:
    
    if front.empty() == True:
      print "No solution"
      break
    
    node = front.get()
    frontset.remove(node[0])
    explored[node[0]] = node[1]
    
    if node[0][-2:] in first.keys():
      for child in first[node[0][-2:]]:
	if child not in explored.keys() and child not in frontset:
	  if child[-2:] == end[:2] or child[:2] == end[-2:]:
	    chain = [end, child, node[0]]
	    if node[0] == start[0]:
	      found = True
	      break
	    parent = node[1]
	    while parent != start[0]:
	      chain.append(parent)
	      parent = explored[parent]
	    chain.append(start[0])
	    found = True
	    break
	  frontset.add(child)
	  child = child, node[0]
	  front.put(child)
    if node[0][:2] in last.keys() and not found:
      for child in last[node[0][:2]]:
	if child not in explored.keys() and child not in frontset:
	  if child[-2:] == end[:2] or child[:2] == end[-2:]:
	    chain = [end, child, node[0]]
	    if node[0] == start[0]:
	      found = True
	      break
	    parent = node[1]
	    while parent != start[0]:
	      chain.append(parent)
	      parent = explored[parent]
	    chain.append(start[0])
	    found = True
	    break
	  frontset.add(child)
	  child = child, node[0]
	  front.put(child)
    if found:
      break
    
print ''
print 'Found Chain:'
print ''
for i in reversed(chain):
    print i
print ''