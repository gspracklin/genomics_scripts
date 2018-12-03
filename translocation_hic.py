def translocation(heatmap):
    #create cis_mask
    #move inside for simplicity
    #cis_mask = np.zeros(A.shape, dtype=bool)
    #for chrom in clr.chromnames:
    #    lo, hi = clr.extent(chrom)
    #    cis_mask[lo:hi, lo:hi] = True

    #create cis/trans map with nan
    cisMap = heatmap * (cis_mask==1)
    cisMap[cisMap==0]=np.nan
    transMap = heatmap * (cis_mask==0)
    transMap[transMap==0]=np.nan

    #compare top percentile, if true then translocation
    badBins=np.asarray([((np.nanpercentile(transMap[x,:], 99.5)) > (np.nanpercentile(cisMap_test[x,:], 35))).any() for x in range(len(transMap))])
    #filter for consecutive badBins, remove singletons
    #really_badBins=np.array([sum(badBins[abs(i-2):(i+3):1])>4  for i in range(len(badBins))])
    return badBins

"""
Alternative strategy, use pecentile to identify 'bowties' (check both Mij) then
filter to the end of the chromosomes - because the signal decays over distance
"""
