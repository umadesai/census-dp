# Disclosure Avoidance Repository

### Motivation
The Census Bureau is by law required to keep its survey responses confidential, and is beginning the transition from “ad-hoc” privacy techniques towards a formally private framework known as **differential privacy.** All public data releases must go thorough the **Disclosure Review Board (DRB)**, whose newest policy states that *any data release at the sub-state level or lower must be protected with noise injection techniques.*

External researchers using restricted census data at Federal Statistical Research Data Centers (FSRDCs) are among the first affected by these policies, but all census data products will eventually require these techniques. Researchers generally do not have a background in formal privacy, so they face a road block if they are interested in publishing sub-state results. This repository strives to deliver the tools and documentation to address this problem. *Content here is WIP and all releases utilizing this library still require official approval from the DRB.*

#### Differential Privacy
   - mathematically provable privacy guarantee
   - states that any information-related risk to a person should not change significantly as a result of that person's information being included, or not, in the analysis

   ##### [A Privacy "Budget"](https://github.com/umadesai/census-dp/blob/master/notebooks/dp-budget.ipynb)
   - DP provides provable privacy guarantees with respect to the cumulative risk from successive data releases
   - Setting the budget is a policy question

   ##### Differentially Private Computations
   Algorithms maintain differential privacy via the introduction of carefully crafted random noise into the computation. 
   Types of computations that can be made differentiallly private:
   - descriptive statistics
       - [counts](https://github.com/umadesai/census-dp/blob/master/notebooks/dp-count.ipynb)
       - [mean](https://github.com/umadesai/census-dp/blob/master/notebooks/dp-mean.ipynb)
       - [median](https://github.com/umadesai/census-dp/blob/master/notebooks/dp-median.ipynb)
       - histograms
       - boxplots
       - [cdf](https://github.com/umadesai/census-dp/blob/master/notebooks/dp-mm.ipynb)
   - supervised and unsupervised ML tasks
       - [regression](https://github.com/umadesai/census-dp/blob/master/notebooks/dp-regression.ipynb)
       - classification
   - generation of synthetic data

   #### Read more
   - [Differential Privacy: An Introduction For Statistical Agencies](https://gss.civilservice.gov.uk/wp-content/uploads/2018/12/12-12-18_FINAL_Privitar_Kobbi_Nissim_article.pdf) Page et al.
   - [Differential Privacy: A Primer for a Non-technical Audience](http://www.jetlaw.org/wp-content/uploads/2018/12/4_Wood_Final.pdf) Wood et al.
   - [A Firm Foundation for Private Data Analysis](http://delivery.acm.org/10.1145/1870000/1866758/p86-dwork.pdf?ip=108.28.104.96&id=1866758&acc=OPEN&key=4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E6D218144511F3437&__acm__=1562937387_c049c03e734df8e04aac19ab857b3961) Dwork.
   - [The Algorithmic Foundations of Differential Privacy](https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf) Dwork & Roth.
   - [Introductory Readings in Formal Privacy for Economists](https://labordynamicsinstitute.github.io/privacy-bibliography/index.html) Abowd, Schmutte, Sexton, & Vilhuber.

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
