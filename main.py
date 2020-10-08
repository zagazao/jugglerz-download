import argparse
import os
import sys

import requests

BASE_URL = 'http://jugglerz.de/shows/'


def read_files(path):
    try:
        with open(path, 'r') as file_list:
            content = [file.replace('\n', '').replace(' ', '%20') for file in file_list.readlines()]
            return content
    except FileNotFoundError as e:
        print('File {} does not exist.'.format(path))
        sys.exit(1)


def save_content_to_file(response, path):
    if os.path.exists(path):
        print('Output already exists..')
        
    try:
        with open(path, 'wb') as f:
            f.write(response.content)
    except KeyboardInterrupt as e:
        # Cleanup possible unfinished result writeback
        print('Interrupted...')
        if os.path.exists(path):
            os.remove(path)
        sys.exit(0)


# Catch keyboard error and finish current download?

def download_stuff(args):
    stuff_to_download = read_files(args.input)
    # Assert output exists

    if not os.path.exists(args.output):
        print('Creating output directory - {}'.format(args.output))
        os.makedirs(args.output)

    for file in stuff_to_download:
        out_file = os.path.join(args.output, file)
        # Skip download if target already exists
        if os.path.exists(out_file):
            continue

        print('Downloading {}.'.format(file))

        try:
            response = requests.get(BASE_URL + file)
            if response.status_code != 200:
                print('Not okay...')
                continue
        except Exception as e:
            # If an error occured during download we just continue with next item.
            # TODO: We could check for timeouts (if there are any?)
            print('Error during download of file {}.'.format(file))
            continue

        save_content_to_file(response, out_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Jugglerz.de radioshow downloader')
    parser.add_argument('-i', '--input', default='data.txt', help='Path to list with all files.')
    parser.add_argument('-o', '--output', default='jugglerz')

    args = parser.parse_args()

    download_stuff(args)
