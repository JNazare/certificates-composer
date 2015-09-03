import json
import csv
from datetime import date
import base64
import config
import copy

csv_info = []
with open('data/participant_info.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=",")
	for row in reader:
		data = {
				"uid": row[0],
				"publicKey": row[1],
				"givenName": unicode(row[2], "utf-8").encode("utf-8"),
				"familyName": unicode(row[3], "utf-8").encode("utf-8"),
				"identity": row[4]
			}
		if len(row)>5:
			data["company"]=row[5]
		csv_info.append(data)
csvfile.close()

def create_recipient(person):
	recipient = {
		"type": config.IDENTITY_TYPE,
		"familyName": person["familyName"],
		"givenName": person["givenName"],
		"publicKey": person["publicKey"],
		"identity": person["identity"],
		"hashed": False
	}
	if person.get("company", None):
		recipient["company"] = person["company"]
	return recipient

def create_assertion(person, issued_on=str(date.today())):
	assertion = {
			"issuedOn": issued_on,
			"image:signature": config.SIGNATURE_IMAGE,
			"uid": person["uid"],
			"evidence": {} #this will be figured out tomorrow
		}
	return assertion


def create_certificate():
	certificate = {
		"facts": {
	      	"date": config.WORKSHOP_DATE,
	      	"hours": config.WORKSHOP_HOURS,
	      	"numberOfParticipants": config.WORKSHOP_PARTICIPANTS
	    },
	    "title": config.WORKSHOP_TITLE,
	    "image": config.WORKSHOP_IMAGE,
	    "description": config.WORKSHOP_DESCRIPTION,
	    "definition": {
	    	config.EVENT_TYPE: config.WORKSHOP_DEFINITION
	    },
	    "issuer": {
	      	"url": config.LAB_URL,
	      	"image": config.LAB_IMAGE,
	      	"email": config.LAB_EMAIL,
	      	"name": config.LAB_NAME,
	      	"description": config.LAB_DESCRIPTION
	    },
	    "collaborators":[
	    	{
	        	"url": config.MEDIA_LAB_URL,
	        	"image": config.MEDIA_LAB_IMAGE,
	        	"name": config.MEDIA_LAB_NAME
	      	},
	    	{
	    		"url": config.IDEO_URL,
	        	"image": config.IDEO_IMAGE,
	        	"name": config.IDEO_NAME
	      	}
	    ]
	}
	return certificate

def create_verification():
	issuer = copy.deepcopy(config.GENERAL_SIGNATURE)
	issuer["name"]=config.LAB_NAME
	issuer["signer"]=config.LAB_PUBLIC_KEY

	medialab = copy.deepcopy(config.GENERAL_SIGNATURE)
	medialab["name"]=config.MEDIA_LAB_NAME
	medialab["signer"]=config.MEDIA_LAB_PUBLIC_KEY

	ideo = copy.deepcopy(config.GENERAL_SIGNATURE)
	ideo["name"]=config.IDEO_NAME
	ideo["signer"]=config.IDEO_PUBLIC_KEY

	verify = {
		"issuer": issuer,
		"collaborators": [medialab, ideo]
	}
	return verify

def make_raw_json(recipient, assertion, certificate, verify):
	raw_json = {
		"recipient": recipient,
		"assertion": assertion,
		"certificate": certificate,
		"verify": verify
	}
	return raw_json

verify = create_verification()
certificate = create_certificate()
for person in csv_info:
	recipient = create_recipient(person)
	assertion = create_assertion(person)
	raw_json = make_raw_json(recipient, assertion, certificate, verify)
	filename = "raw_jsons/" + person["uid"]+".json"
	with open(filename, "wb") as jsonfile:
		jsonfile.write(json.dumps(raw_json, ensure_ascii=False)) #ensure the dumping doesn't mess up the JSON encoding!
