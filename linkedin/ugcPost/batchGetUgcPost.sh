TOKEN="AQX27ZGt4ZK_ELg0gWY19dWDO0E9dUCDTBHVmxX55Omecp7dfyBklmfJ6zC83poBKhDORlrC7OhK74eStN4SjVgwU3_NHWQ_Ft79_BU6LyDtW_j5wRmlUovj1bKr-2eYzKBylu7967FIuZHgy7_oUIAmxUSp-sAaz0ShNqXGOqzlqVx9hDzFfXkwM_Pi4GHWb-OQQJQRnQNDq2cez9__qnlWaZ0rSDUZoQ0uolFfw-0v4xlsZSMsw-n9ygbyC-eUXnewWXQFEGkk-ymXnvB_Oko75snwv8GxHmSO_mg6xMJiVlOj-uY4xzN0ihc95OmgD72gX3iRBo_BAfQsNuullYzeoxpfXw"
URL="https://api.linkedin.com/v2/ugcPosts?ids=List(urn%3Ali%3AugcPost%3A6456174447488430082,urn%3Ali%3AugcPost%3A6452598395432505344)"

curl -v -H 'Authorization: Bearer '$TOKEN -H 'X-RestLi-Protocol-Version: 2.0.0' $URL
