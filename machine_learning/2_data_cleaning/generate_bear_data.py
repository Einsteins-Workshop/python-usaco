if __name__ == '__main__':
    # fastai methods
    from fastbook import resize_images

    # Convenience method for getting images from the internet
    from fastbook import search_images_ddg

    from duckduckgo_search import DDGS
    # Utility methods
    from pathlib import Path
    import urllib.request

    # See https://pixspy.com/ in order to see how an image is stored as an array of numbers, equating to a list of
    # pixels, each of which contain a triple of RGB values.

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

    def download_images(urls, directory):
        for i in range(len(urls)):
            file_name = directory / f"{i}.jpg"
            if file_name.exists():
                return
            download_image(urls[i], file_name)

    # Create the training data set, which will consist of up to 200 images resulting from searches on bears
    image_categories = ['grizzly', 'black', 'teddy']
    path = Path('bears')

    if not path.exists():
        path.mkdir(exist_ok=True) # Create the overall bear directory

    for image_type in image_categories:
        test_file = path / image_type  # This is a special operator for Path objects, which creates a subdirectory
        test_file.mkdir(exist_ok=True) # Create the subdirectory with the image category
        results = get_images(f"{image_type} bear photo", max_results=200)
        download_images(results, test_file)
        resize_images(test_file, max_size=400, dest=test_file) # Resize to only 400 pixels in size

