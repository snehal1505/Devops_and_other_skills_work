import argparse


# Create the parser
parser = argparse.ArgumentParser(description='Example argument parser')

 

# Add arguments
parser.add_argument('--source_url', help='localhost:3306', required=True)
parser.add_argument('--source_username', help='root', required=True)
parser.add_argument('--source_password', help='Root@123', required=False)
parser.add_argument('--source_db', help='hr', required=True)
parser.add_argument('--source_port', help='3306', type=int, required=True)
parser.add_argument('--source_table', help='employees', required=True)
parser.add_argument('--target_url', help='localhost:3306', required=True)
parser.add_argument('--target_username', help='root', required=True)
parser.add_argument('--target_password', help='Root@123', required=True)
parser.add_argument('--target_port', help='3306', type=int, required=True)
parser.add_argument('--target_db', help='mydb', required=True)
parser.add_argument('--target_table', help='student', required=True)

# Parse the arguments
args = parser.parse_args()

# Access the argument values
source_url = args.source_url
source_username = args.source_username
source_password = args.source_password
source_port = args.source_port
source_db = args.source_db
source_table = args.source_table
target_url = args.target_url 
target_username = args.target_username
target_password = args.target_password
target_port = args.target_port
target_db = args.target_db
target_table = args.target_table


# Print the values
print('SOURCE_URL:', source_url)
print('SOURCE_USERNAME:', source_username)
print('SOURCE_PASSWORD:', source_password)
print('SOURCE_PORT:', source_port)
print('SOURCE_DB:', source_db)
print('SOURCE_TABLE:', source_table)
print('TARGET_URL:', target_url)
print('TARGET_USERNAME:', target_username)
print('TARGET_PASSWORD:', target_password)
print('SOURCE_PORT:' , source_port)
print('TARGET_DB:', target_db)
print('TARGET_TABLE:', target_table)
