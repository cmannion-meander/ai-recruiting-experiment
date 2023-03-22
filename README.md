# The AI Recruiter

## Goal: Test the AI capabilities of language models to support recruiting processes

### Prerequisites
To get started, you will need the latest version of conda:

    pip install conda

Next, you will need to create a local virtual environment with the packages required for this project. From the directory of this repo, create the environment using:

    conda env create --name airecruiter --file environment.yml

Finally, you can install the custom functions we have developed using:

    pip install -e .

* NOTE: These packages are a baseline requirement. You may need to load more as you experiment with the scripts.

Once this is established, you should be able to open Jupyter Notebooks by entering:

    jupyter notebook

Navigate to the scripts folder to find the latest executable notebooks.

* NOTE: You will need to add your OpenAPI credentials to the script in order to access ChatGPT.
