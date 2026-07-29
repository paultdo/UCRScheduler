from app.models.section import Section
from app.models.meeting import Meeting
from app.scheduler.solver import bundles_conflict  # adjust import path to wherever you put it
from app.scraper.parser import parse_time

# Case 1: conflicting bundles
section_1 = Section(meetings=[Meeting(begin_time=parse_time("1000"), end_time=parse_time("1100"), monday=True)])
section_2 = Section(meetings=[Meeting(begin_time=parse_time("1030"), end_time=parse_time("1130"), monday=True)])

bundle_a = (section_1,)
bundle_b = (section_2,)

print("Test 1 (should be True):", bundles_conflict(bundle_a, bundle_b))

# Case 2: non-conflicting bundles
section_3 = Section(meetings=[Meeting(begin_time=parse_time("1000"), end_time=parse_time("1100"), monday=True)])
section_4 = Section(meetings=[Meeting(begin_time=parse_time("1000"), end_time=parse_time("1100"), tuesday=True)])

bundle_c = (section_3,)
bundle_d = (section_4,)

print("Test 2 (should be False):", bundles_conflict(bundle_c, bundle_d))