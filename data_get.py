'''
Data Acquisition -- Gets a csv of wildfire data
Cody Crofoot

This code should produce 7 csv files to set up the wildfire database
It can be adjusted to specify which csv is desired
'''

import big_fires
import fire_causes
import suppression_costs
import total_fires


def main():
    big_fires.get_big_fires()
    fire_causes.get_human_fire_acres()
    fire_causes.get_human_fire_num()
    fire_causes.get_lightning_fire_acres()
    fire_causes.get_lightning_fire_num()
    suppression_costs.get_suppression_costs()
    total_fires.get_total_fires()


if __name__ == '__main__':
    main()
