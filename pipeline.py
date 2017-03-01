def pipeline(image):
    # convert to grayscale
    gray = grayscale(image)

    # gaussian smoothing
    kernel_size = 3 # parameter
    blur_gray = gaussian_blur(gray, kernel_size)

    # canny edge detection
    low_threshold = 60 # parameter
    high_threshold = 180 # parameter
    edges = canny(blur_gray, low_threshold, high_threshold)

    # mask region
    vertices = np.array([[(110, image.shape[0]),
                          (450, 330),
                          (520, 330),
                          (image.shape[1] - 60, image.shape[0])]],
                        dtype=np.int32) # parameter
    masked_image = region_of_interest(edges, vertices)

    # hough transform
    rho = 1 # parameter
    theta = math.pi / 90 # parameter
    threshold = 10 # parameter
    min_line_len = 5 # parameter
    max_line_gap = 10 # parameter
    hough = hough_lines(masked_image, rho, theta, threshold, min_line_len, max_line_gap)

    # return overlay
    return weighted_img(hough, image)

for im in os.listdir("test_images/"):
    # read image
    image = mpimg.imread('test_images/' + im)

    # save result
    mpimg.imsave("test_images/overlay_" + im, pipeline(image))
