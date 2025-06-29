if __name__ == '__main__':
    # fastai methods
    from fastbook import download_images, resize_images, verify_images, get_image_files
    from fastbook import DataBlock, ImageBlock, CategoryBlock, RandomSplitter, Resize, ResizeMethod, RandomResizedCrop
    from fastbook import parent_label, vision_learner, error_rate
    from fastbook import ClassificationInterpretation

    # pytorch method
    from fastbook import resnet18

    # Convenience method for getting images from the internet
    from fastbook import search_images_ddg, download_url

    # Utility methods
    from PIL import Image
    from pathlib import Path

    import matplotlib.pyplot as plt

    from fastai.vision.augment import *
    import urllib.request

    def get_images(keywords, max_results=10):
        duck_duck_go_search = DDGS(proxy="tb", timeout=5)
        search_urls = duck_duck_go_search.images(keywords, max_results=max_results)
        return [url['image'] for url in search_urls]

    def download_image(url, file):
        try:
            urllib.request.urlretrieve(url, file)
        except Exception as err:
            print(err)
            print(f"Could not load {url}, skipping")

    custom_aug_transforms = [RandomResizedCrop(128, min_scale=0.35), Flip(), Brightness(), Contrast(),
                             Rotate(max_deg=10.0)]

    # Save a test image to a file
    urls = search_images_ddg('grizzly bear', max_images=1)
    test_file = Path('../test.jpg')
    if not test_file.exists():
        download_url(urls[0], test_file, show_progress=True)

    image = Image.open(test_file)
    image.thumbnail((128, 128)) # This resizes the file to a thumbnail size of 128 x 128 pixels

    # Create the training data set, which will consist of up to 200 images resulting from searches on forest and birds
    image_categories = ['grizzly', 'black', 'teddy']
    path = Path('../bears')

    # Remove images that are from broken links
    failed = verify_images(get_image_files(path))
    for file in failed:
       file.unlink()

    # Create the machine learning model.  Note that the parameters here will be discussed in a later class, and should
    # for now be considered a black box.
    bear_data = DataBlock(
        blocks=(ImageBlock, CategoryBlock),
        get_items=get_image_files,
        splitter=RandomSplitter(valid_pct=0.2, seed=42),
        get_y=parent_label,
        item_tfms=[Resize(128)]
    )

    # This is the standard resizer, which does a crop around the center
    #bear_data.dataloaders(path).valid.show_batch(max_n=8, nrows=2)
    #plt.show()

    # This is the squish resizer, which changes the dimensions of the image
    #squishy_bear_data = bear_data.new(item_tfms=Resize(128, ResizeMethod.Squish))
    #squishy_bear_data.dataloaders(path).train.show_batch(max_n=8, nrows=2)
    #plt.show()

    # This is the pad resizer, which adds empty space to the image
    #padded_bear_data = bear_data.new(item_tfms=Resize(128, ResizeMethod.Pad, pad_mode='zeros'))
    #padded_bear_data.dataloaders(path).train.show_batch(max_n=8, nrows=2)
    #plt.show()

    # This is the pad resizer, which adds empty space to the image
    #random_bear_data = bear_data.new(item_tfms=RandomResizedCrop(88, min_scale=0.5))
    #random_bear_data.dataloaders(path).train.show_batch(max_n=8, nrows=2, unique=True)
    #plt.show()

    augmented_bear_data = bear_data.new(
        item_tfms=RandomResizedCrop(128, min_scale=0.5),
        batch_tfms=custom_aug_transforms
    )
    augmented_bear_data_loader = augmented_bear_data.dataloaders(path)
    # Create the model
    learn = vision_learner(augmented_bear_data_loader, resnet18, metrics=error_rate)
    learn.fine_tune(4)

    # Shows the images that the largest loss (biggest mistakes) are made.  The first is the prediction, the second is
    # its classification
    interp = ClassificationInterpretation.from_learner(learn)
    interp.plot_confusion_matrix()
    plt.show()

    interp.plot_top_losses(5, nrows=1, figsize=(17,4))
    plt.show()

    losses, idx, file_names = interp.top_losses(20, items=True)
    for image in interp.top_losses(20, items=True)[2]:
        file_name = str(image)
        bear_type, _, probability = learn.predict(image)
        print(f"Displaying image {file_name}")
        print(f"In {parent_label(image)} folder")
        print(f"Probabilities: Black {probability[0]:.4f}, Grizzly {probability[1]:.4f}, Teddy {probability[2]:.4f}")
        image = Image.open(image)
        image.show(title=file_name)
        input("Hit any button to show next ")

