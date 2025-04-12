if __name__ == '__main__':
    # fastai methods
    from fastbook import verify_images, get_image_files
    from fastbook import DataBlock, ImageBlock, CategoryBlock, RandomSplitter, Resize
    from fastbook import parent_label, vision_learner

    # pytorch method
    from fastbook import resnet18

    # Utility methods
    from PIL import Image
    from pathlib import Path

    # Create the training data set, which will consist of up to 200 images resulting from searches on forest and birds
    image_categories = ['forest', 'bird']
    path = Path('bird_or_not')

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
    data_loaders.show_batch(max_n=6)
    learn = vision_learner(data_loaders, resnet18)
    learn.fine_tune(3)

    # Test your model on the test file.
    is_bird, _, probability = learn.predict(test_file)
    print(f"This is a: {is_bird}.")
    print(f"Probability it's a bird: {probability[0]:.4f}")