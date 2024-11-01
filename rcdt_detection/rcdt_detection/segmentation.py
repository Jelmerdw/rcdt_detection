# SPDX-FileCopyrightText: Alliander N. V.
#
# SPDX-License-Identifier: Apache-2.0

import ultralytics
import numpy as np

SEGMENTATION_MODEL_PATH: str = "/home/wp/projects/realsense/models/FastSAM-x.pt"


def load_segmentation_model(
    model_path: str = SEGMENTATION_MODEL_PATH,
) -> ultralytics.engine.model.Model:
    """Load segmentation model from given path."""
    return ultralytics.FastSAM(model_path)


def segment_image(
    model: ultralytics.engine.model.Model, image: np.array
) -> ultralytics.engine.results.Results:
    """Segment given image using given model."""
    height, width, _ = image.shape
    return model(image, imgsz=(height, width))[0]
