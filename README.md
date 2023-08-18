<h1 align="center"> GND-RI: A Normalized Difference Form More Suitable for Remote Sensing Applications </h1>

<h5 align="center"><em>Linxin Zou, Bo Wei</em></h5>

</p >
<p align="center">
<a href="https://ieeexplore.ieee.org/document/10105625"><img src="https://img.shields.io/badge/Paper-IEEE%20TGRS-red"></a>
</p>

## Introduction

**Abstract:** The normalized difference index (NDI) originates from NDVI, which has been widely used in remote sensing applications and to guide the development of NDI in other fields due to its excellent performance; however, injective mapping from the original bands to NDI leads to information loss in land cover classification. When NDI is represented as a simple form, it is, furthermore, prone to premature saturation in specific change detection and variable inversion tasks. In this study, we first propose the radius index (RI), a new index to represent illumination variations by using the missing band information from NDI. Based on RI, we develop a generalized NDI (GND) by adding four positive scaling coefficients to NDI foundation, and the value range and sensitivity of GND are adjusted by these four coefficients, which are derived from the statistical information of the study area. The derivation of these four coefficients is, moreover, reversible, making it possible to interpret the applicable range of the derived set of coefficients. Our experiments demonstrate that: 1) GND is more effective in terms of improving saturation than the traditional indices and 2) mapping the original bands to GND-RI (GND combined with RI) can guide classifiers to learn more generalized features based on spectral information and thus achieve higher classification accuracy both in machine learning and the latest deep learning semantic segmentation models. The data and code for the article can be found at https://github.com/Zoulinx/GND.

<figure>
<div align="center">
<img src=resources/swin.png width="90%">
</div>
</figure>

## Dataset/Model

Supported datasets:

- [x] [RIT-18](https://github.com/rmkemker/RIT-18)


Supported backbones:

- [x] [Swin Transformer (ICCV'2021)](https://github.com/microsoft/Swin-Transformer)
- [x] [ConvNeXt (CVPR'2022)](https://github.com/facebookresearch/ConvNeXt)

Supported methods:

- [x] [UPerNet (ECCV'2018)](configs/upernet)


## Installation

Please refer to [get_started.md](https://github.com/open-mmlab/mmsegmentation/releases/tag/v0.24.0) for install mmseg-0.24

Clone my git

Download [shadow_dataset](https://drive.google.com/file/d/12fvd1He8hQdkC2PTBLM_X2mwR92BcStF/view?usp=share_link) and
[sun_dataset](https://drive.google.com/file/d/1--j4s1uvJiONb7apNJ9V3syrmWgY2o9u/view?usp=share_link)

If you need to verify the model accuracy in the paper, download the following four checkpoint file

- [convnext_band.pth](https://drive.google.com/file/d/1-3NxTRQ0SuEjhsN9yeXw1QHjfPJl3YBM/view?usp=share_link)

- [convnext_index.pth](https://drive.google.com/file/d/1-3XPDAvw6gN5LIo00t0exaPntx4ktRXy/view?usp=share_link)

- [swin_band.pth](https://drive.google.com/file/d/1-5mCnnELnjMIqm5r_89l1TC3KSP6sQ65/view?usp=share_link)

- [swin_index.pth](https://drive.google.com/file/d/1-8ls60lsybqSnQ5EdjNteoCVyASKp36d/view?usp=share_link)

Place the data and checkpoint as follows:
```none
GND-main
├── configs
├── data
│   ├── RIT-18
│   │   ├── sun
│   │   │   ├── clip_sun_label
│   │   │   ├── clip_sun_index_img
│   │   │   ├── clip_sun_band_img
│   │   ├── shadow
│   │   │   ├── clip_shadow_label
│   │   │   ├── clip_shadow_index_img
│   │   │   ├── clip_shadow_band_img
├── mmseg
├── paper
│   ├── checkpoint
│   │   ├── convnext_band.pth
│   │   ├── convnext_index.pth
│   │   ├── swin_band.pth
│   │   ├── swin_index.pth
├── resources
├── tests
├── tools
...
```

## Evaluation
Check out our train log directly 
👋🏻[log](/paper/log)

### or

Open [test.py](/test.py) and modify 24-26 rows
```none
python test.py
```
## Train
Open [train.py](/train.py) and modify 23-24 rows
```none
python train.py
```
## Acknowledgement

We thank [openMMlab](https://github.com/open-mmlab) for the open-source libraries with excellent features.

## Citation

If you find this project useful in your research, please consider cite:

```BibTeX
zou, linxin; Wei, Bo (2022): GND:A normalized difference form more suitable for remote sensing applications. TechRxiv. Preprint. https://doi.org/10.36227/techrxiv.21687326.v1 
```

## License

This project is released under the [Apache 2.0 license](LICENSE).
