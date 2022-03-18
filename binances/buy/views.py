from textwrap import indent
from django.http import HttpResponse
import asyncio
import json
from binance.client import Client
from binance.exceptions import BinanceAPIException
from binance import AsyncClient
# import config

api_key='B75Fr12BqrqCurNtEvVlGAL2hTPMOh4veKSVqKrM50Voxm5DtZD9c7kuPr6mCcjt'
api_secret='HzML11zTS6GS6dHkf03Hec4LW3rwm8eSD5qlxE5yna8TadsxGB9YH1G28BN3pDF6'

# def index(request):
    
#     # # client = Client(config.apiKey, config.apiSecurity)
    

#     # client = Client(apiKey, apiSecurity )
#     # # depth = client.get_order_book(symbol='BNBBTC')
#     # # order = client.create_test_order(
#     # # symbol='BNBBTC',
#     # # side=Client.SIDE_BUY,
#     # # type=Client.ORDER_TYPE_MARKET,
#     # # quantity=1)

#     # prices = client.get_all_tickers()

#     # print('----', prices)
#     async def main():
#         quantity = '0.000001'
#         client = await AsyncClient.create(api_key=api_key, api_secret=api_secret, testnet=True)
#         print('start ****')
#         try:
#             market_res = await client.order_market_sell(symbol='BTCUSDT', quantity=quantity)
#         except BinanceAPIException as e:
#             print(e)
#         else:
#             print(json.dumps(market_res, indent=2))
#         await client.close_connection()
    
#     if __name__ == "__main__":
    
#         loop = asyncio.get_event_loop()
#         loop.run_until_complete(main())
#     return HttpResponse("Hello, world. You're at the polls index.")
# @staticmethod
async def main(self):
    
        client = await AsyncClient.create()
        symbol_info = await client.get_symbol_info('BTCUSDT')
    
        # print(json.dumps(symbol_info, indent=2))
        quantity = '0.001'
        client = await AsyncClient.create(api_key=api_key, api_secret=api_secret, testnet=True)

        try:
            market_res = await client.order_market_sell(symbol='BTCUSDT', quantity=quantity)
        except BinanceAPIException as e:
            print('__Error___',e)
        else:
            print('__Res___ : ',json.dumps(market_res, indent=2))

        await client.close_connection()
    
if __name__ == "__main__":
    
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())