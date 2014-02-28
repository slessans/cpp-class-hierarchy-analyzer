#!/usr/bin/env python

import glob
import os
import re

pattern = re.compile("^\s*class\s*(\w+)\s*:\s*public\s*(\w+)\s*")

hierarchy = {}
subclasses = set()
all_classes = set()

os.chdir(".")
for file_name in glob.glob("*.h"):

	print "Analyzing " + file_name
	
	for i, line in enumerate(open(file_name)):
	
		for match in re.finditer(pattern, line):
			class_name = match.groups()[0]
			super_class_name = match.groups()[1]			
			print '\tLine %s: %s --> %s' % (i+1, super_class_name, class_name)

			if super_class_name not in hierarchy:
				hierarchy[super_class_name] = [];

			hierarchy[super_class_name].append(class_name)
			subclasses.add(class_name)
			all_classes.add(class_name)
			all_classes.add(super_class_name)

print "Finished analyzing header files. Hierarchies:\n"

root_classes = all_classes - subclasses

def get_indent_str(level):
	if level <= 0:
		return ""
	else:
		return ("--"*level) + "> "

def print_class_info (class_name, level=0):

	indent = get_indent_str(level)

	if class_name in hierarchy:
		print indent + class_name + ":"
		for subclass in hierarchy[class_name]:
			print_class_info(subclass, level + 1)
	else:
		print indent + class_name

def traverse_leaves(node_name, visitor):
	if node_name in hierarchy:
		for child_node in hierarchy[node_name]:
			traverse_leaves(child_node, visitor)
	else:
		# this is a leaf
		visitor(node_name)



for root_class in root_classes:
	print_class_info(root_class)
	print "-" * 10
	print ""

print "Root Classes:"
for root_class in root_classes:
	print " - " + root_class

def print_leaf_node(node_name):
	print " - " + node_name;

print "Leaf classes (organized by root):\n"
for root_class in root_classes:
	print "Leaf classes of " + root_class
	traverse_leaves(root_class, lambda node_name: print_leaf_node(node_name));

