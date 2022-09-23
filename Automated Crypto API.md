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
# import os 
from time import time
from time import sleep

for i in range(333):
    api_runner()
    print('API Working')
    sleep(60)
exit()
```


```python
df3.head()
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
  </tbody>
</table>
</div>




```python
pd.set_option('display.float_format', lambda x: '%.5f' % x)
```


```python
df3.head()
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
