# Data preprocessing utilities
import pandas as pd
import numpy as np

def load_data(filepath):
    """Load insurance data from CSV"""
    return pd.read_csv(filepath)
