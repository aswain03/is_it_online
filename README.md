# is_it_online

A Python website connectivity checker

## Description

is_it_online is a Python script that checks the connectivity of websites. It can be used to monitor the availability of websites and alert the user if any of them are offline.

## Features

- Checks the connectivity of multiple websites
- Sends alerts if any website is offline
- Customizable settings for monitoring interval and alert method

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/aswain03/is_it_online.git
    ```
2. Install requirements: 
    ```shell
    pip install requirements.txt
    ```
3. Run:
    ```shell
    python is_it_online [-h] [-u <URLs> [URLs ...]] [-f <FILE>] [-a]
    ```

## Options:

 - -h, --help: Shows a list of all available options.
 - -u URLs [URLs ...], --urls URLs [URLs ...]: Enter one or more URLs to check.
 - -f FILE, --input-file FILE: Read URLs from a file (one URL per line).
 - -a, --asynchronous: Use asynchronous requests to check URLs.