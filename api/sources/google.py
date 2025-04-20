from .base import CategorySource, CompanySource

google_sources = CompanySource(
    name="Google",
    categories=[
        CategorySource(
            name="ML",
            url="https://www.google.com/about/careers/applications/jobs/results?location=United%20States&degree=MASTERS&degree=BACHELORS&employment_type=FULL_TIME&sort_by=date&q=ML&target_level=MID&target_level=EARLY",
        ),
        CategorySource(
            name="Software Engineer",
            url="https://www.google.com/about/careers/applications/jobs/results?location=United%20States&degree=MASTERS&degree=BACHELORS&employment_type=FULL_TIME&sort_by=date&q=%22Software%20Engineer%22&target_level=MID&target_level=EARLY",
        ),
        CategorySource(
            name="Technical Program Manager",
            url="https://www.google.com/about/careers/applications/jobs/results/?q=%22Technical%20Program%20Manager%22&location=United%20States&target_level=MID&target_level=EARLY&degree=BACHELORS&degree=MASTERS&employment_type=FULL_TIME&sort_by=date",
        ),
    ],
)
