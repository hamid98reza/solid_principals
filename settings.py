from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

DATA_FILE = os.environ.get("txtfile_path")