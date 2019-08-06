# Disclosure Avoidance Repository

### How to install & run a notebook.

1. Install Anaconda (Census employees must submit a Remedy ticket).

2. Open an Anaconda prompt

3. Install git by typing the following into your Anaconda prompt and pressing enter.
```
conda install git
``` 

4. Navigate to the directory you would like to download this repository in. 

    *For example:*
```
cd Downloads/privacy/
```

5. Clone this repository
```
git clone https://github.com/umadesai/census-dp.git
```
6. Navigate to the notebooks folder.
```
cd census-dp/notebooks
```
7. Run Jupyter Notebook.
```
jupyter notebook
```
This command should launch Jupyter Notebook locally in your browser. If it does not, open your browser and navigate to the localhost address that is provided in your Anaconda prompt.

8. Click on the IPython Notebook you would like to open. We recommend starting with [dp-intro](https://github.com/umadesai/census-dp/blob/master/notebooks/dp-intro.ipynb).

9. Reference [this sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Jupyter_Notebook_Cheat_Sheet.pdf) for help using Jupyter Notebook.

### Setting up your conda environment.

1. Create the environment from the ```env.yml``` file:
```
conda env create -f env.yml
```
2. Activate the new environment:
```
conda activate env
```
3. Once you've finished your work in this environment, you can deactivate the environment using:
```
conda deactivate
```
### Importing a module from the library.

If you want to use a module or algorithm from the library in your own python script, you can follow the structure of the example below.
```
from census_dp import laplace

my_laplace = laplace.laplace_mech(mu=0, epsilon=1, sensitivity=1)
```
### Running tests.

There are tests for each of the library modules, implemented with pytest. To run all the tests at once, run pytest from the base directory of the project.
```
pytest
```
