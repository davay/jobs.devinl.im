from .base import CategorySource, CompanySource

meta_sources = CompanySource(
    name="Meta",
    categories=[
        CategorySource(
            name="Technical Program Management",
            url="https://www.metacareers.com/jobs/?sort_by_new=true&teams[0]=Technical%20Program%20Management&offices[0]=North%20America",
        ),
        CategorySource(
            name="Software Engineering",
            url="https://www.metacareers.com/jobs/?sort_by_new=true&teams[0]=Software%20Engineering&offices[0]=North%20America",
        ),
        CategorySource(
            name="Data & Analytics",
            url="https://www.metacareers.com/jobs/?sort_by_new=true&teams[0]=Data%20%26%20Analytics&offices[0]=North%20America",
        ),
        CategorySource(
            name="Artificial Intelligence",
            url="https://www.metacareers.com/jobs/?sort_by_new=true&teams[0]=Artificial%20Intelligence&offices[0]=North%20America",
        ),
        CategorySource(
            name="AR/VR",
            url="https://www.metacareers.com/jobs/?sort_by_new=true&teams[0]=AR%2FVR&offices[0]=North%20America",
        ),
    ],
)
