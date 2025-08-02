# Enhanced Self-Checkout System for Retail Based on Improved YOLOv10

Official PyTorch implementation of **MidState-YOLO-ED**.

## Paper

[Enhanced Self-Checkout System for Retail Based on Improved YOLOv10](https://doi.org/10.3390/jimaging10100248)

**Authors**: Lianghao Tan, Shubing Liu, Jing Gao, Xiaoyi Liu, Linyue Chu, Huangqi Jiang

**Published in**: *Journal of Imaging* 2024, 10, 248

**DOI**: https://doi.org/10.3390/jimaging10100248

## Abstract

This paper presents a novel self-checkout system for retail based on an improved YOLOv10 network, aimed at enhancing checkout efficiency and reducing labor costs. We propose targeted optimizations for the YOLOv10 model, incorporating the detection head structure from YOLOv8, which significantly improves product recognition accuracy. Additionally, we develop a post-processing algorithm tailored for self-checkout scenarios, to further enhance the application of the system.

## Key Improvements

- **Hybrid Architecture**: Combines YOLOv8 detection head with YOLOv10 backbone
- **EMA Attention**: Efficient multi-scale attention mechanism for better feature extraction
- **C2f-Dual Convolution**: Lightweight dual convolution design reducing parameters while improving accuracy
- **23.2% mAP improvement** over original YOLOv10-n
- **Optimized for retail environments**: Specifically designed for multi-product checkout scenarios

## Performance

| Model | mAP@0.5 | mAP@0.5:0.95 | Params | GFLOPs | FPS |
|:------|:-------:|:------------:|:------:|:------:|:---:|
| YOLOv10-n | 61.0% | 48.1% | 2.89M | 9.2 | 112.36 |
| **MidState-YOLO-ED** | **99.4%** | **87.5%** | **3.29M** | **9.6** | **109.89** |

## Citation

If you use this work in your research, please cite:

```bibtex
@article{tan2024enhanced,
  title={Enhanced Self-Checkout System for Retail Based on Improved YOLOv10},
  author={Tan, Lianghao and Liu, Shubing and Gao, Jing and Liu, Xiaoyi and Chu, Linyue and Jiang, Huangqi},
  journal={Journal of Imaging},
  volume={10},
  number={10},
  pages={248},
  year={2024},
  publisher={MDPI},
  doi={10.3390/jimaging10100248}
}
```