'''
commands: 
    -i info: prints all buckets
    
    -i info bucket_name: prints all files in the bucket
    
    -di detailed_info: prints all buckets and files in each bucket
    
    -c create bucket_name: creates a bucket with the bucket name
    
    -u upload file bucket: uploads file into bucket
    
    -db download_bucket bucket_name: downloads bucket
    
    -d download file bucket_name: downloads file from bucket
'''
import os
import sys
from pprint import pprint

from s3 import S3

if __name__ == '__main__':
    print()
    s3 = S3()
    try:
        command = sys.argv[1].lower()
    except IndexError:
        print('No command found. Please type -h or help for list of commands.')
        exit()
    
    if (command == '-h' or command == 'help'):
        print('Welcome to the python AWS S3 library')
        print()
        print('These are the available commands:\n')
        print('-i info: prints all buckets')
        print('-i info bucket_name: prints all files in the bucket')
        print('-di detailed_info: prints all buckets and files in each bucket\n')
        
        print('-c create bucket_name: creates a bucket with the bucket name\n')
        print('-u upload file bucket: uploads file into bucket')
        print('-db download_bucket bucket_name download_path: downloads bucket to download_path')
        print('-d download file bucket_name download_path: downloads file from bucket to download_path') 
        print()
    if (command == '-i' or command == 'info'):
        try:
            bucket = sys.argv[2]
            s3.print_files_in_buckets(bucket)
        except IndexError:
            s3.print_buckets()
    
    if (command == '-di' or command == 'detailed_info'):
        for bucket in s3.get_buckets(s3):
            print('Bucket Name:', bucket)
            s3.print_files_in_buckets(bucket)
            
    if (command == '-c' or command == 'create'):
        try:
            bucket = sys.argv[2]
            s3.create_bucket(bucket)
        except IndexError:
            print('Bucket name not specified. Please enter a bucket name or type -h or help for list of commands.')
            exit()
    
    if (command == '-u' or command == 'upload'):
        try:
            file = sys.argv[2]
            bucket = sys.argv[3]
            s3.upload_file(file, bucket)
        except IndexError:
            print('File or Bucket name not specified. Please enter both names or type -h or help for list of commands.')
            exit()
            
    if (command == '-db' or command == 'download_bucket'):
        try:
            bucket = sys.argv[2]
        except IndexError:
            print('Bucket name or download path not specified. Please enter both names or type -h or help for list of commands.')
            exit()
        download_path = sys.argv[3] if len(sys.argv) > 3 else bucket
        s3.download_bucket(bucket, download_path = download_path)
            
    if (command == '-d' or command == 'download'):
        try:
            file = sys.argv[2]
            bucket = sys.argv[3]
        except IndexError:
            print('File Name or Bucket name or download path not specified. Please enter both names or type -h or help for list of commands.')
            exit()
        download_path = sys.argv[4] if len(sys.argv) > 4 else bucket
        s3.download_file(file, bucket, download_path = download_path)