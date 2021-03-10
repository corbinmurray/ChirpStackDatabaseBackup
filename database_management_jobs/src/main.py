

"""
    This file will be the main driver for configuring and adding two cron jobs.

    First cron job will be the database management archiving process.

    Second cron job will be the database management retention process.
"""

from pathlib import Path
import os


def main():
    file_dir_path = Path(__file__).parent.absolute()
    python_executable_path = Path.joinpath(file_dir_path.parent, "bin", "python3").absolute()
    database_backup_process_file_path = Path.joinpath(file_dir_path, "database_backup", "database_backup.py")
    database_retention_process_file_path = Path.joinpath(file_dir_path, "database_retention", "database_retention.py")

    # Every day at 12:00am
    backup_process_crontime = "0 0 * * *"

    # Every first day of the month at 12:00am
    retention_process_crontime = "0 0 1 * *"

    print("Starting configuration for database management backup and retention processes...\n")

    backup_cronjob_cmd = f'echo "{backup_process_crontime}" {python_executable_path} {database_backup_process_file_path} | sort - | uniq - | crontab -'
    os.system(backup_cronjob_cmd)

    print("Added backup cronjob")

    retention_cronjob_cmd = f'echo "{retention_process_crontime}" {python_executable_path} {database_retention_process_file_path} | sort - | uniq - | crontab -'
    os.system(retention_cronjob_cmd)

    print("Added retention cronjob")

    print("\nFinished configuration")


if __name__ == "__main__":
    main()