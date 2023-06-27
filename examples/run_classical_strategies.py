import os
from mom_trans.backtest import run_classical_methods


INTERVALS = [(1990, y, min(y + 5, 2023 -1)) for y in range(2010, 2023 -1, 5)]

REFERENCE_EXPERIMENT = "experiment_sp500_tsmom_tft_cpnone_len252_notime_div_v1"

features_file_path = os.path.join(
    "data",
    "quandl_cpd_nonelbw_tsmom.csv",
)

run_classical_methods(features_file_path, INTERVALS, REFERENCE_EXPERIMENT)
