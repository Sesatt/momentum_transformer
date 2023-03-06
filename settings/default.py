import os

CPD_LBWS = [10, 21, 63, 126, 256]
CPD_DEFAULT_LBW = 21
BACKTEST_AVERAGE_BASIS_POINTS = [None, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
USE_KM_HYP_TO_INITIALISE_KC = True

CPD_QUANDL_OUTPUT_FOLDER = lambda lbw: os.path.join(
    "data", f"quandl_cpd_{(lbw if lbw else 'none')}lbw"
)

CPD_QUANDL_OUTPUT_FOLDER_DEFAULT = CPD_QUANDL_OUTPUT_FOLDER(CPD_DEFAULT_LBW)

FEATURES_QUANDL_FILE_PATH = lambda lbw: os.path.join(
    "data", f"quandl_cpd_{(lbw if lbw else 'none')}lbw.csv"
)

FEATURES_QUANDL_FILE_PATH_DEFAULT = FEATURES_QUANDL_FILE_PATH(CPD_DEFAULT_LBW)

# QUANDL_TICKERS = ['AAPL', 'MSFT', 'PEP', 'WMT']

# ALL_QUANDL_CODES = ['AAPL', 'MSFT', 'PEP', 'WMT']

QUANDL_TICKERS = ['AMT',
 'ORCL',
 'MSFT',
 'TROW',
 'HON',
 'T',
 'AME',
 'ADM',
 'FRC',
 'FISV',
 'CF',
 'BKNG',
 'CE',
 'C',
 'KO',
 'A',
 'CDNS',
 'ED',
 'XRAY',
 'FAST',
 'DTE',
 'DD',
 'ETN',
 'SIVB',
 'XOM',
 'MGM',
 'WM',
 'GD',
 'GE',
 'LH',
 'GM',
 'NXPI',
 'CHTR',
 'AIZ',
 'LYB',
 'IR',
 'TT',
 'FLT',
 'TRGP',
 'IBM',
 'KMI',
 'HCA',
 'HII',
 'MPC',
 'XYL',
 'MA',
 'APTV',
 'EPAM',
 'CZR',
 'ENPH',
 'PSX',
 'META',
 'NOW',
 'PNR',
 'FANG',
 'PCG',
 'ABBV',
 'NCLH',
 'ZTS',
 'PEP',
 'MO',
 'IQV',
 'COP',
 'CDW',
 'NWSA',
 'NWS',
 'AMGN',
 'LIN',
 'SLB',
 'ALLE',
 'HLT',
 'CVX',
 'GOOG',
 'PAYC',
 'AAPL',
 'AMAT',
 'ANET',
 'CTLT',
 'SYF',
 'CFG',
 'KEYS',
 'MRO',
 'VMC',
 'SEDG',
 'ETSY',
 'KHC',
 'PYPL',
 'TXN',
 'HPE',
 'EIX',
 'MTCH',
 'FTV',
 'LW',
 'INVH',
 'HSY',
 'KR',
 'CVS',
 'GIS',
 'FOX',
 'VICI',
 'SPGI',
 'CDAY',
 'WRB',
 'KMB',
 'RTX',
 'KDP',
 'PG',
 'CTRA',
 'MRNA',
 'SO',
 'FOXA',
 'DOW',
 'CAT',
 'CTVA',
 'AMCR',
 'CL',
 'ROK',
 'FMC',
 'CARR',
 'OTIS',
 'DE',
 'BMY',
 'WBA',
 'BA',
 'IVZ',
 'UAL',
 'VTRS',
 'ABT',
 'AAL',
 'OGN',
 'LMT',
 'WRK',
 'NEM',
 'CAH',
 'IP',
 'EXC',
 'CNP',
 'PFE',
 'EMR',
 'JNJ',
 'GLW',
 'PPG',
 'PPL',
 'MMM',
 'CEG',
 'MRK',
 'MSI',
 'WBD',
 'FE',
 'CMS',
 'CHD',
 'CINF',
 'WEC',
 'AWK',
 'TXT',
 'CTAS',
 'PEG',
 'HAL',
 'XEL',
 'ETR',
 'EVRG',
 'AEP',
 'NEE',
 'EQT',
 'HWM',
 'NOC',
 'AEE',
 'CMCSA',
 'CMA',
 'OKE',
 'CPB',
 'WHR',
 'LHX',
 'F',
 'DOV',
 'DAL',
 'ADP',
 'DIS',
 'TGT',
 'L',
 'K',
 'AMP',
 'HPQ',
 'BAX',
 'DUK',
 'PNW',
 'APD',
 'HES',
 'ALK',
 'DG',
 'OMC',
 'HRL',
 'ATO',
 'MAS',
 'FITB',
 'NUE',
 'OXY',
 'RF',
 'MTB',
 'ROL',
 'SHW',
 'BEN',
 'AJG',
 'WMB',
 'EA',
 'WFC',
 'NI',
 'APA',
 'BDX',
 'WY',
 'DXC',
 'IFF',
 'TJX',
 'CMI',
 'PH',
 'HST',
 'PKI',
 'JCI',
 'SJM',
 'JBHT',
 'HBAN',
 'TDY',
 'SWK',
 'MCD',
 'VFC',
 'ES',
 'TFX',
 'AVY',
 'MMC',
 'SWKS',
 'J',
 'CLX',
 'GPC',
 'KLAC',
 'CCI',
 'MKC',
 'JPM',
 'LRCX',
 'MCO',
 'HUM',
 'UNP',
 'LNC',
 'BK',
 'DHR',
 'LLY',
 'TER',
 'SYY',
 'RHI',
 'EFX',
 'BKR',
 'GWW',
 'LEN',
 'HAS',
 'IPG',
 'MU',
 'PHM',
 'WMT',
 'CAG',
 'ITW',
 'BALL',
 'NKE',
 'TEL',
 'NDSN',
 'AFL',
 'NTRS',
 'FRT',
 'LUV',
 'LNT',
 'BAC',
 'AXP',
 'CB',
 'TAP',
 'UDR',
 'INTC',
 'TRV',
 'MDT',
 'SNA',
 'PNC',
 'PCAR',
 'LUMN',
 'FDX',
 'ADI',
 'NWL',
 'SEE',
 'PTC',
 'AMD',
 'LOW',
 'BIO',
 'PAYX',
 'VLO',
 'AON',
 'TMO',
 'CSX',
 'GEN',
 'GL',
 'WST',
 'PWR',
 'BRO',
 'CI',
 'BBWI',
 'NSC',
 'PGR',
 'PSA',
 'STZ',
 'D',
 'KEY',
 'AOS',
 'COO',
 'VZ',
 'USB',
 'HD',
 'WDC',
 'AIG',
 'PEAK',
 'MS',
 'RJF',
 'ECL',
 'TFC',
 'STT',
 'SYK',
 'CCL',
 'SCHW',
 'PXD',
 'FCX',
 'BR',
 'DVN',
 'MET',
 'STX',
 'ACN',
 'ADBE',
 'IEX',
 'TECH',
 'V',
 'VTR',
 'EOG',
 'CSCO',
 'HOLX',
 'TYL',
 'PARA',
 'TRMB',
 'AZO',
 'REGN',
 'IDXX',
 'AES',
 'VRTX',
 'ZBRA',
 'BIIB',
 'ODFL',
 'APH',
 'KIM',
 'QCOM',
 'GILD',
 'ROP',
 'SNPS',
 'PM',
 'MHK',
 'BSX',
 'STE',
 'DHI',
 'SBUX',
 'TSN',
 'BLK',
 'PFG',
 'INTU',
 'MCHP',
 'CRM',
 'ORLY',
 'RCL',
 'ALL',
 'DFS',
 'CRL',
 'CPT',
 'GRMN',
 'WELL',
 'BWA',
 'EQR',
 'UHS',
 'ATVI',
 'IT',
 'MAR',
 'NRG',
 'REG',
 'NVR',
 'INCY',
 'EMN',
 'SPG',
 'AAP',
 'MAA',
 'ALB',
 'MLM',
 'TSCO',
 'CPRT',
 'AVB',
 'PLD',
 'ESS',
 'O',
 'COF',
 'MCK',
 'DLTR',
 'ABC',
 'DRI',
 'WAB',
 'DISH',
 'RMD',
 'RL',
 'TPR',
 'EBAY',
 'ACGL',
 'RE',
 'DVA',
 'POOL',
 'HSIC',
 'NTAP',
 'EL',
 'WAT',
 'HIG',
 'IRM',
 'FDS',
 'ANSS',
 'ZION',
 'STLD',
 'MNST',
 'DGX',
 'CME',
 'KMX',
 'TTWO',
 'ARE',
 'AMZN',
 'QRVO',
 'BXP',
 'PRU',
 'YUM',
 'CHRW',
 'MTD',
 'WTW',
 'ADSK',
 'URI',
 'VRSN',
 'BBY',
 'MPWR',
 'SRE',
 'CTSH',
 'RSG',
 'CSGP',
 'NVDA',
 'GS',
 'FFIV',
 'CNC',
 'JNPR',
 'SBAC',
 'COST',
 'AKAM',
 'EXPE',
 'UPS',
 'PKG',
 'EW',
 'EXPD',
 'ON',
 'ISRG',
 'ILMN',
 'EQIX',
 'ELV',
 'AVGO',
 'JKHY',
 'ALGN',
 'GPN',
 'FIS',
 'MDLZ',
 'ZBH',
 'NFLX',
 'WYNN',
 'MOH',
 'LKQ',
 'SBNY',
 'CBRE',
 'DPZ',
 'EXR',
 'GOOGL',
 'DLR',
 'MOS',
 'MKTX',
 'LVS',
 'NDAQ',
 'DXCM',
 'ICE',
 'LYV',
 'CMG',
 'TDG',
 'LDOS',
 'ROST',
 'FSLR',
 'TMUS',
 'ULTA',
 'MSCI',
 'UNH',
 'VRSK',
 'FTNT',
 'GNRC',
 'CBOE',
 'TSLA']

ALL_QUANDL_CODES = QUANDL_TICKERS

INDUSTRY_MAPPING = {'AMT': 'Real Estate',
  'ORCL': 'Information Technology',
  'MSFT': 'Information Technology',
  'TROW': 'Financials',
  'HON': 'Industrials',
  'T': 'Communication Services',
  'AME': 'Industrials',
  'ADM': 'Consumer Staples',
  'FRC': 'Financials',
  'FISV': 'Information Technology',
  'CF': 'Materials',
  'BKNG': 'Consumer Discretionary',
  'CE': 'Materials',
  'C': 'Financials',
  'KO': 'Consumer Staples',
  'A': 'Health Care',
  'CDNS': 'Information Technology',
  'ED': 'Utilities',
  'XRAY': 'Health Care',
  'FAST': 'Industrials',
  'DTE': 'Utilities',
  'DD': 'Materials',
  'ETN': 'Industrials',
  'SIVB': 'Financials',
  'XOM': 'Energy',
  'MGM': 'Consumer Discretionary',
  'WM': 'Industrials',
  'GD': 'Industrials',
  'GE': 'Industrials',
  'LH': 'Health Care',
  'GM': 'Consumer Discretionary',
  'NXPI': 'Information Technology',
  'CHTR': 'Communication Services',
  'AIZ': 'Financials',
  'LYB': 'Materials',
  'IR': 'Industrials',
  'TT': 'Industrials',
  'FLT': 'Information Technology',
  'TRGP': 'Energy',
  'IBM': 'Information Technology',
  'KMI': 'Energy',
  'HCA': 'Health Care',
  'HII': 'Industrials',
  'MPC': 'Energy',
  'XYL': 'Industrials',
  'MA': 'Information Technology',
  'APTV': 'Consumer Discretionary',
  'EPAM': 'Information Technology',
  'CZR': 'Consumer Discretionary',
  'ENPH': 'Information Technology',
  'PSX': 'Energy',
  'META': 'Communication Services',
  'NOW': 'Information Technology',
  'PNR': 'Industrials',
  'FANG': 'Energy',
  'PCG': 'Utilities',
  'ABBV': 'Health Care',
  'NCLH': 'Consumer Discretionary',
  'ZTS': 'Health Care',
  'PEP': 'Consumer Staples',
  'MO': 'Consumer Staples',
  'IQV': 'Health Care',
  'COP': 'Energy',
  'CDW': 'Information Technology',
  'NWSA': 'Communication Services',
  'NWS': 'Communication Services',
  'AMGN': 'Health Care',
  'LIN': 'Materials',
  'SLB': 'Energy',
  'ALLE': 'Industrials',
  'HLT': 'Consumer Discretionary',
  'CVX': 'Energy',
  'GOOG': 'Communication Services',
  'PAYC': 'Information Technology',
  'AAPL': 'Information Technology',
  'AMAT': 'Information Technology',
  'ANET': 'Information Technology',
  'CTLT': 'Health Care',
  'SYF': 'Financials',
  'CFG': 'Financials',
  'KEYS': 'Information Technology',
  'MRO': 'Energy',
  'VMC': 'Materials',
  'SEDG': 'Information Technology',
  'ETSY': 'Consumer Discretionary',
  'KHC': 'Consumer Staples',
  'PYPL': 'Information Technology',
  'TXN': 'Information Technology',
  'HPE': 'Information Technology',
  'EIX': 'Utilities',
  'MTCH': 'Communication Services',
  'FTV': 'Industrials',
  'LW': 'Consumer Staples',
  'INVH': 'Real Estate',
  'HSY': 'Consumer Staples',
  'KR': 'Consumer Staples',
  'CVS': 'Health Care',
  'GIS': 'Consumer Staples',
  'FOX': 'Communication Services',
  'VICI': 'Real Estate',
  'SPGI': 'Financials',
  'CDAY': 'Information Technology',
  'WRB': 'Financials',
  'KMB': 'Consumer Staples',
  'RTX': 'Industrials',
  'KDP': 'Consumer Staples',
  'PG': 'Consumer Staples',
  'CTRA': 'Energy',
  'MRNA': 'Health Care',
  'SO': 'Utilities',
  'FOXA': 'Communication Services',
  'DOW': 'Materials',
  'CAT': 'Industrials',
  'CTVA': 'Materials',
  'AMCR': 'Materials',
  'CL': 'Consumer Staples',
  'ROK': 'Industrials',
  'FMC': 'Materials',
  'CARR': 'Industrials',
  'OTIS': 'Industrials',
  'DE': 'Industrials',
  'BMY': 'Health Care',
  'WBA': 'Consumer Staples',
  'BA': 'Industrials',
  'IVZ': 'Financials',
  'UAL': 'Industrials',
  'VTRS': 'Health Care',
  'ABT': 'Health Care',
  'AAL': 'Industrials',
  'OGN': 'Health Care',
  'LMT': 'Industrials',
  'WRK': 'Materials',
  'NEM': 'Materials',
  'CAH': 'Health Care',
  'IP': 'Materials',
  'EXC': 'Utilities',
  'CNP': 'Utilities',
  'PFE': 'Health Care',
  'EMR': 'Industrials',
  'JNJ': 'Health Care',
  'GLW': 'Information Technology',
  'PPG': 'Materials',
  'PPL': 'Utilities',
  'MMM': 'Industrials',
  'CEG': 'Utilities',
  'MRK': 'Health Care',
  'MSI': 'Information Technology',
  'WBD': 'Communication Services',
  'FE': 'Utilities',
  'CMS': 'Utilities',
  'CHD': 'Consumer Staples',
  'CINF': 'Financials',
  'WEC': 'Utilities',
  'AWK': 'Utilities',
  'TXT': 'Industrials',
  'CTAS': 'Industrials',
  'PEG': 'Utilities',
  'HAL': 'Energy',
  'XEL': 'Utilities',
  'ETR': 'Utilities',
  'EVRG': 'Utilities',
  'AEP': 'Utilities',
  'NEE': 'Utilities',
  'EQT': 'Energy',
  'HWM': 'Industrials',
  'NOC': 'Industrials',
  'AEE': 'Utilities',
  'CMCSA': 'Communication Services',
  'CMA': 'Financials',
  'OKE': 'Energy',
  'CPB': 'Consumer Staples',
  'WHR': 'Consumer Discretionary',
  'LHX': 'Industrials',
  'F': 'Consumer Discretionary',
  'DOV': 'Industrials',
  'DAL': 'Industrials',
  'ADP': 'Information Technology',
  'DIS': 'Communication Services',
  'TGT': 'Consumer Discretionary',
  'L': 'Financials',
  'K': 'Consumer Staples',
  'AMP': 'Financials',
  'HPQ': 'Information Technology',
  'BAX': 'Health Care',
  'DUK': 'Utilities',
  'PNW': 'Utilities',
  'APD': 'Materials',
  'HES': 'Energy',
  'ALK': 'Industrials',
  'DG': 'Consumer Discretionary',
  'OMC': 'Communication Services',
  'HRL': 'Consumer Staples',
  'ATO': 'Utilities',
  'MAS': 'Industrials',
  'FITB': 'Financials',
  'NUE': 'Materials',
  'OXY': 'Energy',
  'RF': 'Financials',
  'MTB': 'Financials',
  'ROL': 'Industrials',
  'SHW': 'Materials',
  'BEN': 'Financials',
  'AJG': 'Financials',
  'WMB': 'Energy',
  'EA': 'Communication Services',
  'WFC': 'Financials',
  'NI': 'Utilities',
  'APA': 'Energy',
  'BDX': 'Health Care',
  'WY': 'Real Estate',
  'DXC': 'Information Technology',
  'IFF': 'Materials',
  'TJX': 'Consumer Discretionary',
  'CMI': 'Industrials',
  'PH': 'Industrials',
  'HST': 'Real Estate',
  'PKI': 'Health Care',
  'JCI': 'Industrials',
  'SJM': 'Consumer Staples',
  'JBHT': 'Industrials',
  'HBAN': 'Financials',
  'TDY': 'Information Technology',
  'SWK': 'Industrials',
  'MCD': 'Consumer Discretionary',
  'VFC': 'Consumer Discretionary',
  'ES': 'Utilities',
  'TFX': 'Health Care',
  'AVY': 'Materials',
  'MMC': 'Financials',
  'SWKS': 'Information Technology',
  'J': 'Industrials',
  'CLX': 'Consumer Staples',
  'GPC': 'Consumer Discretionary',
  'KLAC': 'Information Technology',
  'CCI': 'Real Estate',
  'MKC': 'Consumer Staples',
  'JPM': 'Financials',
  'LRCX': 'Information Technology',
  'MCO': 'Financials',
  'HUM': 'Health Care',
  'UNP': 'Industrials',
  'LNC': 'Financials',
  'BK': 'Financials',
  'DHR': 'Health Care',
  'LLY': 'Health Care',
  'TER': 'Information Technology',
  'SYY': 'Consumer Staples',
  'RHI': 'Industrials',
  'EFX': 'Industrials',
  'BKR': 'Energy',
  'GWW': 'Industrials',
  'LEN': 'Consumer Discretionary',
  'HAS': 'Consumer Discretionary',
  'IPG': 'Communication Services',
  'MU': 'Information Technology',
  'PHM': 'Consumer Discretionary',
  'WMT': 'Consumer Staples',
  'CAG': 'Consumer Staples',
  'ITW': 'Industrials',
  'BALL': 'Materials',
  'NKE': 'Consumer Discretionary',
  'TEL': 'Information Technology',
  'NDSN': 'Industrials',
  'AFL': 'Financials',
  'NTRS': 'Financials',
  'FRT': 'Real Estate',
  'LUV': 'Industrials',
  'LNT': 'Utilities',
  'BAC': 'Financials',
  'AXP': 'Financials',
  'CB': 'Financials',
  'TAP': 'Consumer Staples',
  'UDR': 'Real Estate',
  'INTC': 'Information Technology',
  'TRV': 'Financials',
  'MDT': 'Health Care',
  'SNA': 'Industrials',
  'PNC': 'Financials',
  'PCAR': 'Industrials',
  'LUMN': 'Communication Services',
  'FDX': 'Industrials',
  'ADI': 'Information Technology',
  'NWL': 'Consumer Discretionary',
  'SEE': 'Materials',
  'PTC': 'Information Technology',
  'AMD': 'Information Technology',
  'LOW': 'Consumer Discretionary',
  'BIO': 'Health Care',
  'PAYX': 'Information Technology',
  'VLO': 'Energy',
  'AON': 'Financials',
  'TMO': 'Health Care',
  'CSX': 'Industrials',
  'GEN': 'Information Technology',
  'GL': 'Financials',
  'WST': 'Health Care',
  'PWR': 'Industrials',
  'BRO': 'Financials',
  'CI': 'Health Care',
  'BBWI': 'Consumer Discretionary',
  'NSC': 'Industrials',
  'PGR': 'Financials',
  'PSA': 'Real Estate',
  'STZ': 'Consumer Staples',
  'D': 'Utilities',
  'KEY': 'Financials',
  'AOS': 'Industrials',
  'COO': 'Health Care',
  'VZ': 'Communication Services',
  'USB': 'Financials',
  'HD': 'Consumer Discretionary',
  'WDC': 'Information Technology',
  'AIG': 'Financials',
  'PEAK': 'Real Estate',
  'MS': 'Financials',
  'RJF': 'Financials',
  'ECL': 'Materials',
  'TFC': 'Financials',
  'STT': 'Financials',
  'SYK': 'Health Care',
  'CCL': 'Consumer Discretionary',
  'SCHW': 'Financials',
  'PXD': 'Energy',
  'FCX': 'Materials',
  'BR': 'Information Technology',
  'DVN': 'Energy',
  'MET': 'Financials',
  'STX': 'Information Technology',
  'ACN': 'Information Technology',
  'ADBE': 'Information Technology',
  'IEX': 'Industrials',
  'TECH': 'Health Care',
  'V': 'Information Technology',
  'VTR': 'Real Estate',
  'EOG': 'Energy',
  'CSCO': 'Information Technology',
  'HOLX': 'Health Care',
  'TYL': 'Information Technology',
  'PARA': 'Communication Services',
  'TRMB': 'Information Technology',
  'AZO': 'Consumer Discretionary',
  'REGN': 'Health Care',
  'IDXX': 'Health Care',
  'AES': 'Utilities',
  'VRTX': 'Health Care',
  'ZBRA': 'Information Technology',
  'BIIB': 'Health Care',
  'ODFL': 'Industrials',
  'APH': 'Information Technology',
  'KIM': 'Real Estate',
  'QCOM': 'Information Technology',
  'GILD': 'Health Care',
  'ROP': 'Information Technology',
  'SNPS': 'Information Technology',
  'PM': 'Consumer Staples',
  'MHK': 'Consumer Discretionary',
  'BSX': 'Health Care',
  'STE': 'Health Care',
  'DHI': 'Consumer Discretionary',
  'SBUX': 'Consumer Discretionary',
  'TSN': 'Consumer Staples',
  'BLK': 'Financials',
  'PFG': 'Financials',
  'INTU': 'Information Technology',
  'MCHP': 'Information Technology',
  'CRM': 'Information Technology',
  'ORLY': 'Consumer Discretionary',
  'RCL': 'Consumer Discretionary',
  'ALL': 'Financials',
  'DFS': 'Financials',
  'CRL': 'Health Care',
  'CPT': 'Real Estate',
  'GRMN': 'Consumer Discretionary',
  'WELL': 'Real Estate',
  'BWA': 'Consumer Discretionary',
  'EQR': 'Real Estate',
  'UHS': 'Health Care',
  'ATVI': 'Communication Services',
  'IT': 'Information Technology',
  'MAR': 'Consumer Discretionary',
  'NRG': 'Utilities',
  'REG': 'Real Estate',
  'NVR': 'Consumer Discretionary',
  'INCY': 'Health Care',
  'EMN': 'Materials',
  'SPG': 'Real Estate',
  'AAP': 'Consumer Discretionary',
  'MAA': 'Real Estate',
  'ALB': 'Materials',
  'MLM': 'Materials',
  'TSCO': 'Consumer Discretionary',
  'CPRT': 'Industrials',
  'AVB': 'Real Estate',
  'PLD': 'Real Estate',
  'ESS': 'Real Estate',
  'O': 'Real Estate',
  'COF': 'Financials',
  'MCK': 'Health Care',
  'DLTR': 'Consumer Discretionary',
  'ABC': 'Health Care',
  'DRI': 'Consumer Discretionary',
  'WAB': 'Industrials',
  'DISH': 'Communication Services',
  'RMD': 'Health Care',
  'RL': 'Consumer Discretionary',
  'TPR': 'Consumer Discretionary',
  'EBAY': 'Consumer Discretionary',
  'ACGL': 'Financials',
  'RE': 'Financials',
  'DVA': 'Health Care',
  'POOL': 'Consumer Discretionary',
  'HSIC': 'Health Care',
  'NTAP': 'Information Technology',
  'EL': 'Consumer Staples',
  'WAT': 'Health Care',
  'HIG': 'Financials',
  'IRM': 'Real Estate',
  'FDS': 'Financials',
  'ANSS': 'Information Technology',
  'ZION': 'Financials',
  'STLD': 'Materials',
  'MNST': 'Consumer Staples',
  'DGX': 'Health Care',
  'CME': 'Financials',
  'KMX': 'Consumer Discretionary',
  'TTWO': 'Communication Services',
  'ARE': 'Real Estate',
  'AMZN': 'Consumer Discretionary',
  'QRVO': 'Information Technology',
  'BXP': 'Real Estate',
  'PRU': 'Financials',
  'YUM': 'Consumer Discretionary',
  'CHRW': 'Industrials',
  'MTD': 'Health Care',
  'WTW': 'Financials',
  'ADSK': 'Information Technology',
  'URI': 'Industrials',
  'VRSN': 'Information Technology',
  'BBY': 'Consumer Discretionary',
  'MPWR': 'Information Technology',
  'SRE': 'Utilities',
  'CTSH': 'Information Technology',
  'RSG': 'Industrials',
  'CSGP': 'Industrials',
  'NVDA': 'Information Technology',
  'GS': 'Financials',
  'FFIV': 'Information Technology',
  'CNC': 'Health Care',
  'JNPR': 'Information Technology',
  'SBAC': 'Real Estate',
  'COST': 'Consumer Staples',
  'AKAM': 'Information Technology',
  'EXPE': 'Consumer Discretionary',
  'UPS': 'Industrials',
  'PKG': 'Materials',
  'EW': 'Health Care',
  'EXPD': 'Industrials',
  'ON': 'Information Technology',
  'ISRG': 'Health Care',
  'ILMN': 'Health Care',
  'EQIX': 'Real Estate',
  'ELV': 'Health Care',
  'AVGO': 'Information Technology',
  'JKHY': 'Information Technology',
  'ALGN': 'Health Care',
  'GPN': 'Information Technology',
  'FIS': 'Information Technology',
  'MDLZ': 'Consumer Staples',
  'ZBH': 'Health Care',
  'NFLX': 'Communication Services',
  'WYNN': 'Consumer Discretionary',
  'MOH': 'Health Care',
  'LKQ': 'Consumer Discretionary',
  'SBNY': 'Financials',
  'CBRE': 'Real Estate',
  'DPZ': 'Consumer Discretionary',
  'EXR': 'Real Estate',
  'GOOGL': 'Communication Services',
  'DLR': 'Real Estate',
  'MOS': 'Materials',
  'MKTX': 'Financials',
  'LVS': 'Consumer Discretionary',
  'NDAQ': 'Financials',
  'DXCM': 'Health Care',
  'ICE': 'Financials',
  'LYV': 'Communication Services',
  'CMG': 'Consumer Discretionary',
  'TDG': 'Industrials',
  'LDOS': 'Industrials',
  'ROST': 'Consumer Discretionary',
  'FSLR': 'Information Technology',
  'TMUS': 'Communication Services',
  'ULTA': 'Consumer Discretionary',
  'MSCI': 'Financials',
  'UNH': 'Health Care',
  'VRSK': 'Industrials',
  'FTNT': 'Information Technology',
  'GNRC': 'Industrials',
  'CBOE': 'Financials',
  'TSLA': 'Consumer Discretionary'}


# QUANDL_TICKERS = [
#     "ICE_SB",
#     "CME_SF",
#     "CME_SI",
#     "CME_SM",
#     "CME_SP",
#     "ICE_OJ",
#     "CME_TY",
#     "CME_US",
#     "CME_W",
#     "CME_CL",
#     "CME_CD",
#     "CME_C",
#     "ICE_KC",
#     "CME_GC",
#     "CME_AD",
#     "ICE_DX",
#     "ICE_CT",
#     "CME_BP",
#     "CME_S",
#     "ICE_CC",
#     "CME_BO",
#     "CME_PL",
#     "CME_PA",
#     "CME_O",
#     "CME_HG",
#     "CME_FC",
#     "CME_HO",
#     "CME_LN",
#     "CME_LC",
#     "CME_LB",
#     "CME_RR",
#     "CME_KW",
#     "CME_JY",
#     "CME_FV",
#     "CME_NG",
#     "ICE_G",
#     "CME_NK",
#     "CME_MD",
#     "ICE_B",
#     "LIFFE_C",
#     "LIFFE_RC",
#     "CME_MP",
#     "ICE_RS",
#     "EUREX_FDAX",
#     "ICE_M",
#     "CME_ES",
#     "CME_B3",
#     "CME_EC",
#     "EUREX_FGBM",
#     "CME_NQ",
#     "CME_BR",
#     "CME_NE",
#     "ICE_SY",
#     "ICE_ZR",
#     "ICE_SS",
#     "ODE_AB",
#     "ICE_AR",
#     "ICE_MP",
#     "ICE_BPB",
#     "ICE_P",
#     "CBOE_VX",
#     "CME_RB",
#     "ICE_T",
#     "ICE_N",
#     "ICE_O",
#     "ICE_ZJ",
#     "LIFFE_T",
#     "CME_RF",
#     "CME_TU",
#     "CME_YM",
#     "LIFFE_R",
#     "CME_RU",
#     "ICE_NT",
#     "ICE_C",
#     "ICE_NCF",
#     "LIFFE_FCE",
#     "LIFFE_W",
#     "CME_AW",
#     "CME_BZ",
#     "CME_EH",
#     "ICE_KRU",
#     "ICE_TIB",
#     "ICE_CEU",
#     "CME_UL",
#     "EUREX_FGBL",
#     "EUREX_FESX",
#     "ICE_GNM",
#     "ICE_GER",
#     "EUREX_FOAT",
#     "EUREX_FBTS",
#     "EUREX_CONF",
#     "EUREX_FBTP",
#     "EUREX_FGBX",
#     "EUREX_FRDX",
#     "EUREX_FVS",
#     "EUREX_FTDX",
#     "EUREX_FSTX",
#     "EUREX_FSMM",
#     "EUREX_FSMI",
#     "EUREX_FSLI",
# ]

# ALL_QUANDL_CODES = [
#     "CHRIS/ICE_NJ",
#     "CHRIS/CME_FI",
#     "CHRIS/CME_FS",
#     "CHRIS/CME_TY",
#     "CHRIS/CME_N1U",
#     "CHRIS/ASX_XS",
#     "CHRIS/MX_CGB",
#     "CHRIS/SGX_JG",
#     "CHRIS/SGX_JB",
#     "CHRIS/ASX_TN",
#     "CHRIS/LIFFE_EON",
#     "CHRIS/EUREX_FEO1",
#     "CHRIS/CME_EM",
#     "CHRIS/CME_TU",
#     "CHRIS/MX_CGZ",
#     "CHRIS/CME_FO",
#     "CHRIS/CME_BOB",
#     "CHRIS/CME_FF",
#     "CHRIS/CME_I3",
#     "CHRIS/ASX_IB",
#     "CHRIS/MX_ONX",
#     "CHRIS/MX_LGB",
#     "CHRIS/CME_US",
#     "CHRIS/MX_BAX",
#     "CHRIS/LIFFE_EO3",
#     "CHRIS/EUREX_FEU3",
#     "CHRIS/LIFFE_I",
#     "CHRIS/CME_ED",
#     "CHRIS/TFX_JBA",
#     "CHRIS/ASX_OI",
#     "CHRIS/LIFFE_J",
#     "CHRIS/ASX_YS",
#     "CHRIS/ASX_YT",
#     "CHRIS/ASX_TY",
#     "CHRIS/CME_SA",
#     "CHRIS/CME_FV",
#     "CHRIS/MX_CGF",
#     "CHRIS/ASX_IR",
#     "CHRIS/ASX_BB",
#     "CHRIS/LIFFE_AXF",
#     "CHRIS/LIFFE_FTI",
#     "CHRIS/CME_B4",
#     "CHRIS/SHFE_AL",
#     "CHRIS/MCX_AL",
#     "CHRIS/MCX_ALM",
#     "CHRIS/LIFFE_FMX",
#     "CHRIS/CME_NEN",
#     "CHRIS/CME_E5",
#     "CHRIS/CME_AD",
#     "CHRIS/ICE_AR",
#     "CHRIS/ODE_AB",
#     "CHRIS/ICE_BW",
#     "CHRIS/LIFFE_BXF",
#     "CHRIS/CBOE_VXEW",
#     "CHRIS/CME_BR",
#     "CHRIS/MCX_B",
#     "CHRIS/ICE_B",
#     "CHRIS/CME_BB",
#     "CHRIS/CME_DB",
#     "CHRIS/CME_CY",
#     "CHRIS/CME_BZ",
#     "CHRIS/CME_BP",
#     "CHRIS/CME_BY",
#     "CHRIS/EUREX_FBUT",
#     "CHRIS/LIFFE_XFC",
#     "CHRIS/LIFFE_FCE",
#     "CHRIS/CME_CD",
#     "CHRIS/CME_WCC",
#     "CHRIS/ICE_RS",
#     "CHRIS/MCX_CRDM",
#     "CHRIS/CME_CB",
#     "CHRIS/CME_CSC",
#     "CHRIS/ICE_CER",
#     "CHRIS/EUREX_F2CR",
#     "CHRIS/CME_CU",
#     "CHRIS/CME_5C",
#     "CHRIS/SGX_CFF",
#     "CHRIS/CME_CI",
#     "CHRIS/CME_DA",
#     "CHRIS/CME_DK",
#     "CHRIS/CME_QL",
#     "CHRIS/CME_SSI",
#     "CHRIS/CME_MTF",
#     "CHRIS/CME_MFF",
#     "CHRIS/LIFFE_C",
#     "CHRIS/ICE_CC",
#     "CHRIS/LIFFE_RC",
#     "CHRIS/ICE_KC",
#     "CHRIS/CME_TC",
#     "CHRIS/CME_GL",
#     "CHRIS/CME_5Z",
#     "CHRIS/EUREX_CONF",
#     "CHRIS/MCX_CU",
#     "CHRIS/SHFE_CU",
#     "CHRIS/CME_HG",
#     "CHRIS/MCX_CUM",
#     "CHRIS/CME_C",
#     "CHRIS/LIFFE_EMA",
#     "CHRIS/ICE_ICN",
#     "CHRIS/ODE_YC",
#     "CHRIS/ODE_C75",
#     "CHRIS/MCX_CT",
#     "CHRIS/ICE_CT",
#     "CHRIS/MCX_CL",
#     "CHRIS/CBOE_OV",
#     "CHRIS/CME_WS",
#     "CHRIS/CME_CPO",
#     "CHRIS/CME_UB",
#     "CHRIS/CME_FY",
#     "CHRIS/EUREX_FDAX",
#     "CHRIS/EUREX_FTDX",
#     "CHRIS/CME_PG",
#     "CHRIS/CME_JR",
#     "CHRIS/EUREX_FCAG",
#     "CHRIS/CME_AW",
#     "CHRIS/EUREX_FCCO",
#     "CHRIS/EUREX_FCEN",
#     "CHRIS/EUREX_FCXE",
#     "CHRIS/EUREX_FCGR",
#     "CHRIS/EUREX_FCIN",
#     "CHRIS/EUREX_FCLI",
#     "CHRIS/EUREX_FCPE",
#     "CHRIS/EUREX_FCPR",
#     "CHRIS/EUREX_FCSO",
#     "CHRIS/CME_DY",
#     "CHRIS/CME_DC",
#     "CHRIS/ICE_DW",
#     "CHRIS/ASX_VC",
#     "CHRIS/CME_QX",
#     "CHRIS/CME_EW",
#     "CHRIS/ICE_ERU",
#     "CHRIS/ICE_CEU",
#     "CHRIS/CME_A5",
#     "CHRIS/CME_M6B",
#     "CHRIS/CME_M6E",
#     "CHRIS/CME_MGC",
#     "CHRIS/CME_XAY",
#     "CHRIS/CME_XAP",
#     "CHRIS/CME_QM",
#     "CHRIS/CME_YM",
#     "CHRIS/CME_E7",
#     "CHRIS/CME_XAF",
#     "CHRIS/CME_J7",
#     "CHRIS/CME_NQ",
#     "CHRIS/CME_QG",
#     "CHRIS/CME_ES",
#     "CHRIS/CME_XAK",
#     "CHRIS/CME_XAU",
#     "CHRIS/ICE_BPB",
#     "CHRIS/ICE_DPB",
#     "CHRIS/ICE_DPA",
#     "CHRIS/ICE_TFM",
#     "CHRIS/ICE_GER",
#     "CHRIS/ICE_GNM",
#     "CHRIS/CME_I6",
#     "CHRIS/CME_I5",
#     "CHRIS/CME_O1",
#     "CHRIS/CME_N1",
#     "CHRIS/EUREX_FERU",
#     "CHRIS/CME_EH",
#     "CHRIS/CME_71",
#     "CHRIS/CME_Z1",
#     "CHRIS/ICE_C",
#     "CHRIS/EUREX_FEAA",
#     "CHRIS/CME_EC",
#     "CHRIS/EUREX_FEXF",
#     "CHRIS/EUREX_FESX",
#     "CHRIS/EUREX_FEXD",
#     "CHRIS/EUREX_FEDV",
#     "CHRIS/CME_RP",
#     "CHRIS/CME_RY",
#     "CHRIS/CME_Z",
#     "CHRIS/CME_RF",
#     "CHRIS/EUREX_FGBM",
#     "CHRIS/EUREX_FGBL",
#     "CHRIS/EUREX_FGBX",
#     "CHRIS/SGX_ED",
#     "CHRIS/EUREX_FOAT",
#     "CHRIS/CME_UV",
#     "CHRIS/CME_GZ",
#     "CHRIS/CME_EN",
#     "CHRIS/CME_UN",
#     "CHRIS/EUREX_FGBS",
#     "CHRIS/LIFFE_S",
#     "CHRIS/SGX_EL",
#     "CHRIS/SGX_EY",
#     "CHRIS/CME_EY",
#     "CHRIS/ASX_UB",
#     "CHRIS/LIFFE_T",
#     "CHRIS/CME_FC",
#     "CHRIS/CME_FP",
#     "CHRIS/ODE_FS",
#     "CHRIS/LIFFE_YZ",
#     "CHRIS/LIFFE_XZ",
#     "CHRIS/LIFFE_Z",
#     "CHRIS/LIFFE_Y",
#     "CHRIS/SGX_CN",
#     "CHRIS/LIFFE_EPE",
#     "CHRIS/LIFFE_EPR",
#     "CHRIS/LIFFE_Q",
#     "CHRIS/SGX_ST",
#     "CHRIS/LIFFE_FEO",
#     "CHRIS/LIFFE_FEF",
#     "CHRIS/SHFE_FU",
#     "CHRIS/SGX_FB",
#     "CHRIS/CME_DJ",
#     "CHRIS/CME_SP",
#     "CHRIS/ICE_G",
#     "CHRIS/CME_WQ",
#     "CHRIS/CME_RB",
#     "CHRIS/CME_7H",
#     "CHRIS/CME_7K",
#     "CHRIS/ICE_SS",
#     "CHRIS/ICE_SY",
#     "CHRIS/SHFE_AU",
#     "CHRIS/CME_GC",
#     "CHRIS/MCX_GC",
#     "CHRIS/MCX_GG",
#     "CHRIS/MCX_GM",
#     "CHRIS/MCX_GP",
#     "CHRIS/MCX_GD",
#     "CHRIS/CBOE_GV",
#     "CHRIS/ASX_GW",
#     "CHRIS/CME_A6",
#     "CHRIS/MCX_GRM",
#     "CHRIS/MCX_GRS",
#     "CHRIS/CME_ME",
#     "CHRIS/CME_GE",
#     "CHRIS/CME_MG",
#     "CHRIS/CME_MF",
#     "CHRIS/CME_GCU",
#     "CHRIS/CME_GCI",
#     "CHRIS/CME_LY",
#     "CHRIS/CME_GY",
#     "CHRIS/CME_LT",
#     "CHRIS/CME_ARW",
#     "CHRIS/CME_RV",
#     "CHRIS/MGEX_MW",
#     "CHRIS/MGEX_IP",
#     "CHRIS/MGEX_IH",
#     "CHRIS/CME_HO",
#     "CHRIS/ICE_O",
#     "CHRIS/CME_IN",
#     "CHRIS/CME_HB",
#     "CHRIS/CME_NP",
#     "CHRIS/CME_NN",
#     "CHRIS/EUREX_FHOG",
#     "CHRIS/CME_NH",
#     "CHRIS/CME_IBV",
#     "CHRIS/SGX_CIF",
#     "CHRIS/CME_6T",
#     "CHRIS/SGX_IR",
#     "CHRIS/CME_MCC",
#     "CHRIS/SGX_FEF",
#     "CHRIS/CME_TIO",
#     "CHRIS/CME_U6",
#     "CHRIS/CME_H2",
#     "CHRIS/CME_NI",
#     "CHRIS/CME_KI",
#     "CHRIS/CME_U3",
#     "CHRIS/CME_P8",
#     "CHRIS/CME_P7",
#     "CHRIS/CME_U5",
#     "CHRIS/CME_U4",
#     "CHRIS/CME_P5",
#     "CHRIS/CME_L9",
#     "CHRIS/CME_R6",
#     "CHRIS/LIFFE_JGB",
#     "CHRIS/CME_JY",
#     "CHRIS/MCX_KPK",
#     "CHRIS/MCX_KP",
#     "CHRIS/CME_KW",
#     "CHRIS/SHFE_PB",
#     "CHRIS/MCX_PB",
#     "CHRIS/MCX_PBM",
#     "CHRIS/CME_LN",
#     "CHRIS/CME_LC",
#     "CHRIS/CME_WJ",
#     "CHRIS/LIFFE_R",
#     "CHRIS/EUREX_FBTP",
#     "CHRIS/CME_JS",
#     "CHRIS/ICE_ULS",
#     "CHRIS/CME_LB",
#     "CHRIS/SGX_MR",
#     "CHRIS/LIFFE_EOB",
#     "CHRIS/CME_YX",
#     "CHRIS/EUREX_F2MX",
#     "CHRIS/LIFFE_H",
#     "CHRIS/MCX_MO",
#     "CHRIS/CME_MP",
#     "CHRIS/CME_NFN",
#     "CHRIS/EUREX_FOAM",
#     "CHRIS/LIFFE_EBM",
#     "CHRIS/ICE_WA",
#     "CHRIS/LIFFE_MFA",
#     "CHRIS/LIFFE_MFC",
#     "CHRIS/CME_0D",
#     "CHRIS/CME_MNC",
#     "CHRIS/CME_MEO",
#     "CHRIS/CME_MJN",
#     "CHRIS/MX_SXM",
#     "CHRIS/MX_SCF",
#     "CHRIS/CME_0F",
#     "CHRIS/CME_MTS",
#     "CHRIS/CME_YK",
#     "CHRIS/CME_YW",
#     "CHRIS/CME_YC",
#     "CHRIS/CME_H3",
#     "CHRIS/CME_K2",
#     "CHRIS/CME_H5",
#     "CHRIS/CME_EJ",
#     "CHRIS/CME_H4",
#     "CHRIS/CME_MEL",
#     "CHRIS/CME_FDM",
#     "CHRIS/CME_PDM",
#     "CHRIS/CME_FTM",
#     "CHRIS/CME_PTM",
#     "CHRIS/CME_HMO",
#     "CHRIS/CME_HMW",
#     "CHRIS/CME_C0",
#     "CHRIS/CME_MBN",
#     "CHRIS/CME_8I",
#     "CHRIS/CME_B0",
#     "CHRIS/CME_7Q",
#     "CHRIS/CME_D0",
#     "CHRIS/CME_MNB",
#     "CHRIS/CME_MBE",
#     "CHRIS/EUREX_FMAS",
#     "CHRIS/SGX_AP",
#     "CHRIS/EUREX_FMCL",
#     "CHRIS/EUREX_FMCN",
#     "CHRIS/EUREX_FMCO",
#     "CHRIS/EUREX_FMCZ",
#     "CHRIS/EUREX_FMEY",
#     "CHRIS/EUREX_FMEA",
#     "CHRIS/EUREX_FMEE",
#     "CHRIS/EUREX_FMEM",
#     "CHRIS/EUREX_FMEL",
#     "CHRIS/EUREX_FMEU",
#     "CHRIS/LIFFE_MPE",
#     "CHRIS/EUREX_FMFM",
#     "CHRIS/SGX_HK",
#     "CHRIS/EUREX_FMHU",
#     "CHRIS/EUREX_FMIN",
#     "CHRIS/SGX_ID",
#     "CHRIS/EUREX_FMJP",
#     "CHRIS/EUREX_FMMY",
#     "CHRIS/EUREX_FMMX",
#     "CHRIS/EUREX_FMMA",
#     "CHRIS/EUREX_FMPE",
#     "CHRIS/EUREX_FMPH",
#     "CHRIS/EUREX_FMPL",
#     "CHRIS/EUREX_FMRS",
#     "CHRIS/EUREX_FMRU",
#     "CHRIS/SGX_SG",
#     "CHRIS/EUREX_FMZA",
#     "CHRIS/SGX_TW",
#     "CHRIS/EUREX_FMTH",
#     "CHRIS/EUREX_FMWO",
#     "CHRIS/CME_ND",
#     "CHRIS/CBOE_VN",
#     "CHRIS/MGEX_IC",
#     "CHRIS/MGEX_IS",
#     "CHRIS/CME_NG",
#     "CHRIS/MCX_NG",
#     "CHRIS/CME_HH",
#     "CHRIS/CME_HP",
#     "CHRIS/SHFE_RU",
#     "CHRIS/CME_MM",
#     "CHRIS/CME_NE",
#     "CHRIS/ICE_ZJ",
#     "CHRIS/ICE_NCF",
#     "CHRIS/CME_NL",
#     "CHRIS/CME_PD",
#     "CHRIS/MCX_NI",
#     "CHRIS/MCX_NIM",
#     "CHRIS/SGX_IN",
#     "CHRIS/OSE_NK225",
#     "CHRIS/CME_NK",
#     "CHRIS/SGX_NK",
#     "CHRIS/OSE_NK225M",
#     "CHRIS/OSE_NK300",
#     "CHRIS/SGX_ND",
#     "CHRIS/OSE_NKVI",
#     "CHRIS/CME_N1Y",
#     "CHRIS/CME_NF",
#     "CHRIS/ASX_VW",
#     "CHRIS/CME_VR",
#     "CHRIS/CME_NYF",
#     "CHRIS/CME_HOB",
#     "CHRIS/CME_HK",
#     "CHRIS/CME_MPX",
#     "CHRIS/CME_HA",
#     "CHRIS/CME_YH",
#     "CHRIS/CME_1U",
#     "CHRIS/CME_7Y",
#     "CHRIS/ICE_N",
#     "CHRIS/CME_K4",
#     "CHRIS/CME_K3",
#     "CHRIS/CME_KB",
#     "CHRIS/CME_KA",
#     "CHRIS/CME_A3",
#     "CHRIS/CME_Q5",
#     "CHRIS/CME_58",
#     "CHRIS/CME_4M",
#     "CHRIS/CME_4L",
#     "CHRIS/CME_D2",
#     "CHRIS/CME_T3",
#     "CHRIS/CME_KH",
#     "CHRIS/CME_KG",
#     "CHRIS/CME_D4",
#     "CHRIS/CME_D3",
#     "CHRIS/CME_KK",
#     "CHRIS/CME_KJ",
#     "CHRIS/CME_O",
#     "CHRIS/EUREX_FFOX",
#     "CHRIS/CME_OFM",
#     "CHRIS/CME_OPM",
#     "CHRIS/ICE_OJ",
#     "CHRIS/ODE_OR",
#     "CHRIS/OSE_DJIA",
#     "CHRIS/MX_OIS",
#     "CHRIS/CME_PA",
#     "CHRIS/CME_PH",
#     "CHRIS/CME_PC",
#     "CHRIS/EUREX_FPIG",
#     "CHRIS/CME_X1",
#     "CHRIS/CME_Y1",
#     "CHRIS/CME_Z9",
#     "CHRIS/CME_D7",
#     "CHRIS/CME_R7",
#     "CHRIS/CME_VP",
#     "CHRIS/CME_V3",
#     "CHRIS/CME_VM",
#     "CHRIS/CME_W4",
#     "CHRIS/CME_S4",
#     "CHRIS/CME_MOD",
#     "CHRIS/CME_R3",
#     "CHRIS/CME_E3",
#     "CHRIS/CME_D9",
#     "CHRIS/CME_D8",
#     "CHRIS/CME_E8",
#     "CHRIS/CME_D6",
#     "CHRIS/CME_F2",
#     "CHRIS/CME_J2",
#     "CHRIS/CME_46",
#     "CHRIS/CME_47",
#     "CHRIS/CME_B3",
#     "CHRIS/CME_N3",
#     "CHRIS/CME_L3",
#     "CHRIS/CME_UO",
#     "CHRIS/CME_B6",
#     "CHRIS/CME_UM",
#     "CHRIS/CME_JP",
#     "CHRIS/CME_4P",
#     "CHRIS/CME_4N",
#     "CHRIS/CME_F5",
#     "CHRIS/CME_L5",
#     "CHRIS/CME_W6",
#     "CHRIS/CME_L6",
#     "CHRIS/CME_E4",
#     "CHRIS/CME_J4",
#     "CHRIS/CME_L1",
#     "CHRIS/CME_N9",
#     "CHRIS/CME_JM",
#     "CHRIS/CME_PL",
#     "CHRIS/SGX_GOF",
#     "CHRIS/SGX_KRF",
#     "CHRIS/SGX_NJF",
#     "CHRIS/SGX_1MF",
#     "CHRIS/SGX_3MF",
#     "CHRIS/CME_PZ",
#     "CHRIS/MCX_POT",
#     "CHRIS/EUREX_FEPP",
#     "CHRIS/CME_QP",
#     "CHRIS/CME_1R",
#     "CHRIS/LIFFE_PSI",
#     "CHRIS/LIFFE_ECO",
#     "CHRIS/ODE_RS",
#     "CHRIS/CME_RBB",
#     "CHRIS/CME_RM",
#     "CHRIS/CME_RL",
#     "CHRIS/EUREX_FRDX",
#     "CHRIS/ICE_AFR",
#     "CHRIS/CME_NR",
#     "CHRIS/ICE_ATW",
#     "CHRIS/CME_RR",
#     "CHRIS/ICE_RF",
#     "CHRIS/ICE_RG",
#     "CHRIS/ICE_TF",
#     "CHRIS/ICE_RV",
#     "CHRIS/CME_RU",
#     "CHRIS/ICE_KRU",
#     "CHRIS/CME_GI",
#     "CHRIS/CME_MD",
#     "CHRIS/CBOE_VX",
#     "CHRIS/MX_SXF",
#     "CHRIS/MX_SXY",
#     "CHRIS/MX_SXB",
#     "CHRIS/MX_SXH",
#     "CHRIS/MX_SXA",
#     "CHRIS/CME_GA",
#     "CHRIS/CME_NJ",
#     "CHRIS/LIFFE_G",
#     "CHRIS/LIFFE_L",
#     "CHRIS/EUREX_FBTS",
#     "CHRIS/SGX_RT",
#     "CHRIS/SGX_TF",
#     "CHRIS/SHFE_AG",
#     "CHRIS/CME_SI",
#     "CHRIS/MCX_SI",
#     "CHRIS/MCX_AG",
#     "CHRIS/MCX_AGM",
#     "CHRIS/MCX_SIM",
#     "CHRIS/CME_UA",
#     "CHRIS/CME_SD",
#     "CHRIS/CME_SE",
#     "CHRIS/CME_SG",
#     "CHRIS/CME_AGA",
#     "CHRIS/CME_KS",
#     "CHRIS/CME_RK",
#     "CHRIS/CME_1N",
#     "CHRIS/CME_1NB",
#     "CHRIS/SGX_RGF",
#     "CHRIS/SGX_VCF",
#     "CHRIS/LIFFE_EPL",
#     "CHRIS/EUREX_FSMP",
#     "CHRIS/EUREX_FSLI",
#     "CHRIS/ICE_MP",
#     "CHRIS/EUREX_FSMI",
#     "CHRIS/EUREX_FSMM",
#     "CHRIS/CME_NS",
#     "CHRIS/CME_XN",
#     "CHRIS/MGEX_IW",
#     "CHRIS/ASX_US",
#     "CHRIS/CME_RA",
#     "CHRIS/CME_SZ",
#     "CHRIS/CME_8Z",
#     "CHRIS/ICE_IS",
#     "CHRIS/ICE_ISM",
#     "CHRIS/CME_SM",
#     "CHRIS/CME_BO",
#     "CHRIS/ICE_IBO",
#     "CHRIS/CME_S",
#     "CHRIS/ASX_AP",
#     "CHRIS/CME_CNH",
#     "CHRIS/MCX_STLRPR",
#     "CHRIS/SHFE_RB",
#     "CHRIS/SHFE_WR",
#     "CHRIS/EUREX_FSTX",
#     "CHRIS/ICE_SF",
#     "CHRIS/ICE_SB",
#     "CHRIS/CME_NKN",
#     "CHRIS/CME_SF",
#     "CHRIS/EUREX_FDIV",
#     "CHRIS/CME_Y7",
#     "CHRIS/CME_L4",
#     "CHRIS/CME_6Z",
#     "CHRIS/CME_NX",
#     "CHRIS/CME_9F",
#     "CHRIS/SGX_TR",
#     "CHRIS/ODE_TR",
#     "CHRIS/LIFFE_TPI",
#     "CHRIS/CME_CZ",
#     "CHRIS/CME_TR",
#     "CHRIS/CME_NZ",
#     "CHRIS/CME_TZ6",
#     "CHRIS/CME_TRY",
#     "CHRIS/CME_HR",
#     "CHRIS/ICE_Y",
#     "CHRIS/ICE_M",
#     "CHRIS/ICE_P",
#     "CHRIS/CME_UL",
#     "CHRIS/ICE_DX",
#     "CHRIS/ICE_NT",
#     "CHRIS/ICE_ZR",
#     "CHRIS/ODE_SB",
#     "CHRIS/SGX_NU",
#     "CHRIS/CME_UX",
#     "CHRIS/CME_PF",
#     "CHRIS/EUREX_FVS",
#     "CHRIS/ASX_WK",
#     "CHRIS/CME_NW",
#     "CHRIS/ICE_IW",
#     "CHRIS/CME_W",
#     "CHRIS/EUREX_FWHY",
#     "CHRIS/LIFFE_W",
#     "CHRIS/ICE_T",
#     "CHRIS/CME_CL",
#     "CHRIS/CME_CS",
#     "CHRIS/CME_AFF",
#     "CHRIS/ICE_TIB",
#     "CHRIS/CME_ABY",
#     "CHRIS/CME_BK",
#     "CHRIS/CME_FH",
#     "CHRIS/MCX_ZN",
#     "CHRIS/SHFE_ZN",
#     "CHRIS/MCX_ZNM",
# ]

COMMODITIES_TICKERS = [
    "CC=F",
    "CL=F",
    "CT=F",
    "ES=F",
    "GC=F",
    "GF=F",
    "HE=F",
    "HG=F",
    "HO=F",
    "KC=F",
    "KE=F",
    "LBS=F",
    "LE=F",
    "MGC=F",
    "NG=F",
    "NQ=F",
    "OJ=F",
    "PA=F",
    "PL=F",
    "RB=F",
    "RTY=F",
    "SB=F",
    "SI=F",
    "SIL=F",
    "YM=F",
    "ZB=F",
    "ZC=F",
    "ZF=F",
    "ZL=F",
    "ZM=F",
    "ZN=F",
    "ZO=F",
    "ZR=F",
    "ZS=F",
    "ZT=F",
    "BZ=F",
    "B0=F",
    "EURUSD=X",
    "JPY=X",
    "GBPUSD=X",
    "AUDUSD=X",
    "NZDUSD=X",
    "EURJPY=X",
    "GBPJPY=X",
    "EURGBP=X",
    "EURCAD=X",
    "EURSEK=X",
    "EURCHF=X",
    "EURHUF=X",
    "EURJPY=X",
    "CNY=X",
    "HKD=X",
    "SGD=X",
    "INR=X",
    "MXN=X",
    "PHP=X",
    "IDR=X",
    "THB=X",
    "MYR=X",
    "ZAR=X",
    "RUB=X",
    "^GSPC",
    "^DJI",
    "^IXIC",
    "^NYA",
    "^XAX",
    "^BUK100P",
    "^RUT",
    "^VIX",
    "^FTSE",
    "^GDAXI",
    "^FCHI",
    "^STOXX50E",
    "^N100",
    "^BFX",
    "IMOEX.ME",
    "^N225",
    "^HSI",
    "000001.SS",
    "399001.SZ",
    "^STI",
    "^AXJO",
    "^AORD",
    "^BSESN",
    "^JKSE",
    "^KLSE",
    "^NZ50",
    "^KS11",
    "^TWII",
    "^GSPTSE",
    "^BVSP",
    "^MXX",
    "^IPSA",
    "^MERV",
    "^TA125.TA",
    "^CASE30",
    "^JN0U.JO",
]

OTHER_TICKERS = [
    "ES=F",
    "YM=F",
    "NQ=F",
    "RTY=F",
    "ZB=F",
    "ZN=F",
    "ZF=F",
    "ZT=F",
    "GC=F",
    "MGC=F",
    "SI=F",
    "SIL=F",
    "PL=F",
    "HG=F",
    "PA=F",
    "CL=F",
    "HO=F",
    "NG=F",
    "RB=F",
    "BZ=F",
    "B0=F",
    "ZC=F",
    "ZO=F",
    "KE=F",
    "ZR=F",
    "ZM=F",
    "ZL=F",
    "ZS=F",
    "GF=F",
    "HE=F",
    "LE=F",
    "CC=F",
    "KC=F",
    "CT=F",
    "LBS=F",
    "OJ=F",
    "SB=F",
]


PINNACLE_DATA_FOLDER = "/nfs/data/files/DAILY/PINNACLE/CLCDATA/"
PINNACLE_DATA_CUT = "RAD"

PINNACLE_ASSETS = [
    "AN",
    "BN",
    "CA",
    "CC",
    "CN",
    "DA",
    "DT",
    "DX",
    "EN",
    "ER",
    "ES",
    "FB",
    "FN",
    "GI",
    "JN",
    "JO",
    "KC",
    "KW",
    "LB",
    "LX",
    "MD",
    "MP",
    "NK",
    "NR",
    "SB",
    "SC",
    "SN",
    "SP",
    "TY",
    "UB",
    "US",
    "XU",
    "XX",
    "YM",
    "ZA",
    "ZC",
    "ZF",
    "ZG",
    "ZH",
    "ZI",
    "ZK",
    "ZL",
    "ZN",
    "ZO",
    "ZP",
    "ZR",
    "ZT",
    "ZU",
    "ZW",
    "ZZ",
]

# TODO get rid of the ones not used get
PINNACLE_ASSET_CLASS_MAPPING = {
    "TY": "FI",
    "US": "FI",
    "FB": "FI",
    "UB": "FI",
    "DT": "FI",
    "ZA": "CM",
    "ZC": "CM",
    "ZG": "CM",
    "ZL": "CM",
    "ZW": "CM",
    "ZI": "CM",
    "ZP": "CM",
    "ZR": "CM",
    "ZZ": "CM",
    "KW": "CM",
    "ZT": "CM",
    "ZF": "CM",
    "ZK": "CM",
    "GI": "CM",
    "ZO": "CM",
    "ZH": "CM",
    "NR": "CM",
    "ZN": "CM",
    "ZU": "CM",
    "LB": "CM",
    "JO": "CM",
    "KC": "CM",
    "CC": "CM",
    "SB": "CM",
    "DA": "CM",
    "NK": "FX",
    "DX": "FX",
    "AN": "FX",
    "BN": "FX",
    "SN": "FX",
    "JN": "FX",
    "FN": "FX",
    "CN": "FX",
    "MP": "FX",
    "ER": "EQ",
    "XX": "EQ",
    "YM": "EQ",
    "ES": "EQ",
    "EN": "EQ",
    "SC": "EQ",
    "SP": "EQ",
    "MD": "EQ",
    "CA": "EQ",
    "XU": "EQ",
    "LX": "EQ",
    "AD": "FX",
    "AP": "FI",
    "AX": "EQ",
    "BC": "CM",
    "BG": "CM",
    "BO": "CM",
    "CB": "FX",
    "CL": "CM",
    "CT": "CM",
    "C_": "CM",
    "FA": "FI",
    "FC": "CM",
    "FX": "FX",
    "GC": "CM",
    "GS": "FI",
    "HG": "CM",
    "HO": "CM",
    "HS": "EQ",
    "LC": "CM",
    "LH": "CM",
    "MW": "CM",
    "NG": "CM",
    "O_": "CM",
    "PA": "CM",
    "PL": "CM",
    "RB": "CM",
    "SF": "FX",
    "SI": "CM",
    "SM": "CM",
    "S_": "CM",
    "TA": "FI",
    "TD": "FI",
    "TU": "FI",
    "UA": "FI",
    "W_": "CM",
    "ZB": "CM",
    "ZM": "CM",
    "ZS": "CM",
}
