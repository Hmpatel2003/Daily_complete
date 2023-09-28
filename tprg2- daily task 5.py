""" circalc.py -- simplistic LCR calculator for TPRG 2131 Week 2 Asmt 1

Assignment 1 for Tprg 2131 intro week 1-2


ADD YOUR NAME, STUDENT ID and SECTION CRN here.
Huzaifa Patel
100866869
TPRG 2131-01

This LCR calculator is ugly and incomplete. The code runs but doesn't actually
calculate anything. For full marks, you must complete the computation. You must
also "clean up" the code according to the course style guide and coding
standard. Specifically, you must:
  1) Take code that is duplicated and encapsulate it into a function that is
     called from the main program; the function must not "reach into" the
     main program for its working values;
  2) Rename variables so that they are not single letters, using descriptive
     names;
  3) Actually calculate the resonant frequency, bandwidth and Q factor for the
     SERIES resonant circuit (look up the formulas from ELEC II).

Keep working on the program. As you fix each problem, commit with an
informative commit message.
When done, commit with a message like "Ready for marking" and push the changes
to your assignment1 repository on the server hg.set.durhamcollege.org.
"""
import math

print("Series resonant circuit calculator\n'q' to quit)")
def get_input(prompt):
        value = float(input(prompt))
        if value > 0:
            return value
        else:
            print("The value must be greater than zero.") # duplicated code into function 


while True:
    cal_type = input("print 'S' for series-parallel calculation or 'R' for RC time constant calculation:")
    if cal_type == 'q' or cal_type == 'Q':
        print("END")
        break
        
        
    elif cal_type == 'S': 
        type_of_circuit = input("print '1' for Series circuit or '2' for Parallel circuit:")
           
        if type_of_circuit == '1':#loop for series circuit
            print("series circuit")       
            L = get_input("What is the inductance in mH? ")
            C = get_input("What is the capacitance in uF? ")
            R1 = get_input("Resistance1 in ohm?")
            R2 = get_input("Resistance2 in ohm?")
            resistance = R1 + R2
            print("total resistance: {}ohm".format(resistance))
            
            
            inductance = L * (1/1000)
            print("inductance in hertz: {}Hz".format(inductance))
            capacitance = C * (1/1000000)
            print("capacitance in Farad: {}F".format(capacitance))#convert mH and uF to Hz and F respectively
      
    
            resonant_frequency = 1 / (2 * math.pi * math.sqrt(inductance * capacitance))# variable renamed with descriptive words
            Q_factor = (1 / resistance) * math.sqrt(inductance / capacitance)
            bandwidth = resonant_frequency / Q_factor#formulas 
            
            print("lcr:", inductance, capacitance, resistance, "\n")
            print("Resonant Frequency : {} Hz ".format(resonant_frequency))#got help from chatgpt
            print("Q Factor : {}".format(Q_factor))# got help from chatgpt
            print("Bandwidth : {} Hz ".format(bandwidth)) # got helped from chatgpt
            
        elif type_of_circuit == '2':#loop for Parallel circuit
            print("Parallel circuit")
            inductance = get_input("What is the inductance in mH? ")
            capacitance = get_input("What is the capacitance in uF? ")
            R1 = get_input("Resistance1 in ohm?")
            R2 = get_input("Resistance2 in ohm?")
            resistance = (1/R1) + (1/R2) 
            print("total resistance: {}ohm".format(resistance))
        
            resonant_frequency = 1 /(2 * math.sqrt(inductance * capacitance))
            Q_factor = (1 / resistance) * math.sqrt(inductance / capacitance)
            bandwidth = resonant_frequency / Q_factor
            
            print("lcr:", inductance, capacitance, resistance, "\n")
            print("Resonant Frequency : {}Hz".format(resonant_frequency))
            print("Q Factor : {}".format(Q_factor))
            print("Bandwidth : {}Hz ".format(bandwidth))
                
        else:
            print("invalid value")
     
    elif cal_type == 'R': #loop to find RC time constant
        print("RC time constant")
        type_of_circuit = input("print '1' for Series circuit or '2' for Parallel circuit:")
        if type_of_circuit == '1': #loop to find series RC time constant
            R1 = get_input("Resistance1 in ohm:")
            R2 = get_input("Resistance2 in ohm:")
            capacitance = get_input("capacitance in Farad:")
            
            Rt = R1 + R2
            print("total resistance : {}ohm" . format(Rt))
            
            RC_constant = Rt * capacitance
            print("RC_constant: {}sec". format(RC_constant))
                  
        elif type_of_circuit == '2': # loop to find parallel rc constant
            R1 = get_input("Resistance1 in ohm:")
            R2 = get_input("Resistance2 in ohm:")
            capacitance = get_input("capacitance in Farad:")
            
            Rt = (1/R1) + (1/R2)
            print("total resistance : {}ohm" . format(Rt))
            
            RC_constant = Rt * capacitance
            print("RC_constant: {}sec". format(RC_constant))
            
        else:
            print("invalid value")
    
    else:
        print("invalid value")
           

        