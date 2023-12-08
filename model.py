from dataGateWay import AstronomicalObservation,AstronomicalEvent,CelestialObject
import tkinter as tk
from tkinter import ttk

class AstronomicalObservationForm:
    def __init__(self, root):
        None

    def add_observation(self, id=None, observation_date=None, location=None, celestial_body_name=None, celestial_body_type=None, observation_conditions=None, observer_name=None, notes=None):
        observation = AstronomicalObservation()
        if observation:
            # 使用设置方法来更改属性值，如果参数不为None，则更新对应属性
            if observation_date is not None:
                observation.set_observation_date(observation_date)
            if location is not None:
                observation.set_location(location)
            if celestial_body_name is not None:
                observation.set_celestial_body_name(celestial_body_name)
            if celestial_body_type is not None:
                observation.set_celestial_body_type(celestial_body_type)
            if observation_conditions is not None:
                observation.set_observation_conditions(observation_conditions)
            if observer_name is not None:
                observation.set_observer_name(observer_name)
            if notes is not None:
                observation.set_notes(notes)

            # 调用更新方法，将对象的更改反映到数据库记录
            observation.insert_into_database()
            print("Record updated successfully.")
        else:
            print("Observation not found.")


    def remove_observation_by_id(self, id):
        observation = AstronomicalObservation.get_observation_by_id(id)
        if observation:
            print("Observation to Delete:")
            print("ID:", observation.id)
            print("Observer Name:", observation.observer_name)

            # 调用删除方法，从数据库中删除记录
            observation.delete_from_database()
            print("Observation Deleted.")
        else:
            print("Observation not found.")

    def get_all_observations(self):
        observations = []  # 用于存储所有观测记录的列表

        # 获取第一个观测记录的ID
        first_observation_id = AstronomicalObservation.get_first_observation_id()

        # 遍历并获取所有记录
        current_observation_id = first_observation_id
        while current_observation_id:
            observation = self.get_observation_details_by_id(current_observation_id)
            if observation:
                observations.append(observation)  # 将观测记录添加到列表中

            # 获取下一个观测记录的ID
            current_observation_id = AstronomicalObservation.get_next_observation_id(current_observation_id)

        return observations  # 返回观测记录列表

    def get_observation_details_by_id(self, id):
        observation = AstronomicalObservation.get_observation_by_id(id)
        if observation:
            return {
                "ID": observation.get_id(),
                "Observation Date": observation.get_observation_date(),
                "Location": observation.get_location(),
                "Celestial Body Name": observation.get_celestial_body_name(),
                "Celestial Body Type": observation.get_celestial_body_type(),
                "Observation Conditions": observation.get_observation_conditions(),
                "Observer Name": observation.get_observer_name(),
                "Notes": observation.get_notes()
            }
        else:
            return None
        
    def show_all_observations(self):
        observations = self.get_all_observations()  # 使用新方法获取所有观测记录

        if not observations:
            print("No observations found.")
            return

        for observation in observations:
            self.show_observation_by_id(observation.id)

    def show_observation_by_id(self, id):
        details = self.get_observation_details_by_id(id)  # 使用新方法获取观测记录的详细信息

        if not details:
            print("Observation not found.")
            return

        print("Observation ID:", id)
        for key, value in details.items():
            print(f"{key}: {value}")
    
    def update_database_record(self, id=None, observation_date=None, location=None, celestial_body_name=None, celestial_body_type=None, observation_conditions=None, observer_name=None, notes=None):
        observation = AstronomicalObservation.get_observation_by_id(id)  # 使用对象的ID来获取观测记录
        if observation:
            # 使用设置方法来更改属性值，如果参数不为None，则更新对应属性
            if observation_date is not None:
                observation.set_observation_date(observation_date)
            if location is not None:
                observation.set_location(location)
            if celestial_body_name is not None:
                observation.set_celestial_body_name(celestial_body_name)
            if celestial_body_type is not None:
                observation.set_celestial_body_type(celestial_body_type)
            if observation_conditions is not None:
                observation.set_observation_conditions(observation_conditions)
            if observer_name is not None:
                observation.set_observer_name(observer_name)
            if notes is not None:
                observation.set_notes(notes)

            # 调用更新方法，将对象的更改反映到数据库记录
            observation.update_database_record()
            print("Record updated successfully.")
        else:
            print("Observation not found.")

class AstronomicalEventForm:
    def __init__(self):
        None

    def add_event(self, event_id=None, event_date=None, event_name=None, event_type=None, event_description=None, location=None, organizer=None, notes=None):
        event = AstronomicalEvent()
        if event:
            # 使用设置方法来更改属性值，如果参数不为None，则更新对应属性
            if event_date is not None:
                event.set_event_date(event_date)
            if event_name is not None:
                event.set_event_name(event_name)
            if event_type is not None:
                event.set_event_type(event_type)
            if event_description is not None:
                event.set_event_description(event_description)
            if location is not None:
                event.set_location(location)
            if organizer is not None:
                event.set_organizer(organizer)
            if notes is not None:
                event.set_notes(notes)

            # 调用插入方法，将对象的数据插入到数据库记录中
            event.insert_into_database()
            print("Record added successfully.")
        else:
            print("Event not found.")

    def remove_event_by_id(self, event_id):
        event = AstronomicalEvent.get_event_by_id(event_id)
        if event:
            print("Event to Delete:")
            print("ID:", event.event_id)
            print("Event Name:", event.event_name)

            # 调用删除方法，从数据库中删除记录
            event.delete_from_database()
            print("Event Deleted.")
        else:
            print("Event not found.")


    def get_all_events(self):
        events = []  # 用于存储所有事件的列表

        # 获取第一个事件的ID
        first_event_id = AstronomicalEvent.get_first_event_id()

        # 遍历并获取所有事件
        current_event_id = first_event_id
        while current_event_id:
            event_details = self.get_event_details_by_id(current_event_id)
            if event_details:
                events.append(event_details)  # 将事件详细信息添加到列表中

            # 获取下一个事件的ID
            current_event_id = AstronomicalEvent.get_next_event_id(current_event_id)

        return events  # 返回事件详细信息列表

    def get_event_details_by_id(self, event_id):
        event = AstronomicalEvent.get_event_by_id(event_id)
        if event:
            return {
                "Event ID": event.get_id(),
                "Event Date": event.get_event_date(),
                "Event Name": event.get_event_name(),
                "Event Type": event.get_event_type(),
                "Event Description": event.get_event_description(),
                "Location": event.get_location(),
                "Organizer": event.get_organizer(),
                "Notes": event.get_notes()
            }
        else:
            return None

    def show_all_events(self):
        events = self.get_all_events()  # 使用新方法获取所有事件

        if not events:
            print("No events found.")
            return

        for event in events:
            self.show_event_by_id(event.event_id)

    def show_event_by_id(self, event_id):
        details = self.get_event_details_by_id(event_id)  # 使用新方法获取事件的详细信息

        if not details:
            print("Event not found.")
            return

        print("Event ID:", event_id)
        for key, value in details.items():
            print(f"{key}: {value}")

    def update_database_record(self, event_id=None, event_date=None, event_name=None, event_type=None, event_description=None, location=None, organizer=None, notes=None):
        event = AstronomicalEvent.get_event_by_id(event_id)  # 使用对象的ID来获取事件
        if event:
            # 使用设置方法来更改属性值，如果参数不为None，则更新对应属性
            if event_date is not None:
                event.set_event_date(event_date)
            if event_name is not None:
                event.set_event_name(event_name)
            if event_type is not None:
                event.set_event_type(event_type)
            if event_description is not None:
                event.set_event_description(event_description)
            if location is not None:
                event.set_location(location)
            if organizer is not None:
                event.set_organizer(organizer)
            if notes is not None:
                event.set_notes(notes)

            # 调用更新方法，将对象的更改反映到数据库记录
            event.update_database_record()
            print("Record updated successfully.")
        else:
            print("Event not found.")

class CelestialObjectForm:
    def add_object(self, object_id=None, object_name=None, object_type=None, object_mass=None, object_radius=None, object_distance=None, object_description=None, notes=None):
        celestial_obj = CelestialObject()

        if celestial_obj:
            if object_name is not None:
                celestial_obj.set_object_name(object_name)
            if object_type is not None:
                celestial_obj.set_object_type(object_type)
            if object_mass is not None:
                celestial_obj.set_object_mass(object_mass)
            if object_radius is not None:
                celestial_obj.set_object_radius(object_radius)
            if object_distance is not None:
                celestial_obj.set_object_distance(object_distance)
            if object_description is not None:
                celestial_obj.set_object_description(object_description)
            if notes is not None:
                celestial_obj.set_notes(notes)

            celestial_obj.insert_into_database()
            print("Record added successfully.")
        else:
            print("Celestial object not found.")

    def remove_object_by_id(self, object_id):
        celestial_obj = CelestialObject.get_object_by_id(object_id)
        if celestial_obj:
            print("Celestial Object to Delete:")
            print("ID:", celestial_obj.object_id)
            print("Object Name:", celestial_obj.object_name)

            celestial_obj.delete_from_database()
            print("Celestial Object Deleted.")
        else:
            print("Celestial Object not found.")

    def show_all_objects(self):
        objects = self.get_all_objects()  # 使用新方法获取所有天体对象记录

        if not objects:
            print("No celestial objects found.")
            return

        for obj in objects:
            self.show_object_by_id(obj.object_id)

    def show_object_by_id(self, object_id):
        details = self.get_object_details_by_id(object_id)  # 使用新方法获取天体对象的详细信息

        if not details:
            print("Celestial Object not found.")
            return

        print("Object ID:", object_id)
        for key, value in details.items():
            print(f"{key}: {value}")

    def get_all_objects(self):
        objects = []  # 用于存储所有天体对象记录的列表

        # 获取第一个天体对象记录的ID
        first_object_id = CelestialObject.get_first_object_id()

        # 遍历并获取所有记录
        current_object_id = first_object_id
        while current_object_id:
            obj = CelestialObject.get_object_by_id(current_object_id)
            if obj:
                objects.append(obj)  # 将天体对象记录添加到列表中

            # 获取下一个天体对象记录的ID
            current_object_id = CelestialObject.get_next_object_id(current_object_id)

        return objects  # 返回天体对象记录列表

    def get_object_details_by_id(self, object_id):
        celestial_obj = CelestialObject.get_object_by_id(object_id)
        if celestial_obj:
            return {
                "Object ID": celestial_obj.get_id(),
                "Object Name": celestial_obj.get_object_name(),
                "Object Type": celestial_obj.get_object_type(),
                "Object Mass": celestial_obj.get_object_mass(),
                "Object Radius": celestial_obj.get_object_radius(),
                "Object Distance": celestial_obj.get_object_distance(),
                "Object Description": celestial_obj.get_object_description(),
                "Notes": celestial_obj.get_notes()
            }
        else:
            return None
        
    def update_database_record(self, object_id=None, object_name=None, object_type=None, object_mass=None, object_radius=None, object_distance=None, object_description=None, notes=None):
        celestial_obj = CelestialObject.get_object_by_id(object_id)
        if celestial_obj:
            if object_name is not None:
                celestial_obj.set_object_name(object_name)
            if object_type is not None:
                celestial_obj.set_object_type(object_type)
            if object_mass is not None:
                celestial_obj.set_object_mass(object_mass)
            if object_radius is not None:
                celestial_obj.set_object_radius(object_radius)
            if object_distance is not None:
                celestial_obj.set_object_distance(object_distance)
            if object_description is not None:
                celestial_obj.set_object_description(object_description)
            if notes is not None:
                celestial_obj.set_notes(notes)

            celestial_obj.update_database_record()
            print("Record updated successfully.")
        else:
            print("Celestial Object not found.")
    
    def calculate(self):
        None

