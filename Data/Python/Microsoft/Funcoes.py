# a funçao é dada pelo nome def
def rocket_parts():
    print("payload, propellant, structure")

# para chamar funçao
rocket_parts()

def rocket_parts():
    return "payload, propellant, structure"
output = rocket_parts()
output

# any é uma funçao que precisa de atributos
any([True, False, False])


#parametros

    def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

    days_to_complete(238855, 75)



def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
    
    
    distance_from_earth("Moon")


def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank} 
    """
    print(output)

    #palavra chave
    from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")
    arrival_time()
    arrival_time(hours=0)



