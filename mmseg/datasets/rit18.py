# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class R18dataset(CustomDataset):
    """Pascal VOC dataset.

    Args:
        split (str): Split txt file for Pascal VOC.
    """

    CLASSES = ('tree', 'build-up', 'bush', 'grass', 'lake', 'pool',
               'road', 'beach')

    PALETTE = [[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0], [0, 0, 128],
               [128, 0, 128], [0, 128, 128], [128, 128, 128]]

    def __init__(self, **kwargs):
        super(R18dataset, self).__init__(
            img_suffix='.tif', seg_map_suffix='.tif', **kwargs)
        assert osp.exists(self.img_dir)
