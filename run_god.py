from god import Transform
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import tqdm
files = None

for i in os.walk('./images/resized/'):
    files = i[-1]
    break

im_res = {}
for file in files:
    img = cv2.imread(f"./images/resized/{file}", cv2.IMREAD_GRAYSCALE).astype(np.bool).astype(np.uint8)
    img[img == 1] = 255
    im_res[file] = img


selection = ["5494.png", "5509.png", "5490.png"]
thetas = [np.arange(0, 180, i) for i in [1, 10, 30]]
'''
for theta in thetas:
    a = 4  # scale
    b = 4  # columns
    fig, axs = plt.subplots(len(selection), b)
    fig.set_size_inches(b * a, len(selection) * a)
    for i, image in enumerate(selection):
        transform = Transform(im_res[image])
        transform.sinogram(theta=theta, circle=False)
        transform.reconstruct()

        # plotting
        axs.flatten()[0].set_title("Original")
        axs[i][0].imshow(transform.image, cmap=plt.cm.Greys_r)

        axs.flatten()[1].set_title("Radon transform\n(Sinogram)")
        axs[i][1].set_xlabel("Projection angle (deg)")
        axs[i][1].set_ylabel("Projection position (pixels)")
        axs[i][1].imshow(transform._sinogram, cmap=plt.cm.Greys_r,
                         extent=(0, 180, 0, transform._sinogram.shape[0]), aspect='auto')

        axs[i][2].set_title("Reconstruction\nFiltered back projection")
        axs[i][2].imshow(transform._reconstructed, cmap=plt.cm.Greys_r)

        axs[i][3].set_title("Reconstruction error\nFiltered back projection")
        axs[i][3].imshow(transform._reconstructed - transform.image, cmap=plt.cm.Greys_r)

        # save data
        fig.tight_layout()
        path = "results/plots/"
        name = f"FBP_reconstruction_step_{theta[1]}"
        fig.savefig(f"{path}{name}.pdf", bbox_inches="tight")
        transform.log_to_file(f"{path}{name}.txt")

for m in [0, 1000, 10000, 20000, 25000, 50000]:
    for v in [1, 5, 10, 25, 100, 500, 1000, 10000]:
        a = 4  # scale
        b = 4  # columns
        fig, axs = plt.subplots(len(selection), b)
        fig.set_size_inches(b * a, len(selection) * a)
        for i, image in enumerate(selection):
            transform = Transform(im_res[image])
            transform.sinogram(theta=thetas[0], circle=False)
            transform.gauss(v, m)
            transform.reconstruct()

            axs.flatten()[0].set_title("Original")
            axs[i][0].imshow(transform.image, cmap=plt.cm.Greys_r)

            axs.flatten()[1].set_title("Radon transform\n(Sinogram)\nWith Gauss noise")
            axs[i][1].set_xlabel("Projection angle (deg)")
            axs[i][1].set_ylabel("Projection position (pixels)")
            axs[i][1].imshow(transform._sinogram, cmap=plt.cm.Greys_r,
                             extent=(0, 180, 0, transform._sinogram.shape[0]), aspect='auto')

            axs[i][2].set_title("Reconstruction\nFiltered back projection")
            axs[i][2].imshow(transform._reconstructed, cmap=plt.cm.Greys_r)

            axs[i][3].set_title("Reconstruction error\nFiltered back projection")
            axs[i][3].imshow(transform._reconstructed - transform.image, cmap=plt.cm.Greys_r)

            # save data
            fig.tight_layout()

            # save data
            path = "results/plots/"
            name = f"FBP_gauss-mean-{m}-var-{v}_reconstruction_step_{thetas[0][1]}"
            fig.savefig(f"{path}{name}.pdf", bbox_inches="tight")
            transform.log_to_file_gauss(f"{path}{name}.txt", sigma=v, mu=m)

for n in [0.005, 0.01, 0.02, 0.1, 0.5]:
    a = 4  # scale
    b = 4  # columns
    fig, axs = plt.subplots(len(selection), b)
    fig.set_size_inches(b * a, len(selection) * a)
    for i, image in enumerate(selection):
        transform = Transform(im_res[image])
        transform.sinogram(theta=thetas[0], circle=False)
        transform.salt_papper(n)
        transform.reconstruct()

        axs.flatten()[0].set_title("Original")
        axs[i][0].imshow(transform.image, cmap=plt.cm.Greys_r)

        axs.flatten()[1].set_title("Radon transform\n(Sinogram)\nWith Salt-papper noise")
        axs[i][1].set_xlabel("Projection angle (deg)")
        axs[i][1].set_ylabel("Projection position (pixels)")
        axs[i][1].imshow(transform._sinogram, cmap=plt.cm.Greys_r,
                         extent=(0, 180, 0, transform._sinogram.shape[0]), aspect='auto')

        axs[i][2].set_title("Reconstruction\nFiltered back projection")
        axs[i][2].imshow(transform._reconstructed, cmap=plt.cm.Greys_r)

        axs[i][3].set_title("Reconstruction error\nFiltered back projection")
        axs[i][3].imshow(transform._reconstructed - transform.image, cmap=plt.cm.Greys_r)

        # save data
        path = "results/plots/"
        name = f"FBP_sap-{n}_reconstruction_step_{thetas[0][1]}"
        fig.savefig(f"{path}{name}.pdf", bbox_inches="tight")
        transform.log_to_file(f"{path}{name}.txt")

a = 4  # scale
b = 4  # columns
fig, axs = plt.subplots(len(selection), b)
fig.set_size_inches(b * a, len(selection) * a)
for i, image in enumerate(selection):
    transform = Transform(im_res[image])
    transform.sinogram(theta=thetas[0], circle=False)
    transform.speckle()
    transform.reconstruct()

    axs.flatten()[0].set_title("Original")
    axs[i][0].imshow(transform.image, cmap=plt.cm.Greys_r)

    axs.flatten()[1].set_title("Radon transform\n(Sinogram)\nWith Speckle noise")
    axs[i][1].set_xlabel("Projection angle (deg)")
    axs[i][1].set_ylabel("Projection position (pixels)")
    axs[i][1].imshow(transform._sinogram, cmap=plt.cm.Greys_r,
                     extent=(0, 180, 0, transform._sinogram.shape[0]), aspect='auto')

    axs[i][2].set_title("Reconstruction\nFiltered back projection")
    axs[i][2].imshow(transform._reconstructed, cmap=plt.cm.Greys_r)

    axs[i][3].set_title("Reconstruction error\nFiltered back projection")
    axs[i][3].imshow(transform._reconstructed - transform.image, cmap=plt.cm.Greys_r)

    # save data
    path = "results/plots/"
    name = f"FBP_speckle_reconstruction_step_{thetas[0][1]}"
    fig.savefig(f"{path}{name}.pdf", bbox_inches="tight")
    transform.log_to_file(f"{path}{name}.txt")

a = 4  # scale
b = 4  # columns
fig, axs = plt.subplots(len(selection), b)
fig.set_size_inches(b * a, len(selection) * a)
for i, image in enumerate(selection):
    transform = Transform(im_res[image])
    transform.sinogram(theta=thetas[0], circle=False)
    transform.poisson()
    transform.reconstruct()

    axs.flatten()[0].set_title("Original")
    axs[i][0].imshow(transform.image, cmap=plt.cm.Greys_r)

    axs.flatten()[1].set_title("Radon transform\n(Sinogram)\nWith Poisson noise")
    axs[i][1].set_xlabel("Projection angle (deg)")
    axs[i][1].set_ylabel("Projection position (pixels)")
    axs[i][1].imshow(transform._sinogram, cmap=plt.cm.Greys_r,
                     extent=(0, 180, 0, transform._sinogram.shape[0]), aspect='auto')

    axs[i][2].set_title("Reconstruction\nFiltered back projection")
    axs[i][2].imshow(transform._reconstructed, cmap=plt.cm.Greys_r)

    axs[i][3].set_title("Reconstruction error\nFiltered back projection")
    axs[i][3].imshow(transform._reconstructed - transform.image, cmap=plt.cm.Greys_r)

    # save data
    path = "results/plots/"
    name = f"FBP_poisson_reconstruction_step_{thetas[0][1]}"
    fig.savefig(f"{path}{name}.pdf", bbox_inches="tight")
    transform.log_to_file(f"{path}{name}.txt")

'''

for theta in thetas:
    a = 4  # scale
    b = 6  # columns
    fig, axs = plt.subplots(len(selection), b)
    fig.set_size_inches(b * a, len(selection) * a)
    for i, image in enumerate(selection):
        transform = Transform(im_res[image], verbose=False)
        transform.sinogram(theta=theta, circle=True)

        axs.flatten()[0].set_title("Original")
        axs[i][0].imshow(transform.image, cmap=plt.cm.Greys_r)

        axs.flatten()[1].set_title("Radon transform\n(Sinogram)")
        axs[i][1].set_xlabel("Projection angle (deg)")
        axs[i][1].set_ylabel("Projection position (pixels)")
        axs[i][1].imshow(transform._sinogram, cmap=plt.cm.Greys_r,
                         extent=(0, 180, 0, transform._sinogram.shape[0]), aspect='auto')

        for _ in tqdm.trange(100):
            transform.reconstruct_sart()

            if _ == 0:
                axs[i][2].set_title("Reconstruction\nSART iter 1")
                axs[i][2].imshow(transform._reconstructed, cmap=plt.cm.Greys_r)
            elif _ == 19:
                axs[i][3].set_title("Reconstruction\nSART iter 20")
                axs[i][3].imshow(transform._reconstructed, cmap=plt.cm.Greys_r)
            elif _ == 99:
                axs[i][4].set_title("Reconstruction\nSART iter 100")
                axs[i][4].imshow(transform._reconstructed, cmap=plt.cm.Greys_r)

        axs[i][5].set_title("Reconstruction error\nSART")
        axs[i][5].imshow(transform._reconstructed - transform.image, cmap=plt.cm.Greys_r)

        # save data
        path = "results/plots/"
        name = f"SART_reconstruction_step_{theta[1]}"
        fig.savefig(f"{path}{name}.pdf", bbox_inches="tight")
        transform.log_to_file(f"{path}{name}.txt")

files = None

for i in os.walk('./images/cropped/'):
    files = i[-1]
    break

im_res = {}
for file in files:
    img = cv2.imread(f"./images/cropped/{file}", cv2.IMREAD_GRAYSCALE).astype(np.bool).astype(np.uint8)
    img[img == 1] = 255
    im_res[file] = img




for theta in thetas:
    a = 4  # scale
    b = 6  # columns
    fig, axs = plt.subplots(len(selection), b)
    fig.set_size_inches(b * a, len(selection) * a)
    for i, image in enumerate(selection):
        transform = Transform(im_res[image], verbose=False)
        transform.sinogram(theta=theta, circle=True)
        axs.flatten()[0].set_title("Original")
        axs[i][0].imshow(transform.image, cmap=plt.cm.Greys_r)

        axs.flatten()[1].set_title("Radon transform\n(Sinogram)")
        axs[i][1].set_xlabel("Projection angle (deg)")
        axs[i][1].set_ylabel("Projection position (pixels)")
        axs[i][1].imshow(transform._sinogram, cmap=plt.cm.Greys_r,
                         extent=(0, 180, 0, transform._sinogram.shape[0]), aspect='auto')

        for _ in tqdm.trange(100):
            transform.reconstruct_sart()

            if _ == 0:
                axs[i][2].set_title("Reconstruction\nSART iter 1")
                axs[i][2].imshow(transform._reconstructed, cmap=plt.cm.Greys_r)
            elif _ == 19:
                axs[i][3].set_title("Reconstruction\nSART iter 20")
                axs[i][3].imshow(transform._reconstructed, cmap=plt.cm.Greys_r)
            elif _ == 99:
                axs[i][4].set_title("Reconstruction\nSART iter 100")
                axs[i][4].imshow(transform._reconstructed, cmap=plt.cm.Greys_r)

        axs[i][5].set_title("Reconstruction error\nSART")
        axs[i][5].imshow(transform._reconstructed - transform.image, cmap=plt.cm.Greys_r)

        # save data
        path = "results/plots/"
        name = f"SART_cropped_reconstruction_step_{theta[1]}"
        fig.savefig(f"{path}{name}.pdf", bbox_inches="tight")
        transform.log_to_file(f"{path}{name}.txt")


for theta in thetas:
    a = 4  # scale
    b = 4  # columns
    fig, axs = plt.subplots(len(selection), b)
    fig.set_size_inches(b * a, len(selection) * a)
    for i, image in enumerate(selection):
        transform = Transform(im_res[image])
        transform.sinogram(theta=theta, circle=False)
        transform.reconstruct()

        # plotting
        axs.flatten()[0].set_title("Original")
        axs[i][0].imshow(transform.image, cmap=plt.cm.Greys_r)

        axs.flatten()[1].set_title("Radon transform\n(Sinogram)")
        axs[i][1].set_xlabel("Projection angle (deg)")
        axs[i][1].set_ylabel("Projection position (pixels)")
        axs[i][1].imshow(transform._sinogram, cmap=plt.cm.Greys_r,
                         extent=(0, 180, 0, transform._sinogram.shape[0]), aspect='auto')

        axs[i][2].set_title("Reconstruction\nFiltered back projection")
        axs[i][2].imshow(transform._reconstructed, cmap=plt.cm.Greys_r)

        axs[i][3].set_title("Reconstruction error\nFiltered back projection")
        axs[i][3].imshow(transform._reconstructed - transform.image, cmap=plt.cm.Greys_r)

        # save data
        fig.tight_layout()
        path = "results/plots/"
        name = f"FBP_cropped_reconstruction_step_{theta[1]}"
        fig.savefig(f"{path}{name}.pdf", bbox_inches="tight")
        transform.log_to_file(f"{path}{name}.txt")