import json
from PIL import Image
import os


def check_image_classes(json_path, image_path, desired_classes):
    with open(json_path, "r") as file:
        json_data = json.load(file)

    total_images = len(json_data["images"])
    checked_images = 0
    images_with_errors = []

    for image in json_data["images"]:
        image_name = image["name"]

        if not image_name:
            image_name = "Unnamed Image"

        image_file = os.path.join(image_path, image_name)

        if not os.path.exists(image_file):
            print(f"Image {image_name} not found.")
            images_with_errors.append(image_name)
            continue

        img = Image.open(image_file)
        classes_present = set(image["classes"])

        if set(desired_classes).issubset(classes_present):
            print(f"Image {image_name} is correctly annotated.")
        else:
            print(f"Image {image_name} has incorrect annotation classes.")
            images_with_errors.append(image_name)

        checked_images += 1
        print(f"Images checked: {checked_images}/{total_images}")

    print("Validation completed.")
    if images_with_errors:
        print(f"Number of images with errors: {len(images_with_errors)}")
        print("Images with errors:")
        for error in images_with_errors:
            print(error)
    else:
        print("All images were successfully checked.")


def main():
    json_path = "/home/Desktop/json/instances_default.json"
    image_path = "/home/Desktop/frames"
    desired_classes = ["hardhat", "uniform", "boots", "gloves", "hearing protection", "safety glasses", "lifejacket"]

    check_image_classes(json_path, image_path, desired_classes)


if __name__ == "__main__":
    main()
