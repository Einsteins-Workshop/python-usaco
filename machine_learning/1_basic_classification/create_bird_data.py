import ssl

if __name__ == '__main__':
    # fastai methods
    from fastbook import resize_images

    # Convenience method for getting images from the internet
    from fastbook import search_images_ddg, download_url

    from duckduckgo_search import DDGS
    from swiftshadow import QuickProxy

    # Utility methods
    from PIL import Image
    from pathlib import Path
    import urllib.request


    def get_images(keywords, max_results=10):
        duck_duck_go_search = DDGS(proxy="tb", timeout=5)
        search_urls = duck_duck_go_search.images(keywords, max_results=max_results)
        return [url['image'] for url in search_urls]

    def download_image(url, file):
        try:
            urllib.request.urlretrieve(url, file)
        except:
            print(f"Could not load {url}, skipping")

    def download_images(urls, directory):
        for i in range(len(urls)):
            file_name = directory / f"{i}.jpg"
            if file_name.exists():
                return
            download_image(urls[i], file_name)

    # Save a test image to a file
    #ddgs = DDGS(proxy="tb", timeout=20)
    #urls = ddgs.images(keywords="robin photos", max_results=1)
    test_file = Path('test.jpg')
    #print(urls)
    urls = get_images("robin photos", max_results=1)
    if not test_file.exists():
        download_image(urls[0], test_file)

    image = Image.open(test_file)
    image.thumbnail((256, 256)) # This resizes the file to a thumbnail size of 256 x 256 pixels

    # See https://pixspy.com/ in order to see how an image is stored as an array of numbers, equating to a list of
    # pixels, each of which contain a triple of RGB values.


    # Create the training data set, which will consist of up to 200 images resulting from searches on forest and birds
    image_categories = ['forest', 'bird']
    path = Path('bird_or_not')

    if not path.exists():
        path.mkdir(exist_ok=True) # Create the overall bird_or_not directory

    for image_type in image_categories:
        test_directory = path / image_type  # This is a special operator for Path objects, which creates a subdirectory
        test_directory.mkdir(exist_ok=True) # Create the subdirectory with the image category

        results = get_images(f"{image_type} photo", max_results=200)
        download_images(results, test_directory)
        resize_images(test_directory, max_size=400, dest=test_directory) # Resize to only 400 pixels in size