# convert to grayscale
gray = grayscale(image)
#plt.imshow(gray, cmap='gray')

# gaussian smoothing
kernel_size = 5 # parameter
blur_gray = gaussian_blur(gray, kernel_size)

# canny edge detection
low_threshold = 50 # parameter
high_threshold = 150 # parameter
edges = canny(blur_gray, low_threshold, high_threshold)

# mask region
vertices = np.array([[(60,image.shape[0]),(420, 300), (image.shape[1] - 420, 300), (image.shape[1] - 60,image.shape[0])]], dtype=np.int32) # parameter
masked_image = region_of_interest(edges, vertices)

# hough transform
rho = 1 # parameter
theta = math.pi / 90 # parameter
threshold = 30 # parameter
min_line_len = 10 # parameter
max_line_gap = 1 # parameter
hough = hough_lines(masked_image, rho, theta, threshold, min_line_len, max_line_gap)

# overlay
overlay = weighted_img(hough, image)

# final result
plt.imshow(overlay)

# saved
mpimg.imsave('test_images/solidWhiteRight_overlay.jpg', overlay)
