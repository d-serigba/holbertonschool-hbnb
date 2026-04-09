#!/bin/bash

# USERS
echo "== USERS =="
curl -s http://127.0.0.1:5000/users/; echo
curl -s -X POST http://127.0.0.1:5000/users/ \
    -H "Content-Type: application/json" \
    -d '{"email":"test@mail.com","password":"1234","first_name":"David","last_name":"Test"}'; echo
curl -s http://127.0.0.1:5000/users/; echo

# PLACES
echo "== PLACES =="
curl -s http://127.0.0.1:5000/places/; echo
curl -s -X POST http://127.0.0.1:5000/places/ \
    -H "Content-Type: application/json" \
    -d '{"title":"Appartement cosy","description":"Petit appartement charmant","price":50,"latitude":48.8566,"longitude":2.3522}'; echo
curl -s http://127.0.0.1:5000/places/; echo

# AMENITIES
echo "== AMENITIES =="
curl -s http://127.0.0.1:5000/amenities/; echo
curl -s -X POST http://127.0.0.1:5000/amenities/ \
    -H "Content-Type: application/json" \
    -d '{"name":"Piscine","description":"Piscine chauffée"}'; echo
curl -s http://127.0.0.1:5000/amenities/; echo

# REVIEWS
echo "== REVIEWS =="
curl -s http://127.0.0.1:5000/reviews/; echo
curl -s -X POST http://127.0.0.1:5000/reviews/ \
    -H "Content-Type: application/json" \
    -d '{"text":"Super séjour!","rating":4.5}'; echo
curl -s http://127.0.0.1:5000/reviews/; echo
