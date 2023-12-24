from dataGateWay import OrbitalParameter
import ephem

class OrbitalDataManager:
    def add_parameter(self, id=None, name=None, data_format=None, line_1=None, line_2=None, line_3=None, description=None):
        parameter = OrbitalParameter()

        if name is not None:
            parameter.set_name(name)
        if data_format is not None:
            parameter.set_data_format(data_format)
        if line_1 is not None:
            parameter.set_line_1(line_1)
        if line_2 is not None:
            parameter.set_line_2(line_2)
        if line_3 is not None:
            parameter.set_line_3(line_3)
        if description is not None:
            parameter.set_description(description)

        parameter.insert_into_database()
        print("Record added successfully.")

    def remove_parameter_by_id(self, id):
        parameter = OrbitalParameter.get_parameter_by_id(id)
        if parameter:
            print("Orbital Parameter to Delete:")
            print("ID:", parameter.get_id())
            print("Name:", parameter.get_name())

            parameter.delete_from_database()
            print("Orbital Parameter Deleted.")
        else:
            print("Orbital Parameter not found.")

    def show_all_parameters(self):
        parameters = OrbitalParameter.get_all_parameters()

        if not parameters:
            print("No orbital parameters found.")
            return

        for param in parameters:
            self.show_parameter_by_id(param.get_id())

    def show_parameter_by_id(self, id):
        details = self.get_parameter_details_by_id(id)

        if not details:
            print("Orbital Parameter not found.")
            return

        print("Parameter ID:", id)
        for key, value in details.items():
            print(f"{key}: {value}")

    def get_parameter_details_by_id(self, id):
        parameter = OrbitalParameter.get_parameter_by_id(id)
        if parameter:
            return {
                "ID": parameter.get_id(),
                "Name": parameter.get_name(),
                "Data Format": parameter.get_data_format(),
                "First Line": parameter.get_line_1(),
                "Second Line": parameter.get_line_2(),
                "Third Line": parameter.get_line_3(),
                "Description": parameter.get_description()
            }
        else:
            return None

    def update_parameter_record(self, id=None, name=None, data_format=None, line_1=None, line_2=None, line_3=None, description=None):
        parameter = OrbitalParameter.get_parameter_by_id(id)
        if parameter:
            if name is not None:
                parameter.set_name(name)
            if data_format is not None:
                parameter.set_data_format(data_format)
            if line_1 is not None:
                parameter.set_line_1(line_1)
            if line_2 is not None:
                parameter.set_line_2(line_2)
            if line_3 is not None:
                parameter.set_line_3(line_3)
            if description is not None:
                parameter.set_description(description)

            parameter.update_database_record()
            print("Record updated successfully.")
        else:
            print("Orbital Parameter not found.")

    def get_parameter_by_name(self, name):
        return OrbitalParameter.get_parameter_by_name(name)
    
    def get_all_parameters(self):
        # 调用 OrbitalParameter 类的静态方法来获取所有轨道参数
        return OrbitalParameter.get_all_parameters()

    def get_star_data_format(self, star_name):
        parameter = self.get_parameter_by_name(star_name)
        if parameter:
            return parameter.get_data_format()
        else:
            return None

class AstronomyCalculator:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def calculate_constellation(self, star_name, date_str):
        try:
            data_format = self.data_manager.get_star_data_format(star_name)

            if data_format == "build_in":
                date = ephem.Date(date_str)
                star_code = f'''
star = ephem.{star_name.capitalize()}()
star.compute("{date}")
constellation = ephem.constellation(star)
'''
                namespace = {}
                exec(star_code, globals(), namespace)

                return namespace['constellation']
            else:
                return "Unsupported data format or star name."
        except Exception as e:
            return f"Error: {str(e)}"
        
    def calculate_position(self, star_name, date_str):
        try:
            # 将日期字符串转换为 ephem 可接受的格式
            date = ephem.Date(date_str)

            # 根据星体名称创建对应的 ephem 对象
            if star_name.lower() == "saturn":
                star = ephem.Saturn(date)
            elif star_name.lower() == "moon":
                star = ephem.Moon(date)
            elif star_name.lower() == "venus":
                star = ephem.Venus(date)
            elif star_name.lower() == "jupiter":
                star = ephem.Jupiter(date)
            else:
                return "Unknown star name"

            # 计算星体的位置
            star.compute(date)
            ecl = ephem.Ecliptic(star)
            return f"{ephem.constellation(star)}, Ecliptic Lon: {ecl.lon}, Ecliptic Lat: {ecl.lat}"
        except Exception as e:
            return f"Error: {str(e)}"

    def calculate_detailed_position(self, star_name, date_str):
        try:
            star_code = f'''
star = ephem.{star_name.capitalize()}("{date_str}")
star.compute()
details = {{
    "ra": str(star.ra),
    "dec": str(star.dec),
    "ecl_lon": str(ephem.Ecliptic(star).lon),
    "ecl_lat": str(ephem.Ecliptic(star).lat),
    "gal_lon": str(ephem.Galactic(star).lon),
    "gal_lat": str(ephem.Galactic(star).lat),
    "a_ra": str(star.a_ra),
    "a_dec": str(star.a_dec),
    "g_ra": str(star.g_ra),
    "g_dec": str(star.g_dec),
    "elong": str(star.elong),
    "mag": str(star.mag),
    "size": str(star.size),
    "radius": str(star.radius),
    "sun_distance": str(star.sun_distance),
    "earth_distance": str(star.earth_distance),
    "phase": str(star.phase)
}}
'''
            namespace = {}
            exec(star_code, globals(), namespace)

            return namespace['details']
        except Exception as e:
            return f"Error: {str(e)}"
        
    def calculate_next_seasonal_points(self, date_str):
        try:
            results = {
                "next_vernal_equinox": ephem.next_vernal_equinox(date_str),
                "next_summer_solstice": ephem.next_summer_solstice(date_str),
                "next_autumnal_equinox": ephem.next_autumnal_equinox(date_str),
                "next_winter_solstice": ephem.next_winter_solstice(date_str)
            }
            return {k: v.datetime().strftime("%Y-%m-%d %H:%M:%S UTC") for k, v in results.items()}
        except Exception as e:
            return f"Error: {str(e)}"
        
        
    def calculate_moon_details(self, date_str):
        try:
            results = {
                "next_full_moon": ephem.next_full_moon(date_str),
                "previous_full_moon": ephem.previous_full_moon(date_str),
                "next_new_moon": ephem.next_new_moon(date_str),
                "previous_new_moon": ephem.previous_new_moon(date_str),
                "next_first_quarter_moon": ephem.next_first_quarter_moon(date_str),
                "previous_first_quarter_moon": ephem.previous_first_quarter_moon(date_str),
                "next_last_quarter_moon": ephem.next_last_quarter_moon(date_str),
                "previous_last_quarter_moon": ephem.previous_last_quarter_moon(date_str)
            }
            moon = ephem.Moon(date_str)
            moon.compute()
            moon_details = {
                "libration_long": moon.libration_long,
                "libration_lat": moon.libration_lat,
                "colong": moon.colong,
                "moon_phase": moon.moon_phase,
                "subsolar_lat": moon.subsolar_lat
            }
            return {k: v.datetime().strftime("%Y-%m-%d %H:%M:%S UTC") if hasattr(v, 'datetime') else str(v) for k, v in {**results, **moon_details}.items()}
        except Exception as e:
            return f"Error: {str(e)}"
        