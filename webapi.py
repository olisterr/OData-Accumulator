# Created By: Olister Rumao
# Email: olisterr@gmail.com/ olisterr.cf@outlook.com
# Mob : +91 8983161585
# Skype: olisterr.cf

# This program reads the file ODATA?.txt in cosecutive increments when it finds @odata.nextlink tag and reads the next file and accumulates and stores the ouput 
# Replace reading of the file to getting the ODATA data from the OData Service Endpoint and store in the variable "contents"
# I've marked "******************************" where the files are to be replaced OData connectors value
# Cheers!! :)

import sys

#CALL YOUR ODATA CONNECTION HERE            ******************************
f= open("ODATA.txt","r+")
contents = f.read()
f.close()

finalodatavalues = ""
#AUTHENTICATE WITH THE BASE URL

#SPLIT NEXT LINK
value = contents.split("],\"@odata.nextLink\":\"",1)
if len(value) > 1:
    nextlink = value[1].split("\"}",1)
    nextlink = nextlink[0]
    #print nextlink 

    finalodatavalues = value[0] #SAVE THE CURRENT CONTEXT

    #SPLIT THE CONTEXT +  VALUE TAG
    valuecontext = value[0].split(",\"value",1) 
    valuecontext = valuecontext[0]+ ",\"value\":["
    count = 1
    #print valuecontext
    
    #READ THE NEXT LINK AND LOOP
    while nextlink != "":
        count += 1 
        filename = "ODATA"+ str(count)+ ".txt"
        #print count
        try:
            #CALL YOUR ODATA CONNECTION HERE            ******************************
            f2 = open(filename,'r+')
        except:
            break
        contents = f2.read()
        value = contents.split("],\"@odata.nextLink\":\"",1)
        if len(value) > 1:
            nextlink = value[1].split("\"}",1)
            nextlink = nextlink[0]
            #print nextlink
            value =  value[0].split(valuecontext,1)
            #print value[1]
            finalodatavalues = finalodatavalues + ","+ str(value[1])
            #print('IF')
        else:    
            nextlink = ""
            #print(value[0])
            value =  value[0].split(valuecontext,1)

            finalodatavalues = finalodatavalues + ","+ str(value[1])
            #print('ELSE')
        
    if count > 1:
        finalodatavalues = finalodatavalues + "}"



else:
   finalodatavalues = value[0]
   print finalodatavalues

finalop = open("Output.txt","w+")
finalop.truncate()
finalop.close()
print ("Writing final output to Output.txt")
finalop = open("Output.txt","w+")
finalop.write(finalodatavalues)
finalop.close()

