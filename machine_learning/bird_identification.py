if __name__ == '__main__':
    # fastai methods
    from fastbook import download_images, resize_images, verify_images, get_image_files
    from fastbook import DataBlock, ImageBlock, CategoryBlock, RandomSplitter, Resize
    from fastbook import parent_label, vision_learner, error_rate

    # pytorch method
    from fastbook import resnet18

    # Convenience method for getting images from the internet
    from fastbook import search_images_ddg, download_url

    # Utility methods
    from PIL import Image
    from pathlib import Path

    # Save a test image to a file
    urls = search_images_ddg('toucan photos', max_images=1)
    test_file = Path('test.jpg')
    if not test_file.exists():
        download_url(urls[0], test_file, show_progress=True)

    image = Image.open(test_file)
    image.thumbnail((256, 256)) # This resizes the file to a thumbnail size of 256 x 256 pixels

    exit()

    # See https://pixspy.com/ in order to see how an image is stored as an array of numbers, equating to a list of
    # pixels, each of which contain a triple of RGB values.


    # Create the training data set, which will consist of up to 200 images resulting from searches on forest and birds
    image_categories = ['forest', 'bird']
    path = Path('bird_or_not')

    if not path.exists():
        path.mkdir(exist_ok=True) # Create the overall bird_or_not directory

        for image_type in image_categories:
            test_file = path / image_type  # This is a special operator for Path objects, which creates a subdirectory
            test_file.mkdir(exist_ok=True) # Create the subdirectory with the image category
            results = search_images_ddg(f"{image_type} photo")
            download_images(test_file, urls=results[:200])
            resize_images(test_file, max_size=400, dest=test_file) # Resize to only 400 pixels in size

    # Remove images that are from broken links
    failed = verify_images(get_image_files(path))
    for file in failed:
        file.unlink()

    # Create the machine learning model.  Note that the parameters here will be discussed in a later class, and should
    # for now be considered a black box.
    data_loaders = DataBlock(
        blocks=(ImageBlock, CategoryBlock),
        get_items=get_image_files,
        splitter=RandomSplitter(valid_pct=0.2, seed=42),
        get_y=parent_label,
        item_tfms=[Resize(192, method='squish')]
    ).dataloaders(path)

    learn = vision_learner(data_loaders, resnet18)
    learn.fine_tune(3)

    # Test your model on the test file.
    is_bird, _, probability = learn.predict(test_file)
    print(f"This is a: {is_bird}.")
    print(f"Probability it's a bird: {probability[0]:.4f}")