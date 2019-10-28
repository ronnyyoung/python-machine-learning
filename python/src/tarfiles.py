#!/usr/bin/env python3

import os
import tarfile
import argparse
from multiprocessing import Pool


def make_targz(output_filename, source_dir):
  print("packing: %s ...", output_filename)
  with tarfile.open(output_filename, "w:gz") as tar:
    tar.add(source_dir, arcname=os.path.basename(source_dir))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='imagenet tar-pack tool')
    parser.add_argument('--num_threads', metavar='int', default=4,
                        type=int, help='number of thread for packing the data')
    parser.add_argument('--imagenet_root', metavar='str',
                        type=str, help='root directory of the imagenet images')
    parser.add_argument('--dir_list', metavar='str', type=str,
                        help='root directory of the imagenet images')
    parser.add_argument('--dst_dir', metavar='str', type=str,
                        help='destination position to save the tgz files')
    args = parser.parse_args()

    pack_pools = Pool(args.num_threads)

    with open(args.dir_list, 'r') as f:
        dirs = f.readlines()
    for dir_elem in dirs:
        source_dir = os.path.join(args.imagenet_root, dir_elem)
        output_filename = os.path.join(args.imagenet_root, dir_elem, ".tgz")
        pack_pools.apply_async(make_targz, args=(output_filename, source_dir))
    pack_pools.close()
    pack_pools.join()
    print('Done!')