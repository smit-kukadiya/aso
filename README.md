# ASO
This defines a lightweight Python class that can be used for store optimization
from Google Play Store and iTunes App Store.

Much of this has been adapted from 
[aso](https://github.com/facundoolano/aso), a 
nodeJS-based repo that does similar things. But this repo uses Python.

## Getting started

```
from aso import PositionKeywordApp

results = PositionKeywordApp("google").PositionKeywordApp(app_id="com.openai.chatgpt", country="en", lang="us")
print(results)
```


## Thanks to our Resources
[google-play-scracper](https://github.com/JoMingyu/google-play-scraper) <br/>
[itunes-app-scraper](https://github.com/digitalmethodsinitiative/itunes-app-scraper)
