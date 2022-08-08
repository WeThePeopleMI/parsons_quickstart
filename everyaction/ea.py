# parsons everyaction docs https://move-coop.github.io/parsons/html/stable/ngpvan.html
from parsons import Table as table, VAN
import everyaction_creds
van = VAN(db='EveryAction')

roles = [233756, 468203, 468204, 468205, 468202, 233757] # new roles
event_types = [
	[543769,"1:1"],
	[265779,"Canvass"],
	[265781,"Training"],
	[543767,"Team meeting"],
	[543768,"Event"],
	[265787,"Ticketed Event"],
	[543779,"Action"],
	[543780,"Fundraiser"],
]
def create_event(values):
	print("in create event")
	event_id_result = van.create_event(
		name=values["name"], 
		short_name=values["short_name"], 
		start_date=values["start_date_time"], 
		end_date=values["end_date_time"], 
		event_type_id=values["event_type_id"], 
		roles=values["roles"], 
		description=values["description"],
	)
	return event_id_result

def get_event(event_id):
	print("in get_event. event_id:", event_id)
	van_event = van.get_event(event_id)
	return van_event


def main():
    print("ea_main_function")
    #example for getting event
    # 750811022 is event id for a demo event https://app.everyaction.com/EventDetailsNew.aspx?EventID=750811022
    returned_van_event = get_event("750811022")
    print(returned_van_event)


    #example for using create event
    returned_create_event = create_event({
    	"short_name":"pyt_crt",
    	"name": "Python create example",
    	"start_date_time":"8/8/2022 1:04:00 AM",
    	"end_date_time": "8/8/2022 8:05:00 AM",
    	"event_type_id": "543769", # view variable at top, this is a 
    	"roles": roles, #see global definition of roles
    	"description": "Python test",

    })
    print("returned_create_event", returned_create_event)
    print("returned event url: https://app.everyaction.com/EventDetailsNew.aspx?EventID=" + str(returned_create_event))
    #end_time_py = datetime.strptime("8/8/2022 8:05:00 AM", "%m/%d/%Y %H:%M:%S %p")  date parsing example


if __name__ == "__main__":
    main()

