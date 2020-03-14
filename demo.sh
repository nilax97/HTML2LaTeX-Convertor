cd src
bash run.sh ../examples/sample1.html ../examples/sample1.tex
cd ../examples/
pdflatex -interaction=nonstopmode sample1.tex
rm sample1.aux sample1.log sample1.out
cd ..