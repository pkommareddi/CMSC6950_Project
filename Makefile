tmp_dir=temp
plt_emissions=plot_emissions.py
plt_emissions_dep=$(tmp_dir)/rcps.tsv
utils=utils.py

report.pdf: $(tmp_dir)/radiative_forcing.png $(tmp_dir)/RCP26_Emissions_CH4.png $(tmp_dir)/RCP45_Emissions_CH4.png $(tmp_dir)/RCP26_Emissions_CO2.png $(tmp_dir)/RCP45_Emissions_CO2.png report.tex
	latexmk -pdf

# Plot Emmisions
$(tmp_dir)/RCP26_Emissions_CH4.png: $(plt_emissions) $(plt_emissions_dep) $(utils)
	python $< 'RCP26' 'Emissions|CH4' $@

$(tmp_dir)/RCP45_Emissions_CH4.png: $(plt_emissions) $(plt_emissions_dep) $(utils)
	python $< 'RCP45' 'Emissions|CH4' $@

$(tmp_dir)/RCP26_Emissions_CO2.png: $(plt_emissions) $(plt_emissions_dep) $(utils)
	python $< 'RCP26' 'Emissions|CO2|MAGICC Fossil and Industrial' $@

$(tmp_dir)/RCP45_Emissions_CO2.png: $(plt_emissions) $(plt_emissions_dep) $(utils)
	python $< 'RCP45' 'Emissions|CO2|MAGICC Fossil and Industrial' $@

# Save scenario data as delimited text 
$(plt_emissions_dep): write_emissions.py $(utils)
	python $<

$(tmp_dir)/radiative_forcing.png: radiative_forcing.py $(utils) $(tmp_dir)/rcp85_magicc_data.tsv $(tmp_dir)/rcp60_magicc_data.tsv $(tmp_dir)/rcp45_magicc_data.tsv $(tmp_dir)/rcp26_magicc_data.tsv
	python $<

$(tmp_dir)/rcp85_magicc_data.tsv: write_magicc_data.py $(utils)
	python $< rcp85
$(tmp_dir)/rcp60_magicc_data.tsv: write_magicc_data.py $(utils)
	python $< rcp60
$(tmp_dir)/rcp45_magicc_data.tsv: write_magicc_data.py $(utils)
	python $< rcp45
$(tmp_dir)/rcp26_magicc_data.tsv: write_magicc_data.py $(utils)
	python $< rcp26

.PHONY: clean deapclean

clean:
	rm -rf $(tmp_dir)
	latexmk -c

deepclean:
	rm -rf $(tmp_dir)
	latexmk -C