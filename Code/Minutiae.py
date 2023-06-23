import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter
from skimage.morphology import skeletonize
from skimage.feature import peak_local_max


def binarize_image(image, threshold):
    """
    Binarize the image based on a threshold value.
    """
    image = image.convert('L')  # Convert to grayscale
    image = np.array(image)
    binary_image = np.where(image <= threshold, 0, 1)
    return binary_image


def ridge_orientations(image, block_size, sigma):
    """
    Compute ridge orientations using the gradient method.
    """
    blurred_image = gaussian_filter(image, sigma=sigma)
    dy, dx = np.gradient(blurred_image)
    orientation = np.arctan2(dy, dx) * (180 / np.pi) % 180
    return orientation


def thinning(image):
    """
    Perform skeletonization/thinning of the binary image.
    """
    skeleton = skeletonize(image)
    skeleton = skeleton.astype(np.uint8) * 255
    return skeleton


def extract_minutiae(skeleton, window_size, threshold):
    """
    Extract minutiae points from the thinned/skeletonized image.
    """
    distance = 2 * window_size
    coordinates = peak_local_max(skeleton, min_distance=distance, threshold_abs=threshold)
    return coordinates


def compute_minutiae(image_path):
    # Load the fingerprint image (assuming it's in JPG format)
    image = Image.open(image_path)

    # Parameters for image processing
    threshold_value = 128  # Adjust this value based on image characteristics
    block_size_value = 16
    sigma_value = 3.0
    window_size_value = 20
    minutiae_threshold_value = 0.1

    # Binarize the image
    binary_image = binarize_image(image, threshold_value)

    # Compute ridge orientations
    orientations = ridge_orientations(binary_image, block_size_value, sigma_value)

    # Thin the binary image
    thinned_image = thinning(binary_image)

    # Extract minutiae points
    minutiae_points = extract_minutiae(thinned_image, window_size_value, minutiae_threshold_value)

    return minutiae_points