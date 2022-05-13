def get_boundaries(ins_table, resolution, sample_id):
    """
    Params: ins_table, resolution, sample_id
    Returns: boundaries_df
    """
    column = 'is_boundary_'+str(resolution)
    return ins_table[sample_id][(ins_table[sample_id].is_bad_bin == False) & (ins_table[sample_id][column] == True)]


def overlap(ipg, boundaries):
    """
    Params: ipg, boundaries_df
    Return: overlap_df
    """
    return bioframe.overlap(dld_ipg, boundaries)


def agg(overlap_df, sample_id):
    """
    Params: sample_id, overlap_df
    Return: concat_df
    """
    df = overlap_df.groupby(['chrom','start','end','length','state']).agg(**{
    'boundaries' : ('chrom_', 'count'),
    })
    
    df['sample'] = sample_id
    
    return df.reset_index()

def normalize(concat_df):
    """
    Params: concat_df
    Returns: norm_df
    """

    df = concat_df.groupby(['state','sample']).agg(**{
    'boundaries_sum' : ('boundaries', sum),
    'length_sum' : ('length', sum)
    })

    df['bound_norm'] = df['boundaries_sum'] / (df['length_sum'] / 1_000_000)

    return df.reset_index()

def norm_boundaries_ipg(ins_table, dld_ipg, resolution, sample_id_list):
    appended_data = []   
    for sample_id in sample_id_list:
        b = get_boundaries(ins_table, resolution, sample_id)
        o = overlap(dld_ipg, b)
        ag = agg(o, sample_id)
        n = normalize(ag)
        appended_data.append(n)
    appended_data = pd.concat(appended_data)
    return appended_data 






