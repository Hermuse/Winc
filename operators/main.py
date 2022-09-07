# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
# 1 The language spoken the most in Switzerland is the same as in Spain
spain_language = "spanish" 
switzerland_language = "german"
print(spain_language == switzerland_language)
# 2 The most prevalent religion in Switzerland is the same as in Spain
spain_religion = "roman_catholic"
switzerland_religion = "roman_catholic"
print(spain_religion == switzerland_religion)
# 3 The name length of Spain's capital does not equal that of Switzerland
spain_name_length_capital = len("madrid")
switzerland_name_length_capital = len("bern")
print(spain_name_length_capital != switzerland_name_length_capital)
# 4 Switzerland's GDP is greater than Spain's GDP
spain_gdp = 1714860000000
switzerland_gdp= 590710000000 
print(spain_gdp<switzerland_gdp)
# 5 The population growth is less than 1% in Switzerland and Spain
spain_population_growth = -0.03#procent
switzerland_population_growth = 0.65#procent
print(spain_population_growth < switzerland_population_growth)
# 6 At least one of the two countries has a population count of over 10 million
spain_population_count = 47163418
switzerland_population_count= 8508698
population_count_over = 10000000
print(spain_population_count > population_count_over or switzerland_population_count > population_count_over)
# 7 Exactly one of the two countries has a population count of over 10 million
if ((spain_population_count>population_count_over) and (switzerland_population_count<population_count_over)) or ((spain_population_count<population_count_over) and (switzerland_population_count>population_count_over)) :
    Exactly_one_of_the_two_countries_has_a_population_count_of_over_10_million = True
else: Exactly_one_of_the_two_countries_has_a_population_count_of_over_10_million = False
print(Exactly_one_of_the_two_countries_has_a_population_count_of_over_10_million)
