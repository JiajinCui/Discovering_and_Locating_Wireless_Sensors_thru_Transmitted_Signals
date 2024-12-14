import h5py
import numpy as np

def explore_h5_file(file_path):
    # Open the HDF5 file in read-only mode
    with h5py.File(file_path, 'r') as f:
        # Print the structure of the file
        print("File structure:\n")
        print(f"Root keys: {list(f.keys())}")  # Show top-level groups or datasets

        # Recursively explore all groups and datasets
        def explore_group(group, indent=0):
            """Recursively explore groups and datasets."""
            for key in group.keys():
                item = group[key]
                # Print the name of the item (dataset or group)
                print(" " * indent + f"Key: {key} - Type: {type(item)}")

                if isinstance(item, h5py.Group):
                    # If the item is a group, recurse into it
                    print(" " * (indent + 2) + f"Group '{key}' contains:")
                    explore_group(item, indent + 4)
                elif isinstance(item, h5py.Dataset):
                    # If the item is a dataset, print its shape and dtype
                    print(" " * (indent + 2) + f"Dataset '{key}' shape: {item.shape} dtype: {item.dtype}")

                    # Optionally, read a portion of the dataset (first 5 entries, if it's not too large)
                    try:
                        sample_data = item[:5]  # Read first 5 entries
                        print(" " * (indent + 4) + f"Sample data: {np.mean(sample_data)}")
                    except Exception as e:
                        print(" " * (indent + 4) + f"Error reading sample data: {e}")
                else:
                    print(" " * (indent + 2) + f"Unknown item type: {type(item)}")

        # Start exploring the root of the file
        explore_group(f)

# Replace with the path to your .h5 file
file_path = '/media/gaofeng/Extreme SSD/datasets/spectrum_sensing_stitching/signal_bank/wifi.h5'
explore_h5_file(file_path)

