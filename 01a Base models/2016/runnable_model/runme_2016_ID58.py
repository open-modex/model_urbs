import os
import shutil
import urbs


input_files = '2016_ID_58.xlsx'  # for single year file name, for intertemporal folder name
input_dir = 'Input'
input_path = os.path.join(input_dir, input_files)

result_name = 'Run'
result_dir = urbs.prepare_result_directory(result_name)  # name + time stamp

# copy input file to result directory
try:
    shutil.copytree(input_path, os.path.join(result_dir, input_dir))
except NotADirectoryError:
    shutil.copyfile(input_path, os.path.join(result_dir, input_files))
# copy run file to result directory
shutil.copy(__file__, result_dir)

# objective function
objective = 'cost'  # set either 'cost' or 'CO2' as objective

# Choose Solver (cplex, glpk, gurobi, ...)
solver = 'gurobi'

# simulation timesteps
(offset, length) = (0, 8784) # time step selection
timesteps = range(offset, offset+length+1)
dt = 1  # length of each time step (unit: hours)

# detailed reporting commodity/sites
report_tuples = [
    (2016, 'BB', 'electricity'),
    (2016, 'BE', 'electricity'),
    (2016, 'BW', 'electricity'),
    (2016, 'BY', 'electricity'),
    (2016, 'HB', 'electricity'),
    (2016, 'HE', 'electricity'),
    (2016, 'HH', 'electricity'),
    (2016, 'MV', 'electricity'),
    (2016, 'NI', 'electricity'),
    (2016, 'NW', 'electricity'),
    (2016, 'RP', 'electricity'),
    (2016, 'SH', 'electricity'),
    (2016, 'SL', 'electricity'),
    (2016, 'SN', 'electricity'),
    (2016, 'ST', 'electricity'),
    (2016, 'TH', 'electricity'),
    (2016, 'Baltic', 'electricity'),
    (2016, 'North', 'electricity')  
    #(2016, ['BB', 'BE', 'BW', 'BY','HB','HE','HH','MV','NI','NW','RP','SH','SL','SN','ST','TH', 'Baltic','North'], 'Elec')
    ]

# optional: define names for sites in report_tuples
report_sites_name = {}

# plotting commodities/sites
plot_tuples = []

# optional: define names for sites in plot_tuples
plot_sites_name = {}

# plotting timesteps
plot_periods = {
    'all': timesteps[1:]
}

# add or change plot colors
my_colors = {}
for country, color in my_colors.items():
    urbs.COLORS[country] = color

# select scenarios to be run
scenarios = [
             urbs.scenario_base
            ]

for scenario in scenarios:
    prob = urbs.run_scenario(input_path, solver, timesteps, scenario,
                             result_dir, dt, objective,
                             plot_tuples=plot_tuples,
                             plot_sites_name=plot_sites_name,
                             plot_periods=plot_periods,
                             report_tuples=report_tuples,
                             report_sites_name=report_sites_name)
