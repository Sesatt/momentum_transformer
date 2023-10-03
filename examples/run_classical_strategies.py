import os
from mom_trans.backtest import run_classical_methods


INTERVALS = [(max(1990, y-10), y, min(y + 5, 2023 -1)) for y in range(2000, 2023 -1, 5)]

REFERENCE_EXPERIMENT = "experiment_sp500_tsmom_final_split80_tft_cpnone_len252_notime_div_v1"

features_file_path = os.path.join(
    "data",
    "quandl_cpd_nonelbw_tsmom_full_top2.csv",
)

run_classical_methods(features_file_path, INTERVALS, REFERENCE_EXPERIMENT)
