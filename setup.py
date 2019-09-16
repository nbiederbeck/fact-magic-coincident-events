from setuptools import setup, find_packages

setup(
    name="coincident_event_finder",
    description="Get event numbers of coincident fact-magic events",
    version="0.1.0",
    author="Noah Biederbeck",
    author_email="noah.biederbeck@tu-dortmund.de",
    packages=find_packages(),
    usage_requires=["pandas", "numpy", "sortedcontainers"],
    test_requires=["pandas"],
)
