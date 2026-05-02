# Jordyn Rylander
# Module 7.2 Assignment
# This program defines a function that returns a formatted city and country string.

def city_country(city, country, population=None, language=None):
    if population and language:
       return f"{city.title()}, {country.title()} - population {population}, {language}"
    elif population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
        
            

print(city_country("santiago", "chile"))
print(city_country("paris", "france", population=2148000))
print(city_country("tokyo", "japan", population=13920000, language="Japanese"))