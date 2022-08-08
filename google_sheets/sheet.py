# parsons google sheet docs https://move-coop.github.io/parsons/html/stable/google.html#id15
# Table object type info https://move-coop.github.io/parsons/html/stable/table.html

from parsons import Table, GoogleSheets
import json
from datetime import datetime, timedelta


with open('service_account_parsons.json') as creds:
  gs = GoogleSheets(google_keyfile_dict=json.load(creds))

# sheet here: https://docs.google.com/spreadsheets/d/1RFCaphy9moYa5qjXIAGb57M0U3fBNBQqutQDtcy7h9s/edit#gid=0
# confirm your service account email, under "client_email" is shared to it.
ss_id = "1RFCaphy9moYa5qjXIAGb57M0U3fBNBQqutQDtcy7h9s"

ss = gs.get_worksheet(ss_id)


def main():
  print(ss)

  ss_dict = ss.to_dicts()

  print(ss_dict)

  #to overwrite the sheet after an anlysis
  # gs.overwrite_sheet(ss_id, Table(ss_dict))

  #example rows to append, have to be a parsons table
  example_table = Table(
        [
          {
            "header1":"new row!", 
            "header2": str(datetime.now())
          }
        ]
      )
  #append
  gs.append_to_sheet(
      spreadsheet_id=ss_id, 
      table=example_table,
      worksheet=0, 
    )


if __name__ == "__main__":
    main()
