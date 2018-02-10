from __future__ import division
import pytest
import tinysumma as ts
from pkg_resources import resource_filename

@pytest.fixture(scope='module')
def sampledatadir():
    sampledatadir = resource_filename('tinysumma', 'data/')
    return sampledatadir

# bare bones tests for no glaring issues: can we load the sample csv files and
# run the analysis functions without throwing an error, and returning something
# other than None? Include non-ascii characters in messages.csv.
def test_latest_issue(sampledatadir):
    print(sampledatadir)
    latest = ts.latest_issue(sampledatadir)
    assert latest is not None

def test_numbered_issue(sampledatadir):
    issue = ts.numbered_issue(2, sampledatadir)
    assert issue is not None
