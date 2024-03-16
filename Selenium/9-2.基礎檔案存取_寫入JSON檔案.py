rimport json
dictobject = {'x':60, 'y':55, 'z':90}
fn = r'C:\Users\Roy\Documents\git\Python\Selenium\samples\CreateJson_object.json'
with open(fn,'w') as fnObj:
    json.dump(dictobject, fnObj)
    
listarray = [{'x':"一二三",'y':55,'z':90},{'a':10,'b':25,'c':30}]
fn = r'C:\Users\Roy\Documents\git\Python\Selenium\samples\CreateJson_array.json'
with open(fn, 'w') as fnarray:
    json.dump(listarray, fnarray, ensure_ascii=False)
    
