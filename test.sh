#!/bin/sh

curl -X POST -v http://localhost/api/client/ -H 'Content-Type: application/json' -d '{ "name": "zdb" }'
curl -X POST -v http://localhost/api/user/ -H 'Content-Type: application/json' -d '{ "name": "eric", "roles": ["ADMIN", "ARCHILYSE_ONE_ADMIN"], "password": "eric123", "client_id": "1", "login": "eric", "email": "eric.norman@zynka.se", "email_validated": true }'
