# PedesFormer

PedesFormer is a [MMDetection](https://github.com/open-mmlab/mmdetection) and [SwinTransformer](https://github.com/SwinTransformer/Swin-Transformer-Object-Detection) based repository. It is a successor to our earlier work [Pedestron](https://github.com/hasanirtiza/Pedestron). PedesFormer, focuses on the adavancement of reseach on pedestrian detection using transformer networks.


<img title="Amsterdam" src="gifs/1.gif" width="400" /> <img title="Amsterdam" src="gifs/2.gif" width="400"/>
<img title="Amsterdam" src="gifs/3.gif" width="400"/> <img title="Amsterdam" src="gifs/4.gif" width="400"/>


# :fire: **Updates** :fire:
* 🧨 **Swin Transformer CityPerson model released.** 🧨

# Pretrained Models


# Benchmarking 

### Benchmarking of pre-trained models on pedestrian detection datasets (autonomous driving)
|    Backbone                | Dataset   | Backbone |Configuration | Reasonable  | Heavy    | 
|--------------------|:-------------|:--------:|:--------:|:--------:|:--------:|
| [Cascade Mask R-CNN]| CityPersons        | [Swin - Transformer](https://drive.google.com/file/d/1T74Ug-GEazcWFrwV1-i9jftw3EyV5uXR/view?usp=sharing) |[Config](https://drive.google.com/file/d/1ojsaY-8--Z_9WDWQCDWgCHjg6Z4rQEfJ/view?usp=sharing) | 9.2       |   36.9      | 
| [Cascade Mask R-CNN]| EuroCity Persons        | Swin - Transformer |  -- |        |         | 
| [Cascade Mask R-CNN]| Crowd Human        | Swin - Transformer | -- |        |         | 




More Pre-trained models are coming soon.



# Installation 
For installation, please see [this](https://github.com/open-mmlab/mmdetection/blob/master/docs/en/get_started.md).



# Citation 
### Please cite the following works
[CVPR2021](https://openaccess.thecvf.com/content/CVPR2021/papers/Hasan_Generalizable_Pedestrian_Detection_The_Elephant_in_the_Room_CVPR_2021_paper.pdf)
```
@InProceedings{Hasan_2021_CVPR,
    author    = {Hasan, Irtiza and Liao, Shengcai and Li, Jinpeng and Akram, Saad Ullah and Shao, Ling},
    title     = {Generalizable Pedestrian Detection: The Elephant in the Room},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    month     = {June},
    year      = {2021},
    pages     = {11328-11337}
}
```

[ArXiv 2022](https://arxiv.org/pdf/2201.03176.pdf)
```
@article{hasan2022pedestrian,
  title={Pedestrian Detection: Domain Generalization, CNNs, Transformers and Beyond},
  author={Hasan, Irtiza and Liao, Shengcai and Li, Jinpeng and Akram, Saad Ullah and Shao, Ling},
  journal={arXiv preprint arXiv:2201.03176},
  year={2022}
}
```
