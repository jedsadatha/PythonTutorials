#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_data(filename) :
    '''
    get_data() 
    Loads the data from a filename.
    Organizes the data and retunrs key data values
    '''
    import numpy as np
    import pandas as pd
    
    my_input_data = pd.read_csv(filename)  # read the data

    raw_data   = my_input_data.to_numpy()                    # convert to numpy array
    obs, grps  = raw_data.shape                              # get the number of rows and columns
    new_length = obs*grps                                    # compute total number of observations
    values_col = np.reshape(raw_data, (new_length, 1), 
                            order = 'F')                     # reshape the array
    values_col = np.squeeze(values_col)                      # squeeze to make 1D

    return values_col, obs


# In[2]:


def get_strains(obs=10, names=['wildtype', 'mutant']) :
    '''
    get_strains() 
    Takes names of rat types (e.g., names=['wildtype', 'mutant']) and 
    the number of observation per group (obs_per_grp=10).
    Returns the variable `strain` containing.
    User specifies a filename string.
    '''
    import pandas as pd
 
    strain = pd.Series(names)                   # make the short series
    strain = strain.repeat([2*obs])     # repeat each over two cell's worth of data
    strain = strain.reset_index(drop=True)      # reset the series's index value
    
    return strain


# In[5]:


def get_sexes(obs=10, sexLabels=['male', 'female']) :
    '''
    tidyMyData() Takes one-column-per-cell rat reaction time data as input.
    Returns tidy one-column-per-variable data.
    User specifies a filename string.
    '''
    import pandas as pd
 
    sexes = pd.Series(sexLabels)                      # make the short series
    sexes = sexes.repeat(obs)                 # repeat each over one cell's worth of data
    sexes = pd.concat([sexes]*2, ignore_index=True)   # stack or "concatonate" two copies
    
    return sexes


# In[4]:


def tidy_data(values_col,strain,sexes) :
    '''
    tidyMyData() Takes 
    1. A one-column-per-cell rat reaction time data (values_col).
    2. A sexes variables labelling each entry in values_col by rat-sex
    3. A strain variable labelling entries in values_col by rat strain
    
    Returns one-column-per-variable data adhering to the tidy format.
    
    '''
    
    import pandas as pd

    # construct the data frame
    my_new_tidy_data = pd.DataFrame(
        {
            "RTs": values_col,                               # make a column named RTs and put the values in
            "sex": sexes,                                    # ditto for sex
            "strain": strain                                 # and for genetic strain
        }    
    )
    
    return my_new_tidy_data

