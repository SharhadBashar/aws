import os
import joblib
"""
Deserialize fitted model
"""
def model_fn(model_dir, language = 'en'):
    model = joblib.load(os.path.join(model_dir, f'model_{language}.joblib'))
    return model

"""
input_fn
    request_body: The body of the request sent to the model.
    request_content_type: (string) specifies the format/variable type of the request
"""
def input_fn(request_body):
    if (type(request_body) == str):
        return [request_body]
    else:
        raise ValueError('This model only supports string inputs')

"""
predict_fn
    input_data: returned array from input_fn above
    model (sklearn model) returned model loaded from model_fn above
"""
def predict_fn(input_data, model):
    return model.predict(input_data)[0]

"""
output_fn
    prediction: the returned value from predict_fn above
    content_type: the content type the endpoint expects to be returned. Ex: JSON, string

"""
def output_fn(prediction):
    return int(prediction[0])