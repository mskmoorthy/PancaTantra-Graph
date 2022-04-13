PROGS:=twopi  dot   circo patchwork osage 
all: pdf plain

pdf: graph.py entities.py cast-1.csv book-1.csv
	python graph.py	
	$(foreach p,${PROGS},$p book-1.dot |gvcolor | $p -Tpdf -o $p-book-1.pdf;)

plain:
	python graph.py	
	$(foreach p,${PROGS},$p book-1.dot |gvcolor | $p -Tplain -o $p-book-1.plain;)

clean:
	rm -f book-1.dot  *.pdf *.plain

test: classes.py  entities.py utils.py
	python classes.py
	python entities.py
	python utils.py
