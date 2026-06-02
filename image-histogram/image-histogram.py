def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    histogram = [0] * 256
    
    # 遍历每一行
    for row in image:
        # 遍历每个像素值
        for pixel in row:
            histogram[pixel] += 1
            
    return histogram