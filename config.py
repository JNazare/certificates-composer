# coding=utf-8

import base64
from datetime import date
from helpers import encode_image

# GENERAL_INFORMATION
GENERAL_SIGNATURE = {
	"attribute-signed": "uid",
	"type": "ECDSA(secp256k1)"
}
IDENTITY_TYPE = "email"

#ASSERTION INFORMATION
SIGNATURE_IMAGE = encode_image("img/signature.png")

# WORKSHOP INFORMATION
EVENT_TYPE = "workshop"
WORKSHOP_DEFINITION = {
	"english": "An immersive learning experience where the participants are supported to develop their skills in a particular area through active engagement in which they share, learn, create, and reflect.",
	"spanish": "Experiencia intensiva de aprendizaje donde los participantes cuentan con el apoyo y las herramientas necesarias para desarrollar sus habilidades en un área específica mediante una participación activa en la que aprenden, comparten, crean y reflexionan."
}
WORKSHOP_DESCRIPTION = {
	"english": "In appreciation of your participation in CIUDAD PROTOTIPO, a workshop in collaboration with the MIT Media Lab and IDEO with the aim of exploring, sharing, and prototyping new approaches to problems in Mexico City through collaboration between students, professionals, and specialists.",
	"spanish": "En reconocimiento a tu participación en \"ciudad prototipo\", un taller realizado en colaboración con el MIT Media Lab e IDEO con el propósito de explorar, compartir y prototipar nuevas maneras de acercamiento a problemas cotidianos de la ciudad de México mediante la colaboración entre estudiantes, profesionales y especialistas. "
}
WORKSHOP_START_DATE = str(date(month=9, day=1, year=2015))
WORKSHOP_END_DATE = str(date(month=9, day=4, year=2015))
WORKSHOP_DATE = WORKSHOP_START_DATE+"/"+WORKSHOP_END_DATE
WORKSHOP_HOURS = 40
WORKSHOP_PARTICIPANTS = 31
WORKSHOP_TITLE = "Ciudad Prototipo"
WORKSHOP_IMAGE = encode_image("img/header.png")

