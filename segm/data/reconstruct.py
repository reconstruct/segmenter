import numpy as np

try:
    import cityscapesscripts.helpers.labels as CSLabels
except:
    pass

from pathlib import Path
from segm.data.base import BaseMMSeg
from segm.data import utils
from segm.config import dataset_dir

RECONSTRUCT_CONFIG_PATH = Path(__file__).parent / "config" / "reconstruct.py"
RECONSTRUCT_CATS_PATH = Path(__file__).parent / "config" / "reconstruct.yml"


class ReconstructDataset(BaseMMSeg):
    def __init__(self, image_size, crop_size, split, **kwargs):
        super().__init__(image_size, crop_size, split, RECONSTRUCT_CONFIG_PATH, **kwargs)
        self.names, self.colors = utils.dataset_cat_description(RECONSTRUCT_CATS_PATH)
        self.n_cls = 29 # as created in our labels.json. This includes subclasses
        self.ignore_label = 255
        self.reduce_zero_label = False

    def update_default_config(self, config):

        root_dir = dataset_dir()
        path = Path(root_dir) / "reconstruct"
        config.data_root = path

        config.data[self.split]["data_root"] = path
        config = super().update_default_config(config)

        return config

    def test_post_process(self, labels):
        labels_copy = np.copy(labels)
        cats = np.unique(labels_copy)
        for cat in cats:
            labels_copy[labels == cat] = CSLabels.trainId2label[cat].id
        return labels_copy
