# 📷 Imgur Image Brute Forcer 🕵️‍♂️

A Python script that brute forces Imgur images by randomly generating URLs until a valid image is found. The valid images are then saved to disk.

## Requirements 📋

This script requires the following libraries to be installed:

- requests
- BeautifulSoup

You can install the required libraries using pip:
`pip install requests beautifulsoup4`


## Usage 🚀

To use the script, follow these steps:

1. Clone the repository or download the script file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the following command:

`python main.py`

5. The script will prompt you to specify the type of image you want to brute force. You can choose from the following options: PNG, JPG, JPEG, GIF, WEBP, or CUSTOM. If you choose CUSTOM, you will be prompted to enter the extension of the image you want to brute force.
6. Once you have specified the image type, the script will start brute forcing. It will generate random URLs and check if they lead to a valid image. Valid images will be saved to the `images` directory.

## Author 🧑‍💻

This script was created by @DRQSuperior.

## License 🔒

This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
