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

def create_recipient(person):
	recipient = {
		"type": "email",
		"familyName": person["familyName"],
		"givenName": person["givenName"],
		"pubkey": person["publicKey"],
		"identity": person["identity"],
		"hashed": False
	}
	return recipient

def create_assertion(person, issued_on=str(date.today())):
	assertion = {
			"issuedOn": issued_on,
			"image:signature": config.ISSUER_SIGNATURE_IMAGE,
			"uid": person["uid"],
			"id": config.ISSUER_CERTS_URL+"/"+person["uid"],
			"evidence": {
				"type": "url",
				"data": config.ISSUER_CERTS_URL+"/"+person["uid"]+"/evidence"
			}
		}
	return assertion


def create_certificate():
	certificate = {
		"subtitle": {
	      	"content": config.CERTIFICATE_DATE,
	      	"display": True
	    },
	    "title": config.CERTIFICATE_TITLE,
	    "language": config.CERTIFICATE_LANGUAGE,
	    "image": config.CERTIFICATE_IMAGE,
	    "description": config.CERTIFICATE_DESCRIPTION,
	    "id": config.CERTIFICATE_ID,
	    "issuer": {
	    	"url": config.ISSUER_URL,
	    	"image": helpers.encode_image('img/labcdmx.png'),
	    	"email": config.ISSUER_EMAIL,
	    	"name": config.ISSUER_NAME,
	    	"id": config.ISSUER_ID
	    }
	}
	return certificate

def create_verification():
	verify = {
		"signer": config.ISSUER_PUBLIC_KEY_URL,
		"attribute-signed": "uid",
    	"type": "ECDSA(secp256k1)"
	}
	return verify

def create_extension(person):
	extension = {
	"assertion": {
		"endorsers": config.ASSERTION_ENSORERS
		}
	}
	return extension

def make_raw_json(recipient, assertion, certificate, verify, extension):
	raw_json = {
		"recipient": recipient,
		"assertion": assertion,
		"certificate": certificate,
		"verify": verify,
		"extension": extension
	}
	return raw_json

verify = create_verification()
certificate = create_certificate()
for person in people_info:
	recipient = create_recipient(person)
	assertion = create_assertion(person)
	extension = create_extension(person)
	raw_json = make_raw_json(recipient, assertion, certificate, verify, extension)
	filename = "raw_jsons/" + person["uid"]+".json"
	with open(filename, "wb") as jsonfile:
		jsonfile.write(json.dumps(raw_json, ensure_ascii=False)) #ensure the dumping doesn't mess up the JSON encoding!
