# Trading Halt Alerts w/ Telegram Delivery

[NasdaqTrader](https://www.nasdaqtrader.com/trader.aspx?id=TradeHalts) provides an RSS feed that outputs any new and active trading halts occurring across both Nasdaq and other U.S. exchanges.

There are a lot of reasons for why trading of a stock should be halted. This can be due to operational activity, or due to regulatory concern. The NasdaqTrader website offers a [comprehensive list of all halt codes](https://www.nasdaqtrader.com/Trader.aspx?id=TradeHaltCodes) and their meanings.  

### Files

Here are the files that are included in the repository.
| file | desc. |
|--|--|
| engine .py | Contains the main script responsible for parsing incoming RSS items, and routes them through Telegram |
| telegram_messenger .py | Small module for sending messages to a Telegram user or group|
| logs .csv | File where all incoming trading halts are logged.|
| markets .csv| File where you can store a list of markets that you want to filter your halt results by. |



### Requirements

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### Installation

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
