from .base import CategorySource, CompanySource

nvidia_sources = CompanySource(
    name="NVIDIA",
    categories=[
        CategorySource(
            name="Engineering",
            url="https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite?locationHierarchy1=2fcb99c455831013ea52fb338f2932d8&jobFamilyGroup=0c40f6bd1d8f10ae43ffaefd46dc7e78",
        ),
        CategorySource(
            name="Program Management",
            url="https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite?locationHierarchy1=2fcb99c455831013ea52fb338f2932d8&jobFamilyGroup=0c40f6bd1d8f10ae43ffc668c6847e8c",
        ),
    ],
)
