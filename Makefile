tmp_dir=temp
plt_emissions=plt_emissions.py
plt_emissions_dep=$(tmp_dir)/rcps.tsv

report.pdf: $(tmp_dir)/radiative_forcing.png $(tmp_dir)/RCP26_Emissions_CH4.png $(tmp_dir)/RCP45_Emissions_CH4.png $(tmp_dir)/RCP26_Emissions_CO2.png $(tmp_dir)/RCP45_Emissions_CO2.png
	latexmk -pdf

$(tmp_dir)/RCP26_Emissions_CH4.png: $(plt_emissions) $(plt_emissions_dep)
	python $< 'RCP26' 'Emissions|CH4' $@

$(tmp_dir)/RCP45_Emissions_CH4.png: $(plt_emissions) $(plt_emissions_dep)
	python $< 'RCP45' 'Emissions|CH4' $@

$(tmp_dir)/RCP26_Emissions_CO2.png: $(plt_emissions) $(plt_emissions_dep)
	python $< 'RCP26' 'Emissions|CO2|MAGICC Fossil and Industrial' $@

$(tmp_dir)/RCP45_Emissions_CO2.png: $(plt_emissions) $(plt_emissions_dep)
	python $< 'RCP45' 'Emissions|CO2|MAGICC Fossil and Industrial' $@

$(plt_emissions_dep): write_emissions.py
	python $<

$(tmp_dir)/radiative_forcing.png: radiative_forcing.py $(tmp_dir)/magicc.tsv utils.py
	python $<

$(tmp_dir)/magicc.tsv: apply_magicc_model.py utils.py
	python $<

.PHONY: clean deapclean

clean:
	rm -rf $(tmp_dir)
	latexmk -c

deepclean:
	rm -rf $(tmp_dir)
	latexmk -C