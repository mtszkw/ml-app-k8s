# ML App Template

Simple application for testing productization/deployment of ML apps. 

##### Training

Jupyter notebook ([boston_train.ipynb](/boston_train.ipynb)) downloads Boston Dataset and performs a quick training using XGBoostRegressor model. Training parameters as well as train/valid/test split were chosen arbitrarly and don't guarantee good results, but that's not the point here. At the end, notebook saves the model to [xgbregressor_boston.json](xgbregressor_boston.json) file which can be then loaded back for inference.

##### Inference

Inference script [boston_inference.py](boston_inference.py) is a FastAPI app with single endpoint which expects POST requests with JSON payload (see Sending Requests section). After request is received, data is then converted to XGBRegressor input format and used for inference. Response contains single number which is a predicted house price based on input features.

### Building & Running

```
docker build --no-cache -t ml_app_template .
docker run --rm -p 8000:8000 ml_app_template
```

### Sending Requests

When docker container is running, endpoint should be available on http://0.0.0.0:8000/predict and JSON payload with features can be sent via POST. Here is an example payload with 13 features (see [dataset description](https://scikit-learn.org/stable/datasets/toy_dataset.html#boston-dataset)):

```
{
    "crim": 6.71772,
    "zn": 0.0,
    "indus": 18.1,
    "chas": 0.0,
    "nox": 0.713,
    "rm": 6.749,
    "age": 92.6,
    "dis": 2.323,
    "rad": 24.0,
    "tax": 666.0,
    "ptratio": 20.2,
    "b": 0.32,
    "lstat": 17.44
}
```