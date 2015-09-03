# coding=utf-8

import base64
from datetime import date
from helpers import encode_image

# GENERAL_INFORMATION
GENERAL_SIGNATURE = {
	"attribute-signed": "uid",
	"type": "ECDSA(secp256k1)"
}

# ISSUER INFORMATION
LAB_NAME = "Laboratorio para la Ciudad"
LAB_URL = "https://labcd.mx"
LAB_PUBLIC_KEY = ""
LAB_EMAIL = "certs@labcd.mx"
LAB_IMAGE = encode_image("img/labcdmx.png")
LAB_DESCRIPTION = {
	"english": "The Laboratorio para la Ciudad (Laboratory for the City) is Mexico City's new experimental office for civic innovation and urban creativity, the first city government department of its kind in Latin America. The Lab is a space for rethinking, reimagining, and reinventing the way citizens and government can work together towards a more open, more livable and more imaginative city.",
	"spanish": "El Laboratorio para la Ciudad es la nueva área experimental del Gobierno del Distrito Federal. El Laboratorio es un espacio de especulación y ensayo, donde lanzamos provocaciones que plantean nuevas formas de acercarse a temas relevantes para la ciudad, incubamos proyectos piloto y promovemos encuentros multidisciplinarios en torno a la innovación cívica y la creatividad urbana. El Laboratorio crea diálogos y complicidades entre gobierno, sociedad civil, iniciativa privada y organizaciones no gubernamentales con el propósito de reinventar, en conjunto, algunos territorios de ciudad y gobierno."
}

# COLLABORATOR INFORMATION
IDEO_PUBLIC_KEY = ""
IDEO_IMAGE = encode_image("img/ideo.png")
IDEO_URL = "http://ideo.com"
IDEO_NAME = "Ideo"

MEDIA_LAB_PUBLIC_KEY = ""
MEDIA_LAB_IMAGE = encode_image("img/medialab.png")
MEDIA_LAB_URL = "http://media.mit.edu"
MEDIA_LAB_NAME = "MIT Media Lab"

# PARTICIPANT INFORMATION
IDENTITY_TYPE = "email"

# WORKSHOP DEFINITION
WORKSHOP_DEFINITION = {
	"english": "An immersive learning experience where the participants are supported to develop their skills in a particular area through active engagement in which they share, learn, create, and reflect.",
	"spanish": "Experiencia intensiva de aprendizaje donde los participantes cuentan con el apoyo y las herramientas necesarias para desarrollar sus habilidades en un área específica mediante una participación activa en la que aprenden, comparten, crean y reflexionan."
}
EVENT_TYPE = "workshop"

# WORKSHOP INFORMATION
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

#ASSERTION INFORMATION
SIGNATURE_IMAGE = encode_image("img/signature.png")
