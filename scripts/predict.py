"""Script for running inference on an image or multiple images. The top K number of predictions are printed."""
import argparse
import glob
import os

from titans.tfefficientnet import EfficientNet


def predict(inpaths: list, scale: int, top_k: int):
    patterns = [
        os.path.join(inpath, "*") if os.path.isdir(inpath) else inpath
        for inpath in inpaths
    ]
    img_paths = [path for pattern in patterns for path in glob.glob(pattern)]

    print(f"Loading EfficientNetB{scale} model")
    model = EfficientNet(scale=scale)

    batch, img_paths = model.load_batch(img_paths)

    print(f"Predicting on {len(img_paths)} images with model '{model.name}'")
    preds = model.predict(batch)
    
    # prints output
    for i, img_path in enumerate(img_paths):
        conf_labels = sorted(zip(preds[i, :], model.label_map), reverse=True)

        print(os.path.basename(img_path))
        for j, (confidence, label) in enumerate(conf_labels[:top_k]):
            print(f"  {j}: {confidence:.3f} {label}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Runs inference on an image or many images"
    )
    parser.add_argument(
        "input_paths",
        nargs="+",
        type=str,
    )
    parser.add_argument(
        "-m",
        "--model-scale",
        type=int,
        default=4,
    )
    parser.add_argument(
        "-k",
        "--top-k",
        type=int,
        default=5,
    )
    args = parser.parse_args()

    predict(inpaths=args.input_paths, scale=args.model_scale, top_k=args.top_k)
    