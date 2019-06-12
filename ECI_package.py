import numpy as np
import pandas as pd
import scipy.stats as ss

def standardize_index(eci_input):
    """
    INPUTS:
    ------
    eci_input       : vector of iteration to be standardized

   OUTPUTS:
    -------
    ECI             : M x 1 vecor of ECI measure for iteration = rep
    """
    mean = np.mean(eci_input)
    std = np.std(eci_input);
    ECI = (eci_input - mean)/std
    return ECI


def rank_list(eci_list):
    """
    INPUTS:
    ------
    eci_list        : vector ECI or MOR values
    
    OUTPUTS:
    -------
    ECI_Rank        : M x 1 vector of ECI rankings (rank: 1 = largest/highest ECI)
    """
    return (len(eci_list) - ss.rankdata(eci_list).astype(int))+1



def eci_compute(AdjData,iterations):
    """
    This function computes the Economic Complexity Index (ECI) using the 
    method of reflections first introduced Hidalgo et al. (). 
    
    INPUTS:
    ------
    AdjData              : M x N count (unweighted) adjacency matrix (M = #Majors; N = #Occs)
    iterations           : scalar number of iterations to run the method for.
    
    OUTPUTS:
    -------
    ECI_Maj_Odd          : M x 1 vector of ECI measure
    ECI_Maj_Even         : M x 1 vector of ECI measure (gives correct rank of the majors)
    ECI_Occ_Odd          : N x 1 vector of ECI measure
    ECI_Occ_Even         : N x 1 vector of ECI measure (gives correct rank of the majors)
    ECI_Maj_All          : M x iter matrix of ECI measures (iter = #iterations)
    ECI_Occ_All
    
    DEPENDENCIES:
    -------------
    standardize_index(eci_input,rep)       : Function that standardizes the MOR into ECI. 
    
    """
    ###############################
    # DATA PREPARATION
    ###############################
    M, N = np.shape(AdjData); # M = NumMajors; N = NumOccs.
    TotalM = np.sum(AdjData, axis = 1,dtype='float64')
    TotalN = np.sum(AdjData, axis = 0,dtype='float64')
    
    # Major Weights
    MajWeight = np.zeros((M,N),dtype='float64')
    for i in range(M):
        MajWeight[i,:] = AdjData[i,:] / TotalM[i]
    # Occupation Weights
    OccWeight = np.zeros((M,N),dtype='float64')
    for i in range(N):
        OccWeight[:,i] = AdjData[:,i] / TotalN[i]
    
    ###############################
    # METHOD OF REFLECTIONS
    ###############################
    # First iteration --> spread
    MajFactor1 = np.sum((AdjData>0)*1, axis=1, dtype='float64').reshape(M,1)
    OccFactor1 = np.sum((AdjData>0)*1, axis=0, dtype='float64').reshape(N,1)
    # MOR iterations
    for i in range(iterations):
        MajFactor1 = np.hstack((MajFactor1, MajWeight *  np.mat(OccFactor1[:,i]).reshape(N,1)))
        OccFactor1 = np.hstack((OccFactor1, OccWeight.T * np.mat(MajFactor1[:,i]).reshape(M,1)))
    
    ###############################
    # OUTPUT PREPARATION
    ############################### 
    if iterations % 2 == 0: 
        rep = iterations 
    else: 
        rep = iterations - 1
        
    ECI_Maj_Odd = standardize_index(MajFactor1[:,rep-1])
    ECI_Maj_Even = standardize_index(MajFactor1[:,rep])
    ECI_Occ_Odd = standardize_index(OccFactor1[:,rep-1])
    ECI_Occ_Even = standardize_index(OccFactor1[:,rep])
    ECI_Maj_All = MajFactor1
    ECI_Occ_All = OccFactor1
 
    
    ###############################
    # REPORT RESULTS AND RETURN OUTPUTS
    ###############################                 
    print ""
    print "-------------------------------------------------------------------------------------------"
    print "- Computation Completed Successfully                             -"
    print "-------------------------------------------------------------------------------------------"
    print ""
    print "Number of Majors,                           M : " + "{:>15,.0f}".format(M)
    print "Number of Occupations,                      N : " + "{:>15,.0f}".format(N)
    print "Number of Iterations used for even,      Iter : " + "{:>15,.0f}".format(rep)
    print "Number of Iterations used for odd,       Iter : " + "{:>15,.0f}".format(rep-1)
    print ""
    print "-------------------------------------------------------------------------------------------"
    print "- Main Results                              -"
    print "-------------------------------------------------------------------------------------------"
    print 
    #print "ECI Maj Even: *USE* " 
    #print pd.DataFrame(ECI_Maj_Even).head(10)
    #print "ECI Occ Odd: *USE* " 
    #print pd.DataFrame(ECI_Occ_Odd).head(10)
    #print "-------------------------------------------------------------------------------------------"
    #print "ECI Maj Odd:  " 
    #print pd.DataFrame(ECI_Maj_Odd).head(10)
    #print "ECI Occ Even:  " 
    #print pd.DataFrame(ECI_Occ_Even).head(10)
    print "-------------------------------------------------------------------------------------------"
    print "ECI Maj ALL: " 
    print pd.DataFrame(ECI_Maj_All).head(10)
    print "-------------------------------------------------------------------------------------------"
    print "ECI Occ ALL: " 
    print pd.DataFrame(ECI_Occ_All).head(10)
    print "-------------------------------------------------------------------------------------------"
    # Output returned
    # return [ECI_Maj_Odd, ECI_Maj_Even, ECI_Occ_Odd, ECI_Occ_Even, ECI_Maj_All, ECI_Occ_All, ECI_Maj_All_std, ECI_Occ_All_std, ECI_Maj_All_rank, ECI_Occ_All_rank]
    return [ECI_Maj_All, ECI_Occ_All]



# BELOW FUNCTIONS NEEDS TO BE DEVELOPED FURTHER...

def post_analysis(eci_maj_iter_matrix,eci_occ_iter_matrix,names_list_majs,names_list_occs):
    """
    INPUTS:
    ------
    eci_maj_iter_matrix : maj vector of iteration to be standardized
    eci_occ_iter_matrix : occ vector of iteration to be standardized
    names_list majs : list of maj names
    names_list_occs : list of occ names [to be added]
    
    OUTPUTS:
    -------
    ECI_Maj_Even_rank   : M x (iter/2)+1 matrix
    ECI_Occ_Odd_rank    : O x (iter/2)+1 matrix
    """

    #Standardized ECI for each iteration:
    #ECI_Maj_All_std = pd.DataFrame(eci_iter_matrix, index = names_list_majs).apply(ECI.standardize_index)
    #ECI_Occ_All_std = pd.DataFrame(eci_iter_matrix_occs, index = names_list_occs).apply(ECI.standardize_index)
    
    #Rankings within each iteration:
    ECI_Maj_All_rank = pd.DataFrame(eci_maj_iter_matrix,index = names_list_majs).apply(rank_list)
    ECI_Occ_All_rank = pd.DataFrame(eci_occ_iter_matrix,index = names_list_occs).apply(rank_list)  
    
    #Report only even for Maj, and Odd for Occupation
    ECI_Maj_Even_rank = ECI_Maj_All_rank.loc[:,::2]
    ECI_Occ_Odd_rank = ECI_Occ_All_rank.loc[:,1::2]
    
    return ECI_Maj_Even_rank, ECI_Occ_Odd_rank


    
def MOR_plot(ECI_Maj_Even_rank,title_label_str,x_label_str):
    """
    INPUTS:
    ------
    ECI_Maj_Even_rank   : either occ or major matrix
    title_label_str     : string label for TITLE
    x_label_str         : string label for X-axis
    
    OUTPUTS:
    -------
    ECI_Maj_Even_rank   : M x (iter/2)+1 matrix
    """
    return ECI_Maj_Even_rank.transpose().plot(legend=False, title= title_label_str, figsize=(5,10)).set_xlabel(x_label_str)
    
    
# Below Added to use on Xiao's data.      
    
def eci_compute_withWeights(AdjData,iterations,MajWeight,OccWeight):
    """
    This function computes the Economic Complexity Index (ECI) using the 
    method of reflections first introduced Hidalgo et al. (). 
    
    INPUTS:
    ------
    AdjData              : M x N count (unweighted) adjacency matrix (M = #Majors; N = #Occs)
    iterations           : scalar number of iterations to run the method for.
    
    OUTPUTS:
    -------
    ECI_Maj_Odd          : M x 1 vector of ECI measure
    ECI_Maj_Even         : M x 1 vector of ECI measure (gives correct rank of the majors)
    ECI_Occ_Odd          : N x 1 vector of ECI measure
    ECI_Occ_Even         : N x 1 vector of ECI measure (gives correct rank of the majors)
    ECI_Maj_All          : M x iter matrix of ECI measures (iter = #iterations)
    ECI_Occ_All
    
    DEPENDENCIES:
    -------------
    standardize_index(eci_input,rep)       : Function that standardizes the MOR into ECI. 
    
    """
    ###############################
    # DATA PREPARATION
    ###############################
    M, N = np.shape(AdjData); # M = NumMajors; N = NumOccs.
    TotalM = np.sum(AdjData, axis = 1,dtype='float64')
    TotalN = np.sum(AdjData, axis = 0,dtype='float64')
    
#    # Major Weights
#    MajWeight = np.zeros((M,N),dtype='float64')
#    for i in range(M):
#        MajWeight[i,:] = AdjData[i,:] / TotalM[i]
#    # Occupation Weights
#    OccWeight = np.zeros((M,N),dtype='float64')
#    for i in range(N):
#        OccWeight[:,i] = AdjData[:,i] / TotalN[i]
        
        
        
        
    
    ###############################
    # METHOD OF REFLECTIONS
    ###############################
    # First iteration --> spread
    MajFactor1 = np.sum((AdjData>0)*1, axis=1, dtype='float64').reshape(M,1)
    OccFactor1 = np.sum((AdjData>0)*1, axis=0, dtype='float64').reshape(N,1)
    # MOR iterations
    for i in range(iterations):
        MajFactor1 = np.hstack((MajFactor1, MajWeight *  np.mat(OccFactor1[:,i]).reshape(N,1)))
        OccFactor1 = np.hstack((OccFactor1, OccWeight.T * np.mat(MajFactor1[:,i]).reshape(M,1)))
    
    ###############################
    # OUTPUT PREPARATION
    ############################### 
    if iterations % 2 == 0: 
        rep = iterations 
    else: 
        rep = iterations - 1
        
    ECI_Maj_Odd = standardize_index(MajFactor1[:,rep-1])
    ECI_Maj_Even = standardize_index(MajFactor1[:,rep])
    ECI_Occ_Odd = standardize_index(OccFactor1[:,rep-1])
    ECI_Occ_Even = standardize_index(OccFactor1[:,rep])
    ECI_Maj_All = MajFactor1
    ECI_Occ_All = OccFactor1
 
    
    ###############################
    # REPORT RESULTS AND RETURN OUTPUTS
    ###############################                 
    print ""
    print "-------------------------------------------------------------------------------------------"
    print "- Computation Completed Successfully                             -"
    print "-------------------------------------------------------------------------------------------"
    print ""
    print "Number of Majors,                           M : " + "{:>15,.0f}".format(M)
    print "Number of Occupations,                      N : " + "{:>15,.0f}".format(N)
    print "Number of Iterations used for even,      Iter : " + "{:>15,.0f}".format(rep)
    print "Number of Iterations used for odd,       Iter : " + "{:>15,.0f}".format(rep-1)
    print ""
    print "-------------------------------------------------------------------------------------------"
    print "- Main Results                              -"
    print "-------------------------------------------------------------------------------------------"
    print 
    #print "ECI Maj Even: *USE* " 
    #print pd.DataFrame(ECI_Maj_Even).head(10)
    #print "ECI Occ Odd: *USE* " 
    #print pd.DataFrame(ECI_Occ_Odd).head(10)
    #print "-------------------------------------------------------------------------------------------"
    #print "ECI Maj Odd:  " 
    #print pd.DataFrame(ECI_Maj_Odd).head(10)
    #print "ECI Occ Even:  " 
    #print pd.DataFrame(ECI_Occ_Even).head(10)
    print "-------------------------------------------------------------------------------------------"
    print "ECI Maj ALL: " 
    print pd.DataFrame(ECI_Maj_All).head(10)
    print "-------------------------------------------------------------------------------------------"
    print "ECI Occ ALL: " 
    print pd.DataFrame(ECI_Occ_All).head(10)
    print "-------------------------------------------------------------------------------------------"
    # Output returned
    # return [ECI_Maj_Odd, ECI_Maj_Even, ECI_Occ_Odd, ECI_Occ_Even, ECI_Maj_All, ECI_Occ_All, ECI_Maj_All_std, ECI_Occ_All_std, ECI_Maj_All_rank, ECI_Occ_All_rank]
    return [ECI_Maj_All, ECI_Occ_All]    
    
    
    
