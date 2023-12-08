# Import necessary modules
from dataGateWay import AstronomicalObservation, AstronomicalEvent, CelestialObject

# Define a function to create test data
def create_test_data():
    # Create new astronomical observation records
    observation1 = AstronomicalObservation(id=None, observation_date='2023-12-08', location='Space Observation Station',
                                           celestial_body_name='Sun', celestial_body_type='Star',
                                           observation_conditions='Clear', observer_name='Zhang San', notes='Observation')
    
    observation2 = AstronomicalObservation(id=None, observation_date='2023-12-09', location='Ground Observation Point',
                                           celestial_body_name='Moon', celestial_body_type='Satellite',
                                           observation_conditions='Cloudy', observer_name='Li Si', notes='Lunar Phase Observation')
    
    observation3 = AstronomicalObservation(id=None, observation_date='2023-12-10', location='Space Telescope',
                                           celestial_body_name='Mars', celestial_body_type='Planet',
                                           observation_conditions='Clear', observer_name='Wang Wu', notes='Mars Orbit Observation')

    observation4 = AstronomicalObservation(id=None, observation_date='2023-12-05', location='Space Observation Station',
                                           celestial_body_name='Sun', celestial_body_type='Star',
                                           observation_conditions='Clear', observer_name='Zhang San', notes='First Observation')

    # Insert observation records into the database
    observation1.insert_into_database()
    observation2.insert_into_database()
    observation3.insert_into_database()
    observation4.insert_into_database()

    # Create instances of AstronomicalEvent class and set their properties
    event1 = AstronomicalEvent(event_id=None, event_date='2023-12-15', event_name='Lunar Eclipse', event_type='Astronomical Phenomenon', event_description='Observe the Lunar Eclipse', location='Some Place', organizer='Some Organization', notes='Note 1')
    event2 = AstronomicalEvent(event_id=None, event_date='2023-11-20', event_name='Solar Eclipse', event_type='Astronomical Phenomenon', event_description='Observe the Solar Eclipse', location='Another Place', organizer='Another Organization', notes='Note 2')
    event3 = AstronomicalEvent(event_id=None, event_date='2023-10-10', event_name='Meteor Shower', event_type='Astronomical Phenomenon', event_description='Observe the Meteor Shower', location='Some Place', organizer='Some Organization', notes='Note 3')
    event4 = AstronomicalEvent(event_id=None, event_date='2023-12-31', event_name='Meteor Shower', event_type='Astronomical Event', event_description='Meteor Shower', location='Night Sky', organizer='Astronomy Club', notes='Public Event')

    # Insert these events into the database
    event1.insert_into_database()
    event2.insert_into_database()
    event3.insert_into_database()
    event4.insert_into_database()

    # Create a CelestialObject object and insert data
    object1 = CelestialObject(
        object_id=None,  # Set to None if object_id is auto-assigned
        object_name='Sun',
        object_type='Star',
        object_mass=1.989e30,
        object_radius=6.9634e8,
        object_distance=0,
        object_description='Our Sun is a G-type main-sequence star.',
        notes='It is the star at the center of our Solar System.'
    )

    # Insert the object into the database
    object1.insert_into_database()

    # Create another CelestialObject object and insert data
    object2 = CelestialObject(
        object_id=None,
        object_name='Earth',
        object_type='Planet',
        object_mass=5.972e24,
        object_radius=6.371e6,
        object_distance=149.6e9,
        object_description='Earth is the third planet in the Solar System.',
        notes='It is our home planet.'
    )

    # Insert the object into the database
    object2.insert_into_database()

    # Create another CelestialObject object and insert data
    object3 = CelestialObject(
        object_id=None,
        object_name='Moon',
        object_type='Satellite',
        object_mass=7.342e22,
        object_radius=1.737e6,
        object_distance=384.4e6,
        object_description='The Moon is one of Earth’s satellites.',
        notes='It has a significant impact on Earth’s tides.'
    )

    # Insert the object into the database
    object3.insert_into_database()

    # Create another CelestialObject object and insert data
    object4 = CelestialObject(
        object_id=None,
        object_name='Jupiter',
        object_type='Planet',
        object_mass=1.898e27,
        object_radius=6.991e7,
        object_distance=778.3e9,
        object_description='Jupiter is a giant gas planet in the Solar System.',
        notes='It has a large number of satellites, the largest being the Galilean moons.'
    )

    # Insert the object into the database
    object4.insert_into_database()

# Call the function to create test data
create_test_data()
