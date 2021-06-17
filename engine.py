import feedparser
from datetime import datetime
import telegram_messenger as TM
import markets
import csv
import pandas as pd
from time import sleep

test = True #if True will inject fake data to simulate a feed item.

broadcast = True #if True will route the message through Telegram, otherwise just prints

symbol_filter = False #if False will disregard your symbol list and output all events

markets = pd.read_csv("markets.csv")["symbols"].to_list() #a list of tickers to filter down your results


def log(do):
	"""
	This function logs events in a CSV. This is important to ensure that repeat
	signals don't get blasted from the feed constantly.
	"""
    fields = [do["symbol"],
              do["name"],
              do["reason"],
              do["timestamp"]]
    f = open(r'logs.csv', 'a', newline='')
    writer = csv.writer(f)
    writer.writerow(fields)
    f.close()
    return None

logs_of_fire = []
infinity = list(range(0,1000))

nasdaq_src = 'http://www.nasdaqtrader.com/rss.aspx?feed=tradehalts'
bot = "the_username_of_your_bot"

for x in infinity:
    now = datetime.now()
    current_minute = datetime(now.year, now.month,now.day,now.hour, now.minute).strftime("%m/%d/%Y, %H:%M")
    
    if current_minute not in logs_of_fire:
        print("Running - {}".format(current_minute))
        logs_of_fire.append(current_minute)
        log_reader =  pd.read_csv("logs.csv").to_dict(orient = 'records')
        halts = []
        
        morpher_markets = parse_markets()
        items = feedparser.parse(nasdaq_src).entries
        
        for i in items:
            
            data = {"symbol" : i["title"],
                    "name" : i["ndaq_issuename"],
                    "reason" : i["ndaq_reasoncode"],
                    "timestamp" : "{} {}".format(
                                    i["ndaq_haltdate"],    
                                    i["ndaq_halttime"]
                                                )
                   }
            timestamp =  datetime.strptime(data["timestamp"], "%m/%d/%Y %H:%M:%S")
            data.update({"timestamp" : timestamp})
            halts.append(data)
        
        
        if test == True:
            fake_data = {
                "symbol" : "HNRD",
                "name" : "100 Eyes Holding",
                "reason" : "This is a test",
                "timestamp" : datetime(2021, 6, 9, 9, 41, 29)
            }
            halts.append(fake_data)
            morpher_markets.append("HNRD")
        
        for data in halts:
            log_reader =  pd.read_csv("logs.csv").to_dict(orient = 'records')
            
            if symbol_filter == True:
                #Is the symbol within your list?
                if data["symbol"] in morpher_markets:
                    permission_to_parse = True

                else:
                    permission_to_parse = False

            else:
                permission_to_parse = True

            if permission_to_parse == True:

                #if log file is new then we skip
                if len(log_reader) > 0:
                    #checking against previous halts
                    for i in log_reader:
                        #print(i)
                        ctime = datetime.strptime(i["timestamp"], "%Y-%m-%d %H:%M:%S")
                        if (i["symbol"] == data["symbol"]) and (ctime == data["timestamp"]):
                            reported = True
                            break
                        
                        else:
                            reported = False
                else:
                    print("The Log does not exist")
                    reported = False

                if reported == False:
                	#Change the messaging to whatever suits your needs
                    message = '''
                    Trading Halt: ${}
                    ({})
                    Reason: {}
                    TS: {}
        
                    Code Disambiguation: https://www.nasdaqtrader.com/Trader.aspx?id=tradehaltcodes
                    '''.format(data["symbol"],
                              data["name"],
                              data["reason"],
                              data["timestamp"].strftime("%m/%d/%Y, %H:%M:%S"))
        
                    TM.bot_send("Hear ye ! Hear ye !", bot,broadcast)
                    TM.bot_send(message, bot,broadcast)
                    log(data)
    else:
        print("Cooldown - {}".format(current_minute))
        sleep(56) # NASDAQ asks that you don't query more than once a minute.

quit() #shutdown after having run through the entire script