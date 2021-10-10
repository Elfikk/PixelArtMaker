from numpy import array, zeros, shape, sqrt, ceil

def pixelise(image, pixel_width):

    image_shape = shape(image)
    pixelisation_shape = pixelised_shape(image_shape, pixel_width)
    # print(pixelisation_shape)
    pixelised_image = zeros(pixelisation_shape)

    for i in range(pixelisation_shape[0]):
        image_x = i * pixel_width
        for j in range(pixelisation_shape[1]):
            image_y = j * pixel_width
            pixels = access_pixel_group(image, image_x, image_y, pixel_width)
            # print(pixels, pixels[0].dtype, np.square(pixels), pixel_blend(pixels))
            pixelised_image[i,j] = pixel_blend(pixels)
            # print(len(pixels))

    final_image = pixelised_image.astype(int)

    return final_image

def pixel_blend(pixels):
    #Will fail with an empty array.
    squared_rgb = pixels**2
    average_of_squares = sum(squared_rgb) / len(pixels)
    return sqrt(average_of_squares)

def pixelised_shape(image_shape, pixel_width):
    if len(image_shape) == 2:
        width, height = image_shape
        return int(ceil(width / pixel_width)), int(ceil(height / pixel_width))
    elif len(image_shape) == 3:
        width, height, colour_dimensions = image_shape
        return int(ceil(width / pixel_width)), int(ceil(height / pixel_width)), \
            colour_dimensions
    elif len(image_shape) == 4:
        width, height, colour_dimensions, alpha = image_shape
        return int(ceil(width / pixel_width)), int(ceil(height / pixel_width)), \
            colour_dimensions

def access_pixel_group(original_image, top_left_x, top_left_y, pixel_width):
    pixel_values = []
    for i in range(pixel_width):
        for j in range(pixel_width):
            try:
                pixel_values.append(original_image[top_left_x + i, \
                    top_left_y + j])
            except:
                # print("uh, oh")
                pass 
                #can fail if access overflows - resolution not being divisble by the pixel width.
                #final image will overflow in such a case. (slightly larger resolution)
    return array(pixel_values)