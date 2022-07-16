all:  graph.py entities.py cast-1.csv book-1.csv cast-2.csv book-2.csv cast-3.csv book-3.csv cast-4.csv book-4.csv
	python graph.py

clean:
	rm -f *.dot  *.pdf *.plain

test: classes.py  entities.py utils.py
	python classes.py
	python entities.py
	python utils.py
