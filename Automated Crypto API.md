```python
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'20',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'Enter Your Crypto API Key',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  
```

    {'status': {'timestamp': '2022-09-23T15:16:59.591Z', 'error_code': 0, 'error_message': None, 'elapsed': 21, 'credit_count': 1, 'notice': None, 'total_count': 9447}, 'data': [{'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'num_market_pairs': 9748, 'date_added': '2013-04-28T00:00:00.000Z', 'tags': ['mineable', 'pow', 'sha-256', 'store-of-value', 'state-channel', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio', 'binance-labs-portfolio', 'blockchain-capital-portfolio', 'boostvc-portfolio', 'cms-holdings-portfolio', 'dcg-portfolio', 'dragonfly-capital-portfolio', 'electric-capital-portfolio', 'fabric-ventures-portfolio', 'framework-ventures-portfolio', 'galaxy-digital-portfolio', 'huobi-capital-portfolio', 'alameda-research-portfolio', 'a16z-portfolio', '1confirmation-portfolio', 'winklevoss-capital-portfolio', 'usv-portfolio', 'placeholder-ventures-portfolio', 'pantera-capital-portfolio', 'multicoin-capital-portfolio', 'paradigm-portfolio'], 'max_supply': 21000000, 'circulating_supply': 19158500, 'total_supply': 19158500, 'platform': None, 'cmc_rank': 1, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 18690.447223972424, 'volume_24h': 36977556124.69532, 'volume_change_24h': -31.6811, 'percent_change_1h': 0.09201389, 'percent_change_24h': -1.18364484, 'percent_change_7d': -4.96116898, 'percent_change_30d': -13.02576535, 'percent_change_60d': -14.44873654, 'percent_change_90d': -11.47350901, 'market_cap': 358080933140.4757, 'market_cap_dominance': 39.014, 'fully_diluted_market_cap': 392499391703.42, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'num_market_pairs': 6103, 'date_added': '2015-08-07T00:00:00.000Z', 'tags': ['pos', 'smart-contracts', 'ethereum-ecosystem', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio', 'binance-labs-portfolio', 'blockchain-capital-portfolio', 'boostvc-portfolio', 'cms-holdings-portfolio', 'dcg-portfolio', 'dragonfly-capital-portfolio', 'electric-capital-portfolio', 'fabric-ventures-portfolio', 'framework-ventures-portfolio', 'hashkey-capital-portfolio', 'kenetic-capital-portfolio', 'huobi-capital-portfolio', 'alameda-research-portfolio', 'a16z-portfolio', '1confirmation-portfolio', 'winklevoss-capital-portfolio', 'usv-portfolio', 'placeholder-ventures-portfolio', 'pantera-capital-portfolio', 'multicoin-capital-portfolio', 'paradigm-portfolio', 'injective-ecosystem'], 'max_supply': None, 'circulating_supply': 122492189.499, 'total_supply': 122492189.499, 'platform': None, 'cmc_rank': 2, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 1284.8094745587118, 'volume_24h': 18814771193.53058, 'volume_change_24h': -23.0881, 'percent_change_1h': 0.36289485, 'percent_change_24h': 1.43671821, 'percent_change_7d': -11.16953766, 'percent_change_30d': -22.23174765, 'percent_change_60d': -15.51892837, 'percent_change_90d': 7.65543095, 'market_cap': 157379125627.75635, 'market_cap_dominance': 17.1469, 'fully_diluted_market_cap': 157379125627.76, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 825, 'name': 'Tether', 'symbol': 'USDT', 'slug': 'tether', 'num_market_pairs': 40036, 'date_added': '2015-02-25T00:00:00.000Z', 'tags': ['payments', 'stablecoin', 'asset-backed-stablecoin', 'avalanche-ecosystem', 'solana-ecosystem', 'arbitrum-ecosytem', 'moonriver-ecosystem', 'injective-ecosystem', 'bnb-chain', 'usd-stablecoin'], 'max_supply': None, 'circulating_supply': 67954703168.01751, 'total_supply': 70155449908.74805, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0xdac17f958d2ee523a2206206994597c13d831ec7'}, 'cmc_rank': 3, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 0.9999714550712279, 'volume_24h': 54536112804.543205, 'volume_change_24h': -22.7203, 'percent_change_1h': -0.00037489, 'percent_change_24h': -0.0101332, 'percent_change_7d': 0.00054655, 'percent_change_30d': -0.00811799, 'percent_change_60d': -0.00834497, 'percent_change_90d': 0.04723331, 'market_cap': 67952763405.85585, 'market_cap_dominance': 7.4037, 'fully_diluted_market_cap': 70153447326.43, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 3408, 'name': 'USD Coin', 'symbol': 'USDC', 'slug': 'usd-coin', 'num_market_pairs': 6294, 'date_added': '2018-10-08T00:00:00.000Z', 'tags': ['medium-of-exchange', 'stablecoin', 'asset-backed-stablecoin', 'fantom-ecosystem', 'arbitrum-ecosytem', 'moonriver-ecosystem', 'bnb-chain', 'usd-stablecoin'], 'max_supply': None, 'circulating_supply': 49761335172.820656, 'total_supply': 49761335172.820656, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'}, 'cmc_rank': 4, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 0.9999797640385886, 'volume_24h': 5113201594.951205, 'volume_change_24h': -23.5646, 'percent_change_1h': 0.00116837, 'percent_change_24h': -0.00894559, 'percent_change_7d': -0.00406166, 'percent_change_30d': -0.00549112, 'percent_change_60d': 0.02782187, 'percent_change_90d': -0.02424359, 'market_cap': 49760328204.36232, 'market_cap_dominance': 5.4215, 'fully_diluted_market_cap': 49760328204.36, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 1839, 'name': 'BNB', 'symbol': 'BNB', 'slug': 'bnb', 'num_market_pairs': 1110, 'date_added': '2017-07-25T00:00:00.000Z', 'tags': ['marketplace', 'centralized-exchange', 'payments', 'smart-contracts', 'alameda-research-portfolio', 'multicoin-capital-portfolio', 'moonriver-ecosystem', 'bnb-chain'], 'max_supply': 200000000, 'circulating_supply': 161337261.09, 'total_supply': 161337261.09, 'platform': None, 'cmc_rank': 5, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 270.3722804454594, 'volume_24h': 881845025.4512974, 'volume_change_24h': -21.6284, 'percent_change_1h': -0.09524683, 'percent_change_24h': 0.93702344, 'percent_change_7d': -1.55946965, 'percent_change_30d': -8.79832744, 'percent_change_60d': 5.76673971, 'percent_change_90d': 15.59189463, 'market_cap': 43621123201.72779, 'market_cap_dominance': 4.7526, 'fully_diluted_market_cap': 54074456089.09, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 52, 'name': 'XRP', 'symbol': 'XRP', 'slug': 'xrp', 'num_market_pairs': 820, 'date_added': '2013-08-04T00:00:00.000Z', 'tags': ['medium-of-exchange', 'enterprise-solutions', 'arrington-xrp-capital-portfolio', 'galaxy-digital-portfolio', 'a16z-portfolio', 'pantera-capital-portfolio'], 'max_supply': 100000000000, 'circulating_supply': 49848747475, 'total_supply': 99989294935, 'platform': None, 'cmc_rank': 6, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 0.4830966020101945, 'volume_24h': 7555718857.912322, 'volume_change_24h': 78.0965, 'percent_change_1h': 0.18562668, 'percent_change_24h': 9.86139782, 'percent_change_7d': 45.84056673, 'percent_change_30d': 40.49606912, 'percent_change_60d': 39.83610598, 'percent_change_90d': 33.93971177, 'market_cap': 24081760519.636765, 'market_cap_dominance': 2.6238, 'fully_diluted_market_cap': 48309660201.02, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 4687, 'name': 'Binance USD', 'symbol': 'BUSD', 'slug': 'binance-usd', 'num_market_pairs': 5163, 'date_added': '2019-09-20T00:00:00.000Z', 'tags': ['stablecoin', 'asset-backed-stablecoin', 'binance-chain', 'harmony-ecosystem', 'moonriver-ecosystem', 'usd-stablecoin'], 'max_supply': None, 'circulating_supply': 20517253084.589256, 'total_supply': 20517253084.589256, 'platform': {'id': 1839, 'name': 'BNB', 'symbol': 'BNB', 'slug': 'bnb', 'token_address': 'BUSD-BD1'}, 'cmc_rank': 7, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 0.9998429332572485, 'volume_24h': 9505003038.74831, 'volume_change_24h': -10.9604, 'percent_change_1h': -0.02482558, 'percent_change_24h': -0.07000446, 'percent_change_7d': -0.06668667, 'percent_change_30d': -0.01953681, 'percent_change_60d': -0.10991468, 'percent_change_90d': 0.00298118, 'market_cap': 20514030506.47705, 'market_cap_dominance': 2.2351, 'fully_diluted_market_cap': 20514030506.48, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 2010, 'name': 'Cardano', 'symbol': 'ADA', 'slug': 'cardano', 'num_market_pairs': 571, 'date_added': '2017-10-01T00:00:00.000Z', 'tags': ['dpos', 'pos', 'platform', 'research', 'smart-contracts', 'staking', 'cardano-ecosystem', 'cardano'], 'max_supply': 45000000000, 'circulating_supply': 34227040771.909, 'total_supply': 34950580348.963, 'platform': None, 'cmc_rank': 8, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 0.4509975669443387, 'volume_24h': 1025814771.5903634, 'volume_change_24h': -6.5417, 'percent_change_1h': 0.0869026, 'percent_change_24h': 0.71422936, 'percent_change_7d': -1.83793413, 'percent_change_30d': -2.13599085, 'percent_change_60d': -8.023954, 'percent_change_90d': -7.09634852, 'market_cap': 15436312111.835638, 'market_cap_dominance': 1.6808, 'fully_diluted_market_cap': 20294890512.5, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 5426, 'name': 'Solana', 'symbol': 'SOL', 'slug': 'solana', 'num_market_pairs': 386, 'date_added': '2020-04-10T00:00:00.000Z', 'tags': ['pos', 'platform', 'solana-ecosystem', 'cms-holdings-portfolio', 'kenetic-capital-portfolio', 'alameda-research-portfolio', 'multicoin-capital-portfolio', 'okex-blockdream-ventures-portfolio'], 'max_supply': None, 'circulating_supply': 354521530.96390605, 'total_supply': 511616946.142289, 'platform': None, 'cmc_rank': 9, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 31.462853959450577, 'volume_24h': 834962523.5325351, 'volume_change_24h': -37.0503, 'percent_change_1h': 0.02362588, 'percent_change_24h': -0.86886305, 'percent_change_7d': -2.64497032, 'percent_change_30d': -11.14094734, 'percent_change_60d': -18.81421652, 'percent_change_90d': -21.64806916, 'market_cap': 11154259154.198212, 'market_cap_dominance': 1.2153, 'fully_diluted_market_cap': 16096929259.65, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 74, 'name': 'Dogecoin', 'symbol': 'DOGE', 'slug': 'dogecoin', 'num_market_pairs': 567, 'date_added': '2013-12-15T00:00:00.000Z', 'tags': ['mineable', 'pow', 'scrypt', 'medium-of-exchange', 'memes', 'payments', 'doggone-doggerel', 'bnb-chain'], 'max_supply': None, 'circulating_supply': 132670764299.89409, 'total_supply': 132670764299.89409, 'platform': None, 'cmc_rank': 10, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 0.06044207227180351, 'volume_24h': 445370531.52633786, 'volume_change_24h': 9.5092, 'percent_change_1h': 0.63107155, 'percent_change_24h': 2.5818719, 'percent_change_7d': 1.58415072, 'percent_change_30d': -11.19328759, 'percent_change_60d': -6.79950718, 'percent_change_90d': -8.73057991, 'market_cap': 8018895924.169607, 'market_cap_dominance': 0.8737, 'fully_diluted_market_cap': 8018895924.17, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 6636, 'name': 'Polkadot', 'symbol': 'DOT', 'slug': 'polkadot-new', 'num_market_pairs': 414, 'date_added': '2020-08-19T00:00:00.000Z', 'tags': ['substrate', 'polkadot', 'binance-chain', 'polkadot-ecosystem', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio', 'arrington-xrp-capital-portfolio', 'blockchain-capital-portfolio', 'boostvc-portfolio', 'cms-holdings-portfolio', 'coinfund-portfolio', 'fabric-ventures-portfolio', 'fenbushi-capital-portfolio', 'hashkey-capital-portfolio', 'kenetic-capital-portfolio', '1confirmation-portfolio', 'placeholder-ventures-portfolio', 'pantera-capital-portfolio', 'exnetwork-capital-portfolio', 'web3', 'spartan-group', 'injective-ecosystem', 'bnb-chain'], 'max_supply': None, 'circulating_supply': 1119485867.095681, 'total_supply': 1234909537.420861, 'platform': None, 'cmc_rank': 11, 'self_reported_circulating_supply': 904869778, 'self_reported_market_cap': 5695241948.936583, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 6.293990679547906, 'volume_24h': 324099449.45735747, 'volume_change_24h': -23.8718, 'percent_change_1h': 0.66271938, 'percent_change_24h': -0.81940784, 'percent_change_7d': -7.91020431, 'percent_change_30d': -16.83214006, 'percent_change_60d': -10.56759899, 'percent_change_90d': -20.65291459, 'market_cap': 7046033613.385821, 'market_cap_dominance': 0.7677, 'fully_diluted_market_cap': 7772509118.61, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 4943, 'name': 'Dai', 'symbol': 'DAI', 'slug': 'multi-collateral-dai', 'num_market_pairs': 1374, 'date_added': '2019-11-22T00:00:00.000Z', 'tags': ['defi', 'stablecoin', 'asset-backed-stablecoin', 'ethereum-ecosystem', 'avalanche-ecosystem', 'polygon-ecosystem', 'fantom-ecosystem', 'arbitrum-ecosytem', 'harmony-ecosystem', 'moonriver-ecosystem', 'bnb-chain', 'usd-stablecoin'], 'max_supply': None, 'circulating_supply': 6981237837.056313, 'total_supply': 6981237837.056313, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x6b175474e89094c44da98b954eedeac495271d0f'}, 'cmc_rank': 12, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 1.0002023891536413, 'volume_24h': 347119867.41114926, 'volume_change_24h': -35.3891, 'percent_change_1h': 0.04219522, 'percent_change_24h': 0.04987856, 'percent_change_7d': 0.07067375, 'percent_change_30d': 0.00765118, 'percent_change_60d': 0.10055961, 'percent_change_90d': 0.05291383, 'market_cap': 6982650763.873524, 'market_cap_dominance': 0.7603, 'fully_diluted_market_cap': 6982650763.87, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 3890, 'name': 'Polygon', 'symbol': 'MATIC', 'slug': 'polygon', 'num_market_pairs': 490, 'date_added': '2019-04-28T00:00:00.000Z', 'tags': ['platform', 'enterprise-solutions', 'scaling', 'state-channel', 'coinbase-ventures-portfolio', 'binance-launchpad', 'binance-labs-portfolio', 'polygon-ecosystem', 'moonriver-ecosystem', 'injective-ecosystem'], 'max_supply': 10000000000, 'circulating_supply': 8734317475.28493, 'total_supply': 10000000000, 'platform': None, 'cmc_rank': 13, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 0.735229134107275, 'volume_24h': 415055503.694775, 'volume_change_24h': -22.7951, 'percent_change_1h': 0.5897961, 'percent_change_24h': 0.31774378, 'percent_change_7d': -8.35862711, 'percent_change_30d': -10.18070507, 'percent_change_60d': -10.7464762, 'percent_change_90d': 27.28275554, 'market_cap': 6421724674.3717785, 'market_cap_dominance': 0.6992, 'fully_diluted_market_cap': 7352291341.07, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 5994, 'name': 'Shiba Inu', 'symbol': 'SHIB', 'slug': 'shiba-inu', 'num_market_pairs': 418, 'date_added': '2020-08-01T00:00:00.000Z', 'tags': ['memes', 'ethereum-ecosystem', 'doggone-doggerel'], 'max_supply': None, 'circulating_supply': 549063278876301.94, 'total_supply': 589735030408322.8, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce'}, 'cmc_rank': 14, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 1.065587859040987e-05, 'volume_24h': 244980521.9556539, 'volume_change_24h': -31.0835, 'percent_change_1h': 0.31521408, 'percent_change_24h': -0.31068149, 'percent_change_7d': -8.05748821, 'percent_change_30d': -19.11240409, 'percent_change_60d': -4.95455695, 'percent_change_90d': -5.28505933, 'market_cap': 5850751638.158229, 'market_cap_dominance': 0.6375, 'fully_diluted_market_cap': 6284144884.54, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 1958, 'name': 'TRON', 'symbol': 'TRX', 'slug': 'tron', 'num_market_pairs': 685, 'date_added': '2017-09-13T00:00:00.000Z', 'tags': ['media', 'payments', 'tron-ecosystem'], 'max_supply': None, 'circulating_supply': 92354607190.8173, 'total_supply': 92354638009.11899, 'platform': None, 'cmc_rank': 15, 'self_reported_circulating_supply': 71659659264, 'self_reported_market_cap': 4266067094.886732, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 0.05953233853890087, 'volume_24h': 362744077.10155207, 'volume_change_24h': -24.58, 'percent_change_1h': 0.11756489, 'percent_change_24h': 0.165079, 'percent_change_7d': -2.23818657, 'percent_change_30d': -8.94455708, 'percent_change_60d': -7.87778122, 'percent_change_90d': -7.38492384, 'market_cap': 5498085740.910945, 'market_cap_dominance': 0.5987, 'fully_diluted_market_cap': 5498087575.6, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 5805, 'name': 'Avalanche', 'symbol': 'AVAX', 'slug': 'avalanche', 'num_market_pairs': 317, 'date_added': '2020-07-13T00:00:00.000Z', 'tags': ['defi', 'smart-contracts', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio', 'avalanche-ecosystem', 'cms-holdings-portfolio', 'dragonfly-capital-portfolio', 'moonriver-ecosystem', 'injective-ecosystem'], 'max_supply': 720000000, 'circulating_supply': 295866222.17204005, 'total_supply': 404229626.49901325, 'platform': None, 'cmc_rank': 16, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 17.4291094294107, 'volume_24h': 264863391.1728464, 'volume_change_24h': -40.0494, 'percent_change_1h': 0.59581621, 'percent_change_24h': 0.93750549, 'percent_change_7d': -2.96876107, 'percent_change_30d': -24.58308219, 'percent_change_60d': -20.56309853, 'percent_change_90d': -14.13503794, 'market_cap': 5156684762.702825, 'market_cap_dominance': 0.5615, 'fully_diluted_market_cap': 12548958789.18, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 3717, 'name': 'Wrapped Bitcoin', 'symbol': 'WBTC', 'slug': 'wrapped-bitcoin', 'num_market_pairs': 610, 'date_added': '2019-01-30T00:00:00.000Z', 'tags': ['medium-of-exchange', 'defi', 'wrapped-tokens', 'fantom-ecosystem', 'arbitrum-ecosytem', 'moonriver-ecosystem'], 'max_supply': None, 'circulating_supply': 244707.06137105, 'total_supply': 244707.06137105, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x2260fac5e5542a773aa44fbcfedf7c193bc2c599'}, 'cmc_rank': 17, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 18684.247624840336, 'volume_24h': 232447597.78040728, 'volume_change_24h': -37.4347, 'percent_change_1h': 0.10055535, 'percent_change_24h': -1.19454596, 'percent_change_7d': -4.96907115, 'percent_change_30d': -13.01704565, 'percent_change_60d': -14.56523878, 'percent_change_90d': -11.38590194, 'market_cap': 4572167330.203699, 'market_cap_dominance': 0.4982, 'fully_diluted_market_cap': 4572167330.2, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 7083, 'name': 'Uniswap', 'symbol': 'UNI', 'slug': 'uniswap', 'num_market_pairs': 480, 'date_added': '2020-09-17T00:00:00.000Z', 'tags': ['decentralized-exchange', 'defi', 'dao', 'yield-farming', 'amm', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'governance', 'blockchain-capital-portfolio', 'defiance-capital-portfolio', 'alameda-research-portfolio', 'a16z-portfolio', 'pantera-capital-portfolio', 'parafi-capital', 'paradigm-portfolio', 'arbitrum-ecosytem', 'injective-ecosystem'], 'max_supply': 1000000000, 'circulating_supply': 762209326.5354977, 'total_supply': 1000000000, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x1f9840a85d5af5bf1d1762f925bdaddc4201f984'}, 'cmc_rank': 18, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': 0.8639131, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 5.821264018877274, 'volume_24h': 112157307.81865074, 'volume_change_24h': -18.2148, 'percent_change_1h': 0.61801691, 'percent_change_24h': 3.09088363, 'percent_change_7d': 0.68937262, 'percent_change_30d': -17.7346908, 'percent_change_60d': -19.04553082, 'percent_change_90d': 8.78987583, 'market_cap': 4437021727.413772, 'market_cap_dominance': 0.4834, 'fully_diluted_market_cap': 5821264018.88, 'tvl': 5135958401.74284, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 3794, 'name': 'Cosmos', 'symbol': 'ATOM', 'slug': 'cosmos', 'num_market_pairs': 345, 'date_added': '2019-03-14T00:00:00.000Z', 'tags': ['platform', 'cosmos-ecosystem', 'content-creation', 'interoperability', 'polychain-capital-portfolio', 'dragonfly-capital-portfolio', 'hashkey-capital-portfolio', '1confirmation-portfolio', 'paradigm-portfolio', 'exnetwork-capital-portfolio', 'injective-ecosystem'], 'max_supply': None, 'circulating_supply': 286370297, 'total_supply': 0, 'platform': None, 'cmc_rank': 19, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 13.732285717488939, 'volume_24h': 685670559.8085932, 'volume_change_24h': -3.3366, 'percent_change_1h': 0.4616475, 'percent_change_24h': -2.14243528, 'percent_change_7d': -14.79685666, 'percent_change_30d': 12.14444011, 'percent_change_60d': 48.33111907, 'percent_change_90d': 68.83114934, 'market_cap': 3932518739.4061656, 'market_cap_dominance': 0.4282, 'fully_diluted_market_cap': 0, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}, {'id': 3957, 'name': 'UNUS SED LEO', 'symbol': 'LEO', 'slug': 'unus-sed-leo', 'num_market_pairs': 20, 'date_added': '2019-05-21T00:00:00.000Z', 'tags': ['marketplace', 'centralized-exchange', 'discount-token', 'payments', 'kenetic-capital-portfolio', 'alameda-research-portfolio'], 'max_supply': None, 'circulating_supply': 953954130, 'total_supply': 985239504, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x2af5d2ad76741191d15dfe7bf6ac92d4bd912ca3'}, 'cmc_rank': 20, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T15:14:00.000Z', 'quote': {'USD': {'price': 4.1134954298757105, 'volume_24h': 4927387.42779256, 'volume_change_24h': -10.166, 'percent_change_1h': 0.13893308, 'percent_change_24h': -13.45411536, 'percent_change_7d': -16.49086106, 'percent_change_30d': -22.06120126, 'percent_change_60d': -19.10868799, 'percent_change_90d': -30.45626426, 'market_cap': 3924085954.0660596, 'market_cap_dominance': 0.4275, 'fully_diluted_market_cap': 4052778197.04, 'tvl': None, 'last_updated': '2022-09-23T15:14:00.000Z'}}}]}
    


```python
type(data)
```




    dict




```python
import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.json_normalize(data['data'])

df['timestamp'] = pd.Timestamp('now') #GMT+3 For Me

df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>symbol</th>
      <th>slug</th>
      <th>num_market_pairs</th>
      <th>date_added</th>
      <th>tags</th>
      <th>max_supply</th>
      <th>circulating_supply</th>
      <th>total_supply</th>
      <th>platform</th>
      <th>cmc_rank</th>
      <th>self_reported_circulating_supply</th>
      <th>self_reported_market_cap</th>
      <th>tvl_ratio</th>
      <th>last_updated</th>
      <th>quote.USD.price</th>
      <th>quote.USD.volume_24h</th>
      <th>quote.USD.volume_change_24h</th>
      <th>quote.USD.percent_change_1h</th>
      <th>quote.USD.percent_change_24h</th>
      <th>quote.USD.percent_change_7d</th>
      <th>quote.USD.percent_change_30d</th>
      <th>quote.USD.percent_change_60d</th>
      <th>quote.USD.percent_change_90d</th>
      <th>quote.USD.market_cap</th>
      <th>quote.USD.market_cap_dominance</th>
      <th>quote.USD.fully_diluted_market_cap</th>
      <th>quote.USD.tvl</th>
      <th>quote.USD.last_updated</th>
      <th>platform.id</th>
      <th>platform.name</th>
      <th>platform.symbol</th>
      <th>platform.slug</th>
      <th>platform.token_address</th>
      <th>timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bitcoin</td>
      <td>BTC</td>
      <td>bitcoin</td>
      <td>9748</td>
      <td>2013-04-28T00:00:00.000Z</td>
      <td>[mineable, pow, sha-256, store-of-value, state...</td>
      <td>2.100000e+07</td>
      <td>1.915850e+07</td>
      <td>1.915850e+07</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>18690.447224</td>
      <td>3.697756e+10</td>
      <td>-31.6811</td>
      <td>0.092014</td>
      <td>-1.183645</td>
      <td>-4.961169</td>
      <td>-13.025765</td>
      <td>-14.448737</td>
      <td>-11.473509</td>
      <td>3.580809e+11</td>
      <td>39.0140</td>
      <td>3.924994e+11</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1027</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>6103</td>
      <td>2015-08-07T00:00:00.000Z</td>
      <td>[pos, smart-contracts, ethereum-ecosystem, coi...</td>
      <td>NaN</td>
      <td>1.224922e+08</td>
      <td>1.224922e+08</td>
      <td>NaN</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1284.809475</td>
      <td>1.881477e+10</td>
      <td>-23.0881</td>
      <td>0.362895</td>
      <td>1.436718</td>
      <td>-11.169538</td>
      <td>-22.231748</td>
      <td>-15.518928</td>
      <td>7.655431</td>
      <td>1.573791e+11</td>
      <td>17.1469</td>
      <td>1.573791e+11</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>2</th>
      <td>825</td>
      <td>Tether</td>
      <td>USDT</td>
      <td>tether</td>
      <td>40036</td>
      <td>2015-02-25T00:00:00.000Z</td>
      <td>[payments, stablecoin, asset-backed-stablecoin...</td>
      <td>NaN</td>
      <td>6.795470e+10</td>
      <td>7.015545e+10</td>
      <td>NaN</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.999971</td>
      <td>5.453611e+10</td>
      <td>-22.7203</td>
      <td>-0.000375</td>
      <td>-0.010133</td>
      <td>0.000547</td>
      <td>-0.008118</td>
      <td>-0.008345</td>
      <td>0.047233</td>
      <td>6.795276e+10</td>
      <td>7.4037</td>
      <td>7.015345e+10</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0xdac17f958d2ee523a2206206994597c13d831ec7</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3408</td>
      <td>USD Coin</td>
      <td>USDC</td>
      <td>usd-coin</td>
      <td>6294</td>
      <td>2018-10-08T00:00:00.000Z</td>
      <td>[medium-of-exchange, stablecoin, asset-backed-...</td>
      <td>NaN</td>
      <td>4.976134e+10</td>
      <td>4.976134e+10</td>
      <td>NaN</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.999980</td>
      <td>5.113202e+09</td>
      <td>-23.5646</td>
      <td>0.001168</td>
      <td>-0.008946</td>
      <td>-0.004062</td>
      <td>-0.005491</td>
      <td>0.027822</td>
      <td>-0.024244</td>
      <td>4.976033e+10</td>
      <td>5.4215</td>
      <td>4.976033e+10</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1839</td>
      <td>BNB</td>
      <td>BNB</td>
      <td>bnb</td>
      <td>1110</td>
      <td>2017-07-25T00:00:00.000Z</td>
      <td>[marketplace, centralized-exchange, payments, ...</td>
      <td>2.000000e+08</td>
      <td>1.613373e+08</td>
      <td>1.613373e+08</td>
      <td>NaN</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>270.372280</td>
      <td>8.818450e+08</td>
      <td>-21.6284</td>
      <td>-0.095247</td>
      <td>0.937023</td>
      <td>-1.559470</td>
      <td>-8.798327</td>
      <td>5.766740</td>
      <td>15.591895</td>
      <td>4.362112e+10</td>
      <td>4.7526</td>
      <td>5.407446e+10</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>5</th>
      <td>52</td>
      <td>XRP</td>
      <td>XRP</td>
      <td>xrp</td>
      <td>820</td>
      <td>2013-08-04T00:00:00.000Z</td>
      <td>[medium-of-exchange, enterprise-solutions, arr...</td>
      <td>1.000000e+11</td>
      <td>4.984875e+10</td>
      <td>9.998929e+10</td>
      <td>NaN</td>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.483097</td>
      <td>7.555719e+09</td>
      <td>78.0965</td>
      <td>0.185627</td>
      <td>9.861398</td>
      <td>45.840567</td>
      <td>40.496069</td>
      <td>39.836106</td>
      <td>33.939712</td>
      <td>2.408176e+10</td>
      <td>2.6238</td>
      <td>4.830966e+10</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4687</td>
      <td>Binance USD</td>
      <td>BUSD</td>
      <td>binance-usd</td>
      <td>5163</td>
      <td>2019-09-20T00:00:00.000Z</td>
      <td>[stablecoin, asset-backed-stablecoin, binance-...</td>
      <td>NaN</td>
      <td>2.051725e+10</td>
      <td>2.051725e+10</td>
      <td>NaN</td>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.999843</td>
      <td>9.505003e+09</td>
      <td>-10.9604</td>
      <td>-0.024826</td>
      <td>-0.070004</td>
      <td>-0.066687</td>
      <td>-0.019537</td>
      <td>-0.109915</td>
      <td>0.002981</td>
      <td>2.051403e+10</td>
      <td>2.2351</td>
      <td>2.051403e+10</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1839.0</td>
      <td>BNB</td>
      <td>BNB</td>
      <td>bnb</td>
      <td>BUSD-BD1</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2010</td>
      <td>Cardano</td>
      <td>ADA</td>
      <td>cardano</td>
      <td>571</td>
      <td>2017-10-01T00:00:00.000Z</td>
      <td>[dpos, pos, platform, research, smart-contract...</td>
      <td>4.500000e+10</td>
      <td>3.422704e+10</td>
      <td>3.495058e+10</td>
      <td>NaN</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.450998</td>
      <td>1.025815e+09</td>
      <td>-6.5417</td>
      <td>0.086903</td>
      <td>0.714229</td>
      <td>-1.837934</td>
      <td>-2.135991</td>
      <td>-8.023954</td>
      <td>-7.096349</td>
      <td>1.543631e+10</td>
      <td>1.6808</td>
      <td>2.029489e+10</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5426</td>
      <td>Solana</td>
      <td>SOL</td>
      <td>solana</td>
      <td>386</td>
      <td>2020-04-10T00:00:00.000Z</td>
      <td>[pos, platform, solana-ecosystem, cms-holdings...</td>
      <td>NaN</td>
      <td>3.545215e+08</td>
      <td>5.116169e+08</td>
      <td>NaN</td>
      <td>9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>31.462854</td>
      <td>8.349625e+08</td>
      <td>-37.0503</td>
      <td>0.023626</td>
      <td>-0.868863</td>
      <td>-2.644970</td>
      <td>-11.140947</td>
      <td>-18.814217</td>
      <td>-21.648069</td>
      <td>1.115426e+10</td>
      <td>1.2153</td>
      <td>1.609693e+10</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>9</th>
      <td>74</td>
      <td>Dogecoin</td>
      <td>DOGE</td>
      <td>dogecoin</td>
      <td>567</td>
      <td>2013-12-15T00:00:00.000Z</td>
      <td>[mineable, pow, scrypt, medium-of-exchange, me...</td>
      <td>NaN</td>
      <td>1.326708e+11</td>
      <td>1.326708e+11</td>
      <td>NaN</td>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.060442</td>
      <td>4.453705e+08</td>
      <td>9.5092</td>
      <td>0.631072</td>
      <td>2.581872</td>
      <td>1.584151</td>
      <td>-11.193288</td>
      <td>-6.799507</td>
      <td>-8.730580</td>
      <td>8.018896e+09</td>
      <td>0.8737</td>
      <td>8.018896e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>10</th>
      <td>6636</td>
      <td>Polkadot</td>
      <td>DOT</td>
      <td>polkadot-new</td>
      <td>414</td>
      <td>2020-08-19T00:00:00.000Z</td>
      <td>[substrate, polkadot, binance-chain, polkadot-...</td>
      <td>NaN</td>
      <td>1.119486e+09</td>
      <td>1.234910e+09</td>
      <td>NaN</td>
      <td>11</td>
      <td>9.048698e+08</td>
      <td>5.695242e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>6.293991</td>
      <td>3.240994e+08</td>
      <td>-23.8718</td>
      <td>0.662719</td>
      <td>-0.819408</td>
      <td>-7.910204</td>
      <td>-16.832140</td>
      <td>-10.567599</td>
      <td>-20.652915</td>
      <td>7.046034e+09</td>
      <td>0.7677</td>
      <td>7.772509e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>11</th>
      <td>4943</td>
      <td>Dai</td>
      <td>DAI</td>
      <td>multi-collateral-dai</td>
      <td>1374</td>
      <td>2019-11-22T00:00:00.000Z</td>
      <td>[defi, stablecoin, asset-backed-stablecoin, et...</td>
      <td>NaN</td>
      <td>6.981238e+09</td>
      <td>6.981238e+09</td>
      <td>NaN</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1.000202</td>
      <td>3.471199e+08</td>
      <td>-35.3891</td>
      <td>0.042195</td>
      <td>0.049879</td>
      <td>0.070674</td>
      <td>0.007651</td>
      <td>0.100560</td>
      <td>0.052914</td>
      <td>6.982651e+09</td>
      <td>0.7603</td>
      <td>6.982651e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x6b175474e89094c44da98b954eedeac495271d0f</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>12</th>
      <td>3890</td>
      <td>Polygon</td>
      <td>MATIC</td>
      <td>polygon</td>
      <td>490</td>
      <td>2019-04-28T00:00:00.000Z</td>
      <td>[platform, enterprise-solutions, scaling, stat...</td>
      <td>1.000000e+10</td>
      <td>8.734317e+09</td>
      <td>1.000000e+10</td>
      <td>NaN</td>
      <td>13</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.735229</td>
      <td>4.150555e+08</td>
      <td>-22.7951</td>
      <td>0.589796</td>
      <td>0.317744</td>
      <td>-8.358627</td>
      <td>-10.180705</td>
      <td>-10.746476</td>
      <td>27.282756</td>
      <td>6.421725e+09</td>
      <td>0.6992</td>
      <td>7.352291e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>13</th>
      <td>5994</td>
      <td>Shiba Inu</td>
      <td>SHIB</td>
      <td>shiba-inu</td>
      <td>418</td>
      <td>2020-08-01T00:00:00.000Z</td>
      <td>[memes, ethereum-ecosystem, doggone-doggerel]</td>
      <td>NaN</td>
      <td>5.490633e+14</td>
      <td>5.897350e+14</td>
      <td>NaN</td>
      <td>14</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.000011</td>
      <td>2.449805e+08</td>
      <td>-31.0835</td>
      <td>0.315214</td>
      <td>-0.310681</td>
      <td>-8.057488</td>
      <td>-19.112404</td>
      <td>-4.954557</td>
      <td>-5.285059</td>
      <td>5.850752e+09</td>
      <td>0.6375</td>
      <td>6.284145e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1958</td>
      <td>TRON</td>
      <td>TRX</td>
      <td>tron</td>
      <td>685</td>
      <td>2017-09-13T00:00:00.000Z</td>
      <td>[media, payments, tron-ecosystem]</td>
      <td>NaN</td>
      <td>9.235461e+10</td>
      <td>9.235464e+10</td>
      <td>NaN</td>
      <td>15</td>
      <td>7.165966e+10</td>
      <td>4.266067e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.059532</td>
      <td>3.627441e+08</td>
      <td>-24.5800</td>
      <td>0.117565</td>
      <td>0.165079</td>
      <td>-2.238187</td>
      <td>-8.944557</td>
      <td>-7.877781</td>
      <td>-7.384924</td>
      <td>5.498086e+09</td>
      <td>0.5987</td>
      <td>5.498088e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>15</th>
      <td>5805</td>
      <td>Avalanche</td>
      <td>AVAX</td>
      <td>avalanche</td>
      <td>317</td>
      <td>2020-07-13T00:00:00.000Z</td>
      <td>[defi, smart-contracts, three-arrows-capital-p...</td>
      <td>7.200000e+08</td>
      <td>2.958662e+08</td>
      <td>4.042296e+08</td>
      <td>NaN</td>
      <td>16</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>17.429109</td>
      <td>2.648634e+08</td>
      <td>-40.0494</td>
      <td>0.595816</td>
      <td>0.937505</td>
      <td>-2.968761</td>
      <td>-24.583082</td>
      <td>-20.563099</td>
      <td>-14.135038</td>
      <td>5.156685e+09</td>
      <td>0.5615</td>
      <td>1.254896e+10</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>16</th>
      <td>3717</td>
      <td>Wrapped Bitcoin</td>
      <td>WBTC</td>
      <td>wrapped-bitcoin</td>
      <td>610</td>
      <td>2019-01-30T00:00:00.000Z</td>
      <td>[medium-of-exchange, defi, wrapped-tokens, fan...</td>
      <td>NaN</td>
      <td>2.447071e+05</td>
      <td>2.447071e+05</td>
      <td>NaN</td>
      <td>17</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>18684.247625</td>
      <td>2.324476e+08</td>
      <td>-37.4347</td>
      <td>0.100555</td>
      <td>-1.194546</td>
      <td>-4.969071</td>
      <td>-13.017046</td>
      <td>-14.565239</td>
      <td>-11.385902</td>
      <td>4.572167e+09</td>
      <td>0.4982</td>
      <td>4.572167e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x2260fac5e5542a773aa44fbcfedf7c193bc2c599</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>17</th>
      <td>7083</td>
      <td>Uniswap</td>
      <td>UNI</td>
      <td>uniswap</td>
      <td>480</td>
      <td>2020-09-17T00:00:00.000Z</td>
      <td>[decentralized-exchange, defi, dao, yield-farm...</td>
      <td>1.000000e+09</td>
      <td>7.622093e+08</td>
      <td>1.000000e+09</td>
      <td>NaN</td>
      <td>18</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.863913</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>5.821264</td>
      <td>1.121573e+08</td>
      <td>-18.2148</td>
      <td>0.618017</td>
      <td>3.090884</td>
      <td>0.689373</td>
      <td>-17.734691</td>
      <td>-19.045531</td>
      <td>8.789876</td>
      <td>4.437022e+09</td>
      <td>0.4834</td>
      <td>5.821264e+09</td>
      <td>5.135958e+09</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x1f9840a85d5af5bf1d1762f925bdaddc4201f984</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>18</th>
      <td>3794</td>
      <td>Cosmos</td>
      <td>ATOM</td>
      <td>cosmos</td>
      <td>345</td>
      <td>2019-03-14T00:00:00.000Z</td>
      <td>[platform, cosmos-ecosystem, content-creation,...</td>
      <td>NaN</td>
      <td>2.863703e+08</td>
      <td>0.000000e+00</td>
      <td>NaN</td>
      <td>19</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>13.732286</td>
      <td>6.856706e+08</td>
      <td>-3.3366</td>
      <td>0.461647</td>
      <td>-2.142435</td>
      <td>-14.796857</td>
      <td>12.144440</td>
      <td>48.331119</td>
      <td>68.831149</td>
      <td>3.932519e+09</td>
      <td>0.4282</td>
      <td>0.000000e+00</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>19</th>
      <td>3957</td>
      <td>UNUS SED LEO</td>
      <td>LEO</td>
      <td>unus-sed-leo</td>
      <td>20</td>
      <td>2019-05-21T00:00:00.000Z</td>
      <td>[marketplace, centralized-exchange, discount-t...</td>
      <td>NaN</td>
      <td>9.539541e+08</td>
      <td>9.852395e+08</td>
      <td>NaN</td>
      <td>20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>4.113495</td>
      <td>4.927387e+06</td>
      <td>-10.1660</td>
      <td>0.138933</td>
      <td>-13.454115</td>
      <td>-16.490861</td>
      <td>-22.061201</td>
      <td>-19.108688</td>
      <td>-30.456264</td>
      <td>3.924086e+09</td>
      <td>0.4275</td>
      <td>4.052778e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x2af5d2ad76741191d15dfe7bf6ac92d4bd912ca3</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
  </tbody>
</table>
</div>




```python
def api_runner():
    global df3
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'20',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'Enter Your Crypto API Key',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
    df2 = pd.json_normalize(data['data'])
    df2['timestamp'] = pd.Timestamp('now') #GMT+3 For Me
    df3 = pd.concat([df,df2])
    
    if not os.path.isfile(r'D:\Data\CryptoAPI\API.csv'):
       df3.to_csv(r'D:\Data\CryptoAPI\API.csv', header = 'column_names') 
    else:
       df3.to_csv(r'D:\Data\CryptoAPI\API.csv', mode = 'a', header = False) 
```


```python
import os 
from time import time
from time import sleep

for i in range(333):
    api_runner()
    print('API Working')
    sleep(60)
exit()
```

    {'status': {'timestamp': '2022-09-23T16:23:35.884Z', 'error_code': 0, 'error_message': None, 'elapsed': 50, 'credit_count': 1, 'notice': None, 'total_count': 9447}, 'data': [{'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'num_market_pairs': 9748, 'date_added': '2013-04-28T00:00:00.000Z', 'tags': ['mineable', 'pow', 'sha-256', 'store-of-value', 'state-channel', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio', 'binance-labs-portfolio', 'blockchain-capital-portfolio', 'boostvc-portfolio', 'cms-holdings-portfolio', 'dcg-portfolio', 'dragonfly-capital-portfolio', 'electric-capital-portfolio', 'fabric-ventures-portfolio', 'framework-ventures-portfolio', 'galaxy-digital-portfolio', 'huobi-capital-portfolio', 'alameda-research-portfolio', 'a16z-portfolio', '1confirmation-portfolio', 'winklevoss-capital-portfolio', 'usv-portfolio', 'placeholder-ventures-portfolio', 'pantera-capital-portfolio', 'multicoin-capital-portfolio', 'paradigm-portfolio'], 'max_supply': 21000000, 'circulating_supply': 19158581, 'total_supply': 19158581, 'platform': None, 'cmc_rank': 1, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 18706.65528672906, 'volume_24h': 37334106423.11996, 'volume_change_24h': -31.1533, 'percent_change_1h': -0.12579647, 'percent_change_24h': -1.05214713, 'percent_change_7d': -4.53098282, 'percent_change_30d': -14.05109662, 'percent_change_60d': -14.58909521, 'percent_change_90d': -11.12112224, 'market_cap': 358392970549.8769, 'market_cap_dominance': 38.9562, 'fully_diluted_market_cap': 392839761021.31, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'num_market_pairs': 6103, 'date_added': '2015-08-07T00:00:00.000Z', 'tags': ['pos', 'smart-contracts', 'ethereum-ecosystem', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio', 'binance-labs-portfolio', 'blockchain-capital-portfolio', 'boostvc-portfolio', 'cms-holdings-portfolio', 'dcg-portfolio', 'dragonfly-capital-portfolio', 'electric-capital-portfolio', 'fabric-ventures-portfolio', 'framework-ventures-portfolio', 'hashkey-capital-portfolio', 'kenetic-capital-portfolio', 'huobi-capital-portfolio', 'alameda-research-portfolio', 'a16z-portfolio', '1confirmation-portfolio', 'winklevoss-capital-portfolio', 'usv-portfolio', 'placeholder-ventures-portfolio', 'pantera-capital-portfolio', 'multicoin-capital-portfolio', 'paradigm-portfolio', 'injective-ecosystem'], 'max_supply': None, 'circulating_supply': 122493377.499, 'total_supply': 122493377.499, 'platform': None, 'cmc_rank': 2, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 1291.9072485885663, 'volume_24h': 19021787163.813873, 'volume_change_24h': -23.1122, 'percent_change_1h': -0.09344206, 'percent_change_24h': 2.28645118, 'percent_change_7d': -10.26995955, 'percent_change_30d': -23.06440869, 'percent_change_60d': -15.07393899, 'percent_change_90d': 8.59928945, 'market_cap': 158250082295.05368, 'market_cap_dominance': 17.2013, 'fully_diluted_market_cap': 158250082295.05, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 825, 'name': 'Tether', 'symbol': 'USDT', 'slug': 'tether', 'num_market_pairs': 40036, 'date_added': '2015-02-25T00:00:00.000Z', 'tags': ['payments', 'stablecoin', 'asset-backed-stablecoin', 'avalanche-ecosystem', 'solana-ecosystem', 'arbitrum-ecosytem', 'moonriver-ecosystem', 'injective-ecosystem', 'bnb-chain', 'usd-stablecoin'], 'max_supply': None, 'circulating_supply': 67954703168.01751, 'total_supply': 70155449908.74805, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0xdac17f958d2ee523a2206206994597c13d831ec7'}, 'cmc_rank': 3, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 0.9999777836431918, 'volume_24h': 56709565349.08896, 'volume_change_24h': -20.3974, 'percent_change_1h': 0.00265625, 'percent_change_24h': -0.00669627, 'percent_change_7d': 0.00123377, 'percent_change_30d': -0.00609672, 'percent_change_60d': -0.00692931, 'percent_change_90d': 0.04430946, 'market_cap': 67953193462.08513, 'market_cap_dominance': 7.3863, 'fully_diluted_market_cap': 70153891310.24, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 3408, 'name': 'USD Coin', 'symbol': 'USDC', 'slug': 'usd-coin', 'num_market_pairs': 6295, 'date_added': '2018-10-08T00:00:00.000Z', 'tags': ['medium-of-exchange', 'stablecoin', 'asset-backed-stablecoin', 'fantom-ecosystem', 'arbitrum-ecosytem', 'moonriver-ecosystem', 'bnb-chain', 'usd-stablecoin'], 'max_supply': None, 'circulating_supply': 49836182660.77986, 'total_supply': 49836182660.77986, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'}, 'cmc_rank': 4, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 1.000046113716897, 'volume_24h': 5149800508.476997, 'volume_change_24h': -23.7239, 'percent_change_1h': -0.00518423, 'percent_change_24h': -0.00100371, 'percent_change_7d': 0.01342358, 'percent_change_30d': 0.01627595, 'percent_change_60d': -0.00522184, 'percent_change_90d': -0.01183285, 'market_cap': 49838480792.39831, 'market_cap_dominance': 5.4173, 'fully_diluted_market_cap': 49838480792.4, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 1839, 'name': 'BNB', 'symbol': 'BNB', 'slug': 'bnb', 'num_market_pairs': 1110, 'date_added': '2017-07-25T00:00:00.000Z', 'tags': ['marketplace', 'centralized-exchange', 'payments', 'smart-contracts', 'alameda-research-portfolio', 'multicoin-capital-portfolio', 'moonriver-ecosystem', 'bnb-chain'], 'max_supply': 200000000, 'circulating_supply': 161337261.09, 'total_supply': 161337261.09, 'platform': None, 'cmc_rank': 5, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 271.1849743528157, 'volume_24h': 884514630.8595929, 'volume_change_24h': -21.2716, 'percent_change_1h': 0.07897061, 'percent_change_24h': 1.13223342, 'percent_change_7d': -0.89021987, 'percent_change_30d': -9.31075576, 'percent_change_60d': 5.88800178, 'percent_change_90d': 16.59319738, 'market_cap': 43752241010.84518, 'market_cap_dominance': 4.7557, 'fully_diluted_market_cap': 54236994870.56, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 52, 'name': 'XRP', 'symbol': 'XRP', 'slug': 'xrp', 'num_market_pairs': 820, 'date_added': '2013-08-04T00:00:00.000Z', 'tags': ['medium-of-exchange', 'enterprise-solutions', 'arrington-xrp-capital-portfolio', 'galaxy-digital-portfolio', 'a16z-portfolio', 'pantera-capital-portfolio'], 'max_supply': 100000000000, 'circulating_supply': 49848747475, 'total_supply': 99989294935, 'platform': None, 'cmc_rank': 6, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 0.48594093276832706, 'volume_24h': 7651721504.151783, 'volume_change_24h': 78.5762, 'percent_change_1h': -1.08262983, 'percent_change_24h': 12.3023624, 'percent_change_7d': 45.93095224, 'percent_change_30d': 40.20488223, 'percent_change_60d': 39.93530302, 'percent_change_90d': 35.9925697, 'market_cap': 24223546845.33429, 'market_cap_dominance': 2.633, 'fully_diluted_market_cap': 48594093276.83, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 4687, 'name': 'Binance USD', 'symbol': 'BUSD', 'slug': 'binance-usd', 'num_market_pairs': 5163, 'date_added': '2019-09-20T00:00:00.000Z', 'tags': ['stablecoin', 'asset-backed-stablecoin', 'binance-chain', 'harmony-ecosystem', 'moonriver-ecosystem', 'usd-stablecoin'], 'max_supply': None, 'circulating_supply': 20517253084.589256, 'total_supply': 20517253084.589256, 'platform': {'id': 1839, 'name': 'BNB', 'symbol': 'BNB', 'slug': 'bnb', 'token_address': 'BUSD-BD1'}, 'cmc_rank': 7, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 1.000430854434904, 'volume_24h': 9445031142.448252, 'volume_change_24h': -13.1497, 'percent_change_1h': 0.0030246, 'percent_change_24h': 0.03757092, 'percent_change_7d': 0.10298813, 'percent_change_30d': 0.03951889, 'percent_change_60d': 0.17413913, 'percent_change_90d': -0.02320911, 'market_cap': 20526093034.0728, 'market_cap_dominance': 2.2311, 'fully_diluted_market_cap': 20526093034.07, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 2010, 'name': 'Cardano', 'symbol': 'ADA', 'slug': 'cardano', 'num_market_pairs': 571, 'date_added': '2017-10-01T00:00:00.000Z', 'tags': ['dpos', 'pos', 'platform', 'research', 'smart-contracts', 'staking', 'cardano-ecosystem', 'cardano'], 'max_supply': 45000000000, 'circulating_supply': 34227045077.067, 'total_supply': 34950580348.963, 'platform': None, 'cmc_rank': 8, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 0.4520542875998899, 'volume_24h': 1034363254.773439, 'volume_change_24h': -5.9524, 'percent_change_1h': -0.22896707, 'percent_change_24h': 0.65323896, 'percent_change_7d': -1.65719145, 'percent_change_30d': -2.83178999, 'percent_change_60d': -8.13297874, 'percent_change_90d': -6.38852634, 'market_cap': 15472482478.962843, 'market_cap_dominance': 1.6821, 'fully_diluted_market_cap': 20342442942, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 5426, 'name': 'Solana', 'symbol': 'SOL', 'slug': 'solana', 'num_market_pairs': 386, 'date_added': '2020-04-10T00:00:00.000Z', 'tags': ['pos', 'platform', 'solana-ecosystem', 'cms-holdings-portfolio', 'kenetic-capital-portfolio', 'alameda-research-portfolio', 'multicoin-capital-portfolio', 'okex-blockdream-ventures-portfolio'], 'max_supply': None, 'circulating_supply': 354521459.37243974, 'total_supply': 511616946.142289, 'platform': None, 'cmc_rank': 9, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 31.56403316222359, 'volume_24h': 841297372.6156607, 'volume_change_24h': -37.2808, 'percent_change_1h': -0.20204183, 'percent_change_24h': -0.59555631, 'percent_change_7d': -1.55548082, 'percent_change_30d': -12.55070711, 'percent_change_60d': -17.85174948, 'percent_change_90d': -21.19301067, 'market_cap': 11190127100.351591, 'market_cap_dominance': 1.2163, 'fully_diluted_market_cap': 16148694254.39, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 74, 'name': 'Dogecoin', 'symbol': 'DOGE', 'slug': 'dogecoin', 'num_market_pairs': 567, 'date_added': '2013-12-15T00:00:00.000Z', 'tags': ['mineable', 'pow', 'scrypt', 'medium-of-exchange', 'memes', 'payments', 'doggone-doggerel', 'bnb-chain'], 'max_supply': None, 'circulating_supply': 132670764299.89409, 'total_supply': 132670764299.89409, 'platform': None, 'cmc_rank': 10, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 0.061006392051131, 'volume_24h': 467183300.22296786, 'volume_change_24h': 14.7079, 'percent_change_1h': 0.30540345, 'percent_change_24h': 3.52516122, 'percent_change_7d': 2.58910804, 'percent_change_30d': -11.66899377, 'percent_change_60d': -5.99498943, 'percent_change_90d': -7.37215374, 'market_cap': 8093764660.602533, 'market_cap_dominance': 0.8798, 'fully_diluted_market_cap': 8093764660.6, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 6636, 'name': 'Polkadot', 'symbol': 'DOT', 'slug': 'polkadot-new', 'num_market_pairs': 414, 'date_added': '2020-08-19T00:00:00.000Z', 'tags': ['substrate', 'polkadot', 'binance-chain', 'polkadot-ecosystem', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio', 'arrington-xrp-capital-portfolio', 'blockchain-capital-portfolio', 'boostvc-portfolio', 'cms-holdings-portfolio', 'coinfund-portfolio', 'fabric-ventures-portfolio', 'fenbushi-capital-portfolio', 'hashkey-capital-portfolio', 'kenetic-capital-portfolio', '1confirmation-portfolio', 'placeholder-ventures-portfolio', 'pantera-capital-portfolio', 'exnetwork-capital-portfolio', 'web3', 'spartan-group', 'injective-ecosystem', 'bnb-chain'], 'max_supply': None, 'circulating_supply': 1119696242.3430254, 'total_supply': 1235119912.6682053, 'platform': None, 'cmc_rank': 11, 'self_reported_circulating_supply': 904869778, 'self_reported_market_cap': 5696613090.6929865, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 6.2955059713498205, 'volume_24h': 328794674.01325893, 'volume_change_24h': -22.6725, 'percent_change_1h': -0.42360157, 'percent_change_24h': -0.87584519, 'percent_change_7d': -7.65579969, 'percent_change_30d': -17.8841121, 'percent_change_60d': -10.71380307, 'percent_change_90d': -20.11981654, 'market_cap': 7049054379.768473, 'market_cap_dominance': 0.7662, 'fully_diluted_market_cap': 7775704785.54, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 4943, 'name': 'Dai', 'symbol': 'DAI', 'slug': 'multi-collateral-dai', 'num_market_pairs': 1374, 'date_added': '2019-11-22T00:00:00.000Z', 'tags': ['defi', 'stablecoin', 'asset-backed-stablecoin', 'ethereum-ecosystem', 'avalanche-ecosystem', 'polygon-ecosystem', 'fantom-ecosystem', 'arbitrum-ecosytem', 'harmony-ecosystem', 'moonriver-ecosystem', 'bnb-chain', 'usd-stablecoin'], 'max_supply': None, 'circulating_supply': 6979100352.697633, 'total_supply': 6979100352.697633, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x6b175474e89094c44da98b954eedeac495271d0f'}, 'cmc_rank': 12, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 0.9999836881523606, 'volume_24h': 344138156.86267847, 'volume_change_24h': -37.586, 'percent_change_1h': -0.08316713, 'percent_change_24h': 0.00345197, 'percent_change_7d': 0.06817614, 'percent_change_30d': 0.01105631, 'percent_change_60d': 0.02243926, 'percent_change_90d': 0.00708261, 'market_cap': 6978986510.67602, 'market_cap_dominance': 0.7587, 'fully_diluted_market_cap': 6978986510.68, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 3890, 'name': 'Polygon', 'symbol': 'MATIC', 'slug': 'polygon', 'num_market_pairs': 490, 'date_added': '2019-04-28T00:00:00.000Z', 'tags': ['platform', 'enterprise-solutions', 'scaling', 'state-channel', 'coinbase-ventures-portfolio', 'binance-launchpad', 'binance-labs-portfolio', 'polygon-ecosystem', 'moonriver-ecosystem', 'injective-ecosystem'], 'max_supply': 10000000000, 'circulating_supply': 8734317475.28493, 'total_supply': 10000000000, 'platform': None, 'cmc_rank': 13, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 0.73692945409146, 'volume_24h': 417288904.8319293, 'volume_change_24h': -24.5189, 'percent_change_1h': -0.41218686, 'percent_change_24h': 0.56928325, 'percent_change_7d': -7.74501157, 'percent_change_30d': -11.3988129, 'percent_change_60d': -11.00052452, 'percent_change_90d': 28.34896801, 'market_cap': 6436575808.923223, 'market_cap_dominance': 0.6997, 'fully_diluted_market_cap': 7369294540.91, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 5994, 'name': 'Shiba Inu', 'symbol': 'SHIB', 'slug': 'shiba-inu', 'num_market_pairs': 418, 'date_added': '2020-08-01T00:00:00.000Z', 'tags': ['memes', 'ethereum-ecosystem', 'doggone-doggerel'], 'max_supply': None, 'circulating_supply': 549063278876301.94, 'total_supply': 589735030408322.8, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce'}, 'cmc_rank': 14, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 1.0699173288888657e-05, 'volume_24h': 248461005.15293092, 'volume_change_24h': -31.9341, 'percent_change_1h': -0.01515738, 'percent_change_24h': 0.2045634, 'percent_change_7d': -7.39025917, 'percent_change_30d': -19.8796254, 'percent_change_60d': -4.87917953, 'percent_change_90d': -4.64334174, 'market_cap': 5874523167.262954, 'market_cap_dominance': 0.6385, 'fully_diluted_market_cap': 6309677284.87, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 1958, 'name': 'TRON', 'symbol': 'TRX', 'slug': 'tron', 'num_market_pairs': 685, 'date_added': '2017-09-13T00:00:00.000Z', 'tags': ['media', 'payments', 'tron-ecosystem'], 'max_supply': None, 'circulating_supply': 92354252560.35483, 'total_supply': 92354260195.82248, 'platform': None, 'cmc_rank': 15, 'self_reported_circulating_supply': 71659659264, 'self_reported_market_cap': 4279992344.159038, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 0.05972666334333518, 'volume_24h': 368114452.7355241, 'volume_change_24h': -22.9399, 'percent_change_1h': 0.16826398, 'percent_change_24h': 0.3714398, 'percent_change_7d': -1.85879618, 'percent_change_30d': -9.15257163, 'percent_change_60d': -7.66167963, 'percent_change_90d': -6.80847169, 'market_cap': 5516011350.9976635, 'market_cap_dominance': 0.5997, 'fully_diluted_market_cap': 5516011807.04, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 5805, 'name': 'Avalanche', 'symbol': 'AVAX', 'slug': 'avalanche', 'num_market_pairs': 317, 'date_added': '2020-07-13T00:00:00.000Z', 'tags': ['defi', 'smart-contracts', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio', 'avalanche-ecosystem', 'cms-holdings-portfolio', 'dragonfly-capital-portfolio', 'moonriver-ecosystem', 'injective-ecosystem'], 'max_supply': 720000000, 'circulating_supply': 295868160.8795907, 'total_supply': 404229626.49901325, 'platform': None, 'cmc_rank': 16, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 17.408085591581514, 'volume_24h': 265393593.40408823, 'volume_change_24h': -40.1051, 'percent_change_1h': -0.5854337, 'percent_change_24h': 0.76906834, 'percent_change_7d': -2.43554917, 'percent_change_30d': -25.85373103, 'percent_change_60d': -20.81908528, 'percent_change_90d': -13.40832189, 'market_cap': 5150498268.415724, 'market_cap_dominance': 0.5599, 'fully_diluted_market_cap': 12533821625.94, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 3717, 'name': 'Wrapped Bitcoin', 'symbol': 'WBTC', 'slug': 'wrapped-bitcoin', 'num_market_pairs': 610, 'date_added': '2019-01-30T00:00:00.000Z', 'tags': ['medium-of-exchange', 'defi', 'wrapped-tokens', 'fantom-ecosystem', 'arbitrum-ecosytem', 'moonriver-ecosystem'], 'max_supply': None, 'circulating_supply': 244707.06137105, 'total_supply': 244707.06137105, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x2260fac5e5542a773aa44fbcfedf7c193bc2c599'}, 'cmc_rank': 17, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 18688.628678795158, 'volume_24h': 238223186.49758652, 'volume_change_24h': -36.8562, 'percent_change_1h': -0.19241139, 'percent_change_24h': -1.06433766, 'percent_change_7d': -4.61538252, 'percent_change_30d': -14.01811077, 'percent_change_60d': -14.69056584, 'percent_change_90d': -10.99532918, 'market_cap': 4573239405.042691, 'market_cap_dominance': 0.4971, 'fully_diluted_market_cap': 4573239405.04, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 7083, 'name': 'Uniswap', 'symbol': 'UNI', 'slug': 'uniswap', 'num_market_pairs': 480, 'date_added': '2020-09-17T00:00:00.000Z', 'tags': ['decentralized-exchange', 'defi', 'dao', 'yield-farming', 'amm', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'governance', 'blockchain-capital-portfolio', 'defiance-capital-portfolio', 'alameda-research-portfolio', 'a16z-portfolio', 'pantera-capital-portfolio', 'parafi-capital', 'paradigm-portfolio', 'arbitrum-ecosytem', 'injective-ecosystem'], 'max_supply': 1000000000, 'circulating_supply': 762209326.5354977, 'total_supply': 1000000000, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x1f9840a85d5af5bf1d1762f925bdaddc4201f984'}, 'cmc_rank': 18, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': 0.86323126, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 5.816669654476778, 'volume_24h': 112572044.79909343, 'volume_change_24h': -25.6277, 'percent_change_1h': -0.40894393, 'percent_change_24h': 2.83436677, 'percent_change_7d': 0.64359168, 'percent_change_30d': -19.19172678, 'percent_change_60d': -20.50607542, 'percent_change_90d': 9.11806809, 'market_cap': 4433519860.01821, 'market_cap_dominance': 0.4819, 'fully_diluted_market_cap': 5816669654.48, 'tvl': 5135958401.74284, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 3794, 'name': 'Cosmos', 'symbol': 'ATOM', 'slug': 'cosmos', 'num_market_pairs': 345, 'date_added': '2019-03-14T00:00:00.000Z', 'tags': ['platform', 'cosmos-ecosystem', 'content-creation', 'interoperability', 'polychain-capital-portfolio', 'dragonfly-capital-portfolio', 'hashkey-capital-portfolio', '1confirmation-portfolio', 'paradigm-portfolio', 'exnetwork-capital-portfolio', 'injective-ecosystem'], 'max_supply': None, 'circulating_supply': 286370297, 'total_supply': 0, 'platform': None, 'cmc_rank': 19, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 13.713054199512476, 'volume_24h': 646360960.3805878, 'volume_change_24h': -20.6989, 'percent_change_1h': -0.69155133, 'percent_change_24h': -5.80956656, 'percent_change_7d': -14.26988442, 'percent_change_30d': 7.82776599, 'percent_change_60d': 47.49283214, 'percent_change_90d': 69.37994391, 'market_cap': 3927011403.8914847, 'market_cap_dominance': 0.4269, 'fully_diluted_market_cap': 0, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}, {'id': 3957, 'name': 'UNUS SED LEO', 'symbol': 'LEO', 'slug': 'unus-sed-leo', 'num_market_pairs': 20, 'date_added': '2019-05-21T00:00:00.000Z', 'tags': ['marketplace', 'centralized-exchange', 'discount-token', 'payments', 'kenetic-capital-portfolio', 'alameda-research-portfolio'], 'max_supply': None, 'circulating_supply': 953954130, 'total_supply': 985239504, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x2af5d2ad76741191d15dfe7bf6ac92d4bd912ca3'}, 'cmc_rank': 20, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:22:00.000Z', 'quote': {'USD': {'price': 4.104559993400015, 'volume_24h': 4276389.81202496, 'volume_change_24h': -15.446, 'percent_change_1h': -0.26505095, 'percent_change_24h': -13.57833878, 'percent_change_7d': -16.5227367, 'percent_change_30d': -22.28480909, 'percent_change_60d': -19.39862117, 'percent_change_90d': -30.55020061, 'market_cap': 3915561957.536717, 'market_cap_dominance': 0.4256, 'fully_diluted_market_cap': 4043974652.04, 'tvl': None, 'last_updated': '2022-09-23T16:22:00.000Z'}}}]}
    API Working
    {'status': {'timestamp': '2022-09-23T16:24:36.945Z', 'error_code': 0, 'error_message': None, 'elapsed': 36, 'credit_count': 1, 'notice': None, 'total_count': 9447}, 'data': [{'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'num_market_pairs': 9748, 'date_added': '2013-04-28T00:00:00.000Z', 'tags': ['mineable', 'pow', 'sha-256', 'store-of-value', 'state-channel', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio', 'binance-labs-portfolio', 'blockchain-capital-portfolio', 'boostvc-portfolio', 'cms-holdings-portfolio', 'dcg-portfolio', 'dragonfly-capital-portfolio', 'electric-capital-portfolio', 'fabric-ventures-portfolio', 'framework-ventures-portfolio', 'galaxy-digital-portfolio', 'huobi-capital-portfolio', 'alameda-research-portfolio', 'a16z-portfolio', '1confirmation-portfolio', 'winklevoss-capital-portfolio', 'usv-portfolio', 'placeholder-ventures-portfolio', 'pantera-capital-portfolio', 'multicoin-capital-portfolio', 'paradigm-portfolio'], 'max_supply': 21000000, 'circulating_supply': 19158581, 'total_supply': 19158581, 'platform': None, 'cmc_rank': 1, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 18704.6120597104, 'volume_24h': 37360436505.18902, 'volume_change_24h': -31.17, 'percent_change_1h': -0.12861366, 'percent_change_24h': -1.0554262, 'percent_change_7d': -4.48823781, 'percent_change_30d': -14.01475856, 'percent_change_60d': -14.59535322, 'percent_change_90d': -11.10099287, 'market_cap': 358353825219.5386, 'market_cap_dominance': 38.9519, 'fully_diluted_market_cap': 392796853253.92, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'num_market_pairs': 6103, 'date_added': '2015-08-07T00:00:00.000Z', 'tags': ['pos', 'smart-contracts', 'ethereum-ecosystem', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio', 'binance-labs-portfolio', 'blockchain-capital-portfolio', 'boostvc-portfolio', 'cms-holdings-portfolio', 'dcg-portfolio', 'dragonfly-capital-portfolio', 'electric-capital-portfolio', 'fabric-ventures-portfolio', 'framework-ventures-portfolio', 'hashkey-capital-portfolio', 'kenetic-capital-portfolio', 'huobi-capital-portfolio', 'alameda-research-portfolio', 'a16z-portfolio', '1confirmation-portfolio', 'winklevoss-capital-portfolio', 'usv-portfolio', 'placeholder-ventures-portfolio', 'pantera-capital-portfolio', 'multicoin-capital-portfolio', 'paradigm-portfolio', 'injective-ecosystem'], 'max_supply': None, 'circulating_supply': 122493377.499, 'total_supply': 122493377.499, 'platform': None, 'cmc_rank': 2, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 1291.3882709718487, 'volume_24h': 19032237417.189358, 'volume_change_24h': -23.0702, 'percent_change_1h': -0.16699925, 'percent_change_24h': 2.24763979, 'percent_change_7d': -10.19247247, 'percent_change_30d': -23.05389062, 'percent_change_60d': -15.09422226, 'percent_change_90d': 8.58922326, 'market_cap': 158186510973.93555, 'market_cap_dominance': 17.1944, 'fully_diluted_market_cap': 158186510973.94, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 825, 'name': 'Tether', 'symbol': 'USDT', 'slug': 'tether', 'num_market_pairs': 40036, 'date_added': '2015-02-25T00:00:00.000Z', 'tags': ['payments', 'stablecoin', 'asset-backed-stablecoin', 'avalanche-ecosystem', 'solana-ecosystem', 'arbitrum-ecosytem', 'moonriver-ecosystem', 'injective-ecosystem', 'bnb-chain', 'usd-stablecoin'], 'max_supply': None, 'circulating_supply': 67954703168.01751, 'total_supply': 70155449908.74805, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0xdac17f958d2ee523a2206206994597c13d831ec7'}, 'cmc_rank': 3, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 0.9999822385251477, 'volume_24h': 56744844608.56666, 'volume_change_24h': -20.3454, 'percent_change_1h': 0.00223546, 'percent_change_24h': -0.00603442, 'percent_change_7d': 0.00192583, 'percent_change_30d': -0.0050453, 'percent_change_60d': -0.00734709, 'percent_change_90d': 0.04630955, 'market_cap': 67953496192.26609, 'market_cap_dominance': 7.3863, 'fully_diluted_market_cap': 70154203844.49, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 3408, 'name': 'USD Coin', 'symbol': 'USDC', 'slug': 'usd-coin', 'num_market_pairs': 6295, 'date_added': '2018-10-08T00:00:00.000Z', 'tags': ['medium-of-exchange', 'stablecoin', 'asset-backed-stablecoin', 'fantom-ecosystem', 'arbitrum-ecosytem', 'moonriver-ecosystem', 'bnb-chain', 'usd-stablecoin'], 'max_supply': None, 'circulating_supply': 49836182660.77986, 'total_supply': 49836182660.77986, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'}, 'cmc_rank': 4, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 1.0000541028098133, 'volume_24h': 5156580026.385818, 'volume_change_24h': -23.6439, 'percent_change_1h': 0.00086827, 'percent_change_24h': -0.01155591, 'percent_change_7d': 0.01652085, 'percent_change_30d': 0.01641486, 'percent_change_60d': 0.00108966, 'percent_change_90d': -0.00180502, 'market_cap': 49838878938.29218, 'market_cap_dominance': 5.4173, 'fully_diluted_market_cap': 49838878938.29, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 1839, 'name': 'BNB', 'symbol': 'BNB', 'slug': 'bnb', 'num_market_pairs': 1110, 'date_added': '2017-07-25T00:00:00.000Z', 'tags': ['marketplace', 'centralized-exchange', 'payments', 'smart-contracts', 'alameda-research-portfolio', 'multicoin-capital-portfolio', 'moonriver-ecosystem', 'bnb-chain'], 'max_supply': 200000000, 'circulating_supply': 161337261.09, 'total_supply': 161337261.09, 'platform': None, 'cmc_rank': 5, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 271.03251611690695, 'volume_24h': 884656872.6178299, 'volume_change_24h': -21.2645, 'percent_change_1h': 0.0283548, 'percent_change_24h': 1.07993823, 'percent_change_7d': -0.83984663, 'percent_change_30d': -9.3158445, 'percent_change_60d': 5.83406043, 'percent_change_90d': 16.5809291, 'market_cap': 43727643816.63305, 'market_cap_dominance': 4.7531, 'fully_diluted_market_cap': 54206503223.38, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 52, 'name': 'XRP', 'symbol': 'XRP', 'slug': 'xrp', 'num_market_pairs': 820, 'date_added': '2013-08-04T00:00:00.000Z', 'tags': ['medium-of-exchange', 'enterprise-solutions', 'arrington-xrp-capital-portfolio', 'galaxy-digital-portfolio', 'a16z-portfolio', 'pantera-capital-portfolio'], 'max_supply': 100000000000, 'circulating_supply': 49848747475, 'total_supply': 99989294935, 'platform': None, 'cmc_rank': 6, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 0.48592045319260935, 'volume_24h': 7666772098.039272, 'volume_change_24h': 78.8399, 'percent_change_1h': -1.02668366, 'percent_change_24h': 12.30165599, 'percent_change_7d': 45.95615491, 'percent_change_30d': 40.22602134, 'percent_change_60d': 39.94803533, 'percent_change_90d': 36.01983185, 'market_cap': 24222525964.13594, 'market_cap_dominance': 2.6329, 'fully_diluted_market_cap': 48592045319.26, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 4687, 'name': 'Binance USD', 'symbol': 'BUSD', 'slug': 'binance-usd', 'num_market_pairs': 5163, 'date_added': '2019-09-20T00:00:00.000Z', 'tags': ['stablecoin', 'asset-backed-stablecoin', 'binance-chain', 'harmony-ecosystem', 'moonriver-ecosystem', 'usd-stablecoin'], 'max_supply': None, 'circulating_supply': 20517253084.589256, 'total_supply': 20517253084.589256, 'platform': {'id': 1839, 'name': 'BNB', 'symbol': 'BNB', 'slug': 'bnb', 'token_address': 'BUSD-BD1'}, 'cmc_rank': 7, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 0.9998755602238052, 'volume_24h': 9453500038.555975, 'volume_change_24h': -13.0923, 'percent_change_1h': -0.04438829, 'percent_change_24h': 0.01978891, 'percent_change_7d': -0.01973033, 'percent_change_30d': -0.009134, 'percent_change_60d': 0.11735237, 'percent_change_90d': -0.07198204, 'market_cap': 20514699922.20728, 'market_cap_dominance': 2.2299, 'fully_diluted_market_cap': 20514699922.21, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 2010, 'name': 'Cardano', 'symbol': 'ADA', 'slug': 'cardano', 'num_market_pairs': 571, 'date_added': '2017-10-01T00:00:00.000Z', 'tags': ['dpos', 'pos', 'platform', 'research', 'smart-contracts', 'staking', 'cardano-ecosystem', 'cardano'], 'max_supply': 45000000000, 'circulating_supply': 34227045077.067, 'total_supply': 34950580348.963, 'platform': None, 'cmc_rank': 8, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 0.45193017330771673, 'volume_24h': 1034509694.871, 'volume_change_24h': -5.9046, 'percent_change_1h': -0.24476787, 'percent_change_24h': 0.63164072, 'percent_change_7d': -1.63621434, 'percent_change_30d': -2.82265379, 'percent_change_60d': -8.12995252, 'percent_change_90d': -6.39506613, 'market_cap': 15468234413.489923, 'market_cap_dominance': 1.6803, 'fully_diluted_market_cap': 20336857798.85, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 5426, 'name': 'Solana', 'symbol': 'SOL', 'slug': 'solana', 'num_market_pairs': 386, 'date_added': '2020-04-10T00:00:00.000Z', 'tags': ['pos', 'platform', 'solana-ecosystem', 'cms-holdings-portfolio', 'kenetic-capital-portfolio', 'alameda-research-portfolio', 'multicoin-capital-portfolio', 'okex-blockdream-ventures-portfolio'], 'max_supply': None, 'circulating_supply': 354521459.37243974, 'total_supply': 511616946.142289, 'platform': None, 'cmc_rank': 9, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 31.55579895992627, 'volume_24h': 841099651.2703431, 'volume_change_24h': -37.291, 'percent_change_1h': -0.22417748, 'percent_change_24h': -0.60090684, 'percent_change_7d': -1.53565108, 'percent_change_30d': -12.5291544, 'percent_change_60d': -17.87202318, 'percent_change_90d': -21.155723, 'market_cap': 11187207898.936378, 'market_cap_dominance': 1.216, 'fully_diluted_market_cap': 16144481496.96, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 74, 'name': 'Dogecoin', 'symbol': 'DOGE', 'slug': 'dogecoin', 'num_market_pairs': 567, 'date_added': '2013-12-15T00:00:00.000Z', 'tags': ['mineable', 'pow', 'scrypt', 'medium-of-exchange', 'memes', 'payments', 'doggone-doggerel', 'bnb-chain'], 'max_supply': None, 'circulating_supply': 132670764299.89409, 'total_supply': 132670764299.89409, 'platform': None, 'cmc_rank': 10, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 0.06097535698725045, 'volume_24h': 467297047.56778824, 'volume_change_24h': 14.4922, 'percent_change_1h': 0.27224438, 'percent_change_24h': 3.47680914, 'percent_change_7d': 2.58033211, 'percent_change_30d': -11.67642435, 'percent_change_60d': -6.0246149, 'percent_change_90d': -7.38826468, 'market_cap': 8089647214.957404, 'market_cap_dominance': 0.8793, 'fully_diluted_market_cap': 8089647214.96, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 6636, 'name': 'Polkadot', 'symbol': 'DOT', 'slug': 'polkadot-new', 'num_market_pairs': 414, 'date_added': '2020-08-19T00:00:00.000Z', 'tags': ['substrate', 'polkadot', 'binance-chain', 'polkadot-ecosystem', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio', 'arrington-xrp-capital-portfolio', 'blockchain-capital-portfolio', 'boostvc-portfolio', 'cms-holdings-portfolio', 'coinfund-portfolio', 'fabric-ventures-portfolio', 'fenbushi-capital-portfolio', 'hashkey-capital-portfolio', 'kenetic-capital-portfolio', '1confirmation-portfolio', 'placeholder-ventures-portfolio', 'pantera-capital-portfolio', 'exnetwork-capital-portfolio', 'web3', 'spartan-group', 'injective-ecosystem', 'bnb-chain'], 'max_supply': None, 'circulating_supply': 1119696242.3430254, 'total_supply': 1235119912.6682053, 'platform': None, 'cmc_rank': 11, 'self_reported_circulating_supply': 904869778, 'self_reported_market_cap': 5695249872.936073, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 6.293999436608517, 'volume_24h': 328849892.65856916, 'volume_change_24h': -22.706, 'percent_change_1h': -0.44441109, 'percent_change_24h': -0.91891602, 'percent_change_7d': -7.64454777, 'percent_change_30d': -17.87384466, 'percent_change_60d': -10.73037208, 'percent_change_90d': -20.10428758, 'market_cap': 7047367518.479675, 'market_cap_dominance': 0.766, 'fully_diluted_market_cap': 7773844034.48, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 4943, 'name': 'Dai', 'symbol': 'DAI', 'slug': 'multi-collateral-dai', 'num_market_pairs': 1374, 'date_added': '2019-11-22T00:00:00.000Z', 'tags': ['defi', 'stablecoin', 'asset-backed-stablecoin', 'ethereum-ecosystem', 'avalanche-ecosystem', 'polygon-ecosystem', 'fantom-ecosystem', 'arbitrum-ecosytem', 'harmony-ecosystem', 'moonriver-ecosystem', 'bnb-chain', 'usd-stablecoin'], 'max_supply': None, 'circulating_supply': 6979100352.697633, 'total_supply': 6979100352.697633, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x6b175474e89094c44da98b954eedeac495271d0f'}, 'cmc_rank': 12, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 0.9999453525760814, 'volume_24h': 342518840.73626536, 'volume_change_24h': -37.9078, 'percent_change_1h': -0.0342913, 'percent_change_24h': -0.02266498, 'percent_change_7d': 0.07744538, 'percent_change_30d': 0.01629522, 'percent_change_60d': 0.02187079, 'percent_change_90d': 0.00692547, 'market_cap': 6978718962.842089, 'market_cap_dominance': 0.7581, 'fully_diluted_market_cap': 6978718962.84, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 3890, 'name': 'Polygon', 'symbol': 'MATIC', 'slug': 'polygon', 'num_market_pairs': 490, 'date_added': '2019-04-28T00:00:00.000Z', 'tags': ['platform', 'enterprise-solutions', 'scaling', 'state-channel', 'coinbase-ventures-portfolio', 'binance-launchpad', 'binance-labs-portfolio', 'polygon-ecosystem', 'moonriver-ecosystem', 'injective-ecosystem'], 'max_supply': 10000000000, 'circulating_supply': 8734317475.28493, 'total_supply': 10000000000, 'platform': None, 'cmc_rank': 13, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 0.7368091391005727, 'volume_24h': 417382294.30117834, 'volume_change_24h': -24.4963, 'percent_change_1h': -0.41261208, 'percent_change_24h': 0.56435191, 'percent_change_7d': -7.69643084, 'percent_change_30d': -11.37491584, 'percent_change_60d': -11.01057964, 'percent_change_90d': 28.38180724, 'market_cap': 6435524939.595777, 'market_cap_dominance': 0.6991, 'fully_diluted_market_cap': 7368091391.01, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 5994, 'name': 'Shiba Inu', 'symbol': 'SHIB', 'slug': 'shiba-inu', 'num_market_pairs': 418, 'date_added': '2020-08-01T00:00:00.000Z', 'tags': ['memes', 'ethereum-ecosystem', 'doggone-doggerel'], 'max_supply': None, 'circulating_supply': 549063278876301.94, 'total_supply': 589735030408322.8, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce'}, 'cmc_rank': 14, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 1.0697283118921347e-05, 'volume_24h': 248558006.93959475, 'volume_change_24h': -31.8972, 'percent_change_1h': -0.03070402, 'percent_change_24h': 0.18197223, 'percent_change_7d': -7.36558174, 'percent_change_30d': -19.86153798, 'percent_change_60d': -4.88999287, 'percent_change_90d': -4.59652589, 'market_cap': 5873485344.343069, 'market_cap_dominance': 0.6384, 'fully_diluted_market_cap': 6308562585.42, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 1958, 'name': 'TRON', 'symbol': 'TRX', 'slug': 'tron', 'num_market_pairs': 685, 'date_added': '2017-09-13T00:00:00.000Z', 'tags': ['media', 'payments', 'tron-ecosystem'], 'max_supply': None, 'circulating_supply': 92354252560.35483, 'total_supply': 92354260195.82248, 'platform': None, 'cmc_rank': 15, 'self_reported_circulating_supply': 71659659264, 'self_reported_market_cap': 4279415715.149901, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 0.059718616570366125, 'volume_24h': 368210303.8876786, 'volume_change_24h': -22.9202, 'percent_change_1h': 0.15099726, 'percent_change_24h': 0.36104942, 'percent_change_7d': -1.85002029, 'percent_change_30d': -9.16007544, 'percent_change_60d': -7.68119828, 'percent_change_90d': -6.80431111, 'market_cap': 5515268197.294584, 'market_cap_dominance': 0.5991, 'fully_diluted_market_cap': 5515268653.27, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 5805, 'name': 'Avalanche', 'symbol': 'AVAX', 'slug': 'avalanche', 'num_market_pairs': 317, 'date_added': '2020-07-13T00:00:00.000Z', 'tags': ['defi', 'smart-contracts', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio', 'avalanche-ecosystem', 'cms-holdings-portfolio', 'dragonfly-capital-portfolio', 'moonriver-ecosystem', 'injective-ecosystem'], 'max_supply': 720000000, 'circulating_supply': 295868160.8795907, 'total_supply': 404229626.49901325, 'platform': None, 'cmc_rank': 16, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 17.404952229994603, 'volume_24h': 265263679.95523503, 'volume_change_24h': -40.1354, 'percent_change_1h': -0.60271726, 'percent_change_24h': 0.7589894, 'percent_change_7d': -2.3739555, 'percent_change_30d': -25.83122456, 'percent_change_60d': -20.83184165, 'percent_change_90d': -13.39738798, 'market_cap': 5149571206.485634, 'market_cap_dominance': 0.5594, 'fully_diluted_market_cap': 12531565605.6, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 3717, 'name': 'Wrapped Bitcoin', 'symbol': 'WBTC', 'slug': 'wrapped-bitcoin', 'num_market_pairs': 610, 'date_added': '2019-01-30T00:00:00.000Z', 'tags': ['medium-of-exchange', 'defi', 'wrapped-tokens', 'fantom-ecosystem', 'arbitrum-ecosytem', 'moonriver-ecosystem'], 'max_supply': None, 'circulating_supply': 244707.06137105, 'total_supply': 244707.06137105, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x2260fac5e5542a773aa44fbcfedf7c193bc2c599'}, 'cmc_rank': 17, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 18699.161265658844, 'volume_24h': 238247123.84035248, 'volume_change_24h': -36.8974, 'percent_change_1h': -0.13494319, 'percent_change_24h': -1.0680471, 'percent_change_7d': -4.54218209, 'percent_change_30d': -13.94366585, 'percent_change_60d': -14.64407628, 'percent_change_90d': -10.92141458, 'market_cap': 4575816803.42274, 'market_cap_dominance': 0.4974, 'fully_diluted_market_cap': 4575816803.42, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 7083, 'name': 'Uniswap', 'symbol': 'UNI', 'slug': 'uniswap', 'num_market_pairs': 480, 'date_added': '2020-09-17T00:00:00.000Z', 'tags': ['decentralized-exchange', 'defi', 'dao', 'yield-farming', 'amm', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'governance', 'blockchain-capital-portfolio', 'defiance-capital-portfolio', 'alameda-research-portfolio', 'a16z-portfolio', 'pantera-capital-portfolio', 'parafi-capital', 'paradigm-portfolio', 'arbitrum-ecosytem', 'injective-ecosystem'], 'max_supply': 1000000000, 'circulating_supply': 762209326.5354977, 'total_supply': 1000000000, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x1f9840a85d5af5bf1d1762f925bdaddc4201f984'}, 'cmc_rank': 18, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': 0.86326893, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 5.816923477464185, 'volume_24h': 112491672.43369435, 'volume_change_24h': -25.7118, 'percent_change_1h': -0.38472164, 'percent_change_24h': 2.83618538, 'percent_change_7d': 0.71913689, 'percent_change_30d': -19.15848265, 'percent_change_60d': -20.46689509, 'percent_change_90d': 9.17649291, 'market_cap': 4433713326.266501, 'market_cap_dominance': 0.4819, 'fully_diluted_market_cap': 5816923477.46, 'tvl': 5135958401.74284, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 3794, 'name': 'Cosmos', 'symbol': 'ATOM', 'slug': 'cosmos', 'num_market_pairs': 345, 'date_added': '2019-03-14T00:00:00.000Z', 'tags': ['platform', 'cosmos-ecosystem', 'content-creation', 'interoperability', 'polychain-capital-portfolio', 'dragonfly-capital-portfolio', 'hashkey-capital-portfolio', '1confirmation-portfolio', 'paradigm-portfolio', 'exnetwork-capital-portfolio', 'injective-ecosystem'], 'max_supply': None, 'circulating_supply': 286370297, 'total_supply': 0, 'platform': None, 'cmc_rank': 19, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 13.707512842274427, 'volume_24h': 645508932.7349029, 'volume_change_24h': -20.8268, 'percent_change_1h': -0.74635824, 'percent_change_24h': -5.86648751, 'percent_change_7d': -14.27672007, 'percent_change_30d': 7.76054879, 'percent_change_60d': 47.45047779, 'percent_change_90d': 69.34901595, 'market_cap': 3925424523.773442, 'market_cap_dominance': 0.4264, 'fully_diluted_market_cap': 0, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}, {'id': 3957, 'name': 'UNUS SED LEO', 'symbol': 'LEO', 'slug': 'unus-sed-leo', 'num_market_pairs': 20, 'date_added': '2019-05-21T00:00:00.000Z', 'tags': ['marketplace', 'centralized-exchange', 'discount-token', 'payments', 'kenetic-capital-portfolio', 'alameda-research-portfolio'], 'max_supply': None, 'circulating_supply': 953954130, 'total_supply': 985239504, 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x2af5d2ad76741191d15dfe7bf6ac92d4bd912ca3'}, 'cmc_rank': 20, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2022-09-23T16:23:00.000Z', 'quote': {'USD': {'price': 4.103490744879567, 'volume_24h': 4274428.30119173, 'volume_change_24h': -15.4995, 'percent_change_1h': -0.22436872, 'percent_change_24h': -13.66303315, 'percent_change_7d': -16.49705478, 'percent_change_30d': -22.30886073, 'percent_change_60d': -19.38972417, 'percent_change_90d': -30.55626725, 'market_cap': 3914541943.494639, 'market_cap_dominance': 0.4255, 'fully_diluted_market_cap': 4042921186.15, 'tvl': None, 'last_updated': '2022-09-23T16:23:00.000Z'}}}]}
    API Working
    


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    Input In [54], in <cell line: 5>()
          6     api_runner()
          7     print('API Working')
    ----> 8     sleep(60)
          9 exit()
    

    KeyboardInterrupt: 



```python
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>symbol</th>
      <th>slug</th>
      <th>num_market_pairs</th>
      <th>date_added</th>
      <th>tags</th>
      <th>max_supply</th>
      <th>circulating_supply</th>
      <th>total_supply</th>
      <th>platform</th>
      <th>cmc_rank</th>
      <th>self_reported_circulating_supply</th>
      <th>self_reported_market_cap</th>
      <th>tvl_ratio</th>
      <th>last_updated</th>
      <th>quote.USD.price</th>
      <th>quote.USD.volume_24h</th>
      <th>quote.USD.volume_change_24h</th>
      <th>quote.USD.percent_change_1h</th>
      <th>quote.USD.percent_change_24h</th>
      <th>quote.USD.percent_change_7d</th>
      <th>quote.USD.percent_change_30d</th>
      <th>quote.USD.percent_change_60d</th>
      <th>quote.USD.percent_change_90d</th>
      <th>quote.USD.market_cap</th>
      <th>quote.USD.market_cap_dominance</th>
      <th>quote.USD.fully_diluted_market_cap</th>
      <th>quote.USD.tvl</th>
      <th>quote.USD.last_updated</th>
      <th>platform.id</th>
      <th>platform.name</th>
      <th>platform.symbol</th>
      <th>platform.slug</th>
      <th>platform.token_address</th>
      <th>timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bitcoin</td>
      <td>BTC</td>
      <td>bitcoin</td>
      <td>9748</td>
      <td>2013-04-28T00:00:00.000Z</td>
      <td>[mineable, pow, sha-256, store-of-value, state...</td>
      <td>2.100000e+07</td>
      <td>1.915850e+07</td>
      <td>1.915850e+07</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>18690.447224</td>
      <td>3.697756e+10</td>
      <td>-31.6811</td>
      <td>0.092014</td>
      <td>-1.183645</td>
      <td>-4.961169</td>
      <td>-13.025765</td>
      <td>-14.448737</td>
      <td>-11.473509</td>
      <td>3.580809e+11</td>
      <td>39.0140</td>
      <td>3.924994e+11</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1027</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>6103</td>
      <td>2015-08-07T00:00:00.000Z</td>
      <td>[pos, smart-contracts, ethereum-ecosystem, coi...</td>
      <td>NaN</td>
      <td>1.224922e+08</td>
      <td>1.224922e+08</td>
      <td>NaN</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1284.809475</td>
      <td>1.881477e+10</td>
      <td>-23.0881</td>
      <td>0.362895</td>
      <td>1.436718</td>
      <td>-11.169538</td>
      <td>-22.231748</td>
      <td>-15.518928</td>
      <td>7.655431</td>
      <td>1.573791e+11</td>
      <td>17.1469</td>
      <td>1.573791e+11</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>2</th>
      <td>825</td>
      <td>Tether</td>
      <td>USDT</td>
      <td>tether</td>
      <td>40036</td>
      <td>2015-02-25T00:00:00.000Z</td>
      <td>[payments, stablecoin, asset-backed-stablecoin...</td>
      <td>NaN</td>
      <td>6.795470e+10</td>
      <td>7.015545e+10</td>
      <td>NaN</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.999971</td>
      <td>5.453611e+10</td>
      <td>-22.7203</td>
      <td>-0.000375</td>
      <td>-0.010133</td>
      <td>0.000547</td>
      <td>-0.008118</td>
      <td>-0.008345</td>
      <td>0.047233</td>
      <td>6.795276e+10</td>
      <td>7.4037</td>
      <td>7.015345e+10</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0xdac17f958d2ee523a2206206994597c13d831ec7</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3408</td>
      <td>USD Coin</td>
      <td>USDC</td>
      <td>usd-coin</td>
      <td>6294</td>
      <td>2018-10-08T00:00:00.000Z</td>
      <td>[medium-of-exchange, stablecoin, asset-backed-...</td>
      <td>NaN</td>
      <td>4.976134e+10</td>
      <td>4.976134e+10</td>
      <td>NaN</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.999980</td>
      <td>5.113202e+09</td>
      <td>-23.5646</td>
      <td>0.001168</td>
      <td>-0.008946</td>
      <td>-0.004062</td>
      <td>-0.005491</td>
      <td>0.027822</td>
      <td>-0.024244</td>
      <td>4.976033e+10</td>
      <td>5.4215</td>
      <td>4.976033e+10</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1839</td>
      <td>BNB</td>
      <td>BNB</td>
      <td>bnb</td>
      <td>1110</td>
      <td>2017-07-25T00:00:00.000Z</td>
      <td>[marketplace, centralized-exchange, payments, ...</td>
      <td>2.000000e+08</td>
      <td>1.613373e+08</td>
      <td>1.613373e+08</td>
      <td>NaN</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>270.372280</td>
      <td>8.818450e+08</td>
      <td>-21.6284</td>
      <td>-0.095247</td>
      <td>0.937023</td>
      <td>-1.559470</td>
      <td>-8.798327</td>
      <td>5.766740</td>
      <td>15.591895</td>
      <td>4.362112e+10</td>
      <td>4.7526</td>
      <td>5.407446e+10</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>5</th>
      <td>52</td>
      <td>XRP</td>
      <td>XRP</td>
      <td>xrp</td>
      <td>820</td>
      <td>2013-08-04T00:00:00.000Z</td>
      <td>[medium-of-exchange, enterprise-solutions, arr...</td>
      <td>1.000000e+11</td>
      <td>4.984875e+10</td>
      <td>9.998929e+10</td>
      <td>NaN</td>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.483097</td>
      <td>7.555719e+09</td>
      <td>78.0965</td>
      <td>0.185627</td>
      <td>9.861398</td>
      <td>45.840567</td>
      <td>40.496069</td>
      <td>39.836106</td>
      <td>33.939712</td>
      <td>2.408176e+10</td>
      <td>2.6238</td>
      <td>4.830966e+10</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4687</td>
      <td>Binance USD</td>
      <td>BUSD</td>
      <td>binance-usd</td>
      <td>5163</td>
      <td>2019-09-20T00:00:00.000Z</td>
      <td>[stablecoin, asset-backed-stablecoin, binance-...</td>
      <td>NaN</td>
      <td>2.051725e+10</td>
      <td>2.051725e+10</td>
      <td>NaN</td>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.999843</td>
      <td>9.505003e+09</td>
      <td>-10.9604</td>
      <td>-0.024826</td>
      <td>-0.070004</td>
      <td>-0.066687</td>
      <td>-0.019537</td>
      <td>-0.109915</td>
      <td>0.002981</td>
      <td>2.051403e+10</td>
      <td>2.2351</td>
      <td>2.051403e+10</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1839.0</td>
      <td>BNB</td>
      <td>BNB</td>
      <td>bnb</td>
      <td>BUSD-BD1</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2010</td>
      <td>Cardano</td>
      <td>ADA</td>
      <td>cardano</td>
      <td>571</td>
      <td>2017-10-01T00:00:00.000Z</td>
      <td>[dpos, pos, platform, research, smart-contract...</td>
      <td>4.500000e+10</td>
      <td>3.422704e+10</td>
      <td>3.495058e+10</td>
      <td>NaN</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.450998</td>
      <td>1.025815e+09</td>
      <td>-6.5417</td>
      <td>0.086903</td>
      <td>0.714229</td>
      <td>-1.837934</td>
      <td>-2.135991</td>
      <td>-8.023954</td>
      <td>-7.096349</td>
      <td>1.543631e+10</td>
      <td>1.6808</td>
      <td>2.029489e+10</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5426</td>
      <td>Solana</td>
      <td>SOL</td>
      <td>solana</td>
      <td>386</td>
      <td>2020-04-10T00:00:00.000Z</td>
      <td>[pos, platform, solana-ecosystem, cms-holdings...</td>
      <td>NaN</td>
      <td>3.545215e+08</td>
      <td>5.116169e+08</td>
      <td>NaN</td>
      <td>9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>31.462854</td>
      <td>8.349625e+08</td>
      <td>-37.0503</td>
      <td>0.023626</td>
      <td>-0.868863</td>
      <td>-2.644970</td>
      <td>-11.140947</td>
      <td>-18.814217</td>
      <td>-21.648069</td>
      <td>1.115426e+10</td>
      <td>1.2153</td>
      <td>1.609693e+10</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>9</th>
      <td>74</td>
      <td>Dogecoin</td>
      <td>DOGE</td>
      <td>dogecoin</td>
      <td>567</td>
      <td>2013-12-15T00:00:00.000Z</td>
      <td>[mineable, pow, scrypt, medium-of-exchange, me...</td>
      <td>NaN</td>
      <td>1.326708e+11</td>
      <td>1.326708e+11</td>
      <td>NaN</td>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.060442</td>
      <td>4.453705e+08</td>
      <td>9.5092</td>
      <td>0.631072</td>
      <td>2.581872</td>
      <td>1.584151</td>
      <td>-11.193288</td>
      <td>-6.799507</td>
      <td>-8.730580</td>
      <td>8.018896e+09</td>
      <td>0.8737</td>
      <td>8.018896e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>10</th>
      <td>6636</td>
      <td>Polkadot</td>
      <td>DOT</td>
      <td>polkadot-new</td>
      <td>414</td>
      <td>2020-08-19T00:00:00.000Z</td>
      <td>[substrate, polkadot, binance-chain, polkadot-...</td>
      <td>NaN</td>
      <td>1.119486e+09</td>
      <td>1.234910e+09</td>
      <td>NaN</td>
      <td>11</td>
      <td>9.048698e+08</td>
      <td>5.695242e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>6.293991</td>
      <td>3.240994e+08</td>
      <td>-23.8718</td>
      <td>0.662719</td>
      <td>-0.819408</td>
      <td>-7.910204</td>
      <td>-16.832140</td>
      <td>-10.567599</td>
      <td>-20.652915</td>
      <td>7.046034e+09</td>
      <td>0.7677</td>
      <td>7.772509e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>11</th>
      <td>4943</td>
      <td>Dai</td>
      <td>DAI</td>
      <td>multi-collateral-dai</td>
      <td>1374</td>
      <td>2019-11-22T00:00:00.000Z</td>
      <td>[defi, stablecoin, asset-backed-stablecoin, et...</td>
      <td>NaN</td>
      <td>6.981238e+09</td>
      <td>6.981238e+09</td>
      <td>NaN</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1.000202</td>
      <td>3.471199e+08</td>
      <td>-35.3891</td>
      <td>0.042195</td>
      <td>0.049879</td>
      <td>0.070674</td>
      <td>0.007651</td>
      <td>0.100560</td>
      <td>0.052914</td>
      <td>6.982651e+09</td>
      <td>0.7603</td>
      <td>6.982651e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x6b175474e89094c44da98b954eedeac495271d0f</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>12</th>
      <td>3890</td>
      <td>Polygon</td>
      <td>MATIC</td>
      <td>polygon</td>
      <td>490</td>
      <td>2019-04-28T00:00:00.000Z</td>
      <td>[platform, enterprise-solutions, scaling, stat...</td>
      <td>1.000000e+10</td>
      <td>8.734317e+09</td>
      <td>1.000000e+10</td>
      <td>NaN</td>
      <td>13</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.735229</td>
      <td>4.150555e+08</td>
      <td>-22.7951</td>
      <td>0.589796</td>
      <td>0.317744</td>
      <td>-8.358627</td>
      <td>-10.180705</td>
      <td>-10.746476</td>
      <td>27.282756</td>
      <td>6.421725e+09</td>
      <td>0.6992</td>
      <td>7.352291e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>13</th>
      <td>5994</td>
      <td>Shiba Inu</td>
      <td>SHIB</td>
      <td>shiba-inu</td>
      <td>418</td>
      <td>2020-08-01T00:00:00.000Z</td>
      <td>[memes, ethereum-ecosystem, doggone-doggerel]</td>
      <td>NaN</td>
      <td>5.490633e+14</td>
      <td>5.897350e+14</td>
      <td>NaN</td>
      <td>14</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.000011</td>
      <td>2.449805e+08</td>
      <td>-31.0835</td>
      <td>0.315214</td>
      <td>-0.310681</td>
      <td>-8.057488</td>
      <td>-19.112404</td>
      <td>-4.954557</td>
      <td>-5.285059</td>
      <td>5.850752e+09</td>
      <td>0.6375</td>
      <td>6.284145e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1958</td>
      <td>TRON</td>
      <td>TRX</td>
      <td>tron</td>
      <td>685</td>
      <td>2017-09-13T00:00:00.000Z</td>
      <td>[media, payments, tron-ecosystem]</td>
      <td>NaN</td>
      <td>9.235461e+10</td>
      <td>9.235464e+10</td>
      <td>NaN</td>
      <td>15</td>
      <td>7.165966e+10</td>
      <td>4.266067e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.059532</td>
      <td>3.627441e+08</td>
      <td>-24.5800</td>
      <td>0.117565</td>
      <td>0.165079</td>
      <td>-2.238187</td>
      <td>-8.944557</td>
      <td>-7.877781</td>
      <td>-7.384924</td>
      <td>5.498086e+09</td>
      <td>0.5987</td>
      <td>5.498088e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>15</th>
      <td>5805</td>
      <td>Avalanche</td>
      <td>AVAX</td>
      <td>avalanche</td>
      <td>317</td>
      <td>2020-07-13T00:00:00.000Z</td>
      <td>[defi, smart-contracts, three-arrows-capital-p...</td>
      <td>7.200000e+08</td>
      <td>2.958662e+08</td>
      <td>4.042296e+08</td>
      <td>NaN</td>
      <td>16</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>17.429109</td>
      <td>2.648634e+08</td>
      <td>-40.0494</td>
      <td>0.595816</td>
      <td>0.937505</td>
      <td>-2.968761</td>
      <td>-24.583082</td>
      <td>-20.563099</td>
      <td>-14.135038</td>
      <td>5.156685e+09</td>
      <td>0.5615</td>
      <td>1.254896e+10</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>16</th>
      <td>3717</td>
      <td>Wrapped Bitcoin</td>
      <td>WBTC</td>
      <td>wrapped-bitcoin</td>
      <td>610</td>
      <td>2019-01-30T00:00:00.000Z</td>
      <td>[medium-of-exchange, defi, wrapped-tokens, fan...</td>
      <td>NaN</td>
      <td>2.447071e+05</td>
      <td>2.447071e+05</td>
      <td>NaN</td>
      <td>17</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>18684.247625</td>
      <td>2.324476e+08</td>
      <td>-37.4347</td>
      <td>0.100555</td>
      <td>-1.194546</td>
      <td>-4.969071</td>
      <td>-13.017046</td>
      <td>-14.565239</td>
      <td>-11.385902</td>
      <td>4.572167e+09</td>
      <td>0.4982</td>
      <td>4.572167e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x2260fac5e5542a773aa44fbcfedf7c193bc2c599</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>17</th>
      <td>7083</td>
      <td>Uniswap</td>
      <td>UNI</td>
      <td>uniswap</td>
      <td>480</td>
      <td>2020-09-17T00:00:00.000Z</td>
      <td>[decentralized-exchange, defi, dao, yield-farm...</td>
      <td>1.000000e+09</td>
      <td>7.622093e+08</td>
      <td>1.000000e+09</td>
      <td>NaN</td>
      <td>18</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.863913</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>5.821264</td>
      <td>1.121573e+08</td>
      <td>-18.2148</td>
      <td>0.618017</td>
      <td>3.090884</td>
      <td>0.689373</td>
      <td>-17.734691</td>
      <td>-19.045531</td>
      <td>8.789876</td>
      <td>4.437022e+09</td>
      <td>0.4834</td>
      <td>5.821264e+09</td>
      <td>5.135958e+09</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x1f9840a85d5af5bf1d1762f925bdaddc4201f984</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>18</th>
      <td>3794</td>
      <td>Cosmos</td>
      <td>ATOM</td>
      <td>cosmos</td>
      <td>345</td>
      <td>2019-03-14T00:00:00.000Z</td>
      <td>[platform, cosmos-ecosystem, content-creation,...</td>
      <td>NaN</td>
      <td>2.863703e+08</td>
      <td>0.000000e+00</td>
      <td>NaN</td>
      <td>19</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>13.732286</td>
      <td>6.856706e+08</td>
      <td>-3.3366</td>
      <td>0.461647</td>
      <td>-2.142435</td>
      <td>-14.796857</td>
      <td>12.144440</td>
      <td>48.331119</td>
      <td>68.831149</td>
      <td>3.932519e+09</td>
      <td>0.4282</td>
      <td>0.000000e+00</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>19</th>
      <td>3957</td>
      <td>UNUS SED LEO</td>
      <td>LEO</td>
      <td>unus-sed-leo</td>
      <td>20</td>
      <td>2019-05-21T00:00:00.000Z</td>
      <td>[marketplace, centralized-exchange, discount-t...</td>
      <td>NaN</td>
      <td>9.539541e+08</td>
      <td>9.852395e+08</td>
      <td>NaN</td>
      <td>20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>4.113495</td>
      <td>4.927387e+06</td>
      <td>-10.1660</td>
      <td>0.138933</td>
      <td>-13.454115</td>
      <td>-16.490861</td>
      <td>-22.061201</td>
      <td>-19.108688</td>
      <td>-30.456264</td>
      <td>3.924086e+09</td>
      <td>0.4275</td>
      <td>4.052778e+09</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x2af5d2ad76741191d15dfe7bf6ac92d4bd912ca3</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bitcoin</td>
      <td>BTC</td>
      <td>bitcoin</td>
      <td>9748</td>
      <td>2013-04-28T00:00:00.000Z</td>
      <td>[mineable, pow, sha-256, store-of-value, state...</td>
      <td>2.100000e+07</td>
      <td>1.915858e+07</td>
      <td>1.915858e+07</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>18704.612060</td>
      <td>3.736044e+10</td>
      <td>-31.1700</td>
      <td>-0.128614</td>
      <td>-1.055426</td>
      <td>-4.488238</td>
      <td>-14.014759</td>
      <td>-14.595353</td>
      <td>-11.100993</td>
      <td>3.583538e+11</td>
      <td>38.9519</td>
      <td>3.927969e+11</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1027</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>6103</td>
      <td>2015-08-07T00:00:00.000Z</td>
      <td>[pos, smart-contracts, ethereum-ecosystem, coi...</td>
      <td>NaN</td>
      <td>1.224934e+08</td>
      <td>1.224934e+08</td>
      <td>NaN</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1291.388271</td>
      <td>1.903224e+10</td>
      <td>-23.0702</td>
      <td>-0.166999</td>
      <td>2.247640</td>
      <td>-10.192472</td>
      <td>-23.053891</td>
      <td>-15.094222</td>
      <td>8.589223</td>
      <td>1.581865e+11</td>
      <td>17.1944</td>
      <td>1.581865e+11</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>2</th>
      <td>825</td>
      <td>Tether</td>
      <td>USDT</td>
      <td>tether</td>
      <td>40036</td>
      <td>2015-02-25T00:00:00.000Z</td>
      <td>[payments, stablecoin, asset-backed-stablecoin...</td>
      <td>NaN</td>
      <td>6.795470e+10</td>
      <td>7.015545e+10</td>
      <td>NaN</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.999982</td>
      <td>5.674484e+10</td>
      <td>-20.3454</td>
      <td>0.002235</td>
      <td>-0.006034</td>
      <td>0.001926</td>
      <td>-0.005045</td>
      <td>-0.007347</td>
      <td>0.046310</td>
      <td>6.795350e+10</td>
      <td>7.3863</td>
      <td>7.015420e+10</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0xdac17f958d2ee523a2206206994597c13d831ec7</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3408</td>
      <td>USD Coin</td>
      <td>USDC</td>
      <td>usd-coin</td>
      <td>6295</td>
      <td>2018-10-08T00:00:00.000Z</td>
      <td>[medium-of-exchange, stablecoin, asset-backed-...</td>
      <td>NaN</td>
      <td>4.983618e+10</td>
      <td>4.983618e+10</td>
      <td>NaN</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1.000054</td>
      <td>5.156580e+09</td>
      <td>-23.6439</td>
      <td>0.000868</td>
      <td>-0.011556</td>
      <td>0.016521</td>
      <td>0.016415</td>
      <td>0.001090</td>
      <td>-0.001805</td>
      <td>4.983888e+10</td>
      <td>5.4173</td>
      <td>4.983888e+10</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1839</td>
      <td>BNB</td>
      <td>BNB</td>
      <td>bnb</td>
      <td>1110</td>
      <td>2017-07-25T00:00:00.000Z</td>
      <td>[marketplace, centralized-exchange, payments, ...</td>
      <td>2.000000e+08</td>
      <td>1.613373e+08</td>
      <td>1.613373e+08</td>
      <td>NaN</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>271.032516</td>
      <td>8.846569e+08</td>
      <td>-21.2645</td>
      <td>0.028355</td>
      <td>1.079938</td>
      <td>-0.839847</td>
      <td>-9.315845</td>
      <td>5.834060</td>
      <td>16.580929</td>
      <td>4.372764e+10</td>
      <td>4.7531</td>
      <td>5.420650e+10</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>5</th>
      <td>52</td>
      <td>XRP</td>
      <td>XRP</td>
      <td>xrp</td>
      <td>820</td>
      <td>2013-08-04T00:00:00.000Z</td>
      <td>[medium-of-exchange, enterprise-solutions, arr...</td>
      <td>1.000000e+11</td>
      <td>4.984875e+10</td>
      <td>9.998929e+10</td>
      <td>NaN</td>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.485920</td>
      <td>7.666772e+09</td>
      <td>78.8399</td>
      <td>-1.026684</td>
      <td>12.301656</td>
      <td>45.956155</td>
      <td>40.226021</td>
      <td>39.948035</td>
      <td>36.019832</td>
      <td>2.422253e+10</td>
      <td>2.6329</td>
      <td>4.859205e+10</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4687</td>
      <td>Binance USD</td>
      <td>BUSD</td>
      <td>binance-usd</td>
      <td>5163</td>
      <td>2019-09-20T00:00:00.000Z</td>
      <td>[stablecoin, asset-backed-stablecoin, binance-...</td>
      <td>NaN</td>
      <td>2.051725e+10</td>
      <td>2.051725e+10</td>
      <td>NaN</td>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.999876</td>
      <td>9.453500e+09</td>
      <td>-13.0923</td>
      <td>-0.044388</td>
      <td>0.019789</td>
      <td>-0.019730</td>
      <td>-0.009134</td>
      <td>0.117352</td>
      <td>-0.071982</td>
      <td>2.051470e+10</td>
      <td>2.2299</td>
      <td>2.051470e+10</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1839.0</td>
      <td>BNB</td>
      <td>BNB</td>
      <td>bnb</td>
      <td>BUSD-BD1</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2010</td>
      <td>Cardano</td>
      <td>ADA</td>
      <td>cardano</td>
      <td>571</td>
      <td>2017-10-01T00:00:00.000Z</td>
      <td>[dpos, pos, platform, research, smart-contract...</td>
      <td>4.500000e+10</td>
      <td>3.422705e+10</td>
      <td>3.495058e+10</td>
      <td>NaN</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.451930</td>
      <td>1.034510e+09</td>
      <td>-5.9046</td>
      <td>-0.244768</td>
      <td>0.631641</td>
      <td>-1.636214</td>
      <td>-2.822654</td>
      <td>-8.129953</td>
      <td>-6.395066</td>
      <td>1.546823e+10</td>
      <td>1.6803</td>
      <td>2.033686e+10</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5426</td>
      <td>Solana</td>
      <td>SOL</td>
      <td>solana</td>
      <td>386</td>
      <td>2020-04-10T00:00:00.000Z</td>
      <td>[pos, platform, solana-ecosystem, cms-holdings...</td>
      <td>NaN</td>
      <td>3.545215e+08</td>
      <td>5.116169e+08</td>
      <td>NaN</td>
      <td>9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>31.555799</td>
      <td>8.410997e+08</td>
      <td>-37.2910</td>
      <td>-0.224177</td>
      <td>-0.600907</td>
      <td>-1.535651</td>
      <td>-12.529154</td>
      <td>-17.872023</td>
      <td>-21.155723</td>
      <td>1.118721e+10</td>
      <td>1.2160</td>
      <td>1.614448e+10</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>9</th>
      <td>74</td>
      <td>Dogecoin</td>
      <td>DOGE</td>
      <td>dogecoin</td>
      <td>567</td>
      <td>2013-12-15T00:00:00.000Z</td>
      <td>[mineable, pow, scrypt, medium-of-exchange, me...</td>
      <td>NaN</td>
      <td>1.326708e+11</td>
      <td>1.326708e+11</td>
      <td>NaN</td>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.060975</td>
      <td>4.672970e+08</td>
      <td>14.4922</td>
      <td>0.272244</td>
      <td>3.476809</td>
      <td>2.580332</td>
      <td>-11.676424</td>
      <td>-6.024615</td>
      <td>-7.388265</td>
      <td>8.089647e+09</td>
      <td>0.8793</td>
      <td>8.089647e+09</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>10</th>
      <td>6636</td>
      <td>Polkadot</td>
      <td>DOT</td>
      <td>polkadot-new</td>
      <td>414</td>
      <td>2020-08-19T00:00:00.000Z</td>
      <td>[substrate, polkadot, binance-chain, polkadot-...</td>
      <td>NaN</td>
      <td>1.119696e+09</td>
      <td>1.235120e+09</td>
      <td>NaN</td>
      <td>11</td>
      <td>9.048698e+08</td>
      <td>5.695250e+09</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>6.293999</td>
      <td>3.288499e+08</td>
      <td>-22.7060</td>
      <td>-0.444411</td>
      <td>-0.918916</td>
      <td>-7.644548</td>
      <td>-17.873845</td>
      <td>-10.730372</td>
      <td>-20.104288</td>
      <td>7.047368e+09</td>
      <td>0.7660</td>
      <td>7.773844e+09</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>11</th>
      <td>4943</td>
      <td>Dai</td>
      <td>DAI</td>
      <td>multi-collateral-dai</td>
      <td>1374</td>
      <td>2019-11-22T00:00:00.000Z</td>
      <td>[defi, stablecoin, asset-backed-stablecoin, et...</td>
      <td>NaN</td>
      <td>6.979100e+09</td>
      <td>6.979100e+09</td>
      <td>NaN</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.999945</td>
      <td>3.425188e+08</td>
      <td>-37.9078</td>
      <td>-0.034291</td>
      <td>-0.022665</td>
      <td>0.077445</td>
      <td>0.016295</td>
      <td>0.021871</td>
      <td>0.006925</td>
      <td>6.978719e+09</td>
      <td>0.7581</td>
      <td>6.978719e+09</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x6b175474e89094c44da98b954eedeac495271d0f</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>12</th>
      <td>3890</td>
      <td>Polygon</td>
      <td>MATIC</td>
      <td>polygon</td>
      <td>490</td>
      <td>2019-04-28T00:00:00.000Z</td>
      <td>[platform, enterprise-solutions, scaling, stat...</td>
      <td>1.000000e+10</td>
      <td>8.734317e+09</td>
      <td>1.000000e+10</td>
      <td>NaN</td>
      <td>13</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.736809</td>
      <td>4.173823e+08</td>
      <td>-24.4963</td>
      <td>-0.412612</td>
      <td>0.564352</td>
      <td>-7.696431</td>
      <td>-11.374916</td>
      <td>-11.010580</td>
      <td>28.381807</td>
      <td>6.435525e+09</td>
      <td>0.6991</td>
      <td>7.368091e+09</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>13</th>
      <td>5994</td>
      <td>Shiba Inu</td>
      <td>SHIB</td>
      <td>shiba-inu</td>
      <td>418</td>
      <td>2020-08-01T00:00:00.000Z</td>
      <td>[memes, ethereum-ecosystem, doggone-doggerel]</td>
      <td>NaN</td>
      <td>5.490633e+14</td>
      <td>5.897350e+14</td>
      <td>NaN</td>
      <td>14</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.000011</td>
      <td>2.485580e+08</td>
      <td>-31.8972</td>
      <td>-0.030704</td>
      <td>0.181972</td>
      <td>-7.365582</td>
      <td>-19.861538</td>
      <td>-4.889993</td>
      <td>-4.596526</td>
      <td>5.873485e+09</td>
      <td>0.6384</td>
      <td>6.308563e+09</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1958</td>
      <td>TRON</td>
      <td>TRX</td>
      <td>tron</td>
      <td>685</td>
      <td>2017-09-13T00:00:00.000Z</td>
      <td>[media, payments, tron-ecosystem]</td>
      <td>NaN</td>
      <td>9.235425e+10</td>
      <td>9.235426e+10</td>
      <td>NaN</td>
      <td>15</td>
      <td>7.165966e+10</td>
      <td>4.279416e+09</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.059719</td>
      <td>3.682103e+08</td>
      <td>-22.9202</td>
      <td>0.150997</td>
      <td>0.361049</td>
      <td>-1.850020</td>
      <td>-9.160075</td>
      <td>-7.681198</td>
      <td>-6.804311</td>
      <td>5.515268e+09</td>
      <td>0.5991</td>
      <td>5.515269e+09</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>15</th>
      <td>5805</td>
      <td>Avalanche</td>
      <td>AVAX</td>
      <td>avalanche</td>
      <td>317</td>
      <td>2020-07-13T00:00:00.000Z</td>
      <td>[defi, smart-contracts, three-arrows-capital-p...</td>
      <td>7.200000e+08</td>
      <td>2.958682e+08</td>
      <td>4.042296e+08</td>
      <td>NaN</td>
      <td>16</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>17.404952</td>
      <td>2.652637e+08</td>
      <td>-40.1354</td>
      <td>-0.602717</td>
      <td>0.758989</td>
      <td>-2.373956</td>
      <td>-25.831225</td>
      <td>-20.831842</td>
      <td>-13.397388</td>
      <td>5.149571e+09</td>
      <td>0.5594</td>
      <td>1.253157e+10</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>16</th>
      <td>3717</td>
      <td>Wrapped Bitcoin</td>
      <td>WBTC</td>
      <td>wrapped-bitcoin</td>
      <td>610</td>
      <td>2019-01-30T00:00:00.000Z</td>
      <td>[medium-of-exchange, defi, wrapped-tokens, fan...</td>
      <td>NaN</td>
      <td>2.447071e+05</td>
      <td>2.447071e+05</td>
      <td>NaN</td>
      <td>17</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>18699.161266</td>
      <td>2.382471e+08</td>
      <td>-36.8974</td>
      <td>-0.134943</td>
      <td>-1.068047</td>
      <td>-4.542182</td>
      <td>-13.943666</td>
      <td>-14.644076</td>
      <td>-10.921415</td>
      <td>4.575817e+09</td>
      <td>0.4974</td>
      <td>4.575817e+09</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x2260fac5e5542a773aa44fbcfedf7c193bc2c599</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>17</th>
      <td>7083</td>
      <td>Uniswap</td>
      <td>UNI</td>
      <td>uniswap</td>
      <td>480</td>
      <td>2020-09-17T00:00:00.000Z</td>
      <td>[decentralized-exchange, defi, dao, yield-farm...</td>
      <td>1.000000e+09</td>
      <td>7.622093e+08</td>
      <td>1.000000e+09</td>
      <td>NaN</td>
      <td>18</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.863269</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>5.816923</td>
      <td>1.124917e+08</td>
      <td>-25.7118</td>
      <td>-0.384722</td>
      <td>2.836185</td>
      <td>0.719137</td>
      <td>-19.158483</td>
      <td>-20.466895</td>
      <td>9.176493</td>
      <td>4.433713e+09</td>
      <td>0.4819</td>
      <td>5.816923e+09</td>
      <td>5.135958e+09</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x1f9840a85d5af5bf1d1762f925bdaddc4201f984</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>18</th>
      <td>3794</td>
      <td>Cosmos</td>
      <td>ATOM</td>
      <td>cosmos</td>
      <td>345</td>
      <td>2019-03-14T00:00:00.000Z</td>
      <td>[platform, cosmos-ecosystem, content-creation,...</td>
      <td>NaN</td>
      <td>2.863703e+08</td>
      <td>0.000000e+00</td>
      <td>NaN</td>
      <td>19</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>13.707513</td>
      <td>6.455089e+08</td>
      <td>-20.8268</td>
      <td>-0.746358</td>
      <td>-5.866488</td>
      <td>-14.276720</td>
      <td>7.760549</td>
      <td>47.450478</td>
      <td>69.349016</td>
      <td>3.925425e+09</td>
      <td>0.4264</td>
      <td>0.000000e+00</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>19</th>
      <td>3957</td>
      <td>UNUS SED LEO</td>
      <td>LEO</td>
      <td>unus-sed-leo</td>
      <td>20</td>
      <td>2019-05-21T00:00:00.000Z</td>
      <td>[marketplace, centralized-exchange, discount-t...</td>
      <td>NaN</td>
      <td>9.539541e+08</td>
      <td>9.852395e+08</td>
      <td>NaN</td>
      <td>20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>4.103491</td>
      <td>4.274428e+06</td>
      <td>-15.4995</td>
      <td>-0.224369</td>
      <td>-13.663033</td>
      <td>-16.497055</td>
      <td>-22.308861</td>
      <td>-19.389724</td>
      <td>-30.556267</td>
      <td>3.914542e+09</td>
      <td>0.4255</td>
      <td>4.042921e+09</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x2af5d2ad76741191d15dfe7bf6ac92d4bd912ca3</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.set_option('display.float_format', lambda x: '%.5f' % x)
```


```python
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>symbol</th>
      <th>slug</th>
      <th>num_market_pairs</th>
      <th>date_added</th>
      <th>tags</th>
      <th>max_supply</th>
      <th>circulating_supply</th>
      <th>total_supply</th>
      <th>platform</th>
      <th>cmc_rank</th>
      <th>self_reported_circulating_supply</th>
      <th>self_reported_market_cap</th>
      <th>tvl_ratio</th>
      <th>last_updated</th>
      <th>quote.USD.price</th>
      <th>quote.USD.volume_24h</th>
      <th>quote.USD.volume_change_24h</th>
      <th>quote.USD.percent_change_1h</th>
      <th>quote.USD.percent_change_24h</th>
      <th>quote.USD.percent_change_7d</th>
      <th>quote.USD.percent_change_30d</th>
      <th>quote.USD.percent_change_60d</th>
      <th>quote.USD.percent_change_90d</th>
      <th>quote.USD.market_cap</th>
      <th>quote.USD.market_cap_dominance</th>
      <th>quote.USD.fully_diluted_market_cap</th>
      <th>quote.USD.tvl</th>
      <th>quote.USD.last_updated</th>
      <th>platform.id</th>
      <th>platform.name</th>
      <th>platform.symbol</th>
      <th>platform.slug</th>
      <th>platform.token_address</th>
      <th>timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bitcoin</td>
      <td>BTC</td>
      <td>bitcoin</td>
      <td>9748</td>
      <td>2013-04-28T00:00:00.000Z</td>
      <td>[mineable, pow, sha-256, store-of-value, state...</td>
      <td>21000000.00000</td>
      <td>19158500.00000</td>
      <td>19158500.00000</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>18690.44722</td>
      <td>36977556124.69532</td>
      <td>-31.68110</td>
      <td>0.09201</td>
      <td>-1.18364</td>
      <td>-4.96117</td>
      <td>-13.02577</td>
      <td>-14.44874</td>
      <td>-11.47351</td>
      <td>358080933140.47571</td>
      <td>39.01400</td>
      <td>392499391703.41998</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1027</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>6103</td>
      <td>2015-08-07T00:00:00.000Z</td>
      <td>[pos, smart-contracts, ethereum-ecosystem, coi...</td>
      <td>NaN</td>
      <td>122492189.49900</td>
      <td>122492189.49900</td>
      <td>NaN</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1284.80947</td>
      <td>18814771193.53058</td>
      <td>-23.08810</td>
      <td>0.36289</td>
      <td>1.43672</td>
      <td>-11.16954</td>
      <td>-22.23175</td>
      <td>-15.51893</td>
      <td>7.65543</td>
      <td>157379125627.75635</td>
      <td>17.14690</td>
      <td>157379125627.76001</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>2</th>
      <td>825</td>
      <td>Tether</td>
      <td>USDT</td>
      <td>tether</td>
      <td>40036</td>
      <td>2015-02-25T00:00:00.000Z</td>
      <td>[payments, stablecoin, asset-backed-stablecoin...</td>
      <td>NaN</td>
      <td>67954703168.01751</td>
      <td>70155449908.74805</td>
      <td>NaN</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.99997</td>
      <td>54536112804.54321</td>
      <td>-22.72030</td>
      <td>-0.00037</td>
      <td>-0.01013</td>
      <td>0.00055</td>
      <td>-0.00812</td>
      <td>-0.00834</td>
      <td>0.04723</td>
      <td>67952763405.85585</td>
      <td>7.40370</td>
      <td>70153447326.42999</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.00000</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0xdac17f958d2ee523a2206206994597c13d831ec7</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3408</td>
      <td>USD Coin</td>
      <td>USDC</td>
      <td>usd-coin</td>
      <td>6294</td>
      <td>2018-10-08T00:00:00.000Z</td>
      <td>[medium-of-exchange, stablecoin, asset-backed-...</td>
      <td>NaN</td>
      <td>49761335172.82066</td>
      <td>49761335172.82066</td>
      <td>NaN</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.99998</td>
      <td>5113201594.95121</td>
      <td>-23.56460</td>
      <td>0.00117</td>
      <td>-0.00895</td>
      <td>-0.00406</td>
      <td>-0.00549</td>
      <td>0.02782</td>
      <td>-0.02424</td>
      <td>49760328204.36232</td>
      <td>5.42150</td>
      <td>49760328204.36000</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.00000</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1839</td>
      <td>BNB</td>
      <td>BNB</td>
      <td>bnb</td>
      <td>1110</td>
      <td>2017-07-25T00:00:00.000Z</td>
      <td>[marketplace, centralized-exchange, payments, ...</td>
      <td>200000000.00000</td>
      <td>161337261.09000</td>
      <td>161337261.09000</td>
      <td>NaN</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>270.37228</td>
      <td>881845025.45130</td>
      <td>-21.62840</td>
      <td>-0.09525</td>
      <td>0.93702</td>
      <td>-1.55947</td>
      <td>-8.79833</td>
      <td>5.76674</td>
      <td>15.59189</td>
      <td>43621123201.72779</td>
      <td>4.75260</td>
      <td>54074456089.09000</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>5</th>
      <td>52</td>
      <td>XRP</td>
      <td>XRP</td>
      <td>xrp</td>
      <td>820</td>
      <td>2013-08-04T00:00:00.000Z</td>
      <td>[medium-of-exchange, enterprise-solutions, arr...</td>
      <td>100000000000.00000</td>
      <td>49848747475.00000</td>
      <td>99989294935.00000</td>
      <td>NaN</td>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.48310</td>
      <td>7555718857.91232</td>
      <td>78.09650</td>
      <td>0.18563</td>
      <td>9.86140</td>
      <td>45.84057</td>
      <td>40.49607</td>
      <td>39.83611</td>
      <td>33.93971</td>
      <td>24081760519.63676</td>
      <td>2.62380</td>
      <td>48309660201.02000</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4687</td>
      <td>Binance USD</td>
      <td>BUSD</td>
      <td>binance-usd</td>
      <td>5163</td>
      <td>2019-09-20T00:00:00.000Z</td>
      <td>[stablecoin, asset-backed-stablecoin, binance-...</td>
      <td>NaN</td>
      <td>20517253084.58926</td>
      <td>20517253084.58926</td>
      <td>NaN</td>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.99984</td>
      <td>9505003038.74831</td>
      <td>-10.96040</td>
      <td>-0.02483</td>
      <td>-0.07000</td>
      <td>-0.06669</td>
      <td>-0.01954</td>
      <td>-0.10991</td>
      <td>0.00298</td>
      <td>20514030506.47705</td>
      <td>2.23510</td>
      <td>20514030506.48000</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1839.00000</td>
      <td>BNB</td>
      <td>BNB</td>
      <td>bnb</td>
      <td>BUSD-BD1</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2010</td>
      <td>Cardano</td>
      <td>ADA</td>
      <td>cardano</td>
      <td>571</td>
      <td>2017-10-01T00:00:00.000Z</td>
      <td>[dpos, pos, platform, research, smart-contract...</td>
      <td>45000000000.00000</td>
      <td>34227040771.90900</td>
      <td>34950580348.96300</td>
      <td>NaN</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.45100</td>
      <td>1025814771.59036</td>
      <td>-6.54170</td>
      <td>0.08690</td>
      <td>0.71423</td>
      <td>-1.83793</td>
      <td>-2.13599</td>
      <td>-8.02395</td>
      <td>-7.09635</td>
      <td>15436312111.83564</td>
      <td>1.68080</td>
      <td>20294890512.50000</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5426</td>
      <td>Solana</td>
      <td>SOL</td>
      <td>solana</td>
      <td>386</td>
      <td>2020-04-10T00:00:00.000Z</td>
      <td>[pos, platform, solana-ecosystem, cms-holdings...</td>
      <td>NaN</td>
      <td>354521530.96391</td>
      <td>511616946.14229</td>
      <td>NaN</td>
      <td>9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>31.46285</td>
      <td>834962523.53254</td>
      <td>-37.05030</td>
      <td>0.02363</td>
      <td>-0.86886</td>
      <td>-2.64497</td>
      <td>-11.14095</td>
      <td>-18.81422</td>
      <td>-21.64807</td>
      <td>11154259154.19821</td>
      <td>1.21530</td>
      <td>16096929259.65000</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>9</th>
      <td>74</td>
      <td>Dogecoin</td>
      <td>DOGE</td>
      <td>dogecoin</td>
      <td>567</td>
      <td>2013-12-15T00:00:00.000Z</td>
      <td>[mineable, pow, scrypt, medium-of-exchange, me...</td>
      <td>NaN</td>
      <td>132670764299.89409</td>
      <td>132670764299.89409</td>
      <td>NaN</td>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.06044</td>
      <td>445370531.52634</td>
      <td>9.50920</td>
      <td>0.63107</td>
      <td>2.58187</td>
      <td>1.58415</td>
      <td>-11.19329</td>
      <td>-6.79951</td>
      <td>-8.73058</td>
      <td>8018895924.16961</td>
      <td>0.87370</td>
      <td>8018895924.17000</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>10</th>
      <td>6636</td>
      <td>Polkadot</td>
      <td>DOT</td>
      <td>polkadot-new</td>
      <td>414</td>
      <td>2020-08-19T00:00:00.000Z</td>
      <td>[substrate, polkadot, binance-chain, polkadot-...</td>
      <td>NaN</td>
      <td>1119485867.09568</td>
      <td>1234909537.42086</td>
      <td>NaN</td>
      <td>11</td>
      <td>904869778.00000</td>
      <td>5695241948.93658</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>6.29399</td>
      <td>324099449.45736</td>
      <td>-23.87180</td>
      <td>0.66272</td>
      <td>-0.81941</td>
      <td>-7.91020</td>
      <td>-16.83214</td>
      <td>-10.56760</td>
      <td>-20.65291</td>
      <td>7046033613.38582</td>
      <td>0.76770</td>
      <td>7772509118.61000</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>11</th>
      <td>4943</td>
      <td>Dai</td>
      <td>DAI</td>
      <td>multi-collateral-dai</td>
      <td>1374</td>
      <td>2019-11-22T00:00:00.000Z</td>
      <td>[defi, stablecoin, asset-backed-stablecoin, et...</td>
      <td>NaN</td>
      <td>6981237837.05631</td>
      <td>6981237837.05631</td>
      <td>NaN</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1.00020</td>
      <td>347119867.41115</td>
      <td>-35.38910</td>
      <td>0.04220</td>
      <td>0.04988</td>
      <td>0.07067</td>
      <td>0.00765</td>
      <td>0.10056</td>
      <td>0.05291</td>
      <td>6982650763.87352</td>
      <td>0.76030</td>
      <td>6982650763.87000</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.00000</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x6b175474e89094c44da98b954eedeac495271d0f</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>12</th>
      <td>3890</td>
      <td>Polygon</td>
      <td>MATIC</td>
      <td>polygon</td>
      <td>490</td>
      <td>2019-04-28T00:00:00.000Z</td>
      <td>[platform, enterprise-solutions, scaling, stat...</td>
      <td>10000000000.00000</td>
      <td>8734317475.28493</td>
      <td>10000000000.00000</td>
      <td>NaN</td>
      <td>13</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.73523</td>
      <td>415055503.69477</td>
      <td>-22.79510</td>
      <td>0.58980</td>
      <td>0.31774</td>
      <td>-8.35863</td>
      <td>-10.18071</td>
      <td>-10.74648</td>
      <td>27.28276</td>
      <td>6421724674.37178</td>
      <td>0.69920</td>
      <td>7352291341.07000</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>13</th>
      <td>5994</td>
      <td>Shiba Inu</td>
      <td>SHIB</td>
      <td>shiba-inu</td>
      <td>418</td>
      <td>2020-08-01T00:00:00.000Z</td>
      <td>[memes, ethereum-ecosystem, doggone-doggerel]</td>
      <td>NaN</td>
      <td>549063278876301.93750</td>
      <td>589735030408322.75000</td>
      <td>NaN</td>
      <td>14</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.00001</td>
      <td>244980521.95565</td>
      <td>-31.08350</td>
      <td>0.31521</td>
      <td>-0.31068</td>
      <td>-8.05749</td>
      <td>-19.11240</td>
      <td>-4.95456</td>
      <td>-5.28506</td>
      <td>5850751638.15823</td>
      <td>0.63750</td>
      <td>6284144884.54000</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.00000</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1958</td>
      <td>TRON</td>
      <td>TRX</td>
      <td>tron</td>
      <td>685</td>
      <td>2017-09-13T00:00:00.000Z</td>
      <td>[media, payments, tron-ecosystem]</td>
      <td>NaN</td>
      <td>92354607190.81731</td>
      <td>92354638009.11899</td>
      <td>NaN</td>
      <td>15</td>
      <td>71659659264.00000</td>
      <td>4266067094.88673</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>0.05953</td>
      <td>362744077.10155</td>
      <td>-24.58000</td>
      <td>0.11756</td>
      <td>0.16508</td>
      <td>-2.23819</td>
      <td>-8.94456</td>
      <td>-7.87778</td>
      <td>-7.38492</td>
      <td>5498085740.91094</td>
      <td>0.59870</td>
      <td>5498087575.60000</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>15</th>
      <td>5805</td>
      <td>Avalanche</td>
      <td>AVAX</td>
      <td>avalanche</td>
      <td>317</td>
      <td>2020-07-13T00:00:00.000Z</td>
      <td>[defi, smart-contracts, three-arrows-capital-p...</td>
      <td>720000000.00000</td>
      <td>295866222.17204</td>
      <td>404229626.49901</td>
      <td>NaN</td>
      <td>16</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>17.42911</td>
      <td>264863391.17285</td>
      <td>-40.04940</td>
      <td>0.59582</td>
      <td>0.93751</td>
      <td>-2.96876</td>
      <td>-24.58308</td>
      <td>-20.56310</td>
      <td>-14.13504</td>
      <td>5156684762.70282</td>
      <td>0.56150</td>
      <td>12548958789.18000</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>16</th>
      <td>3717</td>
      <td>Wrapped Bitcoin</td>
      <td>WBTC</td>
      <td>wrapped-bitcoin</td>
      <td>610</td>
      <td>2019-01-30T00:00:00.000Z</td>
      <td>[medium-of-exchange, defi, wrapped-tokens, fan...</td>
      <td>NaN</td>
      <td>244707.06137</td>
      <td>244707.06137</td>
      <td>NaN</td>
      <td>17</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>18684.24762</td>
      <td>232447597.78041</td>
      <td>-37.43470</td>
      <td>0.10056</td>
      <td>-1.19455</td>
      <td>-4.96907</td>
      <td>-13.01705</td>
      <td>-14.56524</td>
      <td>-11.38590</td>
      <td>4572167330.20370</td>
      <td>0.49820</td>
      <td>4572167330.20000</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.00000</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x2260fac5e5542a773aa44fbcfedf7c193bc2c599</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>17</th>
      <td>7083</td>
      <td>Uniswap</td>
      <td>UNI</td>
      <td>uniswap</td>
      <td>480</td>
      <td>2020-09-17T00:00:00.000Z</td>
      <td>[decentralized-exchange, defi, dao, yield-farm...</td>
      <td>1000000000.00000</td>
      <td>762209326.53550</td>
      <td>1000000000.00000</td>
      <td>NaN</td>
      <td>18</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.86391</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>5.82126</td>
      <td>112157307.81865</td>
      <td>-18.21480</td>
      <td>0.61802</td>
      <td>3.09088</td>
      <td>0.68937</td>
      <td>-17.73469</td>
      <td>-19.04553</td>
      <td>8.78988</td>
      <td>4437021727.41377</td>
      <td>0.48340</td>
      <td>5821264018.88000</td>
      <td>5135958401.74284</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.00000</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x1f9840a85d5af5bf1d1762f925bdaddc4201f984</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>18</th>
      <td>3794</td>
      <td>Cosmos</td>
      <td>ATOM</td>
      <td>cosmos</td>
      <td>345</td>
      <td>2019-03-14T00:00:00.000Z</td>
      <td>[platform, cosmos-ecosystem, content-creation,...</td>
      <td>NaN</td>
      <td>286370297.00000</td>
      <td>0.00000</td>
      <td>NaN</td>
      <td>19</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>13.73229</td>
      <td>685670559.80859</td>
      <td>-3.33660</td>
      <td>0.46165</td>
      <td>-2.14244</td>
      <td>-14.79686</td>
      <td>12.14444</td>
      <td>48.33112</td>
      <td>68.83115</td>
      <td>3932518739.40617</td>
      <td>0.42820</td>
      <td>0.00000</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>19</th>
      <td>3957</td>
      <td>UNUS SED LEO</td>
      <td>LEO</td>
      <td>unus-sed-leo</td>
      <td>20</td>
      <td>2019-05-21T00:00:00.000Z</td>
      <td>[marketplace, centralized-exchange, discount-t...</td>
      <td>NaN</td>
      <td>953954130.00000</td>
      <td>985239504.00000</td>
      <td>NaN</td>
      <td>20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>4.11350</td>
      <td>4927387.42779</td>
      <td>-10.16600</td>
      <td>0.13893</td>
      <td>-13.45412</td>
      <td>-16.49086</td>
      <td>-22.06120</td>
      <td>-19.10869</td>
      <td>-30.45626</td>
      <td>3924085954.06606</td>
      <td>0.42750</td>
      <td>4052778197.04000</td>
      <td>NaN</td>
      <td>2022-09-23T15:14:00.000Z</td>
      <td>1027.00000</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x2af5d2ad76741191d15dfe7bf6ac92d4bd912ca3</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bitcoin</td>
      <td>BTC</td>
      <td>bitcoin</td>
      <td>9748</td>
      <td>2013-04-28T00:00:00.000Z</td>
      <td>[mineable, pow, sha-256, store-of-value, state...</td>
      <td>21000000.00000</td>
      <td>19158581.00000</td>
      <td>19158581.00000</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>18704.61206</td>
      <td>37360436505.18902</td>
      <td>-31.17000</td>
      <td>-0.12861</td>
      <td>-1.05543</td>
      <td>-4.48824</td>
      <td>-14.01476</td>
      <td>-14.59535</td>
      <td>-11.10099</td>
      <td>358353825219.53857</td>
      <td>38.95190</td>
      <td>392796853253.91998</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1027</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>6103</td>
      <td>2015-08-07T00:00:00.000Z</td>
      <td>[pos, smart-contracts, ethereum-ecosystem, coi...</td>
      <td>NaN</td>
      <td>122493377.49900</td>
      <td>122493377.49900</td>
      <td>NaN</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1291.38827</td>
      <td>19032237417.18936</td>
      <td>-23.07020</td>
      <td>-0.16700</td>
      <td>2.24764</td>
      <td>-10.19247</td>
      <td>-23.05389</td>
      <td>-15.09422</td>
      <td>8.58922</td>
      <td>158186510973.93555</td>
      <td>17.19440</td>
      <td>158186510973.94000</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>2</th>
      <td>825</td>
      <td>Tether</td>
      <td>USDT</td>
      <td>tether</td>
      <td>40036</td>
      <td>2015-02-25T00:00:00.000Z</td>
      <td>[payments, stablecoin, asset-backed-stablecoin...</td>
      <td>NaN</td>
      <td>67954703168.01751</td>
      <td>70155449908.74805</td>
      <td>NaN</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.99998</td>
      <td>56744844608.56666</td>
      <td>-20.34540</td>
      <td>0.00224</td>
      <td>-0.00603</td>
      <td>0.00193</td>
      <td>-0.00505</td>
      <td>-0.00735</td>
      <td>0.04631</td>
      <td>67953496192.26609</td>
      <td>7.38630</td>
      <td>70154203844.49001</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1027.00000</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0xdac17f958d2ee523a2206206994597c13d831ec7</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3408</td>
      <td>USD Coin</td>
      <td>USDC</td>
      <td>usd-coin</td>
      <td>6295</td>
      <td>2018-10-08T00:00:00.000Z</td>
      <td>[medium-of-exchange, stablecoin, asset-backed-...</td>
      <td>NaN</td>
      <td>49836182660.77986</td>
      <td>49836182660.77986</td>
      <td>NaN</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1.00005</td>
      <td>5156580026.38582</td>
      <td>-23.64390</td>
      <td>0.00087</td>
      <td>-0.01156</td>
      <td>0.01652</td>
      <td>0.01641</td>
      <td>0.00109</td>
      <td>-0.00181</td>
      <td>49838878938.29218</td>
      <td>5.41730</td>
      <td>49838878938.29000</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1027.00000</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1839</td>
      <td>BNB</td>
      <td>BNB</td>
      <td>bnb</td>
      <td>1110</td>
      <td>2017-07-25T00:00:00.000Z</td>
      <td>[marketplace, centralized-exchange, payments, ...</td>
      <td>200000000.00000</td>
      <td>161337261.09000</td>
      <td>161337261.09000</td>
      <td>NaN</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>271.03252</td>
      <td>884656872.61783</td>
      <td>-21.26450</td>
      <td>0.02835</td>
      <td>1.07994</td>
      <td>-0.83985</td>
      <td>-9.31584</td>
      <td>5.83406</td>
      <td>16.58093</td>
      <td>43727643816.63305</td>
      <td>4.75310</td>
      <td>54206503223.38000</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>5</th>
      <td>52</td>
      <td>XRP</td>
      <td>XRP</td>
      <td>xrp</td>
      <td>820</td>
      <td>2013-08-04T00:00:00.000Z</td>
      <td>[medium-of-exchange, enterprise-solutions, arr...</td>
      <td>100000000000.00000</td>
      <td>49848747475.00000</td>
      <td>99989294935.00000</td>
      <td>NaN</td>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.48592</td>
      <td>7666772098.03927</td>
      <td>78.83990</td>
      <td>-1.02668</td>
      <td>12.30166</td>
      <td>45.95615</td>
      <td>40.22602</td>
      <td>39.94804</td>
      <td>36.01983</td>
      <td>24222525964.13594</td>
      <td>2.63290</td>
      <td>48592045319.26000</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4687</td>
      <td>Binance USD</td>
      <td>BUSD</td>
      <td>binance-usd</td>
      <td>5163</td>
      <td>2019-09-20T00:00:00.000Z</td>
      <td>[stablecoin, asset-backed-stablecoin, binance-...</td>
      <td>NaN</td>
      <td>20517253084.58926</td>
      <td>20517253084.58926</td>
      <td>NaN</td>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.99988</td>
      <td>9453500038.55597</td>
      <td>-13.09230</td>
      <td>-0.04439</td>
      <td>0.01979</td>
      <td>-0.01973</td>
      <td>-0.00913</td>
      <td>0.11735</td>
      <td>-0.07198</td>
      <td>20514699922.20728</td>
      <td>2.22990</td>
      <td>20514699922.21000</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1839.00000</td>
      <td>BNB</td>
      <td>BNB</td>
      <td>bnb</td>
      <td>BUSD-BD1</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2010</td>
      <td>Cardano</td>
      <td>ADA</td>
      <td>cardano</td>
      <td>571</td>
      <td>2017-10-01T00:00:00.000Z</td>
      <td>[dpos, pos, platform, research, smart-contract...</td>
      <td>45000000000.00000</td>
      <td>34227045077.06700</td>
      <td>34950580348.96300</td>
      <td>NaN</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.45193</td>
      <td>1034509694.87100</td>
      <td>-5.90460</td>
      <td>-0.24477</td>
      <td>0.63164</td>
      <td>-1.63621</td>
      <td>-2.82265</td>
      <td>-8.12995</td>
      <td>-6.39507</td>
      <td>15468234413.48992</td>
      <td>1.68030</td>
      <td>20336857798.85000</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5426</td>
      <td>Solana</td>
      <td>SOL</td>
      <td>solana</td>
      <td>386</td>
      <td>2020-04-10T00:00:00.000Z</td>
      <td>[pos, platform, solana-ecosystem, cms-holdings...</td>
      <td>NaN</td>
      <td>354521459.37244</td>
      <td>511616946.14229</td>
      <td>NaN</td>
      <td>9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>31.55580</td>
      <td>841099651.27034</td>
      <td>-37.29100</td>
      <td>-0.22418</td>
      <td>-0.60091</td>
      <td>-1.53565</td>
      <td>-12.52915</td>
      <td>-17.87202</td>
      <td>-21.15572</td>
      <td>11187207898.93638</td>
      <td>1.21600</td>
      <td>16144481496.96000</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>9</th>
      <td>74</td>
      <td>Dogecoin</td>
      <td>DOGE</td>
      <td>dogecoin</td>
      <td>567</td>
      <td>2013-12-15T00:00:00.000Z</td>
      <td>[mineable, pow, scrypt, medium-of-exchange, me...</td>
      <td>NaN</td>
      <td>132670764299.89409</td>
      <td>132670764299.89409</td>
      <td>NaN</td>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.06098</td>
      <td>467297047.56779</td>
      <td>14.49220</td>
      <td>0.27224</td>
      <td>3.47681</td>
      <td>2.58033</td>
      <td>-11.67642</td>
      <td>-6.02461</td>
      <td>-7.38826</td>
      <td>8089647214.95740</td>
      <td>0.87930</td>
      <td>8089647214.96000</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>10</th>
      <td>6636</td>
      <td>Polkadot</td>
      <td>DOT</td>
      <td>polkadot-new</td>
      <td>414</td>
      <td>2020-08-19T00:00:00.000Z</td>
      <td>[substrate, polkadot, binance-chain, polkadot-...</td>
      <td>NaN</td>
      <td>1119696242.34303</td>
      <td>1235119912.66821</td>
      <td>NaN</td>
      <td>11</td>
      <td>904869778.00000</td>
      <td>5695249872.93607</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>6.29400</td>
      <td>328849892.65857</td>
      <td>-22.70600</td>
      <td>-0.44441</td>
      <td>-0.91892</td>
      <td>-7.64455</td>
      <td>-17.87384</td>
      <td>-10.73037</td>
      <td>-20.10429</td>
      <td>7047367518.47968</td>
      <td>0.76600</td>
      <td>7773844034.48000</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>11</th>
      <td>4943</td>
      <td>Dai</td>
      <td>DAI</td>
      <td>multi-collateral-dai</td>
      <td>1374</td>
      <td>2019-11-22T00:00:00.000Z</td>
      <td>[defi, stablecoin, asset-backed-stablecoin, et...</td>
      <td>NaN</td>
      <td>6979100352.69763</td>
      <td>6979100352.69763</td>
      <td>NaN</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.99995</td>
      <td>342518840.73627</td>
      <td>-37.90780</td>
      <td>-0.03429</td>
      <td>-0.02266</td>
      <td>0.07745</td>
      <td>0.01630</td>
      <td>0.02187</td>
      <td>0.00693</td>
      <td>6978718962.84209</td>
      <td>0.75810</td>
      <td>6978718962.84000</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1027.00000</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x6b175474e89094c44da98b954eedeac495271d0f</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>12</th>
      <td>3890</td>
      <td>Polygon</td>
      <td>MATIC</td>
      <td>polygon</td>
      <td>490</td>
      <td>2019-04-28T00:00:00.000Z</td>
      <td>[platform, enterprise-solutions, scaling, stat...</td>
      <td>10000000000.00000</td>
      <td>8734317475.28493</td>
      <td>10000000000.00000</td>
      <td>NaN</td>
      <td>13</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.73681</td>
      <td>417382294.30118</td>
      <td>-24.49630</td>
      <td>-0.41261</td>
      <td>0.56435</td>
      <td>-7.69643</td>
      <td>-11.37492</td>
      <td>-11.01058</td>
      <td>28.38181</td>
      <td>6435524939.59578</td>
      <td>0.69910</td>
      <td>7368091391.01000</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>13</th>
      <td>5994</td>
      <td>Shiba Inu</td>
      <td>SHIB</td>
      <td>shiba-inu</td>
      <td>418</td>
      <td>2020-08-01T00:00:00.000Z</td>
      <td>[memes, ethereum-ecosystem, doggone-doggerel]</td>
      <td>NaN</td>
      <td>549063278876301.93750</td>
      <td>589735030408322.75000</td>
      <td>NaN</td>
      <td>14</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.00001</td>
      <td>248558006.93959</td>
      <td>-31.89720</td>
      <td>-0.03070</td>
      <td>0.18197</td>
      <td>-7.36558</td>
      <td>-19.86154</td>
      <td>-4.88999</td>
      <td>-4.59653</td>
      <td>5873485344.34307</td>
      <td>0.63840</td>
      <td>6308562585.42000</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1027.00000</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1958</td>
      <td>TRON</td>
      <td>TRX</td>
      <td>tron</td>
      <td>685</td>
      <td>2017-09-13T00:00:00.000Z</td>
      <td>[media, payments, tron-ecosystem]</td>
      <td>NaN</td>
      <td>92354252560.35483</td>
      <td>92354260195.82248</td>
      <td>NaN</td>
      <td>15</td>
      <td>71659659264.00000</td>
      <td>4279415715.14990</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>0.05972</td>
      <td>368210303.88768</td>
      <td>-22.92020</td>
      <td>0.15100</td>
      <td>0.36105</td>
      <td>-1.85002</td>
      <td>-9.16008</td>
      <td>-7.68120</td>
      <td>-6.80431</td>
      <td>5515268197.29458</td>
      <td>0.59910</td>
      <td>5515268653.27000</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>15</th>
      <td>5805</td>
      <td>Avalanche</td>
      <td>AVAX</td>
      <td>avalanche</td>
      <td>317</td>
      <td>2020-07-13T00:00:00.000Z</td>
      <td>[defi, smart-contracts, three-arrows-capital-p...</td>
      <td>720000000.00000</td>
      <td>295868160.87959</td>
      <td>404229626.49901</td>
      <td>NaN</td>
      <td>16</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>17.40495</td>
      <td>265263679.95524</td>
      <td>-40.13540</td>
      <td>-0.60272</td>
      <td>0.75899</td>
      <td>-2.37396</td>
      <td>-25.83122</td>
      <td>-20.83184</td>
      <td>-13.39739</td>
      <td>5149571206.48563</td>
      <td>0.55940</td>
      <td>12531565605.60000</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>16</th>
      <td>3717</td>
      <td>Wrapped Bitcoin</td>
      <td>WBTC</td>
      <td>wrapped-bitcoin</td>
      <td>610</td>
      <td>2019-01-30T00:00:00.000Z</td>
      <td>[medium-of-exchange, defi, wrapped-tokens, fan...</td>
      <td>NaN</td>
      <td>244707.06137</td>
      <td>244707.06137</td>
      <td>NaN</td>
      <td>17</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>18699.16127</td>
      <td>238247123.84035</td>
      <td>-36.89740</td>
      <td>-0.13494</td>
      <td>-1.06805</td>
      <td>-4.54218</td>
      <td>-13.94367</td>
      <td>-14.64408</td>
      <td>-10.92141</td>
      <td>4575816803.42274</td>
      <td>0.49740</td>
      <td>4575816803.42000</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1027.00000</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x2260fac5e5542a773aa44fbcfedf7c193bc2c599</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>17</th>
      <td>7083</td>
      <td>Uniswap</td>
      <td>UNI</td>
      <td>uniswap</td>
      <td>480</td>
      <td>2020-09-17T00:00:00.000Z</td>
      <td>[decentralized-exchange, defi, dao, yield-farm...</td>
      <td>1000000000.00000</td>
      <td>762209326.53550</td>
      <td>1000000000.00000</td>
      <td>NaN</td>
      <td>18</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.86327</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>5.81692</td>
      <td>112491672.43369</td>
      <td>-25.71180</td>
      <td>-0.38472</td>
      <td>2.83619</td>
      <td>0.71914</td>
      <td>-19.15848</td>
      <td>-20.46690</td>
      <td>9.17649</td>
      <td>4433713326.26650</td>
      <td>0.48190</td>
      <td>5816923477.46000</td>
      <td>5135958401.74284</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1027.00000</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x1f9840a85d5af5bf1d1762f925bdaddc4201f984</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>18</th>
      <td>3794</td>
      <td>Cosmos</td>
      <td>ATOM</td>
      <td>cosmos</td>
      <td>345</td>
      <td>2019-03-14T00:00:00.000Z</td>
      <td>[platform, cosmos-ecosystem, content-creation,...</td>
      <td>NaN</td>
      <td>286370297.00000</td>
      <td>0.00000</td>
      <td>NaN</td>
      <td>19</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>13.70751</td>
      <td>645508932.73490</td>
      <td>-20.82680</td>
      <td>-0.74636</td>
      <td>-5.86649</td>
      <td>-14.27672</td>
      <td>7.76055</td>
      <td>47.45048</td>
      <td>69.34902</td>
      <td>3925424523.77344</td>
      <td>0.42640</td>
      <td>0.00000</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
    <tr>
      <th>19</th>
      <td>3957</td>
      <td>UNUS SED LEO</td>
      <td>LEO</td>
      <td>unus-sed-leo</td>
      <td>20</td>
      <td>2019-05-21T00:00:00.000Z</td>
      <td>[marketplace, centralized-exchange, discount-t...</td>
      <td>NaN</td>
      <td>953954130.00000</td>
      <td>985239504.00000</td>
      <td>NaN</td>
      <td>20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>4.10349</td>
      <td>4274428.30119</td>
      <td>-15.49950</td>
      <td>-0.22437</td>
      <td>-13.66303</td>
      <td>-16.49705</td>
      <td>-22.30886</td>
      <td>-19.38972</td>
      <td>-30.55627</td>
      <td>3914541943.49464</td>
      <td>0.42550</td>
      <td>4042921186.15000</td>
      <td>NaN</td>
      <td>2022-09-23T16:23:00.000Z</td>
      <td>1027.00000</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0x2af5d2ad76741191d15dfe7bf6ac92d4bd912ca3</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4 = df3.groupby('name', sort = False)[['quote.USD.percent_change_1h', 'quote.USD.percent_change_24h', 'quote.USD.percent_change_7d','quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d']].mean()
df4
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>quote.USD.percent_change_1h</th>
      <th>quote.USD.percent_change_24h</th>
      <th>quote.USD.percent_change_7d</th>
      <th>quote.USD.percent_change_30d</th>
      <th>quote.USD.percent_change_60d</th>
      <th>quote.USD.percent_change_90d</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bitcoin</th>
      <td>-0.01830</td>
      <td>-1.11954</td>
      <td>-4.72470</td>
      <td>-13.52026</td>
      <td>-14.52204</td>
      <td>-11.28725</td>
    </tr>
    <tr>
      <th>Ethereum</th>
      <td>0.09795</td>
      <td>1.84218</td>
      <td>-10.68101</td>
      <td>-22.64282</td>
      <td>-15.30658</td>
      <td>8.12233</td>
    </tr>
    <tr>
      <th>Tether</th>
      <td>0.00093</td>
      <td>-0.00808</td>
      <td>0.00124</td>
      <td>-0.00658</td>
      <td>-0.00785</td>
      <td>0.04677</td>
    </tr>
    <tr>
      <th>USD Coin</th>
      <td>0.00102</td>
      <td>-0.01025</td>
      <td>0.00623</td>
      <td>0.00546</td>
      <td>0.01446</td>
      <td>-0.01302</td>
    </tr>
    <tr>
      <th>BNB</th>
      <td>-0.03345</td>
      <td>1.00848</td>
      <td>-1.19966</td>
      <td>-9.05709</td>
      <td>5.80040</td>
      <td>16.08641</td>
    </tr>
    <tr>
      <th>XRP</th>
      <td>-0.42053</td>
      <td>11.08153</td>
      <td>45.89836</td>
      <td>40.36105</td>
      <td>39.89207</td>
      <td>34.97977</td>
    </tr>
    <tr>
      <th>Binance USD</th>
      <td>-0.03461</td>
      <td>-0.02511</td>
      <td>-0.04321</td>
      <td>-0.01434</td>
      <td>0.00372</td>
      <td>-0.03450</td>
    </tr>
    <tr>
      <th>Cardano</th>
      <td>-0.07893</td>
      <td>0.67294</td>
      <td>-1.73707</td>
      <td>-2.47932</td>
      <td>-8.07695</td>
      <td>-6.74571</td>
    </tr>
    <tr>
      <th>Solana</th>
      <td>-0.10028</td>
      <td>-0.73488</td>
      <td>-2.09031</td>
      <td>-11.83505</td>
      <td>-18.34312</td>
      <td>-21.40190</td>
    </tr>
    <tr>
      <th>Dogecoin</th>
      <td>0.45166</td>
      <td>3.02934</td>
      <td>2.08224</td>
      <td>-11.43486</td>
      <td>-6.41206</td>
      <td>-8.05942</td>
    </tr>
    <tr>
      <th>Polkadot</th>
      <td>0.10915</td>
      <td>-0.86916</td>
      <td>-7.77738</td>
      <td>-17.35299</td>
      <td>-10.64899</td>
      <td>-20.37860</td>
    </tr>
    <tr>
      <th>Dai</th>
      <td>0.00395</td>
      <td>0.01361</td>
      <td>0.07406</td>
      <td>0.01197</td>
      <td>0.06122</td>
      <td>0.02992</td>
    </tr>
    <tr>
      <th>Polygon</th>
      <td>0.08859</td>
      <td>0.44105</td>
      <td>-8.02753</td>
      <td>-10.77781</td>
      <td>-10.87853</td>
      <td>27.83228</td>
    </tr>
    <tr>
      <th>Shiba Inu</th>
      <td>0.14226</td>
      <td>-0.06435</td>
      <td>-7.71153</td>
      <td>-19.48697</td>
      <td>-4.92227</td>
      <td>-4.94079</td>
    </tr>
    <tr>
      <th>TRON</th>
      <td>0.13428</td>
      <td>0.26306</td>
      <td>-2.04410</td>
      <td>-9.05232</td>
      <td>-7.77949</td>
      <td>-7.09462</td>
    </tr>
    <tr>
      <th>Avalanche</th>
      <td>-0.00345</td>
      <td>0.84825</td>
      <td>-2.67136</td>
      <td>-25.20715</td>
      <td>-20.69747</td>
      <td>-13.76621</td>
    </tr>
    <tr>
      <th>Wrapped Bitcoin</th>
      <td>-0.01719</td>
      <td>-1.13130</td>
      <td>-4.75563</td>
      <td>-13.48036</td>
      <td>-14.60466</td>
      <td>-11.15366</td>
    </tr>
    <tr>
      <th>Uniswap</th>
      <td>0.11665</td>
      <td>2.96353</td>
      <td>0.70425</td>
      <td>-18.44659</td>
      <td>-19.75621</td>
      <td>8.98318</td>
    </tr>
    <tr>
      <th>Cosmos</th>
      <td>-0.14236</td>
      <td>-4.00446</td>
      <td>-14.53679</td>
      <td>9.95249</td>
      <td>47.89080</td>
      <td>69.09008</td>
    </tr>
    <tr>
      <th>UNUS SED LEO</th>
      <td>-0.04272</td>
      <td>-13.55857</td>
      <td>-16.49396</td>
      <td>-22.18503</td>
      <td>-19.24921</td>
      <td>-30.50627</td>
    </tr>
  </tbody>
</table>
</div>




```python
df5 = df4.stack()
df5
```




    name                                      
    Bitcoin       quote.USD.percent_change_1h     -0.01830
                  quote.USD.percent_change_24h    -1.11954
                  quote.USD.percent_change_7d     -4.72470
                  quote.USD.percent_change_30d   -13.52026
                  quote.USD.percent_change_60d   -14.52204
                                                    ...   
    UNUS SED LEO  quote.USD.percent_change_24h   -13.55857
                  quote.USD.percent_change_7d    -16.49396
                  quote.USD.percent_change_30d   -22.18503
                  quote.USD.percent_change_60d   -19.24921
                  quote.USD.percent_change_90d   -30.50627
    Length: 120, dtype: float64




```python
type(df5)
```




    pandas.core.series.Series




```python
df6 = df5.to_frame(name = 'values')
df6
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>values</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">Bitcoin</th>
      <th>quote.USD.percent_change_1h</th>
      <td>-0.01830</td>
    </tr>
    <tr>
      <th>quote.USD.percent_change_24h</th>
      <td>-1.11954</td>
    </tr>
    <tr>
      <th>quote.USD.percent_change_7d</th>
      <td>-4.72470</td>
    </tr>
    <tr>
      <th>quote.USD.percent_change_30d</th>
      <td>-13.52026</td>
    </tr>
    <tr>
      <th>quote.USD.percent_change_60d</th>
      <td>-14.52204</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">UNUS SED LEO</th>
      <th>quote.USD.percent_change_24h</th>
      <td>-13.55857</td>
    </tr>
    <tr>
      <th>quote.USD.percent_change_7d</th>
      <td>-16.49396</td>
    </tr>
    <tr>
      <th>quote.USD.percent_change_30d</th>
      <td>-22.18503</td>
    </tr>
    <tr>
      <th>quote.USD.percent_change_60d</th>
      <td>-19.24921</td>
    </tr>
    <tr>
      <th>quote.USD.percent_change_90d</th>
      <td>-30.50627</td>
    </tr>
  </tbody>
</table>
<p>120 rows × 1 columns</p>
</div>




```python
type(df6)
```




    pandas.core.frame.DataFrame




```python
df6 = df6.reset_index()
```


```python
df6
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>level_1</th>
      <th>values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bitcoin</td>
      <td>quote.USD.percent_change_1h</td>
      <td>-0.01830</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bitcoin</td>
      <td>quote.USD.percent_change_24h</td>
      <td>-1.11954</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bitcoin</td>
      <td>quote.USD.percent_change_7d</td>
      <td>-4.72470</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bitcoin</td>
      <td>quote.USD.percent_change_30d</td>
      <td>-13.52026</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bitcoin</td>
      <td>quote.USD.percent_change_60d</td>
      <td>-14.52204</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>115</th>
      <td>UNUS SED LEO</td>
      <td>quote.USD.percent_change_24h</td>
      <td>-13.55857</td>
    </tr>
    <tr>
      <th>116</th>
      <td>UNUS SED LEO</td>
      <td>quote.USD.percent_change_7d</td>
      <td>-16.49396</td>
    </tr>
    <tr>
      <th>117</th>
      <td>UNUS SED LEO</td>
      <td>quote.USD.percent_change_30d</td>
      <td>-22.18503</td>
    </tr>
    <tr>
      <th>118</th>
      <td>UNUS SED LEO</td>
      <td>quote.USD.percent_change_60d</td>
      <td>-19.24921</td>
    </tr>
    <tr>
      <th>119</th>
      <td>UNUS SED LEO</td>
      <td>quote.USD.percent_change_90d</td>
      <td>-30.50627</td>
    </tr>
  </tbody>
</table>
<p>120 rows × 3 columns</p>
</div>




```python
df6 = df6.rename(columns = {'level_1' : 'percent_change'})
df6
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>percent_change</th>
      <th>values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bitcoin</td>
      <td>quote.USD.percent_change_1h</td>
      <td>-0.01830</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bitcoin</td>
      <td>quote.USD.percent_change_24h</td>
      <td>-1.11954</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bitcoin</td>
      <td>quote.USD.percent_change_7d</td>
      <td>-4.72470</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bitcoin</td>
      <td>quote.USD.percent_change_30d</td>
      <td>-13.52026</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bitcoin</td>
      <td>quote.USD.percent_change_60d</td>
      <td>-14.52204</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>115</th>
      <td>UNUS SED LEO</td>
      <td>quote.USD.percent_change_24h</td>
      <td>-13.55857</td>
    </tr>
    <tr>
      <th>116</th>
      <td>UNUS SED LEO</td>
      <td>quote.USD.percent_change_7d</td>
      <td>-16.49396</td>
    </tr>
    <tr>
      <th>117</th>
      <td>UNUS SED LEO</td>
      <td>quote.USD.percent_change_30d</td>
      <td>-22.18503</td>
    </tr>
    <tr>
      <th>118</th>
      <td>UNUS SED LEO</td>
      <td>quote.USD.percent_change_60d</td>
      <td>-19.24921</td>
    </tr>
    <tr>
      <th>119</th>
      <td>UNUS SED LEO</td>
      <td>quote.USD.percent_change_90d</td>
      <td>-30.50627</td>
    </tr>
  </tbody>
</table>
<p>120 rows × 3 columns</p>
</div>




```python
df6['percent_change'] = df6['percent_change'].replace(['quote.USD.percent_change_1h', 'quote.USD.percent_change_24h', 'quote.USD.percent_change_7d', 'quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d'],['1h', '24h', '7d', '30d', '60d', '90d'])
df6
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>percent_change</th>
      <th>values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bitcoin</td>
      <td>1h</td>
      <td>-0.01830</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bitcoin</td>
      <td>24h</td>
      <td>-1.11954</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bitcoin</td>
      <td>7d</td>
      <td>-4.72470</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bitcoin</td>
      <td>30d</td>
      <td>-13.52026</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bitcoin</td>
      <td>60d</td>
      <td>-14.52204</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>115</th>
      <td>UNUS SED LEO</td>
      <td>24h</td>
      <td>-13.55857</td>
    </tr>
    <tr>
      <th>116</th>
      <td>UNUS SED LEO</td>
      <td>7d</td>
      <td>-16.49396</td>
    </tr>
    <tr>
      <th>117</th>
      <td>UNUS SED LEO</td>
      <td>30d</td>
      <td>-22.18503</td>
    </tr>
    <tr>
      <th>118</th>
      <td>UNUS SED LEO</td>
      <td>60d</td>
      <td>-19.24921</td>
    </tr>
    <tr>
      <th>119</th>
      <td>UNUS SED LEO</td>
      <td>90d</td>
      <td>-30.50627</td>
    </tr>
  </tbody>
</table>
<p>120 rows × 3 columns</p>
</div>




```python
import seaborn as sns
import matplotlib.pyplot as plt
```


```python
sns.catplot(x = 'percent_change', y = 'values', hue = 'name', data = df6, kind = 'point')
```




    <seaborn.axisgrid.FacetGrid at 0x291d13dce80>




    
![png](output_18_1.png)
    



```python
df7 = df3[['name', 'quote.USD.price', 'timestamp']]
df7 = df7.query('name == "Bitcoin"')
df7
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>quote.USD.price</th>
      <th>timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bitcoin</td>
      <td>18690.44722</td>
      <td>2022-09-23 18:17:01.548074</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Bitcoin</td>
      <td>18704.61206</td>
      <td>2022-09-23 19:24:37.347262</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
