import argparse
from restructure import transform_dataset

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Restructure Downloaded Reconstruct data into a compatible structure with Segmenter")
    parser.add_argument('--all_pid', required=False, dest='all_PID', action='store_true')
    parser.add_argument('--pid', required=False, help="Project ID to restructure")
    parser.set_defaults(all_PID=False)
    args = parser.parse_args()

    transform_dataset(args.pid, args.all_PID)
