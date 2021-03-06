import os
import glob
import argparse
import extrae_letras_toolbox as tb


def get_image_files(path):
    return glob.glob(os.path.join(path, "*"))


def setup_args(parser):
    parser.add_argument(
        '-i',
        dest = 'input_dir',
        default = "../input/captchas_dataset/test_data/",
        type = str,
        help = 'directorio donde estan guardados los captchas.')

    parser.add_argument(
        '-o',
        dest = 'output_dir',
        default = "../input/letter_dataset/training/",
        type = str,
        help = 'directorio donde se guardan las letras extraidas de los captchas.')

    return parser.parse_args()


def main():
    args = setup_args(argparse.ArgumentParser())

    captcha_image_folder = args.input_dir
    letter_destination_folder = args.output_dir

    captcha_image_files = get_image_files(captcha_image_folder)

    for (i, captcha_image_filename) in enumerate(captcha_image_files):
        print(i, captcha_image_filename)

        image = tb.get_image(captcha_image_filename)
        image_bnw = tb.image_to_bnw(image.copy())
        dilation_image = tb.apply_dilation(image_bnw)
        erosion_image = tb.apply_erosion(dilation_image)
        denoise_image = tb.apply_denoise(erosion_image)
        thresholded_image = tb.apply_thresholding(denoise_image)

        contours = tb.get_contours(thresholded_image)

        # Una región es el rectángulo que envuelve cada letra
        regions = tb.get_regions(contours)

        # Estamos tratando captchas de 4 letras.
        # Si recibimos menos de 4 regiones seguramente se han juntado varias letras en una sola región que hay que dividir.
        regions = tb.adjust_regions_by_number(regions, 4)

        # Guardo cada región como imagen
        for region, letter in zip(tb.get_sorted_regions_by_coord_x(regions), tb.get_captcha_text_from_filename(captcha_image_filename)):
            x, y, w, h = region
            
            #letter_image = image[y:y + h, x:x + w]
            letter_image = thresholded_image[y:y + h, x:x + w]

            tb.save_letter_image(letter_image, letter, output_folder = letter_destination_folder)

            print(f"Imagen para la letra {letter} guardada.")


if __name__ == '__main__':
    main()
