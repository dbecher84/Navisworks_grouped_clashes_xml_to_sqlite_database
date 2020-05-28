

import datetime
import xml.etree.ElementTree as ET


#path='C:\\Users\\Derek.Becher\\Desktop\\test\\clashes_in_sql\\00.01 Structural vs Architectural.xml'
#path='C:\\Users\\Derek.Becher\\Desktop\\test\\clashes_in_sql\\navis_output\\'

#test = ['00.01 Structural vs Architectural.xml', '02.06 Equipment vs Plumbing.xml']

#tree = ET.parse(path)
#root = tree.getroot()

clash_list = []

def tests(clash_type, number, test_file, results_date):
    '''clash_type: group or single result
       number: clash test number
       test_file: path to test file'''
    tree = ET.parse(test_file)
    root = tree.getroot()
    
    for clash in root.iter(clash_type):
        clash_info = []
        clash_info.append(clash.get('guid'))
        clash_info.append(clash.get('name'))
        clash_info.append(clash.get('status'))
        clash_info.append(number)

        #now = datetime.datetime.now()
        #clash_report_date = now.strftime('%Y.%m.%d')
        clash_info.append(results_date)
    
        clash_list.append(clash_info)
    
