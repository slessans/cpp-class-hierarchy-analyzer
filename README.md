cpp-class-hierarchy-analyzer
============================

A very simple (and, for now, pretty specific) class hierarchy analyzer. 

Just run it and see. Analyzes .h files in working directory only. Finds class declarations by scanning 
files line by line, and only grabs classes that have super classes. So declaration must be all on one line
and essentially follow the regex (note that in real regex each space below is replaced by \s* or \s+ so 
whitespace is much more flexible)
	
	class ([a-zA-Z0-9_])+ : public ([a-zA-Z0-9_])+ ({ }?)?

Once parsing all classes, prints out class hierarchy tree, root classes, alphabetical leaf classes by root.

Above obviously imposes some limitations such as single inheritence, etc. but built this to help me with a 
specific task in a specific project. Maybe ill revisit this and generalize later, but for now I have a 
project to do ;)

