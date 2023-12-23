Annotation Class Verifier for Images

The provided script serves as an Annotation Class Verifier for Images and performs the following tasks:

    Reads a JSON file containing information about images and their annotations.
    Defines a list of desired annotation classes, including "hardhat," "uniform," "boots," "gloves," "hearing protection," "safety glasses," and "lifejacket."
    Iterates through all the images present in the JSON file.
    For each image, checks if the corresponding image file exists.
    Opens the image using the PIL library.
    Retrieves the annotation classes present in the image from the JSON.
    Verifies if all the desired annotation classes are present in the obtained classes.
    Displays messages indicating whether the image is correctly annotated or has incorrect annotation classes.
    Maintains a counter to track the progress of image verification.
    At the end of the verification, displays a message indicating the total number of images with errors and lists the names of images with errors, if any, or a message indicating that all images were successfully checked.
