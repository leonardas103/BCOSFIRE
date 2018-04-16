# VERSION 09/09/2014
# CREATED BY: George Azzopardi (1), Nicola Strisciuglio (1,2), Mario Vento (2) and Nicolai Petkov (1)
#             1) University of Groningen, Johann Bernoulli Institute for Mathematics and Computer Science, Intelligent Systems
#             1) University of Salerno, Dept. of Information Eng., Electrical Eng. and Applied Math., MIVIA Lab
#
# SystemConfig returns a structure of the parameters required by the
# Bself filter

import numpy
import math

# Use hashtable
ht                             = 1


class COSFIRE:
    # The radii list of concentric circles
    rholist                = [0, 2, 4, 6, 8]    #[i for i in range(0,9,2)]

    # Minimum distance between dominant contours lying on the same concentric circle
    eta                    = 150*math.pi/180

    # Threshold parameter used to suppress the input filters responses that are less than a
    # fraction t1 of the maximum
    t1                     = 0

    # Threshold parameter used to select the channels of input filters that
    # produce a response larger than a fraction t2 of the maximum
    t2                     = 0.4

    # Parameters of the Gaussian function used to blur the input filter
    # responses. sigma = sigma0 + alpha*rho_i
    sigma0                 = 3/6
    alpha                  = 0.8/6

    # Parameters used for the computation of the weighted geometric mean. 

    # mintupleweight is the weight assigned to the peripherial contour parts
    mintupleweight         = 0.5
    outputfunction         = 'geometricmean' # geometricmean OR weightedgeometricmean 
    blurringfunction       = 'max' #max or sum

    # Weights are computed from a 1D Gaussian function. weightingsigma is the
    # standard deviation of this Guassian function
    weightingsigma         = math.sqrt(-max(rholist)**2/(2*math.log(mintupleweight)))

    # Threshold parameter used to suppress the responses of the self filters
    # that are less than a fraction t3 of the maximum response.
    t3                     = 0

# # Parameters of some geometric invariances
class invariance:
    numoriens = 12
    rotation_psilist = [i for i in numpy.arange(0, math.pi, math.pi/numoriens)]
    def set_rotation_psilist(self,numoriens, n):    
        self.rotation_psilist = [i for i in numpy.arange(0, n*math.pi, n*math.pi/numoriens)]
    scale_upsilonlist   = 1 #2.^((0)./2)

    # Reflection invariance about the y-axis. 0 = do not use, 1 = use.
    reflection          = 0

# Minimum distance allowed between detected keypoints. If the distance
# between any two pairs of detected keypoints is less than
# distance.mindistance then we keep only the stronger one.
class detection:
    mindistance          = 8

# Parameters of the input filter. Here we use symmetric Gabor filters.
# Gabor filters are, however, not intrinsic to the method and any other
# filters can be used.
class inputfilter:
    name                     = 'DoG'
    
    class Gabor:
        thetalist          = [i for i in numpy.arange(0, math.pi, math.pi/8)]
        lambdalist         = [4, 4*math.sqrt(2), 8] #4.*(sqrt(2).^(0:2))
        phaseoffset        = math.pi
        halfwaverect       = 0
        bandwidth          = 2
        aspectratio        = 0.5
        inhibition_method  = 1
        inhibition_alpha   = 0
        thinning           = 0
    
    class DoG:
        polaritylist         = [1]
        sigmalist            = 2.4
        sigmaratio           = 0.5
        halfwaverect         = 0

#   if strcmp(params.inputfilter.name,'Gabor')
#       params.inputfilter.symmetric = ismember(params.inputfilter.Gabor.phaseoffset,[0 pi])
#   elseif strcmp(params.inputfilter.name,'DoG')
#       params.inputfilter.symmetric = 1
#   end
