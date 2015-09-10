# coding=utf-8

import base64
from datetime import date
import helpers

# ISSUER INFORMATION
ISSUER_URL = "http://labcd.mx"
ISSUER_CERTS_URL = "http://certs.labcd.mx"
ISSUER_PUBLIC_KEY_URL = "http://certs.labcd.mx/keys/labcdmx-certs-public-key.asc"
ISSUER_SIGNATURE_IMAGE = helpers.encode_image("img/signature.png")
ISSUER_EMAIL = "certs@labcd.mx"
ISSUER_NAME = "Laboratorio para la Ciudad"
ISSUER_ID = "http://certs.labcd.mx/issuer/labcdmx-issuer.json"

# CERTIFICATE INFORMATION
CERTIFICATE_LANGUAGE = "es-MX" #LANGUAGE AND COUNTRY INFORMATION
CERTIFICATE_DESCRIPTION = "En reconocimiento a tu participación en \"ciudad prototipo\", un taller realizado en colaboración con el MIT Media Lab e IDEO con el propósito de explorar, compartir y prototipar nuevas maneras de acercamiento a problemas cotidianos de la ciudad de México mediante la colaboración entre estudiantes, profesionales y especialistas."
CERTIFICATE_DATE = str(date(month=9, day=1, year=2015))+"/"+str(date(month=9, day=4, year=2015))
CERTIFICATE_TITLE = "Ciudad Prototipo"
CERTIFICATE_IMAGE = helpers.encode_image("img/header.png")
CERTIFICATE_ID = ISSUER_CERTS_URL + "/criteria/2015/09/ciudad-prototipo.json"

# EXTENSION INFORMATION
ASSERTION_ENSORERS = [
	{
      "name": "MIT Media Lab",
      "url": "http://media.mit.edu",
      "image": helpers.encode_image("img/medialab.png")
    },
    {
      "name": "IDEO",
      "url": "http://ideo.com",
      "image": helpers.encode_image("img/ideo.png")
    }
]
