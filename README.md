This repository accompanies the paper "Frequency-based particle biosensing over large field ranges with ferromagnetic resonance" available at [...].
It provides the data underlying the figures in the paper as well as Jupyter notebooks to reproduce those figures.

The directory `notebooks/` contains Jupyter notebooks for the relevant figures in the paper.
On Github you can view them directly in the browser:

- [Fig. 2: Dipole field visualisation](./notebooks/fig_2_dipole_field_visualisation.ipynb)
- [Fig. 4: Frequency dependence on external field strength](./notebooks/fig_4_frequency_dependence_on_external_field.ipynb)
- [Fig. 7: Frequency change vs. lateral particle position](./notebooks/fig_7_frequency_change_vs_lateral_particle_position.ipynb)
- [Fig. 8: Frequency change vs. particle-disc separation](./notebooks/fig_8_frequency_change_vs_particle_separation.ipynb)
- [Fig. 9(a): Frequency change vs. particle M_S](./notebooks/fig_9a_dependence_of_frequency_change_on_particle_Ms.ipynb)
- [Fig. 9(b): Frequency change vs. particle size](./notebooks/fig_9b_dependence_of_frequency_change_on_particle_size.ipynb)
- [Fig. 9(c): Frequency change for the fundamental mode for various external field strengths](./notebooks/fig_9c_comparison_of_frequency_change_for_various_external_field_strengths.ipynb)

The raw data is available in the file [data/eigenmode_info_data_frame.csv](./data/eigenmode_info_data_frame.csv), which is a CSV (= comma-separated values) file containing the simulation parameters and computed resonant frequencies for all performed simulations. All notebooks use this data to generate the figures.
The data format is explained in the notebook [Explanation of the data format](./notebooks/explanation_of_the_data_format.ipynb).
