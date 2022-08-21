from PIL import Image
from flask import Blueprint, request, abort, jsonify, g
from titans.tfefficientnet import EfficientNet

api = Blueprint("api", __name__)


@api.route("/predict", methods=["POST"])
def predict():
    scale = request.form.get("scale", 4, type=int)
    top_k = request.form.get("top_k", None, type=int)
    image = request.files["image"]

    img = Image.open(image)
    print(f"Loaded image with size {img.size}")

    print(f"Loading model with scale {scale}")
    model = EfficientNet(scale=scale)

    img = model.preprocess(img)
    preds = model.predict(img).astype(float)
    conf_labels = sorted(zip(preds[0, :], model.label_map), reverse=True)

    result = [
        {"label": label, "confidence": confidence}
        for confidence, label in conf_labels[:top_k]
    ]
    return jsonify(result)