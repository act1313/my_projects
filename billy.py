from bing_image_downloader import downloader
text = input("What would you like to download? ")
downloader.download(text, limit=1000,  output_dir='dataset/train/chicken', adult_filter_off=False)
