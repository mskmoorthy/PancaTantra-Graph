PROGS:=twopi  dot   #circo patchwork osage 
all: pdf plain

pdf: graph.py entities.py cast-1.csv book-1.csv
	python graph.py	
	$(foreach p,${PROGS},$p book-1a.dot |gvcolor | $p -Tpdf -o $p-book-1a.pdf;)
	$(foreach p,${PROGS},$p book-1b.dot |gvcolor | $p -Tpdf -o $p-book-1b.pdf;)

plain:
	python graph.py	
	$(foreach p,${PROGS},$p book-1a.dot |gvcolor | $p -Tplain -o $p-book-1a.plain;)
	$(foreach p,${PROGS},$p book-1b.dot |gvcolor | $p -Tplain -o $p-book-1b.plain;)
clean:
	rm -f book*.dot  *.pdf *.plain

test: classes.py  entities.py utils.py
	python classes.py
	python entities.py
	python utils.py
