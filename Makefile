report.pdf: temp/radiative_forcing.png
	latexmk -pdf

temp/radiative_forcing.png: radiative_forcing.py temp/rcps.tsv utils.py
	python $<

temp/rcps.tsv: apply_magicc_model.py utils.py
	python $<

.PHONY: clean deapclean

clean:
	rm -rf temp/
	latexmk -c

deapclean:
	rm -rf temp/
	latexmk -C