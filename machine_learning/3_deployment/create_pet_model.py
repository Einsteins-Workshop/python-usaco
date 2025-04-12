if __name__ == '__main__':
    # fastai methods
    from fastbook import get_image_files
    from fastbook import DataBlock, ImageBlock, CategoryBlock, RandomSplitter, Resize, ResizeMethod, RandomResizedCrop
    from fastbook import vision_learner, error_rate

    # pytorch method
    from fastbook import resnet18

    # Utilities
    import re

    # Augmented transforms
    from fastai.vision.augment import *

    custom_aug_transforms = [RandomResizedCrop(128, min_scale=0.35), Flip(), Brightness(), Contrast(),
                             Rotate(max_deg=10.0)]


    # Get image files from fastbook
    from fastbook import untar_data, URLs
    path = untar_data(URLs.PETS) / 'images'
    print(path)

    # Reduce the number of files to shorten the model build time
    for file in path.iterdir():
        match = re.search(r"_(\d+).jpg", str(file))
        if not(match) or (int(match.group(1)) > 20):
            file.unlink()

    # All cat files happen to start with an upper case file
    def is_cat(x):
        return x.name[0].isupper()

    # Set up cat/dog model
    pet_data = DataBlock(
        blocks=(ImageBlock, CategoryBlock),
        get_items=get_image_files,
        splitter=RandomSplitter(valid_pct=0.2, seed=42),
        get_y=is_cat,
        item_tfms=[Resize(192)]
    )

    augmented_pet_data_loader = pet_data.new(
        item_tfms=RandomResizedCrop(128, min_scale=0.5),
        batch_tfms=custom_aug_transforms
    ).dataloaders(path)

    learn = vision_learner(augmented_pet_data_loader, resnet18, metrics=error_rate)
    learn.fine_tune(3)

    # Save the model to a file
    learn.export('pet_model.pkl')


