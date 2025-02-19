# Introduction

This project, *Napoleon's Russian Campaign*, is a recreation of the renowned data visualization *Charles Minard's Napoleon's Disastrous Russian Campaign of 1812*. We built a database using `pandas` and `sqlite3` and conducted a proof of concept using `matplotlib` and `basemap` to produce the final visualization.

# How to Reproduce

- Install Miniconda.
- Create the environment based on `environment.yml`:
```bash
conda env create -f environment.yml
```
- Place `minard.txt` from the `data/` folder into the `data/` directory within your working directory.
- Activate the environment and run the following command to create `minard.db` in the `data/` folder:
```bash
python create_minard_db.py
```
- Activate the environment and run the following command to generate `minard_clone.png`:
```bash
python plot_with_basemap.py
```
