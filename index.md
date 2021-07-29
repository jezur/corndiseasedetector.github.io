## Welcome to CDD Main Page

![CDD](./img/img.001.png)

Infectious diseases are a `major threat` to many crops of high importance for the food secutiry of many regions of the world. Each year, around 60% of farmers in Ecuador have reported `pre-harvest losses` due to infectious agents such as fungi and bacteria, in crops like banana, cacao and potato. Outbreaks of infection could endager the country's economy and cause many people to loose their jobs. This project is an effort to develop an `early plant disease detector` as a *proof of concept*, using [publicly available datasets of maize](https://data.mendeley.com/datasets/tywbtsjrjv/1), a very well known species. In the future, we plan to expand this project to cover serveral 


### Replicate our work

If you wish to replicate our work, please download our `jupyter notebook` or clone this whole repository. We trained our NN using Google Cloud GPUs, so you could make a copy of the notebook to your Google Drive, or you can use your resources locally:
```bash
$ git clone https://github.com/corndiseasedetector/corndiseasedetector.github.io
$ cd corndiseasedetector.github.io
$ conda env create -f environment.yml
$ conda activate cddenv
```
The `environment.yml` file only specifies packages to set up the working environment. Please, install the Pytorch version that suits you best inside the `cddenv` environment. If you plan to use your own GPUs, then type
```bash
$ conda install pytorch torchvision cudatoolkit=10.2 -c pytorch -n cddenv
```
If you will only use CPU, then type
```bash
$ conda install pytorch torchvision torchaudio -c pytorch -n cddenv
```

### Support or Contact

If you have any request of trouble using our model, please contact us to out email `ai2021grupo7[at]gmail.com`.
