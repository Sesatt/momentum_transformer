import os
from mom_trans.backtest import run_classical_methods

INTERVALS = [(2012, y, y + 1) for y in range(2020, 2023)]

REFERENCE_EXPERIMENT = "experiment_bitcoin_tft_cpnone_len252_notime_div_v1"

features_file_path = os.path.join(
    "data",
    "quandl_cpd_nonelbw.csv",
)

run_classical_methods(features_file_path, INTERVALS, REFERENCE_EXPERIMENT)
