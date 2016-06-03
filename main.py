import pygal
from pygal.style import CleanStyle
from pygal.style import DarkenStyle
from datetime import datetime, timedelta

# Growth Rate of different sectors in %
agriculture = pygal.Line(interpolate='cubic', fill=True, style=CleanStyle)
agriculture.title = 'Growth Rates\nGraph by Daily Pakistan'
agriculture.y_title = 'in %'
agriculture.x_title = 'Year'
agriculture.x_labels = map(str, ('2013-2014', '2014-2015', '2015-2016'))
agriculture.add("Services", [4.4, 5, 5.71])
agriculture.add("Inflation", [8.62, 4.53, 3.8])
agriculture.add("Industry", [4.5, 3.6, 6.8])
agriculture.add("Agriculture", [2.7, 2.9, -0.19])
agriculture.render_to_file('Growth Rate of different sectors.svg')

# Real GDP Growth Rate
gdp_growthrate = pygal.Line(style=CleanStyle, font_family='googlefont:Raleway')
gdp_growthrate.title = 'Real GDP Growth Rate\nGraph by Daily Pakistan'
gdp_growthrate.y_title = 'Rate'
gdp_growthrate.x_title = 'Year'
# gdp_growthrate.show_legend = False
gdp_growthrate.value_formatter = lambda y: "{:,}%".format(y)
gdp_growthrate.x_labels = map(str, ('2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017(P)'))
gdp_growthrate.add("Pakistan", [0.4, 2.6, 3.6, 3.8, 3.7, 4.05, 4.04, 4.71, 5.7])
gdp_growthrate.add("India", [8.5, 10.3, 6.6, 5.6, 6.6, 7.2, 7.3, 7.5, 7.5])
gdp_growthrate.add("China", [9.2, 10.6, 9.5, 7.7, 7.7, 7.3, 6.9, 6.5, 6.2])
gdp_growthrate.add("Bangladesh", [5.3, 6.0, 6.5, 6.3, 6.0, 6.3, 6.4, 6.6, 6.9])
gdp_growthrate.add("Saudi Arabia", [-2.1, 4.8, 10.0, 5.4, 2.7, 3.6, 3.4, 1.2, 1.9])
gdp_growthrate.add("Iran", [2.3, 6.6, 3.7, -6.6, -1.9, 4.3, 0.0, 4.0, 3.7])
gdp_growthrate.add("World", [-0.1, 5.4, 4.2, 3.5, 3.3, 3.4, 3.1, 3.2, 3.5])

gdp_growthrate.render_to_file('Real GDP Growth Rate.svg')

# Debt
debt = pygal.Dot(style=CleanStyle)
debt.title = 'Debt\nGraph by Daily Pakistan'
debt.x_title = 'Year'
debt.y_title = 'Rs in billion'
debt.value_formatter = lambda y: "{:,}".format(y)
debt.x_labels = map(str, ('2010', '2011', '2012', '2013', '2014', '2015', '2016*'))
debt.add("Total", [9006.2, 10766.9, 12695.3, 14318.4, 15991.5, 17380.7, 19167.9])
debt.add("Domestic Debt", [4654.3, 6016.7, 7638.1, 9521.9, 10920.0, 12198.9, 13398.5])
debt.add("External Debt", [4351.9, 4750.2, 5057.2, 4796.5, 5071.5, 5181.8, 5769.4])
debt.render_to_file('debt.svg')

# Current Expenditure other than GPS
radar_chart = pygal.StackedBar(fill=True, style=CleanStyle)
radar_chart.title = 'Current Expenditure other than GPS\nGraph by Daily Pakistan'
radar_chart.x_labels = ['2014-2015', '2015-2016', '2016-2017']
radar_chart.legend_at_bottom = True
radar_chart.y_title = 'Rs in million'
radar_chart.value_formatter = lambda y: "{:,}".format(y)
# radar_chart.add('General Public Service', [2446604, 2446604, 2446604])
radar_chart.add('Defence', [720002, 781162, 781162])
radar_chart.add('Health', [10124, 11010, 11010])
radar_chart.add('Public Order and Safety', [87598, 94899, 94899])
radar_chart.add('Education', [64519, 75680, 75680])
radar_chart.add('Economic Affairs', [55264, 60195, 60195])
radar_chart.add('Recreation', [7242, 7637, 7637])
radar_chart.add('Social Protection', [2709, 1840, 1840])
radar_chart.add('Housing', [2012, 2256, 2256])
radar_chart.add('Envionment', [936, 1055, 1055])
radar_chart.render_to_file('Current Expenditure other than GPS.svg')


# Current Expenditure
defence = pygal.Treemap(fill=True, style=CleanStyle)
defence.title = 'Current Expenditure\nGraph by Daily Pakistan'
defence.legend_at_bottom = True
defence.y_title = 'Rs in million'
defence.value_formatter = lambda y: "{:,}".format(y)
defence.add('General Public Service', [2446604])
defence.add('Defence', [781162])
defence.add('Health', [11010])
defence.add('Public Order and Safety', [94899])
defence.add('Education', [75680])
defence.add('Economic Affairs', [60195])
defence.add('Recreation', [7637])
defence.add('Social Protection', [1840])
defence.add('Housing', [2256])
defence.add('Envionment', [1055])
defence.render_to_file('Current Expenditure.svg')

# Current expenditure GPS breakdown
pie_chart = pygal.Pie(half_pie=True, inner_radius=.6, style=CleanStyle)
pie_chart.legend_at_bottom = True
pie_chart.truncate_legend = 0
pie_chart.value_formatter = lambda y: "Rs.{:,} million".format(y)
pie_chart.title = 'General Public Service spending 2016 - 2017\nGraph by Daily Pakistan'
pie_chart.add('Servicing of Domestic Debt', 1168676)
pie_chart.add('Servicing of Foreign Debt', 111219)
pie_chart.add('Foreign Loans Repayment', 316373)
pie_chart.add('Transfers', 409875)
pie_chart.add('Allowances & Pensions', 231000)
pie_chart.add('Foreign Economic Aid', 100)
pie_chart.add('General Services', 6415)
pie_chart.add('Basic Research', 3559)
pie_chart.add('Research and Development General Public Services', 10683)
pie_chart.add('Administration of General Public Services', 2150)
pie_chart.add('General Public Services not elsewhere defined ', 9920)
pie_chart.add('Others', 176635)
pie_chart.render_to_file('General Public Service spending.svg')