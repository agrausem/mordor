# -*- coding: utf-8 -*-

import spyre

spec_filepath = '../server/lord_of_the_ring.json'

frodon_client = spyre.new_from_spec(
        spec_filepath,
        base_url="http://localhost:5000")

# activation du middleware de Basic Auth
frodon_client.enable('auth.Basic', username="frodon.sacquet",
        password="i_m_secretly_in_love_with_my_friend_sam_gamegie")

# activation du middleware json
frodon_client.enable('format.Json')


response = frodon_client.get_ring(id="9", format="json")

# code de retour de la réponse -> 200
assert(response.status==200)

# url générée avant envoi de la requête
assert(response.base=='http://localhost:5000/rings/9.json')

# contenu de la réponse
expect_content = {
    "owner": "Dark Lord", 
    "message": "One Ring to rule them all, One Ring to find them \
One Ring to bring them all and in the darkness bind them", 
    "id": 9}
assert(response.content==expect_content)

print response.content
