TOKEN="AQVYKfL3E5Dxkb1QBCWH1edKaaFiYItFuOuHK3_WxOB2ivgMa01_bRxcGdGNxnQC7FV5xKfk3qcC_Rxua-3SGpqTiceHdBw_GtslFHouToPda6FcY-hQwoF1QnoKc9zc-lvsSIDYA_drUJ62ZEenvvaTC7S-BI-MpL9SENPEzEQAMpfQc6SHHPbLox-SL2wqqa6WiWY3Ru0Xiib4b18lxGl-z5zdUmshOKkgFF45VI054-lLBR2qdBGeW8gf5QE5ZFW-zupEM-LyQpwgbfuGDIYT1Cz-OXx_nre-HBrdursRtKfm9cIrURvj-wala_Fjr1DbOv07kmqxRykwCHVMtXgJo1F37Q"
URL="https://api.linkedin.com/v2/audienceCountsV2?q=targetingCriteriaV2&targetingCriteria=(include:(and:List((or:(urn%3Ali%3AadTargetingFacet%3Askills:List(urn%3Ali%3Askill%3A17))),(or:(urn%3Ali%3AadTargetingFacet%3Alocations:List(urn%3Ali%3AcountryGroup%3ANA))),(or:(urn%3Ali%3AadTargetingFacet%3AinterfaceLocales:List(urn%3Ali%3Alocale%3Aen_US))))))"

curl -i -H 'Authorization: Bearer '$TOKEN -H 'X-Restli-Protocol-Version: 2.0.0' $URL
