import json
import csv
from datetime import date
import base64
import config
import copy
import helpers

people_info = []
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
		people_info.append(data)
csvfile.close()

with open('data/issuer_and_collaborator_info.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter=",")
	collaborators = []
	issuer = None
	for row in reader:
		data = {
				"name": row[0],
				"publicKey": row[1],
				"image": helpers.encode_image("img/"+row[2]),
				"url": row[3],
				"type": row[4]
			}
		if row[4] == "collaborator":
			collaborators.append(data)
		elif row[4] == "issuer":
			data["email"] = row[5]
			data["description"] = {
				"english": row[6],
				"spanish": row[7]
				}
			issuer = data
	issuer_and_collaborator_info = {
		"issuer": issuer,
		"collaborators" : collaborators
	}
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
	    }
	}
	for key in issuer_and_collaborator_info:
		certificate[key] = issuer_and_collaborator_info[key]
	return certificate

def create_verification():
	verify = {
		"issuer": None,
		"collaborators": []
	}
	for key in issuer_and_collaborator_info:
		if key == "collaborators":
			for c in issuer_and_collaborator_info[key]:
				data = copy.deepcopy(config.GENERAL_SIGNATURE)
				print c
				data["name"] = c["name"]
				data["signer"] = c["publicKey"]
				verify["collaborators"].append(data)
		elif key == "issuer":
			data = copy.deepcopy(config.GENERAL_SIGNATURE)
			data["name"] = issuer_and_collaborator_info[key]["name"]
			data["signer"] = issuer_and_collaborator_info[key]["publicKey"]
			verify["issuer"] = data
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
for person in people_info:
	recipient = create_recipient(person)
	assertion = create_assertion(person)
	raw_json = make_raw_json(recipient, assertion, certificate, verify)
	filename = "raw_jsons/" + person["uid"]+".json"
	with open(filename, "wb") as jsonfile:
		jsonfile.write(json.dumps(raw_json, ensure_ascii=False)) #ensure the dumping doesn't mess up the JSON encoding!
