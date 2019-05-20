import pandas as pd
import matplotlib.pyplot as plt

sc_df = pd.read_csv('suppression_costs.csv').set_index('Year', drop=False)
bf_df = pd.read_csv('big_fires.csv').set_index('Year', drop=False)
hfa_df = pd.read_csv('human_fire_acres.csv').set_index('Year', drop=False)
hfn_df = pd.read_csv('human_fire_num.csv').set_index('Year', drop=False)
lfa_df = pd.read_csv('lightning_fire_acres.csv').set_index('Year', drop=False)
lfn_df = pd.read_csv('lightning_fire_num.csv').set_index('Year', drop=False)
tf_df = pd.read_csv('total_fires.csv').set_index('Year', drop=False)
#
# ##################################################################################
# # Question 1: How many fires were there in 2018? human caused? lightning caused? #
# ##################################################################################
#
# print("Total Fires in 2018: ", tf_df.loc[2018]['Fires'])
# print("Total Acres in 2018: ", tf_df.loc[2018]['Acres'])
# print()
#
# print("Total Human Fire Number: ", hfn_df.loc[2018]['Total'])
# print("Total Human Fire Acres: ", hfa_df.loc[2018]['Total'])
# print()
#
# print("Total Lightning Fire Number: ", lfn_df.loc[2018]['Total'])
# print("Total Lightning Fire Acres: ", lfa_df.loc[2018]['Total'])
# print()
#
# hfn_num = hfn_df.loc[2018]['Total']
# lfn_num = lfn_df.loc[2018]['Total']
#
# print("Total Number according to hfa and lfa: ", hfn_num+lfn_num)
#
# # This proves that the lfa and hfa (or lfn and hfn) should add up to equal the totals table
#
#
# ##################################################################
# # QUESTION TWO: What year had the most fires? Most Acres burned? #
# ##################################################################
#
# # --- Most Fires
# tf_max_fire = tf_df[tf_df['Fires'] == tf_df['Fires'].max()]
# print(tf_max_fire)
# print(tf_max_fire.iloc[0][1]) # This returns just the number
#
# # --- Most acres
# tf_max_acre = tf_df[tf_df['Acres'] == tf_df['Acres'].max()]
# print(tf_max_acre)
# print(tf_max_acre.iloc[0][2]) # This Returns Just the number
#
#
# ############################################################################
# # QUESTION THREE: From 1985 - 2018 Who has spent more money on wildfires:  #
# #                 The Forest Service or DOI Agencies?                      #
# #                 What has the total spending been?                        #
# ############################################################################
#
# # Get a list of the columns
# print(sc_df.columns)
#
# fs_total = sc_df['ForestService'].sum()
# print('Forest Service Total: ', fs_total)
#
# doi_total = sc_df['DOIAgencies'].sum()
# print('DOI Agencies Total: ', doi_total)
#
# if doi_total > fs_total:
#     print('DOI spent more money on wildfires')
# else:
#     print('USFS spent more money on wildfires')
#
# print()
# print('Total Spending: ', '${:,.2f}'.format((doi_total + fs_total)))
#
#
# ##############################################################################################
# # QUESTION FOUR: What year had the most money spent per acre in federal firefighting costs?  #
# #                Graph that chart                                                            #
# ##############################################################################################
#
# # Get a list of the columns
# print(sc_df.columns)
#
# dollars_per_acre = sc_df['Total']/sc_df['Acres']
#
# print(dollars_per_acre)
#
# # tf_max_fire = tf_df[tf_df['Fires'] == tf_df['Fires'].max()]
# most_dollar_per_acre = dollars_per_acre[dollars_per_acre == dollars_per_acre.max()]
#
# print(most_dollar_per_acre)
# print('${:,.2f}'.format(most_dollar_per_acre.iloc[0]), "dollars per acre")
#
# print()
# print('--------------Graphing-----------------', '\n')
#
# dollars_per_acre.plot(kind='bar', x='Total', y='Year')
# plt.show()


##############################################################################################
# QUESTION FIVE: From the BigFires Table, group all of the fires by each states total acres  #
#                Group them into regions. Graph it by region                                 #
##############################################################################################
print('------------QUESTION FIVE------------\n')

bf_state = bf_df.groupby(['State']).sum()
bf_state['TotalAcres'] = bf_state['TotalAcres']#.map('{:,.2f}'.format)
bf_state = bf_state.drop(['Year'], axis=1)

print(bf_state)

# this is a check sum to make sure I did the math correctly, formatting causes errors
print("Total sum", bf_state['TotalAcres'].sum(axis=0, skipna=True))


# REGIONS
# Note: some generalizations are made because states don't perfectly align with the regions
# Note: if a state was not in the big fire list it was not added into the region

# Alaska Region: AK
# tf_max_acre = tf_df[tf_df['Acres'] == tf_df['Acres'].max()]
bf_alaska = bf_state.loc['Ak']
bf_alaska = bf_alaska + bf_state.loc['A']

# Northwest: WA, OR
bf_northwest = bf_state.loc['Wa'] + bf_state.loc['Or']

# California: CA, HI (note combining the two california regions for comparability)
bf_california = bf_state.loc['Ca']

# Northern Rockies: North ID, MT, ND
bf_northern_rockies = bf_state.loc['Mt']

# Great basin/Western: ID, NV, UT (note combined with western Great Basin)
bf_great_basin = bf_state.loc['Id'] + bf_state.loc['Nv'] + bf_state.loc['Ut']

# Southwest: AZ, NM, West TX
bf_southwest = bf_state.loc['Az'] + bf_state.loc['Nm']

# Rocky Mountains: WY, CO, SD, NE, KS
bf_rocky_mountains = bf_state.loc['Wy'] + bf_state.loc['Co'] + bf_state.loc['Sd']
print(bf_rocky_mountains)

# Eastern: MN, IA, MO, WI, IL, MI, IN, OH, WV, PA, NY, VT, ME, NH, MA, RI, CT, NK, DE, MD
bf_eastern_area = 0


# Southern Area: TX, OK, AR, LA, MS, AL, TN, KY, VA, SC, NC, GA, FL, PR
bf_southern_area = bf_state.loc['Tx'] + bf_state.loc['Ok'] + bf_state.loc['Ga'] + bf_state.loc['Fl']

# Merged
region_list = ['Alaska', 'Northwest', ' California', 'NorthernRockies', 'GreatBasin', 'Southwest', 'RockyMountains', 'EasternArea', 'SouthernArea']
bf_region_list = [bf_alaska, bf_northwest, bf_california, bf_northern_rockies, bf_great_basin, bf_southwest, bf_rocky_mountains, bf_eastern_area, bf_southern_area]

bf_state_region = pd.DataFrame(columns=['Region','TotalAcres'])

for i in range(len(region_list)):
    if type(bf_region_list[i]) == type(0):
        bf_state_region = bf_state_region.append({'Region': f'{region_list[i]}', 'TotalAcres':bf_region_list[i]},
                                                 ignore_index=True)
    else:
        bf_state_region = bf_state_region.append({'Region': f'{region_list[i]}', 'TotalAcres': bf_region_list[i].iloc[0]},
                                                 ignore_index=True)

print("merged: ")
print(bf_state_region)

print()
print('--------------Graphing---------------')
bf_state_region.plot(kind='bar', x='Region', y='TotalAcres')
plt.show()


########################################################################################################
# QUESTION SIX: What results in more acres burned per year per fire? human or lightning caused fires?  #
#               Determine this on an overall scale as well as a per region scale.                      #
########################################################################################################
print('---------------------QUESTION SIX-----------------------')

# Overall acres per fire (acres/fires) -- human caused
# print(hfa_df)
# print(hfn_df)

hf_acres_per_fire_df = pd.DataFrame(columns=['Year', 'HF_AcresPerFire'])
for i in range(len(hfa_df)):
    hf_acres_per_fire_df = hf_acres_per_fire_df.append({'Year': hfa_df['Year'].iloc[i],'HF_AcresPerFire': (hfa_df['Total'].iloc[i]/hfn_df['Total'].iloc[i])}, ignore_index=True)

print(hf_acres_per_fire_df)

# Overall acres per fire (acres/fires) -- lightning caused
# print(lfa_df)
# print(lfn_df)

lf_acres_per_fire_df = pd.DataFrame(columns=['Year', 'LF_AcresPerFire'])
for i in range(len(lfa_df)):
    lf_acres_per_fire_df = lf_acres_per_fire_df.append({'Year': lfa_df['Year'].iloc[i],'LF_AcresPerFire': (lfa_df['Total'].iloc[i]/lfn_df['Total'].iloc[i])}, ignore_index=True)

print(lf_acres_per_fire_df)

# Plot on top of each other
hf_ax = hf_acres_per_fire_df.plot(x='Year', y='HF_AcresPerFire')
lf_acres_per_fire_df.plot(ax=hf_ax, x='Year', y='LF_AcresPerFire')

plt.show()



