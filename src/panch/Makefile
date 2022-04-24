all:  graph.py entities.py cast-1.csv book-1.csv
	python graph.py

clean:
	rm -f book*.dot  *.pdf *.plain

test: classes.py  entities.py utils.py
	python classes.py
	python entities.py
	python utils.py
