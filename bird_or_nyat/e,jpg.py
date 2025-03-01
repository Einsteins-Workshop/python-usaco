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
urls = search_images_ddg('birb.jipig', max_images=1)
test_file = Path('test.jpg')
if test_file.exists():
    test_file.unlink()
if not test_file.exists():
    download_url(urls[0], test_file, show_progress=True)
z = 0
image = Image.open(test_file)
image.thumbnail((256, 256)) # This resizes the file to a thumbnail size of 256 x 256 pixels

# See https://pixspy.com/ in order to see how an image is stored as an array of numbers, equating to a list of
# pixels, each of which contain a triple of RGB values.


# Create the training data set, which will consist of up to 200 images resulting from searches on forest and birds
while z < 2000:
    image_categories = ['forest', 'bird', 'PIGGGG']
    path = Path('bird_or_nyaat')
    for image_type in image_categories:
        test_file = path / image_type  # This is a special operator for Path objects, which creates a subdirectory
        test_file.mkdir(exist_ok=True) # Create the subdirectory with the image category
        results = search_images_ddg(f"{image_type} photo", max_images=6)
        download_url(results[5], test_file)
        resize_images(test_file, max_size=400, dest=test_file) # Resize to only 400 pixels in size
        image = Image.open(test_file)
        image.thumbnail((256, 256))  # This resizes the file to a thumbnail size of 256 x 256 pixels
    z = z+1







# Remove images that are from broken links
#failed = verify_images(get_image_files(path))
#for file in failed:
#    file.unlink()

