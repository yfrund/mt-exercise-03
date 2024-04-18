# MT Exercise 3: Pytorch RNN Language Models

This repo shows how to train neural language models using [Pytorch example code](https://github.com/pytorch/examples/tree/master/word_language_model). Thanks to Emma van den Bold, the original author of these scripts. 

# Requirements

- This only works on a Unix-like system, with bash.
- Python 3 must be installed on your system, i.e. the command `python3` must be available
- Make sure virtualenv is installed on your system. To install, e.g.

    `pip install virtualenv`

# Steps

Clone this repository in the desired place:

    git clone https://github.com/moritz-steiner/mt-exercise-03
    cd mt-exercise-03

Create a new virtualenv that uses Python 3. Please make sure to run this command outside of any virtual Python environment:

    ./scripts/make_virtualenv.sh

**Important**: Then activate the env by executing the `source` command that is output by the shell script above.

Download and install required software:

    ./scripts/install_packages.sh

Download and preprocess data:

    ./scripts/download_data.sh

Current version of the script shows how to obtain *The Art of Perfumery, and Methods of Obtaining the Odors of Plants* from Project Gutenberg.

Train a model:

    ./scripts/train.sh

The training process can be interrupted at any time, and the best checkpoint will always be saved.

*To adapt dropout rate, change the --dropout argument (0 = no dropout).*

*Model training will also generate 3 log files (default destination: ./logs) with perplexity values: training, validation and test.*

Generate (sample) some text from a trained model with:

    ./scripts/generate.sh

Current version of the script generates text based on *The Art of Perfumery, and Methods of Obtaining the Odors of Plants*.

Train multiple models with different parameter settings:

 - activate virtual environment with Pytorch and sacremoses installed;

 - edit and run to download and preprocess your own data:
    
    ./scripts/download_data.sh

  - edit and run to train models, save them and training log files:

    ./scripts/train.sh

  - run to visualise training and validation perplexities as line charts, and create tables for training, validation and testing perplexities:

    visualise.py

  - edit and run to create text samples with data and model of interest:

    ./scripts/generate.sh 
