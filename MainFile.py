import DatabaseQueries as dq
import LoadClinicalData as lcd

#1. Get the studies         : Done
#2. Send the studies for processing to clinicial data   : done
#3. Save the studies data to database : in progress

#To extract clinical data from CBioPortal and update MySQL DB
data_dict = dq.getStudies()
data = lcd.processStudies(data_dict)
dq.updateGleasonScore(data)

#json_data = dq.getClinicalData()
#print(json_data)