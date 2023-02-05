# !/usr/bin/env python3

"""
Author: Alexandro <Alexandros-MacAir>
Date: 2023-02-02
Purpose: Say Hellog
"""
import argparse
# C = 30


# -------------------------------------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="hello project",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "-n",
        "--name",
        help="A named string argument",
        metavar="name",
        type=str,
        default="World",)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """say hello"""

    args = get_args()
    word = args.name
    print(f"Hello, {word}!")


# --------------------------------------------------
if __name__ == '__main__':
    # A = 10
    # B = 20
    # print(A+B)
    main()
