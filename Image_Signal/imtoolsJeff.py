from PIL import Image
import numpy
import matplotlib
import matplotlib.pyplot as plt

plt.ion()

def open_image(path):
    """Convert PNG image to numpy 2D float array"""
    i = Image.open(path).convert('L')
    return numpy.array(i, dtype=numpy.float32)

__zoom = 9.437086092

def display_image(array, vmin=None, vmax=None):
    """Display 2D array as image"""
    plt.rcParams["figure.figsize"] = (__zoom, __zoom)
    plt.imshow(array, cmap=plt.cm.gray, interpolation='nearest', vmin=vmin, vmax=vmax)
    plt.axis('off')
    plt.gca().xaxis.set_major_locator(matplotlib.ticker.NullLocator())
    plt.gca().yaxis.set_major_locator(matplotlib.ticker.NullLocator())

def display_images(images, lines=None, columns=None, indices=None, vmin=None, vmax=None):
    """Display a list of 2D arrays as images"""
    if columns is None:
        columns = int(numpy.ceil(numpy.sqrt(len(images))))
    if lines is None:
        lines = int(numpy.ceil(float(len(images)) / columns))
    if indices is None:
        indices = range(1, len(images) + 1)
    plt.rcParams["figure.figsize"] = (__zoom * columns, __zoom * lines)
    for k in range(len(images)):
        if images[k] is not None:
            plt.subplot(lines, columns, indices[k])
            display_image(images[k], vmin=vmin, vmax=vmax)
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0.05, hspace=0.05)
    plt.axis('off')
    plt.gca().xaxis.set_major_locator(matplotlib.ticker.NullLocator())
    plt.gca().yaxis.set_major_locator(matplotlib.ticker.NullLocator())

def save_image(array, path):
    """Convert numpy 2D float array to PNG image"""
    arr_clipped = numpy.clip(array, 0, 255).astype(numpy.uint8)
    i = Image.fromarray(arr_clipped, mode='L')
    i.save(path, 'PNG')