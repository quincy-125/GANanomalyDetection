import argparse
import logging
import sys


from dataset_tool import create_from_images

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input_dir",
                        dest='input_dir',
                        required=True,
                        help="Folder containing png or jpg images")

    parser.add_argument("-o", "--output_dir",
                        dest='output_dir',
                        default='.',
                        help="Folder to save the tfrecords into")

    parser.add_argument("-s", "--shuffle",
                        dest='shuffle',
                        action='store_false',
                        help="Whether or not to shuffle images before making tfrecord [True]")

    parser.add_argument("-p", "--prefix",
                        dest='prefix',
                        default='custom',
                        help="First part of the tfrecord name")

    parser.add_argument("-V", "--verbose",
                        dest="logLevel",
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        default="INFO",
                        help="Set the logging level")

    args = parser.parse_args()
    logging.basicConfig(stream=sys.stderr, level=args.logLevel,
                        format='%(name)s (%(levelname)s): %(message)s')

    logger = logging.getLogger(__name__)
    logger.setLevel(args.logLevel)

    create_from_images(tfrecord_dir=args.output_dir, image_dir=args.input_dir, shuffle=args.shuffle, prefix=args.prefix)


if __name__ == "__main__":
    main()