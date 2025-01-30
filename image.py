from sklearn.cluster import KMeans
import numpy as np
from PIL import ImageFilter, ImageOps

# Reduce the number of colors in the original image to a maximum of 12 using k-means clustering
def reduce_colors(image, num_colors):
    # Convert image to RGB and then to a numpy array
    image = image.convert("RGB")
    img_array = np.array(image)
    flat_img_array = img_array.reshape((-1, 3))

    # Apply KMeans clustering to reduce the number of colors
    kmeans = KMeans(n_clusters=num_colors, random_state=0)
    labels = kmeans.fit_predict(flat_img_array)
    cluster_centers = np.uint8(kmeans.cluster_centers_)

    # Replace each pixel with the nearest cluster center
    reduced_img_array = cluster_centers[labels].reshape(img_array.shape)
    reduced_image = Image.fromarray(reduced_img_array)
    return reduced_image, kmeans

# Apply the reduction process to the original image
num_colors = 12
reduced_image, kmeans = reduce_colors(original_image, num_colors)

# Save the color-reduced image for reference
reduced_image_path = "/mnt/data/mokes_reduced.png"
reduced_image.save(reduced_image_path)

# Display the reduced image to confirm results
reduced_image.show()

# Provide the path to the user for review
reduced_image_path
