from workbook_loader import wb

from core.bounds.services.coordinates import BoundsService
from core.groups.services.groups import GroupsService

sheet_name = '2 курс'
sheet = wb[sheet_name]

if __name__ == "__main__":
    bounds_coords = BoundsService(sheet=sheet, sheet_name=sheet_name).find_sheet_bounds()
    groups_coords = GroupsService(sheet=sheet).get_groups_from_sheet(bounds_coordinates=bounds_coords)
    print(groups_coords)
