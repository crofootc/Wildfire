import table_create as tc
import table_populate as tp


def main():
    # Create the database frame
    tc.create_BigFires()
    tc.create_TotalFires()
    tc.create_HumanFireAcres()
    tc.create_HumanFireNum()
    tc.create_LightningFireAcres()
    tc.create_LightningFireNum()
    tc.create_SuppressionCosts()

    # Populates the database
    tp.populate_big_fires()
    tp.populate_total_fires()
    tp.populate_human_fire_acres()
    tp.populate_human_fire_num()
    tp.populate_lightning_fire_acres()
    tp.populate_lightning_fire_num()
    tp.populate_suppression_costs()

if __name__ == '__main__':
    main()


