import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import Colouring as co
import Pixelisation as px

if __name__ == "__main__":

    image = img.imread("TestImages/landscape.jpg")
    if np.amax(image) <= 1:
        image = (image * 255).astype(int)

    # print(image)
    # plt.imshow(image)
    # plt.show()
    
    pixelised_image = px.pixelise(image, 25)
    # print(pixelised_image)

    # grayscaled_image = co.standard_grayscale(pixelised_image)
    # grayscaled_image = co.yuv_grayscale(pixelised_image)

    palette = np.array([np.array([44,33,55]), np.array([118,68,98]), np.array([237,180,161]), np.array([169,104,104])])
    # print(paletted_colour(np.array([0,0,0]), palette))
    paletted_image = co.paletting(pixelised_image, palette)

    # plt.imshow(pixelised_image)
    # plt.imshow(grayscaled_image)
    plt.imshow(paletted_image)
    plt.show()
