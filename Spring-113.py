from time import time
cvf=0
import os
import binascii
self="'"

namez = input("for compress c or extract e? ")
#@Author Jurijus pacalovas
class compression:

    def cryptograpy_compression(self):
                
                self.name = "Author: Jurijus pacalovas"
                
                if namez=="c":
                    corridors=0
                    cor=7
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                    Deep=100
                    long_block=100
                        
                    namea="file.W"
                    namem=""
                    namema="?"
                    Portal=2
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
           

                    nameas=name+".bin"
                
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                    sw1=0
                    sw2=0
                    sw3=0
                    sw5=0
                    sw4=0
                    sw6=0
                    sw7=0
                    n1=0
                    n=0
                    n2=0
                    n3=0
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                        if len(data)==0:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                            
                      
                 
                       

                  
                        s=str(data)
                        
                     
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)  
                                
                                size_data3=size_data2
                                long_file=len(size_data3)
                                size_data10=""
                                size_data9=""
                                size_data5=""
                                fda5=""
                                size_data4=""
                                size_data6=""
                                size_data7=""
                                size_data12=""
                                size_data19=""
                                size_data10=size_data3
                                predict=-1
                                
                                Long_block1=0
                                Long_block2=0
                                Long_block3=0
                                Long_block4=0
                                Long_block5=0
                                Long_block6=0
                               
                               
                              
                                times_of_times=0
                                Where4=0
                          
                                

                                cvf1=1
  
                                if cvf1==1:
                                    times_compression=0  
                                    compress_no=0
                                    compress_yes=0
                                    long2=len(size_data3)
                                    Deep=long2//28
                                    times2=Deep
                                    long_block=1024
                                    Where5=0
                                
                                    
                                    
                                    block_compression2=0
                                    
                                    start=-1
                                    Find_guess=0
                                    while Find_guess!=1:
                                        
                                        while  times_compression!=times2 and len(size_data3)>=184:


                                                    
                                                        

                                                    start=0
                                                    blocks=long_block
                                                    size_compress=63
                                                    end=blocks
                                                    
                                                    find_matches1_number1=0
                                                    find_matches1_number2=0
                                                    find_matches1_number3=0   
                                                    
                                                    predict=predict+1
                                                    if predict==16:
                                                        predict=0
                                                    
                                                    
                                                                                                 
                                                                                                                                        
                
                                                    block=0
                                                    b=format(predict,'04b')
                                                    
                                                    Find=1
                                                    block_compression1=0
                                                    block_compression=0
                                                    block_compression2=0
                                                    long=len(size_data3)
                                                    #print(long)
                                                    
                                                    while block<long:
                                                                                str_find_tree_maches=size_data3[block:block+blocks]     
                                                                                Long_block4=Long_block4+1                                                                             
                                                                                Where4=Where4+1
                                                                                if b[0:2]=="01":
                                                                                    b="10"+b[2:]
                                                                                
                                                                                sub2=b
                                                                                sub_info=b
                                                                                
                                                                    
                                                                                
                                                                                find_matches1=str_find_tree_maches.find(sub_info, start, end)
                                                                                find_matches1_1=int(find_matches1)

                                                                                if find_matches1_1==-1:
                                                                                    Find=0 
                                                                                
                                                                                if find_matches1_1!=-1:
                                                                                    
                                                                                    find_matches1_number1=int(find_matches1)
                                           
                                                                                    if find_matches1_1==0:

                                                                                        
                                                                                        Block_Finds=1
                                                                                         
                                                                                        
                                                                                        
                                                                                       
                                                                                        
                                                                                        
                                                                                       
                                                                                        

                                                                                        
                                                                                  
                                                                         
                                                                                     
                                                                                    
                                                                                         
                                                                                    sub_info1="01" 
                                                                                                                     
                                                                                    find_matches2=str_find_tree_maches.find(sub_info1, start, end)
                                                                                    find_matches1_2=int(find_matches2)
                                                                                    if find_matches1_2==0:
                                                                                        
                                                                                        
                                                                                        if Where4!=0:
                                                                                        	
                                                                                    
                                                                                            size_data20=bin(Where4)[2:]
                                                                                            
                                                                                            Where5=Where4
                                                                                            
                                                                                            lenf=len(size_data20)
                                                                                            if lenf>size_compress:
                                                                                                print("File too big")
                                                                                                raise SystemExit
                                                                                                
                                                                                                
                                                                                            
                                                                                            add_bits118=""
                                                                                            count_bits=size_compress-lenf%size_compress
                                                                                            z=0
                                                                                            if count_bits!=0:
                                                                                                if count_bits!=size_compress:
                                                                                                    while z<count_bits:
                                                                                                        add_bits118="0"+add_bits118
                                                                                                        z=z+1
                                                                                                                        
                                                                                                                        
                                                                                            size_data30=size_data20
                                                                                            bits=len(add_bits118)
                                                                                            size_data25=bin(bits)[2:]
                                                                                            lenf=len(size_data25)
                                                                                            if lenf>6:
                                                                                                print("File too big")
                                                                                                raise SystemExit
                                                                                                
                                                                                                
                                                                                            
                                                                                            add_bits119=""
                                                                                            count_bits=6-lenf%6
                                                                                            z=0
                                                                                            if count_bits!=0:
                                                                                                if count_bits!=6:
                                                                                                    while z<count_bits:
                                                                                                        add_bits119="0"+add_bits119
                                                                                                        z=z+1
                                                                                                                        
                                                                                                                        
                                                                                            size_data19="1"+add_bits119+size_data25+size_data30+size_data19
                                                                                            
                                                                                            Find=0

                                                                                    
                                                                                    
                                                                                                                         
                                                                                if Find!=0:
                                                                                    
                                                                                    

                                                                                        
                                                                                     
                                                                                    
                                                                                    compress_yes=compress_yes+1
                                                                                    Long_block5=Long_block5+1
                                                                                    if Long_block5==1:
                                                                                    	Long_block1=len(size_data4)
                                                                                    	
                                                                                    	
                                                                                    if Long_block5>=1:
                                                                                    	Long_block3=len(size_data4)
                                                                                    	
                                                                                    	                                                                                    
                                                                                    
                                                                                        
                                                                                    size_data4=str_find_tree_maches[:0]+"01"+str_find_tree_maches[4:]
                                                                                    size_data6+size_data6+size_data4                                          
                                                                              
                                                                                    size_data5=""
                                                                                    size_data7=""
                                                                                    size_data12=""
                                                                                    size_data4=""
                                                                                    block_compression2=0
                                                                                    Find=1
                                            
                                                                                elif Find==0:
                                                                                    compress_no=compress_no+1
                                                                                    Long_block6=Long_block6+1
                                                                                    #print(compress_no)
                                                                                
                                                                                    block_compression=0
                                                                                    block_compression1=0

                                                                                   
                                                                                    
                                                                                    
                                                                                    size_data4=str_find_tree_maches
                                                                                    
                                                                                    if Long_block6==1:
                                                                                    	Long_block2=len(size_data4)
                                                                                                                                                
                                                                                    if Long_block6>=1:
                                                                                    	Long_block3=len(size_data4)                                                                                                                               	
                                                                                    size_data6=size_data6+size_data4
                                                                                    
                                                                                    
                                                                                   
                                                                             
                                                                                    
                                                                                    size_data5=""
                                                                                    size_data7=""
                                                                                    size_data12=""
                                                                                    block_compression2=0
                                                                                    Find=1
                                                                                        
                                                                                block=block+blocks
                                                                                #print(block)
                                                         
                                                    times_compression=times_compression+1
                                                    size_data19="0"+size_data19
                                                    #print(times_compression)
                                                    
                                                    
                                                         
                                                        
                
                                                    size_data3="1"+size_data6
                                                    
                                                    Where4=0
                                                    
                                                    
                                                    #print(len(size_data6))
                                                    size_data6=""
                                                    
                                        long_after=len(size_data3)
                                        
                                        if long_file<=long_after or long_after<=1:
                                            size_data9="0"+size_data10
                                        elif long_file>long_after:
                                            size_data9="1"+size_data3

                                        #print(size_data9)
                                        long=len(size_data19)    
                                        size_data21=bin(long)[2:]
                                        lenf=len(size_data21)
                                        if lenf>40:
                                                print("File too big")
                                                raise SystemExit
                                                                                        
                                                                                       
                                                                                    
                                        add_bits118=""
                                        count_bits=40-lenf%40
                                        z=0
                                        if count_bits!=0:
                                            if count_bits!=40:
                                                while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                    
                                        size_data22=add_bits118+size_data21+size_data19     
                                        size_data9="1"+size_data22+size_data9

                                        
                                        lenf=len(size_data9)
                                        
                                        add_bits118=""
                                        count_bits=8-lenf%8
                                        z=0
                                        if count_bits!=0:
                                            if count_bits!=8:
                                                while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                                    
                                                                    
                                        size_data9=add_bits118+size_data9

                                        size_data24=bin(times_compression)[2:]
                                        lenf=len(size_data24)
                                        if lenf>40:
                                                print("File too big")
                                                raise SystemExit
                                                                                            
                                                                                            
                                                                                        
                                        add_bits118=""
                                        count_bits=40-lenf%40
                                        z=0
                                        if count_bits!=0:
                                            if count_bits!=40:
                                                while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                                                                                    
                                                                                                                    
                                        size_data9=add_bits118+size_data24+size_data9
                                        
                                        
                                        size_data24=bin(long_block)[2:]
                                        lenf=len(size_data24)
                                        if lenf>40:
                                                print("File too big")
                                                raise SystemExit
                                                                                            
                                                                                            
                                                                                        
                                        add_bits118=""
                                        count_bits=40-lenf%40
                                        z=0
                                        if count_bits!=0:
                                            if count_bits!=40:
                                                while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                                                                                    
                                                                                                                    
                                        size_data9=add_bits118+size_data24+size_data9
                                       
                                        size_data24=bin(Long_block1)[2:]  
                                    	                                    
                                        lenf=len(size_data24)
                                        if lenf>40:
                                                print("File too big")
                                                raise SystemExit
                                                                                        
                                                                                       
                                                                                    
                                        add_bits118=""
                                        count_bits=40-lenf%40
                                        z=0
                                        if count_bits!=0:
                                            if count_bits!=40:
                                                while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                    
                                        size_data9=add_bits118+size_data24+size_data9
                                        size_data24=bin(Long_block2)[2:]  
                                        lenf=len(size_data24)
                                        if lenf>40:
                                                print("File too big")
                                                raise SystemExit
                                                                                        
                                                                                       
                                                                                    
                                        add_bits118=""
                                        count_bits=40-lenf%40
                                        z=0
                                        if count_bits!=0:
                                            if count_bits!=40:
                                                while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                    
                                        size_data9=add_bits118+size_data24+size_data9
                                        size_data24=bin(Long_block3)[2:]
                                        lenf=len(size_data24)
                                        if lenf>40:
                                                print("File too big")
                                                raise SystemExit
                                                                                        
                                                                                       
                                                                                    
                                        add_bits118=""
                                        count_bits=40-lenf%40
                                        z=0
                                        if count_bits!=0:
                                            if count_bits!=40:
                                                while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                    
                                        size_data9=add_bits118+size_data24+size_data9
                                        size_data24=bin(Long_block4)[2:]
                                        lenf=len(size_data24)
                                        if lenf>40:
                                                print("File too big")
                                                raise SystemExit
                                                                                        
                                                                                       
                                                                                    
                                        add_bits118=""
                                        count_bits=40-lenf%40
                                        z=0
                                        if count_bits!=0:
                                            if count_bits!=40:
                                                while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                    
                                        size_data9=add_bits118+size_data24+size_data9
                                       
                                        
                                        
                                        	
                                       			
                                        Long_block1=0
                                        Long_block2=0
                                        Long_block3=0
                                        Long_block4=0
                                        Long_block5=0
                                        Long_block6=0  
                                        
                                        long_file=len(size_data10)
                                        long_after=len(size_data9)
                                        
                                        
                                        if long_file>long_after and long_after<=400 or lenf>39 or long_block>=long_after:
                                          
                                            size_data11=size_data9
                                            Find_guess=1
                                        elif long_file<=long_after:
                                            size_data3=size_data10
                                            long_block=long_block+1
                                            
                                            size_data9=""
                                            size_data19=""
                                            start=-1
                                            times_compression=0
                                            predict=-1
                                            
                                        elif long_file>long_after:
                                            size_data3=size_data9
                                            long_block=long_block+1
                                            times_of_times=times_of_times+1
                                            size_data9=""
                                            size_data19=""
                                            start=-1
                                            times_compression=0
                                            predict=-1    
       
                                    size_data24=bin(times_of_times)[2:]
                                    lenf=len(size_data24)
                                    if lenf>40:
                                        print("File too big")
                                        raise SystemExit
                                                                                            
                                                                                            
                                                                                        
                                    add_bits118=""
                                    count_bits=40-lenf%40
                                    z=0
                                    if count_bits!=0:
                                        if count_bits!=40:
                                            while z<count_bits:
                                                add_bits118="0"+add_bits118
                                                z=z+1
                                                                                                                    
                                                                                                                    
                                    size_data11=add_bits118+size_data24+size_data11
                                    
                                    n = int(size_data11, 2)
                                
                                    qqwslenf=len(size_data11)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                
                                    size_after=len(jl)
                                   
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                            
                                    assxw=assxw+1
                                    if assxw==1:
                                        assx=10
                                        if assx==10:

                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)

    def cryptograpy_unpack(self):                      
                 if namez=="e":
                    corridors=0
                    cor=7
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                    Portal=2
                    namea="file.W"
                    namem=""
                    namema="?"
                    Deep=0
                 
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
                    name_cut=""
                    name_cut=len(".bin")
                    nameas=name
                    
                    name_long=len(nameas)
                    nameSS=name[name_long-name_cut:]
                    if nameSS!=".bin":
                        x3=0.0
                        return print(x3)
                        
                    nameas=name[:name_long-name_cut]
                    nac=len(nameas)
                    
                    Deep=1000
                    
                    
                    nac=len(nameas)
                    sw1=0
                    sw2=0
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                    sw3=0
                    sw4=0
                    sw5=0
                    sw6=0
                    sw7=0
                    n=0
                    n1=0
                    n2=0
                    n3=0
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        
                        data = binary_file.read()
                        if len(data)==0:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                     	

                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)  
                                x4=1
                                if x4==1:
                                
                                    
                                    size_data3=size_data2
                                    Times_extract_of_times=size_data3[0:40]
                                    size_data3=size_data3[40:]
                                    Times_extract_number=0
                                    Times_extract_number=int(Times_extract_of_times,2)
                                    Time_extract=0
                                    Times_extract=Times_extract_number
                              
                                       
                                    Times_count=0
                                    while Times_extract<=Times_count:

                                        Blocks_long=size_data3[0:40]
                                        size_data3=size_data3[40:]
                                        Blocks_long_number=int(Blocks_long,2)
                                        Read_times_compression_info=""
                                        
                                        Read_times_compression_info=size_data3[0:40]
                                        
                                        Save_predict_find=""
                                        Read_times_compression_number =int(Read_times_compression_info,2)
                                        
                                        size_data3=size_data3[40:]

                                        

                                        predict=-1
                                        count_times_compression=0
                                    

                                        while Read_times_compression_number!=count_times_compression:
                                            predict=predict+1
                                            if predict==16:
                                                predict=0
                                            b=format(predict,'04b')
                                            if b[0:2]=="01":
                                                b="10"+b[2:]
                                            Save_predict_find=b+Save_predict_find
                                            count_times_compression=count_times_compression+1
                                                    

                                        #print(Save_predict_find)

                                        if size_data3[0:9]=="000000001":
                                            size_data3=size_data3[9:]
                                        elif size_data3[0:8]=="00000001":
                                            size_data3=size_data3[8:]
                                        elif size_data3[0:7]=="0000001":
                                            size_data3=size_data3[7:]
                                        elif size_data3[0:6]=="000001":
                                            size_data3=size_data3[6:]
                                        elif size_data3[0:5]=="00001":
                                            size_data3=size_data3[5:]
                                        elif size_data3[0:4]=="0001":
                                            size_data3=size_data3[4:]
                                        elif size_data3[0:3]=="001":
                                            size_data3=size_data3[3:]
                                        elif size_data3[0:2]=="01":
                                            size_data3=size_data3[2:]
                                        elif size_data3[0:1]=="1":
                                            size_data3=size_data3[1:]


                                        open_binary_code_01=size_data3[0:40]
                                       
                                        
                                        open_binary_code_01_number=int(open_binary_code_01,2)
                                        
                                        size_data3=size_data3[40:]
                                        long_open_binary_code=open_binary_code_01_number
                                        Infromation_program=size_data3[:long_open_binary_code]
                                        Program=0
                                        Binary_code=""
                                        size_data3=size_data3[long_open_binary_code:]
                                        Binary_code=Infromation_program

                                                
                                                   

                                        extract=0
                                        
                                        if size_data3[0:1]=="0":
                                            extract=1
                                        elif size_data3[0:1]=="1":
                                            extract=2

                                        size_data3[1:]
                                        
                                        
                                        size_data12=""
                                        #print(extract)
                                        if extract==1:
                                            size_data12=size_data3

                                        elif extract==2:
                                            times_compression=0
                                            
                                            compress_no=0
                                            compress_yes=0
                                            long2=len(size_data3)
                                            Deep=Read_times_compression_number
                                            times2=Deep
                                            
                                        
                                            
                                            
                                            block_compression2=0
                                          
                                        
                                            start=-1
                                            while  times_compression<=times2:

                                                        start=0
                                                        blocks=Blocks_long_number
                                                        end=blocks
                                                        
                                                        find_matches1_number1=0
                                                        find_matches1_number2=0
                                                        find_matches1_number3=0   
                                                        
                                                        
                                                        
                                                                                                     
                                                                                                                                            
                    
                                                        block=0
                                                        b=Save_predict_find[times_compression*4:(times_compression*4)+4]
                                                        
                                                        Find=1
                                                        block_compression1=0
                                                        block_compression=0
                                                        block_compression2=0
                                                        long=len(size_data3)
                                                        #print(long)
                                                        
                                                        Binary_code1=""
                                                        Circle_count=Binary_code[0:1]
                                                        if Circle_count=="0":
                                                            Binary_code=Binary_code[1:]
                                                            Program=0
                                                            
                                                        Infromation_program=Binary_code
                                                        Long_Info=len(Infromation_program)
                                                        
                                                        while block<=long:
                                                                                    str_find_tree_maches1=size_data3[block:block+blocks]
                                                                                    sub_info="01"
                                                                                    

                                                                                    find_matches1=str_find_tree_maches1.find(sub_info, start, end)
                                                                                    find_matches1_1=int(find_matches1)

                                                                                    Binary_code2=""
                                                                                    blocks2=0
                                                                                    Have_number=-1
                                                                                    Program=0
                                                                                    
                                                                                    if Long_Info!=0:
                                                                                        Program_code1=Infromation_program[Program:Program+1]
                                                                                        if Program_code1=="1":
                                                                                            Program=Program+1
                                                                                            Program_code_6_bits=Infromation_program[Program:Program+6]
                                                                                            Binary_code1=Program_code_6_bits+Binary_code1
                                                                                            Program=Program+6
                                                                                            Program_code_6_bits_binary=int(Program_code_6_bits,2)
                                                                                            Secret_code=Infromation_program[Program:Program+Program_code_6_bits_binary]
                                                                                            Binary_code1=Secret_code+Binary_code1
                                                                                            
                                                                                            Program=Program+Program_code_6_bits_binary
                                                                                            Sixtythree=63
                                                                                            Left=0
                                                                                            Left=Sixtythree-Program_code_6_bits_binary
                                                                                            Secret_left=Infromation_program[Program:Program+Left]
                                                                                            Binary_code1=Secret_left+Binary_code1
                                                                                            Binary_code2=Secret_left+Binary_code2
                                                                                            

                                                                                            Have_number=int(Binary_code2,2)
                                                                                          
                                                                                            Infromation_program=Infromation_program[Program+Left:]
                                                                                
                                                                                    if find_matches1_1==0 and block!=Have_number:
                                                                                        size_data4=str_find_tree_maches1[:0]+b+str_find_tree_maches[2:]
                                                                                        size_data12=size_data12+size_data4
                                                                                        
                                                                                       
                                                                                        blocks2=blocks-2
                                                                                        
                                                                                    else:
                                                                                        size_data4=str_find_tree_maches1
                                                                                        size_data12=size_data12+size_data4
                                                                                        
                                                                                        
                                                                                        blocks2=blocks
                                                                                        
                                                                                    
                                                                                    block=block+blocks2
                                                                                    
                                                        times_compression=times_compression+1
                                                        #print(times_compression)
                                                        size_data3=size_data12
                                                        print(size_data12)
                                                        
                                                        
                                                        
                                                        size_data12=""
                                                        

                                        Times_count=Times_count+1
                                        
                                        
                                    lenf=len(size_data3)
                                        
                                    add_bits118=""
                                    count_bits=8-lenf%8
                                    z=0
                                   
                                    if count_bits!=0:
                                          if count_bits!=8:
                                               while z<count_bits:
                                                   add_bits118="0"+add_bits118
                                                   z=z+1
                                                                    
                                                                    
                                    size_data3=add_bits118+size_data3
                                      
                                    n = int(size_data3, 2)
                                    
                                    
                                    qqwslenf=len(size_data3)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                 
                               
                                    sssssw=len(jl) 
                                  
                                   

                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                                    
                            
                                    assxw=assxw+1
                                    if assxw==1:
                                        assx=10
                                        if assx==10:
                                        	
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)

 
                  
self=""                                
d=compression()
    
xw=d.cryptograpy_compression()
print(xw)

xw1=d.cryptograpy_unpack()
print(xw1)
