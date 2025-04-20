from .base import CategorySource, CompanySource

hudson_river_trading_sources = CompanySource(
    name="Hudson River Trading",
    categories=[
        CategorySource(
            name="Systems and Networking",
            url="https://www.hudsonrivertrading.com/careers/?_4118765=Full-Time%3A+New+Grad%2CFull-Time%3A+Experienced&_offices=Austin%2CBoulder%2CChicago%2CNew+York&_4168241=Systems+and+Networking%3A+Information+Security",
        ),
        CategorySource(
            name="Strategy Development",
            url="https://www.hudsonrivertrading.com/careers/?_4118765=Full-Time%3A+New+Grad%2CFull-Time%3A+Experienced&_offices=Austin%2CBoulder%2CChicago%2CNew+York&_4168241=Strategy+Development",
        ),
        CategorySource(
            name="Software Engineering",
            url="https://www.hudsonrivertrading.com/careers/?_4118765=Full-Time%3A+New+Grad%2CFull-Time%3A+Experienced&_offices=Austin%2CBoulder%2CChicago%2CNew+York&_4168241=Software+Engineering%3AC%2B%2B%2CSoftware+Engineering%3APython",
        ),
    ],
)
