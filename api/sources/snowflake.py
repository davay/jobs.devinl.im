from .base import CategorySource, CompanySource

snowflake_sources = CompanySource(
    name="Snowflake",
    categories=[
        CategorySource(
            name="IT",
            url="https://careers.snowflake.com/us/en/c/it-jobs?sortBy=Most%20recent&qcountry=United%20States",
        ),
        CategorySource(
            name="Engineering",
            url="https://careers.snowflake.com/us/en/c/engineering-jobs?sortBy=Most%20recent&qcountry=United%20States",
        ),
        CategorySource(
            name="Technical Program Manager",
            url="https://careers.snowflake.com/us/en/search-results?keywords=Technical%20Program%20Manager&qcountry=United%20States&sortBy=Most%20relevant",
        ),
        CategorySource(
            name="Machine Learning",
            url="https://careers.snowflake.com/us/en/search-results?keywords=Machine%20Learning&qcountry=United%20States&sortBy=Most%20relevant",
        ),
    ],
)
