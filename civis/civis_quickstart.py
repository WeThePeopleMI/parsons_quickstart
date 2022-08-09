
from parsons import Table, CivisClient
import civis_creds

def main():
	civis_client = CivisClient()
	#warning this takes a while!
	example_query = civis_client.query(sql="select * from tmc_van.campaigns", 
		preview_rows=10,
		 polling_interval=None, 
		 hidden=True, 
		 wait=True)
	print(example_query)

if __name__ == "__main__":
    main()
