# -*- coding: utf-8 -*-

import spyre
import json

spec_filepath = '../server/lord_of_the_ring.json'

frodon_client = spyre.new_from_spec(
        spec_filepath,
        base_url="http://localhost:5000")


frodon_client.enable('auth.Basic', username="frodon.sacquet",
        password="i_m_secretly_in_love_with_my_friend_sam_gamegie")

response = frodon_client.get_ring(id="9", format="json")

# code de retour de la réponse -> 200
assert(response.status==200)

# url générée avant envoi de la requête
assert(response.base=='http://localhost:5000/rings/9.json')


# contenu de la réponse
the_only_one = json.loads(response.content)
expect_content = {
    "owner": "Dark Lord", 
    "message": "One Ring to rule them all, One Ring to find them \
One Ring to bring them all and in the darkness bind them", 
    "id": 9}
assert(the_only_one==expect_content)

print the_only_one
