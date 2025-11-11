# Create GIF

This Python script generates a GIF image from a series of PNG image files.

## Installation

To use this script, you'll need to have the following dependencies installed:

- Python 3.x
- `imageio` library

You can install the `imageio` library using pip:

```
pip install imageio
```

## Usage

To create a GIF from a set of PNG images, follow these steps:

1. Place the PNG image files in the same directory as the `create_gif.py` script.
2. Open the `create_gif.py` file and update the `filenames` list with the names of your PNG files.
3. Run the script using the following command:

   ```
   python create_gif.py
   ```

   This will generate a new GIF file named `myfirstgif.gif` in the same directory as the script.

   The `duration` parameter in the `iio.imwrite()` function sets the duration of each frame in the GIF (in milliseconds), and the `loop` parameter sets the number of times the GIF should loop (0 means loop indefinitely).

## API

The `create_gif.py` script uses the following functions from the `imageio.v3` library:

- `imread(filename)`: Reads an image from the specified file.
- `imwrite(filename, images, duration, loop)`: Writes a series of images to a GIF file.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open a new issue or submit a pull request on the project's GitHub repository.

## Testing 
<h5>The output :</h5>
<p align="center">
<a href="https://github.com/wissamn19/Create_GIF_Python">
  <img src="myfirstgif.gif" alt="Create GIF with Python" width="300">
</a>  
</p>
