
import os
import pandas as pd

from src.datareader import get_metadata


def find_images_without_metadata(dataset_type: str):
    dataset_type = dataset_type.upper()
    if dataset_type not in ('TRAIN', 'TEST'):
        raise ValueError('The dataset type input must be either\
\"TRAIN\" or \"TEST\"')

    # Load the metadata file names
    metadata_file = os.path.join(os.getcwd(),
                                 'Chest_xray_Corona_Metadata.csv')
    df_name = 'X_ray_image_name'
    df_dataset_type = 'Dataset_type'
    metadata_df: pd.DataFrame = get_metadata(metadata_file)
    df_loc_series: pd.Series = metadata_df[df_dataset_type] == dataset_type
    image_names_with_metadata_dataset = sorted(list(metadata_df.loc[df_loc_series][df_name]))

    # Get the actual image files
    file_path = os.path.join(os.getcwd(), 'dataset', dataset_type)
    files_in_dataset_path = sorted(list(os.listdir(file_path)))

    if image_names_with_metadata_dataset == files_in_dataset_path:
        print('Both lists match!')
        return []
    missing_file_count = abs(len(image_names_with_metadata_dataset)
                             - len(files_in_dataset_path))
    if len(image_names_with_metadata_dataset) > len(files_in_dataset_path):
        print('There are %d more metadata files than available files' % missing_file_count)
        found_files_dict = dict.fromkeys(image_names_with_metadata_dataset, False)
        check_list = files_in_dataset_path
        missing_in_metadata = False
    else:
        print('There are %d more files than listed in the metadata' % missing_file_count)
        found_files_dict = dict.fromkeys(files_in_dataset_path, False)
        check_list = image_names_with_metadata_dataset
        missing_in_metadata = True

    # Cross-reference the names
    for basename in found_files_dict.keys():
        if basename in check_list:
            found_files_dict[basename] = True
    images_missing = [filename for (filename, in_metadata) in found_files_dict.items()
                      if not in_metadata]
    if missing_in_metadata:
        print('These files are missing in the metadata:')
    else:
        print('These files are missing in the data path \"%s\":' % file_path)
    print('\n'.join(images_missing))
    return images_missing
