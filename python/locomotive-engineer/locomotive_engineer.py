"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagon_ids):
  """Return a list of wagons.

  :param: arbitrary number of wagons.
  :return: list - list of wagons.
  """
  return list(wagon_ids)



def fix_list_of_wagons(each_wagons_id, missing_wagons):
  """Fix the list of wagons.

  :param each_wagons_id: list - the list of wagons.
  :param missing_wagons: list - the list of missing wagons.
  :return: list - list of wagons.
  """
  new_wagons = each_wagons_id[:2]
  first_wagon, *remaining_wagons = each_wagons_id[2:]
  return [first_wagon, *missing_wagons, *remaining_wagons, *new_wagons]
  
  
def add_missing_stops(route, **stops):
  """Add missing stops to route dict.

  :param route: dict - the dict of routing information.
  :param: arbitrary number of stops.
  :return: dict - updated route dictionary.
  """
  sorted_stops = [
    stops[key]
    for key in sorted(stops.keys())
  ] if stops else []

  route["stops"] = sorted_stops
  
  return route



def extend_route_information(route, more_route_information):
  """Extend route information with more_route_information.

  :param route: dict - the route information.
  :param more_route_information: dict -  extra route information.
  :return: dict - extended route information.
  """
  return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
  """Fix the list of rows of wagons.

  :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
  :return: list[list[tuple]] - list of rows of wagons.
  """
  return [
    [row[j]
    for row in wagons_rows]
    for j in range(3)
  ]
