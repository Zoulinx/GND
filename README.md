
# Paper with code
### 🌟 We are looking for reviewers for papers in the TGRS journal. If you find our work interesting and would like to serve as a reviewer for the paper, please feel free to contact me.
### 👉🏻linxinzou@foxmail.com
GND:A normalized difference form more suitable for remote sensing applications.
https://doi.org/10.36227/techrxiv.21687326.v1

<div  align="center">
 <img src="resources/swin.png" width = "591" height = "306" alt="GND and RI" align=center />
</div>

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
mmsegmentation
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
