from voxsup.api.client.linkedin import LinkedInClient as Client

account_id = 502977261 # 4C Insights Test Account
client = Client(context={'account_id': account_id})
enable_requests_logging()

client.headers['X-RestLi-Protocol-Version'] = '2.0.0'
serialized_targeting_criteria = '(include:(and:List((or:(urn%3Ali%3AadTargetingFacet%3Askills:List(urn%3Ali%3Askill%3A17))),(or:(urn%3Ali%3AadTargetingFacet%3Alocations:List(urn%3Ali%3AcountryGroup%3ANA))),(or:(urn%3Ali%3AadTargetingFacet%3AinterfaceLocales:List(urn%3Ali%3Alocale%3Aen_US))))))'
url = 'audienceCountsV2?q=targetingCriteriaV2&targetingCriteria={0}'.format(
    serialized_targeting_criteria
)
response = client.get(url)
response.json()
