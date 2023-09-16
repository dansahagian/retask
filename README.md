# Retask

I use Obsidian and wanted a simple way to add my recurring tasks to my daily file. There is likely a plugin for this, but it will inevitably do more than I need, and I'm trying to keep my plugins to a minimum. This isn't something I would go add a one-off task to as it's cumbersome and easier to add to my calendar. I'm going to use this for scheduled recurring tasks that I need to do personally or around the house.

It doesn't have any dependencies other than the standard library and was written with Python 3.11.5. It probably works with other recent versions, but I didn't test it.

## Disclaimer
- Please make sure this works the way you want it to with something non-critical before you expand its use. I don't want anyone missing their daily medication or something important. This is a hobby script, please use at your own risk.

## Setup
- Clone the repo: `git clone git@github.com:dansahagian/retask.git`
- Creat a config.py: `cp template_config.py config.py`
- Update `PATH_TO_DAILY_DIR` in config.py
- Update `TODOS` in config.py
- Run `python3 main.py`

## Task Configuration
- Daily (d) and Weekly (w) tasks are the best options.
- Monthly works (ex: Every 20th of the month), but stick to a number that's in every month (<= 28)
- It won't handle if you pick the 29th - 31st of a month and that doesn't exist in a month.
- Examples:
    - `("2023-09-16", 52, "w", "Do something next year on this Saturday")`
    - `("2023-09-16", 1, "d", "Do something every day")`
    - `("2023-09-20", 0, "m", "Do something ont he 20th every month")`