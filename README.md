# Retask

## Why Retask
- Wanted a simple way to add recurring tasks to my daily markdown file in Obsidian
- Didn't want to use a plugin that does several things or required me to change how I organize notes

## About
- Written with Python 3.11.5, but likely works with other recent versions
- No dependencies and only requires the Standard Library
- Works on macOS, probably Linux, and no idea on Windows

## Disclaimer
- The tool shouldn't be destructive and will only append if it finds a daily file.
- Please make sure this works the way you want it to with something non-critical before you expand its use. I don't want anyone missing their daily medication or something important. This is a hobby script, please use at your own risk.

## Setup
- Clone the repo: `git clone git@github.com:dansahagian/retask.git`
- Creat a config.py: `cp template_config.py config.py`
- Update `PATH_TO_DAILY_DIR` in config.py
- Update `TASKS` in config.py
- Run `python3 main.py`

## Task Configuration
- Daily (d) and Weekly (w) tasks are the best options.
- Monthly works (ex: Every 20th of the month), but stick to a number that's in every month (<= 28)
- It won't handle if you pick the 29th - 31st of a month and that doesn't exist in a month.
- Examples:
    - `("2023-09-16", 52, "w", "Do something next year on this Saturday")`
    - `("2023-09-16", 1, "d", "Do something every day")`
    - `("2023-09-20", 0, "m", "Do something ont he 20th every month")`