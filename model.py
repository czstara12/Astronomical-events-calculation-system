from dataGateWay import OrbitalParameter
import ephem

class OrbitalParametersForm:
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

    def calculate_constellation(self, star_name, date_str):
        try:
            data_format = self.get_star_data_format(star_name)

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

