PROGS:=dot twopi circo patchwork osage
  
all: graph.py entities.py cast-1.csv book-1.csv
	python graph.py	
	$(foreach p,${PROGS},$p book-1.dot |gvcolor | $p -Tpdf -o $p-book-1.pdf;)

clean:
	rm -f book-1.dot book-1.pdf

test: classes.py  entities.py utils.py
	python classes.py
	python entities.py
	python utils.py
