from logger import Logger


def test_logger():
    return Logger("{}_simulation_pop_{}_vp_{}_infected_{}.txt")


def test_write_metadata(self, pop_size, vacc_percentage, virus_name,
                        mortality_rate, basic_repro_num):
    pass


def test_log_interaction(self, sick_person, random_person, did_infect=None):
    pass


def test_log_infection_survival(self, person, survived):
    pass


def test_log_time_step(self, time_step_number):
    pass
