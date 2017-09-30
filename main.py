import json
import web
from response_handler import ResponseHandler
from error_handler import ErrorHandler
from thermostat_model import ThermostatModel


# Setting up the routes and handlers
routes = (
    '/v1/thermostats/(\d+)/?', 'Thermostat',
    '/v1/thermostats/?', 'Thermostats'
)
err_handler = ErrorHandler()
res_handler = ResponseHandler()
therm_list, therm_list_json = [], []


# Decorator to handle keeping track of
# how many times load_data is run
def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper


# Retrieve hard-coded thermostat data
# for this exercise from included json file
def load_data():
    with open('data.json') as data:
        therms = json.load(data)
    for data in therms:
        therm_obj = ThermostatModel()
        therm_obj.set_data(data)
        therm_list.append(therm_obj)
        therm_list_json.append(therm_obj.to_json())


loaded = run_once(load_data)
loaded()


class Thermostats:
    def __init__(self):
        pass

    def GET(self):
        try:
            # clear the current thermometers json list
            therm_list_json = []
            for therm in therm_list:
                therm_list_json.append(therm.to_json())
            return res_handler.get_with_results(therm_list_json)
        except Exception as err:
            return err_handler.handle_server_error(err.message)

    def POST(self):
        try:
            new_therm_obj = ThermostatModel()
            new_therm_obj.set_data(json.loads(web.webapi.data()))
            therm_list.append(new_therm_obj)
            therm_list_json.append(new_therm_obj.to_json())
            return res_handler.created_with_results(new_therm_obj.to_json())
        except Exception as err:
            return err_handler.handle_server_error(err.message)


class Thermostat:
    def __init__(self):
        pass

    def find_by_id(self, id):
        found = False
        for therm in therm_list:
            if therm.get_ID == int(id):
                found = therm
                break
        return found

    def GET(self, id):
        try:
            therm = self.find_by_id(id)
            if not therm:
                return err_handler.handle_not_found_error('Thermostat not found with the provided ID')
            return res_handler.get_with_results(therm.to_json())
        except ValueError as err:
            return err_handler.handle_input_error(err.message)
        except Exception as err:
            return err_handler.handle_server_error(err.message)

    def PUT(self, id):
        try:
            therm = self.find_by_id(id)
            if not therm:
                return err_handler.handle_not_found_error('Thermostat not found with the provided ID')
            therm.set_data(json.loads(web.webapi.data()))
            return res_handler.updated_with_results(therm.to_json())
        except ValueError as err:
            return err_handler.handle_input_error(err.message)
        except Exception as err:
            return err_handler.handle_server_error(err.message)

    def DELETE(self, id):
        try:
            therm = self.find_by_id(id)
            if not therm:
                return err_handler.handle_not_found_error('Thermostat not found with the provided ID')
            idx1 = therm_list.index(therm)
            del therm_list[idx1], therm
            return res_handler.deleted_with_results(id)
        except ValueError as err:
            return err_handler.handle_input_error(err.message)
        except Exception as err:
            return err_handler.handle_server_error(err.message)


if __name__ == "__main__":
    app = web.application(routes, globals())
    app.run()
