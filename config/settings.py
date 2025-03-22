import os

from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PATH_LOG = os.path.join(BASE_DIR, "logs", "log.log")

MODEL_FILENAME = f"cars_pipe_{datetime.now().strftime('%Y%m%d%H%M')}.pkl"
DATA_FILENAME = "data_train.csv"
PREDICTIONS_FILENAME = f"predictions_{datetime.now().strftime('%Y%m%d%H%M')}.csv"

MODEL_DIR_PATH = os.path.join(BASE_DIR, "data", "models")
TRAIN_DIR_PATH = os.path.join(BASE_DIR, "data", "train")
PREDICTIONS_DIR_PATH = os.path.join(BASE_DIR, "data", "predictions")
TEST_DIR_PATH = os.path.join(BASE_DIR, "data", "test")

TRAIN_FULLPATH = os.path.join(TRAIN_DIR_PATH, DATA_FILENAME)
MODEL_FULLPATH = os.path.join(MODEL_DIR_PATH, MODEL_FILENAME)
PREDICTIONS_FULLPATH = os.path.join(PREDICTIONS_DIR_PATH, PREDICTIONS_FILENAME)
