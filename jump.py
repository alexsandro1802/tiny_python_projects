#!/usr/bin/env python3

"""
Author : supreme <supreme@localhost>
Date   : 2023-02-23
Purpose: Rock the Casbah
"""

import argparse

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
              '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

    # Method 5: str.translate
    print(args.text.translate(str.maketrans(jumper)))


# --------------------------------------------------
if __name__ == '__main__':
    main()





#--------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------
#import argparse

# def get_args():
#     """Get command-line arguments"""

#     parser = argparse.ArgumentParser(
#         description='Rock the Casbah',
#         formatter_class=argparse.ArgumentDefaultsHelpFormatter)

#     parser.add_argument('positional',
#                         metavar='str',
#                         help='A positional argument')

#     parser.add_argument('-a',
#                         '--arg',
#                         help='A named string argument',
#                         metavar='str',
#                         type=str,
#                         default='')

#     parser.add_argument('-i',
#                         '--int',
#                         help='A named integer argument',
#                         metavar='int',
#                         type=int,
#                         default=0)

#     parser.add_argument('-f',
#                         '--file',
#                         help='A readable file',
#                         metavar='FILE',
#                         type=argparse.FileType('rt'),
#                         default=None)

#     parser.add_argument('-o',
#                         '--on',
#                         help='A boolean flag',
#                         action='store_true')

#     return parser.parse_args()


# # --------------------------------------------------
# def main():
#     """Make a jazz noise here"""
#    args = get_args()
    # jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
    #           '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

    # # Method 5: str.translate
    # print(args.text.translate(str.maketrans(jumper)))


#     args = get_args()
#     str_arg = args.arg
#     int_arg = args.int
#     file_arg = args.file
#     flag_arg = args.on
#     pos_arg = args.positional

#     print(f'str_arg = "{str_arg}"')
#     print(f'int_arg = "{int_arg}"')
#     print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
#     print(f'flag_arg = "{flag_arg}"')
#     print(f'positional = "{pos_arg}"')


# # --------------------------------------------------
# if __name__ == '__main__':
#     main()
