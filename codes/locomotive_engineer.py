"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    *return_list, = args
    return return_list


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    fixed_list = [each_wagons_id[2], *missing_wagons, *each_wagons_id[3:], each_wagons_id[0], each_wagons_id[1]]
    return fixed_list


def add_missing_stops(*args, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stop_values = []
    for index, value in kwargs.items():
        if index.startswith("stop_"):
            stop_values.append(value)

    list_to_be_returned = dict(*args)
    list_to_be_returned["stops"] = stop_values
    return list_to_be_returned


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return dict(**route, **more_route_information)


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    [*first_list], [*second_list] , [*third_list] = zip(*wagons_rows)
    return [first_list, second_list, third_list]