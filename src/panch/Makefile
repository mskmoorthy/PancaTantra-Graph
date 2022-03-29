book-1.pdf: graph.py entities.py classes.py cast-1.csv book-1.csv
	python graph.py
	dot book-1.dot | gvcolor | dot -Tpdf -o book-1.pdf
clean:
	rm -f book-1.dot book-1.pdf

test: classes.py  entities.py utils.py
	python classes.py
	python entities.py
	python utils.py
