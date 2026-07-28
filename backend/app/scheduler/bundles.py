from app.models.course import Course
from app.models.section import Section
from collections import defaultdict
from itertools import product

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
        result.extend(product(*arr_cartesian))

    return result


    

    
