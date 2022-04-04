PROGS:=dot twopi circo patchwork osage neato
  
all: graph.py entities.py cast-1.csv book-1.csv
	python graph.py	
	$(foreach p,${PROGS},$p book-1.dot |gvcolor | $p -Tpdf -o $p-book-1.pdf;)

plain: graph.py entities.py cast-1.csv book-1.csv
	python graph.py	
	$(foreach p,${PROGS},$p book-1.dot |gvcolor | $p -Tplain -o $p-book-1.plain;)

clean:
	rm -f book-1.dot  *.pdf

test: classes.py  entities.py utils.py
	python classes.py
	python entities.py
	python utils.py
