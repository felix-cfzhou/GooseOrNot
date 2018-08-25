from os import path

import xgboost as xgb
import numpy as np
from PIL import Image


dir_loc = path.abspath(path.dirname(__file__))
model_name = path.join(dir_loc, 'goose.model')


def is_goose(filename):
    im = Image.open(filename).convert('RGB').reshape((256, 256), Image.ANTIALIAS)
    im = np.array(im).reshape(1, -1)/255.
    im = xgb.DMatrx(im)

    bst = xgb.Boost({'nthread': 2})
    bst.load_model(model_name)

    pred = np.squeeze(bst.predict(im))

    return pred >= 0.5
