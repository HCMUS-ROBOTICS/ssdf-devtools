import torch
from .typing import *
import numpy as np
from .color import color_map


def multi_class_prediction(output: Tensor) -> Tensor:
    return torch.argmax(output, dim=1)


def binary_prediction(output: Tensor, thresh: float = 0.5) -> Tensor:
    return (output.squeeze(1) > thresh).long()


def np2cmap(np_image):
    """
    input: numpy batch B x H x W
    output: color map batch  B x C x H x W
    """
    cmap = color_map()[:, np.newaxis, :]
    new_im = np.dot(np_image == 0, cmap[0])
    cmap = color_map()[:, np.newaxis, :]
    for i in range(1, cmap.shape[0]):
        new_im += np.dot(np_image == i, cmap[i])
    return new_im


def tensor2cmap(tensor):
    """
    input: Tensor batch B x H x W
    output: color map batch  B x C x H x W
    """
    np_image = tensor.permute(1, 2, 0).cpu().numpy()
    return torch.tensor(np2cmap(np_image).transpose(2, 0, 1))
