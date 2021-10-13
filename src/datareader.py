
import pandas as pd
from collections import OrderedDict
import numpy as np


def get_metadata(filename='Chest_xray_Corona_Metadata.csv'
                 ) -> pd.DataFrame:
    """Get the metadata CSV file

    :param filename: The filename
    :return: pd.DataFrame
    """
    df: pd.DataFrame
    dtype = OrderedDict({
        'Index': np.int64,
        'X_ray_image_name': str,
        'Label': str,
        'Dataset_type': str,
        'Label_2_Virus_category': str,
        'Label_1_Virus_category': str
    })
    names = list(dtype.keys())
    usecols = range(1, 6)
    df = pd.read_csv(filename,
                     skiprows=[0],
                     names=names,
                     dtype=dtype,
                     usecols=usecols)
    df.fillna('', inplace=True)
    return df


def get_summary_data(filename='Chest_xray_Corona_dataset_Summary.csv'
                     ) -> pd.DataFrame:
    """Get the summary CSV file

    :param filename: The filename
    :return: pd.DataFrame
    """
    df: pd.DataFrame
    dtype = OrderedDict({
        'Index': np.int64,
        'Label': str,
        'Label_2_Virus_category': str,
        'Label_1_Virus_category': str,
        'Image_Count': int
    })
    usecols = range(1, 5)
    names = list(dtype.keys())
    df = pd.read_csv(filename,
                     skiprows=[0],
                     names=names,
                     dtype=dtype,
                     usecols=usecols)
    df.fillna('', inplace=True)
    return df
