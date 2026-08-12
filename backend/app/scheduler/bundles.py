from app.models.course import Course
from app.models.section import Section
from collections import defaultdict
from itertools import product, combinations
from app.scheduler.solver import bundles_conflict

def build_bundles(course: Course) -> list[tuple[Section, ...]]:
    sections_group = defaultdict(list)
    for section in course.sections:
        sections_group[section.link_group].append(section)

    link_type_groups = {}
    for group, sections in sections_group.items():
        link_type_groups[group] = defaultdict(list)
        for section in sections:
            link_type_groups[group][section.link_type].append(section)

    result = []
    for group in link_type_groups:
        arr_cartesian = []
        for arr in link_type_groups[group].values():
            arr_cartesian.append(arr)
        valid_candidates = [c for c in product(*arr_cartesian) if not candidate_conflict(c)]
        result.extend(valid_candidates)

    return result

def candidate_conflict(candidate_bundle: tuple) -> bool:
    for section_a, section_b in combinations(candidate_bundle, 2):
        if bundles_conflict((section_a,), (section_b,)):
            return True
    return False


    

    
