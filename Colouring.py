from numpy import array, zeros, shape, inf, abs

def weighted_grayscale(image, wr, wg, wb):
    image_shape = shape(image)
    new_image = zeros((image_shape[0],image_shape[1]))
    for i in range(image_shape[0]):
        for j in range(image_shape[1]):
            new_image[i,j] = int(wr * image[i,j,0] + wg * image[i,j,1] +\
                wb * image[i,j,2])
    return new_image

def standard_grayscale(image):
    #simple average of rgb values.
    return weighted_grayscale(image, 1/3, 1/3, 1/3)

def yuv_grayscale(image):
    #grayscale closer to human perception.
    return weighted_grayscale(image, 0.299, 0.587, 0.114)

def paletting(image, palette):

    image_shape = shape(image)
    new_image = zeros(image_shape)
    for i in range(image_shape[0]):
        for j in range(image_shape[1]):
            new_image[i,j] = paletted_colour(image[i,j], palette)
            # print(new_image[i,j])

    output = new_image.astype(int)

    return output

def caching(func):
    cache = {}
    def wrapper(*args, **kwargs):
        colour, palette = tuple(args[0]), tuple(map(tuple, args[1]))
        if (colour, palette) in cache:
            return cache[(colour, palette)]
        cache[(colour, palette)] = func(*args, **kwargs)
        return cache[(colour, palette)]

    return wrapper

@caching
def paletted_colour(colour, palette):

    best_match = None
    min_distance = inf #Actually distance squared, to reduce unnecessary computation
    for i in range(len(palette)):
        distance = abs(sum(colour**2 - palette[i]**2))
        if distance < min_distance:
            min_distance = distance
            best_match = palette[i]
    return best_match