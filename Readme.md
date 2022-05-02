# BMED4010 Final Year Project: Exploration of computational and experimental approaches for engineering CRISPR-Cas9 nuclease

## Introduction
The CRISPR-Cas9 technology is burgeoning and many Cas9 nuclease variants have been engineered for genome editing applications. However, the performance of Cas9s still needs further improvement. Machine Learning-Assisted Directed Evolution (MLDE) was developed and applied into the field. MLDE can report the sequence-to-fitness relationship from the pre-labelled dataset, hence to reduce the experimental burden and accelerate the optimal variants filtering from the ultrahigh throughput input space. To further compress the initialization of MLDE model training, different techniques such as zero-shot prediction were proposed to guide the initial library establishment. In this project, ΔΔG was investigated as a structure-based protein descriptor, and its efficacy of predicting the protein fitness was also evaluated.

## ΔΔG Calculation with _in silico_ protein modelling suits
As the characterization of ΔΔG involves laborious experimental effort, engineering simulation was applied in this project rather than constructing the ΔΔG library by experiments. _EvoEF_ and _PyRosetta_ were selected to be the computational kernel due to their individual merits. To automate the overall processing and makes these computational platforms become more user friendly, they were compiled into a pipeline conduct the downstream analysis. More details can be found in each individual folder

## Disclaimer and copyright
No copyright, just a part of my final year project. It is provided to users 
without any charge. Users can freely download, use and make changes to it. 
But unauthorized copying of the source code files via any medium is strictly 
prohibited.


## Bugs report
Please contact me if you find anything bad: u3556373@connect.hku.hk
