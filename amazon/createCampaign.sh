#!/bin/bash

AUTH="Atza|IwEBIEcscbDAVxFjWPiDCQoDlkmJtGPlk7VKhO3kVJf20-BE4quVPA9hkYKnfJwcEl8x5x63fh4Nd9No4Ogi0jwJ6hA1h6WtiJObqZc9MyreYB2HMcZkW3ODvz18e6oEIzJkWJ1ne7mwg9lGJGNgLV2VOYzj_WcZwKjeZzDEvZNmPhTpZh8h-4IUrSGX_RTYF-DdWX790OPyKAwdnWrC5FaIBEXU1E0s54Bu_l_mGVVYQElkj_qBdm-P4YE3-fDHOXC088Lc-v-El9Sn8lZlkWKLhoLGxcI1HvBIZQUu0gdHivmGnwhFUeOvFjts3zmdsZLCi8LlW50cwZmvCa6YH95ITjLB-u1qq8j-wjxy-z2Ls4EgBNEe4gHjzS-DIsQjB4wgY7fI_tURok0AGB-t8JFfjZ8pD2nogiyuagl9w4uInzz528IjWzzOxrsyu9zaK5FvDjFDT0kKfROYjHf7Xg0SfsIpqEVDhN_6VxrV1aZwkIIJ5vn_OA0pfOu05_EvLCoWlE8gXVfnnwg4VQY9A4cmGA-7vtYjihdyeeCWWMVMnApLJ5kp_BR0IO0E1rE8UwTWRZ-5Tkr1JJY-t9aZ0xaRfvz0jn-HkuBisbHEcBK5Y8_kY78kxMH95WdWtFq941aPS3E"
KEYWORD_ID="196862097481071"
ACCOUNT_ID="188564931299575"

curl -X POST \
  https://advertising-api-test.amazon.com/v2/campaigns \
  -H "Content-Type: application/json" \
  -H "Authorization: bearer $AUTH" \
  -H "Amazon-Advertising-API-Scope: $ACCOUNT_ID" \
  -H 'Amazon-Advertising-API-ClientId: amzn1.application-oa2-client.608ec235b92245cfb286ee5c3f23b847' \
  -d '[
    {                                     
      "name": "Hello World Campaign",                                           
      "state": "enabled",                   
      "startDate": "20191021",              
      "campaignType": "sponsoredProducts",  
      "targetingType": "auto",              
      "dailyBudget": 1.00,
      "bidding": {
        "strategy": "legacyForSales",
        "adjustments": [{
          "predicate": "placementTop"
        }, {
          "predicate": "placementProductPage"
        }]
	    }
    }
  ]'
