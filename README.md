# Frequency-based nanoparticle sensing over large field ranges using the ferromagnetic resonances of a magnetic nanodisc: supplementary material

<a href="https://arxiv.org/abs/1604.07277"><img src="https://img.shields.io/badge/preprint-arxiv:1604.07277-lightgrey.svg" alt="arxiv"></a>
[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/maxalbert/paper-supplement-nanoparticle-sensing)
[![MIT license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/poliastro/poliastro/raw/master/COPYING)

This repository accompanies the paper _"Frequency-based nanoparticle sensing over large field ranges using the ferromagnetic resonances of a magnetic nanodisc"_.
It provides the data underlying the figures in the paper as well as [Jupyter](https://jupyter.org/) notebooks to reproduce those figures.
The latest version of this repository can be found at https://github.com/maxalbert/paper-supplement-nanoparticle-sensing

----------

**Authors:**
Maximilian Albert, Marijan Beg, Dmitri Chernyshenko, Marc-Antonio Bisotti, Rebecca L. Carey, Hans Fangohr and Peter Metaxas.


## Contents

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


## Executing the notebooks

### Using a cloud Jupyter server via Binder (no installation required)

The easiest way to execute the notebooks without installing anything
is to launch a cloud [Jupyter](https://jupyter.org/) server using
[Binder](http://mybinder.org/). You can access it here:

http://mybinder.org/repo/maxalbert/paper-supplement-nanoparticle-sensing

After clicking on the link you may need to wait for a minute or so while
a fresh Jupyter server is being generated. Once this process is complete
it will show a dashboard with the contents of this repository. Navigate
to the `notebooks` folder and click on any of the `.ipynb` files to open
the corresponding Jupyter notebook. You can execute all cells through the
the menu item `Cell -> Run All` to reproduce the corresponding paper figure.
For more information on Jupyter notebooks see their
[documentation](https://jupyter.readthedocs.io/en/latest/index.html).

### Running the notebooks locally on your machine

In order to run the notebooks on your own computer, follow the steps below.

1. Clone this repository and change into the newly created directory:
   ```
   git clone https://github.com/maxalbert/paper-supplement-nanoparticle-sensing.git
   cd paper-supplement-nanoparticle-sensing
   ```

2. Make sure that you have all required dependencies installed (see below; we recommend the installation using conda if possible).

3. Start a notebook server:
   ```
   jupyter notebook
   ```
   This will open a browser window with a dashboard showing the contents of this repository.

4. Navigate to the `notebooks/` folder and open any of the `.ipynb` files. You can reproduce
the associated figure by selecting the menu item `Cell -> Run All`.


## Required dependencies

In order to execute the notebooks, the following dependencies are required.

- `python`
- `ipython`
- `jupyter`
- `matplotlib` (>= 1.5)
- `numexpr`
- `pandas` (>= 0.18)
- `statsmodels`

You can install them using `pip` as follows:
```
pip install ipython jupyter matplotlib numexpr pandas statsmodels
```
However, be aware that this may potentially take a *long* time (and
you may need to install additional dependencies via your
distribution's package manager).

Alternatively, if you have `conda` installed (which comes with the [Anaconda](https://docs.continuum.io/anaconda/index) distribution
or can be installed via [Miniconda](http://conda.pydata.org/miniconda.html)) then the recommended (and much faster) way to install these dependencies
is by running the following command from the toplevel of this repository:
```
conda env create -f environment.yml
```
This will create a conda environment called `particle-sensing` which contains all the required dependencies.
Don't forget to activate the new environment before running the notebooks:
```
source activate particle-sensing  # on Linux/Unix
activate particle-sensing         # on Windows
```
