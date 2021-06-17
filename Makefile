temp/radiative_forcing.png: radiative_forcing.py temp/rcps.tsv
	python $<

temp/rcps.tsv: apply_magicc_model.py
	python $<

.PHONY: clean
clean:
	rm -rf temp/