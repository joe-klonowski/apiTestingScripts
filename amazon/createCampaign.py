from voxsup.api.client.amazon import AmazonClient
account_id = "188564931299575"
client = AmazonClient(context={"account_id": account_id})
enable_requests_logging()

data = [{
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
}]
response = client.post('sp/campaigns', json=data)
response.json()
