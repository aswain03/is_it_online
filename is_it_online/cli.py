import argparse


def read_args():
    parser = argparse.ArgumentParser(
        prog="is_it_online", description="Check if a website is online"
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Enter one or more URLs to check.",
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="Read URLs from a file (one URL per line).",
    )
    parser.add_argument(
        "-a",
        "--asynchronous",
        action="store_true",
        help="Use asynchronous requests to check URLs.",
    )

    return parser.parse_args()


def check_result(result, url, err=""):
    if result:
        print(f"👍: {url} is online.")
    else:
        print(f"👎: {url} is offline: \n Error: {err}")
