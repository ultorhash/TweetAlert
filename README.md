# Tweet Alert

## Description 
A script that listens to a tweeting account to notify the user of their latest tweets. The main purpose of its creation was to monitor accounts associated with Web3 technologies. It's dedicated for Windows users due to use of winotify library as notify popups.
## Configuration
File accounts.txt contains a sample configuration for the NASA account. In order to configure your accounts you have to edit file. You will see five sections in it:
- [`SYMBOL`] Account short name.
- [`NAME`] Twitter account after "/" in twitter URL address.
- [`LIFESPAN`] Determines time tweet publication. If the time difference between current time and the specified in the configuration is greater, then the tweet will not be considered.
- [`INTERVAL`] Analyzes account for new tweets every specified period of time. Allowed time units are: sec, min and hrs. For example 5min, 35sec, 1hrs.
- [`KEYWORDS`] You will be notified of only those tweets that contain the given words in the content. Specify keywords in lower case format after the comma or put asterisk(*) to disable filtering.

[`IMPORTANT`]

Each account settings must be separated by `|` sign. Below you can find and example setup pattern for the account. For multiple account add them one by one in new lines. Also remember to leave empty line between column names and first account on the list.

[`FULL CONFIGRATION LINE IN FILE`]

Your_symbol | Account_name | 3min | 1min | keyword1,keyword2,keyword3

## After setup
When you are ready with configured account, simply run `main.py` file. Included logger will be showing scrapping process of current account.
