#!/usr/bin/env python3
# coding: utf-8

import argparse
import prune


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # vg prune
    parser_prune = subparsers.add_parser(
        'prune', help='calculate a metric that vg prune uses')
    parser_prune.add_argument('-k', '--kmer-length', default=24,
                            type=int, help='kmer length used for pruning (24)')
    parser_prune.add_argument('-e', '--edge-max', default=3, type=int,
                              help='remove the edges on kmers making > N edge choices (3)')
    parser_prune.add_argument('gfa', help='GFA file')
    parser_prune.set_defaults(handler=command_prune)

    args = parser.parse_args()
    
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()


def command_prune(args):
    prune.prune_main(args)


if __name__ == "__main__":
    main()
