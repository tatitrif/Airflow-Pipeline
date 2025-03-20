import json
import os
import dill
import pandas as pd

path = os.environ.get("PROJECT_PATH", ".")

from config.settings import TEST_DIR_PATH, MODEL_DIR_PATH, PREDICTIONS_FULLPATH

if len([x for x in os.listdir(MODEL_DIR_PATH) if x.endswith(".pkl")]) > 0:
    MODEL_FILENAME = sorted(
        [x for x in os.listdir(MODEL_DIR_PATH) if x.endswith(".pkl")]
    )[-1]


def predict():
    with open(os.path.join(MODEL_DIR_PATH, MODEL_FILENAME), "rb") as file_model:
        model = dill.load(file_model)

    pred = []

    for filename in (x for x in os.listdir(TEST_DIR_PATH) if x.endswith(".json")):
        with open(os.path.join(TEST_DIR_PATH, filename), "rb") as file_test:
            data = json.load(file_test)
            df = pd.DataFrame([data])
            df["pred"] = model["model"].predict(df)

            pred.append(*df[["id", "price", "pred"]].to_dict(orient="records"))

    df_pred = pd.DataFrame(pred)
    df_pred.to_csv(PREDICTIONS_FULLPATH, sep=",")


if __name__ == "__main__":
    predict()
