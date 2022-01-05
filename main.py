from Wingman.TClient import TClient
import argparse


def main(args):
    PIN = args['PIN']
    TClient(PIN)


if __name__ == '__main__':
    all_args = argparse.ArgumentParser()
    all_args.add_argument("-PIN", "--PIN", required=True, help="Your Phone's PIN Code")
    args = vars(all_args.parse_args())
    main(args)
