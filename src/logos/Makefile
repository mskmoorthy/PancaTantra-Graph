all: panchalogo.png panchalogo.pdf

%.png:%.gv
	dot -Tpng $< -o  $@

%.pdf:%.gv
	dot -Tpdf $< -o  $@
