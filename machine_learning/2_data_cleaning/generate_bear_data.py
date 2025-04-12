if __name__ == '__main__':
    # fastai methods
    from fastbook import download_images, resize_images

    # Convenience method for getting images from the internet
    from fastbook import search_images_ddg

    # Utility methods
    from pathlib import Path

    # See https://pixspy.com/ in order to see how an image is stored as an array of numbers, equating to a list of
    # pixels, each of which contain a triple of RGB values.


    # Create the training data set, which will consist of up to 200 images resulting from searches on bears
    image_categories = ['grizzly', 'black', 'teddy']
    path = Path('bears')

    if not path.exists():
        path.mkdir(exist_ok=True) # Create the overall bear directory

        for image_type in image_categories:
            test_file = path / image_type  # This is a special operator for Path objects, which creates a subdirectory
            test_file.mkdir(exist_ok=True) # Create the subdirectory with the image category
            results = search_images_ddg(f"{image_type} bear photo")
            download_images(test_file, urls=results[:200])
            resize_images(test_file, max_size=400, dest=test_file) # Resize to only 400 pixels in size

