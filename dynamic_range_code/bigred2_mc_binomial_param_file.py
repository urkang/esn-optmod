import bigred2_mc_binomial_process
import numpy as np

experimental_parameters = {
    'q1_list': np.linspace(0.0, 0.5, 20),
    'q2_list': [0.3],
    'q1': 'mu',
    'q2': 'input_fraction',
    'success_rates': utilities.log_linspace(0.001, 0.9, 10),#np.linspace(0.01, 0.9, 10),
    'training_length': 6000,
    'validation_length': 6000,
    'cut': 500,
    'max_delay': 25,
    'shift': 1,
    'input_fraction': 0.3,
    'input_gain': 1.0,
    'input_weight_bounds': (-0.2, 1.0),
    'neuron_type': 'sigmoid',
    'neuron_pars': {'c':1, 'e':10},
    'output_neuron_type': 'heaviside',
    'output_neuron_pars': {'threshold': 0.5},
    'num_reservoir_samplings': 32,
    'N': 500,
    'mu': 0.25,
    'k': 6,
    'maxk': 6,
    'minc':10,
    'maxc':10,
    'deg_exp':1.0,
    'lower_reservoir_bound': -0.2,
    'upper_reservoir_bound': 1.0,
    'reservoir_weight_scale': 1.132,
    'spectral_factor': None,
    'temp_dir_ID': 0, 
    'full_path': '/N/u/njrodrig/BigRed2/topology_of_function/',#'/nobackup/njrodrig/topology_of_function/',
    'worker_file': 'bigred2_mc_binomial_worker.py',
    'num_threads': 512,
    'command_prefix': 'MC_bin_N500_c1_e10_ws1.132_gain1_rsig0.3_p-log_mu',
    'qsub_nodes': 4,
    'qsub_ppn': 32,
    'qsub_time': '00:45:00',
    'qsub_cpu_type': 'debug_cpu'
}

bigred2_mc_binomial_process.run_qsub(experimental_parameters)