import json
import csv
import argparse

# Function to parse the log file and write to CSV


def parse_log_file(input_file, output_file):
    # Open a CSV file for writing
    with open(output_file, mode='w', newline='') as csv_file:
        fieldnames = [
            'node_name', 'time',
            'process_exec_id', 'process_pid', 'process_uid', 'process_cwd', 'process_binary', 'process_arguments', 'process_flags', 'process_start_time', 'process_auid', 'process_docker', 'process_parent_exec_id', 'process_refcnt', 'process_tid',
            'parent_exec_id', 'parent_pid', 'parent_uid', 'parent_cwd', 'parent_binary', 'parent_arguments', 'parent_flags', 'parent_start_time', 'parent_auid', 'parent_parent_exec_id', 'parent_tid',
            'function_name', 'sock_family', 'sock_type', 'sock_protocol', 'sock_saddr', 'sock_daddr', 'sock_sport', 'sock_dport', 'sock_cookie', 'sock_state', 'int_arg', 'action', 'policy_name', 'return_action'
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Read the JSON lines log data from the input file
        with open(input_file, 'r') as file:
            for line in file:
                log_data = json.loads(line)

                process_kprobe = log_data.get('process_kprobe', {})
                process = process_kprobe.get('process', {})
                parent = process_kprobe.get('parent', {})
                args = process_kprobe.get('args', [{}])
                sock_arg = args[0].get('sock_arg', {})
                int_arg = args[1].get('int_arg', None)

                row = {
                    'node_name': log_data.get('node_name'),
                    'time': log_data.get('time'),
                    'process_exec_id': process.get('exec_id'),
                    'process_pid': process.get('pid'),
                    'process_uid': process.get('uid'),
                    'process_cwd': process.get('cwd'),
                    'process_binary': process.get('binary'),
                    'process_arguments': process.get('arguments'),
                    'process_flags': process.get('flags'),
                    'process_start_time': process.get('start_time'),
                    'process_auid': process.get('auid'),
                    'process_docker': process.get('docker'),
                    'process_parent_exec_id': process.get('parent_exec_id'),
                    'process_refcnt': process.get('refcnt'),
                    'process_tid': process.get('tid'),
                    'parent_exec_id': parent.get('exec_id'),
                    'parent_pid': parent.get('pid'),
                    'parent_uid': parent.get('uid'),
                    'parent_cwd': parent.get('cwd'),
                    'parent_binary': parent.get('binary'),
                    'parent_arguments': parent.get('arguments'),
                    'parent_flags': parent.get('flags'),
                    'parent_start_time': parent.get('start_time'),
                    'parent_auid': parent.get('auid'),
                    'parent_parent_exec_id': parent.get('parent_exec_id'),
                    'parent_tid': parent.get('tid'),
                    'function_name': process_kprobe.get('function_name'),
                    'sock_family': sock_arg.get('family'),
                    'sock_type': sock_arg.get('type'),
                    'sock_protocol': sock_arg.get('protocol'),
                    'sock_saddr': sock_arg.get('saddr'),
                    'sock_daddr': sock_arg.get('daddr'),
                    'sock_sport': sock_arg.get('sport'),
                    'sock_dport': sock_arg.get('dport'),
                    'sock_cookie': sock_arg.get('cookie'),
                    'sock_state': sock_arg.get('state'),
                    'int_arg': int_arg,
                    'action': process_kprobe.get('action'),
                    'policy_name': process_kprobe.get('policy_name'),
                    'return_action': process_kprobe.get('return_action'),
                }

                # Write the row to the CSV file
                writer.writerow(row)

    print(f"Log data has been written to {output_file}")

# Main function to handle command-line arguments


def main():
    parser = argparse.ArgumentParser(
        description="Parse a JSONL log file and output to CSV.")
    parser.add_argument('input_file', help="Path to the input log file")
    parser.add_argument('output_file', help="Path to the output CSV file")
    args = parser.parse_args()

    parse_log_file(args.input_file, args.output_file)


if __name__ == '__main__':
    main()
