book-1.pdf: graph.py entities.py classes.py cast-1.csv book-1.csv
	python3 graph.py
	dot book-1.dot | gvcolor | dot -Tpdf -o book-1.pdf

test: classes.py  entities.py utils.py
	python3 classes.py
	python3 entities.py
	python3 utils.py
