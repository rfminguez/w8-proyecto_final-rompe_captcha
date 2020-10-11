from mi_captcha import Captcha
import argparse
import shutil
import os


def dir_exists(dir):
    return os.path.exists(dir)


def delete_directory(dir):
    shutil.rmtree(dir)


def create_directory(dir):
    os.makedirs(dir)


def setup_args(parser):
    parser.add_argument(
        '-n',
        dest = 'n_captchas',
        default = 1,
        type = int,
        help = 'numero de captchas que se van a generar.')

    parser.add_argument(
        '-d',
        dest = 'output_dir',
        default = "../input/captchas_dataset/",
        type = str,
        help = 'directorio donde se guardan los captchas.')

    return parser.parse_args()


def main():
    args = setup_args(argparse.ArgumentParser())

    dir = args.output_dir
    n_captchas = args.n_captchas

    if dir_exists(dir):
        borrar_dir = input(f"El directorio {dir} ya existe. Lo borro? [Y/n]: ")
        if borrar_dir in "Yy":
            print(f"Borrando el directorio {dir}")
            delete_directory(dir)

    if not dir_exists(dir):
        print(f"Creando el directorio {dir}")
        create_directory(dir)

    for i in range(n_captchas):
        print(f"Generando imagen {i + 1}", end='\r')
        captcha = Captcha(output_dir = dir)
        captcha.save()

    print(f"Generados {n_captchas} captchas en el directorio {dir}")


if __name__ == '__main__':
    main()
