from tkinter import * 
from tkinter import  ttk
from tkinter import messagebox

#Weight_Converter
def weight_converter():
    def convert():
        input_get=input_value.get()
        unit1_get= unit1.get()
        unit2_get= unit2.get()
        if unit1_get =='Kilogram (kg)':
            unit1_get = 1
        elif unit1_get=='Gram (g)':
            unit1_get = 2
        elif unit1_get== 'Pound (Ib)':
            unit1_get = 3
        elif unit1_get=='Milligram(mg)':
            unit1_get = 4
        elif unit1_get== 'Centigram(cg)':
            unit1_get = 5
        elif unit1_get=='Decigram(dg)':
            unit1_get = 6
        elif unit1_get== 'Hectogram(hg)':
            unit1_get = 7
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%unit1_get)


        if unit2_get =='Kilogram (kg)':
            unit2_get = 1
        elif unit2_get=='Gram (g)':
            unit2_get = 2
        elif unit2_get== 'Pound (Ib)':
            unit2_get = 3
        elif unit2_get=='Milligram(mg)':
            unit2_get = 4
        elif unit2_get== 'Centigram(cg)':
            unit2_get = 5
        elif unit2_get=='Decigram(dg)':
            unit2_get = 6
        elif unit2_get== 'Hectogram(hg)':
            unit2_get = 7
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%unit2_get)

    
        if unit1_get==1 and unit2_get==1:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Kg')
            
        elif unit1_get==1 and unit2_get==2:
            value= input_get*1000
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end',' g')
       
        elif unit1_get==1 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*2.20462
            output.insert('end',round(value,2))
            output.insert('end',' Pound')

        elif unit1_get==1 and unit2_get==4:
            value= input_get*1000000
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','mg')

        elif unit1_get==1 and unit2_get==5:
            value= input_get*10000
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','cg')
        elif unit1_get==1 and unit2_get==6:
            value= input_get*10000
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','dg')
        elif unit1_get==1 and unit2_get==7:
            value= input_get*10
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','hg')
#gram to all other units
        elif unit1_get==2 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get/1000
            output.insert('end',round(value,2))
            output.insert('end',' Kg')
        
        elif unit1_get==2 and unit2_get==2:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' g')
            
        elif unit1_get==2 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get/454
            output.insert('end',round(value,2))
            output.insert('end',' Pound')
        
        elif unit1_get==2 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*1000
            output.insert('end',round(value,2))
            output.insert('end',' mg')

        elif unit1_get==2 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*100
            output.insert('end',round(value,2))
            output.insert('end',' cg')

        elif unit1_get==2 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*10
            output.insert('end',round(value,2))
            output.insert('end',' dg')

        elif unit1_get==2 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get/100
            output.insert('end',round(value,2))
            output.insert('end',' hg')
        #pound to all other units
        elif unit1_get==3 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get/2.205
            output.insert('end',round(value,2))
            output.insert('end',' Kg')
        
        elif unit1_get==3 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*454
            output.insert('end',round(value,2))
            output.insert('end',' g')
        
        elif unit1_get==3 and unit2_get==3:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Pound')

        elif unit1_get==3 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*453600
            output.insert('end',round(value,2))
            output.insert('end','mg')

        elif unit1_get==3 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*45360
            output.insert('end',round(value,2))
            output.insert('end','cg')

        elif unit1_get==3 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*4536
            output.insert('end',round(value,2))
            output.insert('end','dg')

        elif unit1_get==3 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*4.536
            output.insert('end',round(value,2))
            output.insert('end','hg')
       
        #milligram to all other units
        elif unit1_get==4 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get/1000000
            output.insert('end',round(value,2))
            output.insert('end',' Kg')
        
        elif unit1_get==4 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get/1000
            output.insert('end',input_get)
            output.insert('end',' g')
            
        elif unit1_get==4 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get/453600
            output.insert('end',round(value,2))
            output.insert('end',' Pound')
        
        elif unit1_get==4 and unit2_get==4:
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end',' mg')

        elif unit1_get==4 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get/10
            output.insert('end',round(value,2))
            output.insert('end',' cg')

        elif unit1_get==4 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get/100
            output.insert('end',round(value,2))
            output.insert('end',' dg')

        elif unit1_get==4 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get/100000
            output.insert('end',round(value,2))
            output.insert('end',' hg')
     #centigram to all other units   
        elif unit1_get==5 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get/100000
            output.insert('end',round(value,2))
            output.insert('end',' Kg')
        
        elif unit1_get==5 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get/100
            output.insert('end',round(value,2))
            output.insert('end',' g')
        
        elif unit1_get==5 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get/45360
            output.insert('end',input_get)
            output.insert('end',' Pound')

        elif unit1_get==5 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*10
            output.insert('end',round(value,2))
            output.insert('end','mg')

        elif unit1_get==5 and unit2_get==5:
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','cg')

        elif unit1_get==5 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get/10
            output.insert('end',round(value,2))
            output.insert('end','dg')

        elif unit1_get==5 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get/10000
            output.insert('end',round(value,2))
            output.insert('end','hg')
      #decigram to all other units
        elif unit1_get==6 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get/10000
            output.insert('end',round(value,2))
            output.insert('end',' Kg')
        
        elif unit1_get==6 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get/10
            output.insert('end',input_get)
            output.insert('end',' g')
            
        elif unit1_get==6 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get/4536
            output.insert('end',round(value,2))
            output.insert('end',' Pound')
        
        elif unit1_get==6 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*100
            output.insert('end',round(value,2))
            output.insert('end',' mg')

        elif unit1_get==6 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*10
            output.insert('end',round(value,2))
            output.insert('end',' cg')

        elif unit1_get==6 and unit2_get==6:
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end',' dg')

        elif unit1_get==6 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get/1000
            output.insert('end',round(value,2))
            output.insert('end',' hg')
     #hectogram to all other units   
        elif unit1_get==7 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get/10
            output.insert('end',round(value,2))
            output.insert('end',' Kg')
        
        elif unit1_get==7 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*100
            output.insert('end',round(value,2))
            output.insert('end',' g')
        
        elif unit1_get==7 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get/4.536
            output.insert('end',input_get)
            output.insert('end',' Pound')

        elif unit1_get==7 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*100000
            output.insert('end',round(value,2))
            output.insert('end','mg')

        elif unit1_get==7 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*10000
            output.insert('end',round(value,2))
            output.insert('end','cg')

        elif unit1_get==7 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*1000
            output.insert('end',round(value,2))
            output.insert('end','dg')

        elif unit1_get==7 and unit2_get==7:
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','hg')

    #create gui
    root = Tk()
    root.title('Weight Converter')
    root.geometry('400x300')
    root.resizable(0,0)
    
    root.configure(bg='#FFFFAE')

    Label(root,text='Weight Converter', width = '500',
        height = '2',font = ('Helvetica', 13, 'bold')).pack()
    Label(root,text='Enter value To Convert:',
        bg = '#FFFFAE',font = ('Helvetica', 13,)).place(x= 110,y=55)
    Button(root,text='Convert',width=15,command=convert,bg='light green').place(x=164,y=180)
    exit_button=Button(root,text="Exit",command=root.destroy).place(x=350,y=220)
    input_value= DoubleVar(root)
    Entry(root,textvariable= input_value ,width = 30).place(x= 110,y=85)
    Label(root,text='From :',bg = '#FFFFAE').place(x= 110,y=115)
    Label(root,text='  To :',bg = '#FFFFAE').place(x= 110,y=145)

    unit_list = [
        'Kilogram (kg)','Gram (g)','Pound (Ib)','Milligram(mg)','Centigram(cg)','Decigram(dg)','Hectogram(hg)'
    ] 

    unit1 = ttk.Combobox(root,values=unit_list)
    unit1.set('Kilogram (kg)')
    unit1.place(x=150,y= 115)


    unit2 = ttk.Combobox(root,values=unit_list)
    unit2.set('Gram (g)')
    unit2.place(x=150,y= 145)
    Button(root,text='Convert',width=15,command=convert).place(x=164,y=180)
    

    output = Text(root,width=25,height=2,)
    output.place(x=110,y=218)
    Label(root,text = 'STANDARD UNIT CONVERTER',bg = '#FFFFAE',).place(x = 128, y =270 )
    
    
    root.mainloop()
#length converter
def length_converter():
    def convert():
        input_get=input_value.get()
        unit1_get= unit1.get()
        unit2_get= unit2.get()
        if unit1_get =='Kilometre (km)':
            unit1_get = 1  
        elif unit1_get=='Metre (m)':
            unit1_get = 2  
        elif unit1_get== 'Centimeter (Cm)':
            unit1_get = 3
        elif unit1_get== 'Inch (In)':
            unit1_get = 4    
        elif unit1_get== 'Millimeter (mm)':
            unit1_get = 5
        elif unit1_get== 'Micrometer (um)':
            unit1_get = 6
        elif unit1_get== 'feet (ft)':
            unit1_get = 7
        elif unit1_get== 'yard (yd)':
            unit1_get = 8
        elif unit1_get== 'mile ':
            unit1_get = 9
        elif unit1_get== 'nautical mile (n mile)':
            unit1_get = 10
            
        
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%unit1_get)


        if unit2_get =='Kilometre (km)':
            unit2_get = 1
        elif unit2_get=='Metre (m)':
            unit2_get =2
        elif unit2_get== 'Centimeter (Cm)':
            unit2_get = 3
        elif unit2_get== 'Inch (In)':
            unit2_get = 4
        elif unit2_get== 'Millimeter (mm)':
            unit2_get = 5
        elif unit2_get== 'Micrometer (um)':
            unit2_get = 6
        elif unit2_get== 'feet (ft)':
            unit1_get = 7
        elif unit2_get== 'yard (yd)':
            unit2_get = 8
        elif unit2_get== 'mile ':
            unit2_get = 9
        elif unit2_get== 'nautical mile (n mile)':
            unit2_get = 10
            
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%unit2_get)

    
        if unit1_get==1 and unit2_get==1:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Km')
        elif unit1_get==1 and unit2_get==2:
            value= input_get*1000
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end',' m')
        elif unit1_get==1 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*100000
            output.insert('end',round(value,2))
            output.insert('end',' Cm')
        elif unit1_get==1 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*39370
            output.insert('end',round(value,2))
            output.insert('end',' Inch')
        elif unit1_get==1 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*1000000000
            output.insert('end',round(value,2))
            output.insert('end',' micrometer')
        elif unit1_get==1 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*1000000
            output.insert('end',round(value,2))
            output.insert('end',' millimeter')
        elif unit1_get==1 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*3280.839895
            output.insert('end',round(value,2))
            output.insert('end',' feet')
        elif unit1_get==1 and unit2_get==8:
            output.delete(1.0,END)
            value= input_get*1093.6132983
            output.insert('end',round(value,2))
            output.insert('end',' yard')
        elif unit1_get==1 and unit2_get==9:
            output.delete(1.0,END)
            value= input_get*0.6213711922
            output.insert('end',round(value,2))
            output.insert('end','mile')
        elif unit1_get==1 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get*0.5399568035
            output.insert('end',round(value,2))
            output.insert('end',' nautical mile')
        

        elif unit1_get==2 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get/1000
            output.insert('end',round(value,2))
            output.insert('end',' Km')
        elif unit1_get==2 and unit2_get==2:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' m')
        elif unit1_get==2 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*100
            output.insert('end',round(value,2))
            output.insert('end',' Cm')
        elif unit1_get==2 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*39.37
            output.insert('end',round(value,2))
            output.insert('end',' Inch')
        elif unit1_get==2 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*1000000
            output.insert('end',round(value,2))
            output.insert('end',' micrometer')
        elif unit1_get==2 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*1000
            output.insert('end',round(value,2))
            output.insert('end',' millimeter')
        elif unit1_get==2 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*3.280839895
            output.insert('end',round(value,2))
            output.insert('end',' feet')
        elif unit1_get==2 and unit2_get==8:
            output.delete(1.0,END)
            value= input_get*1.0936132983
            output.insert('end',round(value,2))
            output.insert('end',' yard')
        elif unit1_get==2 and unit2_get==9:
            output.delete(1.0,END)
            value= input_get*0.0006213711922
            output.insert('end',round(value,2))
            output.insert('end','mile')
        elif unit1_get==2 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get*0.0005399568035
            output.insert('end',round(value,2))
            output.insert('end',' nautical mile')
        

        if unit1_get==3 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get/100000
            output.insert('end',round(value,2))
            output.insert('end',' Km')
        elif unit1_get==3 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get/100
            output.insert('end',round(value,2))
            output.insert('end',' m')
        elif unit1_get==3 and unit2_get==3:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Cm')
        elif unit1_get==3 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get/2.54
            output.insert('end',round(value,2))
            output.insert('end',' Inch')
        elif unit1_get==3 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*10000
            output.insert('end',round(value,2))
            output.insert('end',' micrometer')
        elif unit1_get==3 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*10
            output.insert('end',round(value,2))
            output.insert('end',' millimeter')
        elif unit1_get==3 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*0.03280839895
            output.insert('end',round(value,2))
            output.insert('end',' feet')
        elif unit1_get==3 and unit2_get==8:
            output.delete(1.0,END)
            value= input_get*0.010936132983
            output.insert('end',round(value,2))
            output.insert('end',' yard')
        elif unit1_get==3 and unit2_get==9:
            output.delete(1.0,END)
            value= input_get*0.000006213711922
            output.insert('end',round(value,2))
            output.insert('end','mile')
        elif unit1_get==3 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get*0.000005399568035
            output.insert('end',round(value,2))
            output.insert('end',' nautical mile')
        
        
        elif unit1_get==4 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*39370
            output.insert('end',round(value,2))
            output.insert('end',' Km')
        elif unit1_get==4 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get/39.37
            output.insert('end',round(value,2))
            output.insert('end',' m')
        elif unit1_get==4 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*2.54
            output.insert('end',round(value,2))
            output.insert('end',' Cm')
        elif unit1_get==4 and unit2_get==4:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Inch')
        elif unit1_get==4 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*25400
            output.insert('end',round(value,2))
            output.insert('end',' micrometer')
        elif unit1_get==4 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*25.4
            output.insert('end',round(value,2))
            output.insert('end',' millimeter')
        elif unit1_get==4 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*0.08333333333
            output.insert('end',round(value,2))
            output.insert('end',' feet')
        elif unit1_get==4 and unit2_get==8:
            output.delete(1.0,END)
            value= input_get*0.027777777778
            output.insert('end',round(value,2))
            output.insert('end',' yard')
        elif unit1_get==4 and unit2_get==9:
            output.delete(1.0,END)
            value= input_get*0.0000157828
            output.insert('end',round(value,2))
            output.insert('end','mile')
        elif unit1_get==4 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get*0.0000137149
            output.insert('end',round(value,2))
            output.insert('end',' nautical mile')
        
        elif unit1_get==5 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*(1E-9)
            output.insert('end',round(value,2))
            output.insert('end',' Km')
        elif unit1_get==5 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*0.000001
            output.insert('end',round(value,2))
            output.insert('end',' m')
        elif unit1_get==5 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*0.0001
            output.insert('end',round(value,2))
            output.insert('end',' Cm')
        elif unit1_get==5 and unit2_get==4:
            output.delete(1.0,END)
            value=input_get*0.0000393701
            output.insert('end',input_get)
            output.insert('end',' Inch')
        elif unit1_get==4 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*1
            output.insert('end',round(value,2))
            output.insert('end',' micrometer')
        elif unit1_get==5 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*0.001
            output.insert('end',round(value,2))
            output.insert('end',' millimeter')
        elif unit1_get==5 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*0.00000032808
            output.insert('end',round(value,2))
            output.insert('end',' feet')
        elif unit1_get==5 and unit2_get==8:
            output.delete(1.0,END)
            value= input_get*0.0000010936
            output.insert('end',round(value,2))
            output.insert('end',' yard')
        elif unit1_get==5 and unit2_get==9:
            output.delete(1.0,END)
            value= input_get*(6.213711922E-10)
            output.insert('end',round(value,2))
            output.insert('end','mile')
        elif unit1_get==5 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get*(5.399568034E-10)
            output.insert('end',round(value,2))
            output.insert('end',' nautical mile')

        elif unit1_get==6 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*0.000001
            output.insert('end',round(value,2))
            output.insert('end',' Km')
        elif unit1_get==6 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*0.001
            output.insert('end',round(value,2))
            output.insert('end',' m')
        elif unit1_get==6 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*0.1
            output.insert('end',round(value,2))
            output.insert('end',' Cm')
        elif unit1_get==6 and unit2_get==4:
            output.delete(1.0,END)
            value=input_get*0.03933700787
            output.insert('end',input_get)
            output.insert('end',' Inch')
        elif unit1_get==6 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*1000
            output.insert('end',round(value,2))
            output.insert('end',' micrometer')
        elif unit1_get==6 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*1
            output.insert('end',round(value,2))
            output.insert('end',' millimeter')
        elif unit1_get==6 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*0.0032808399
            output.insert('end',round(value,2))
            output.insert('end',' feet')
        elif unit1_get==6 and unit2_get==8:
            output.delete(1.0,END)
            value= input_get*0.0010936133
            output.insert('end',round(value,2))
            output.insert('end',' yard')
        elif unit1_get==6 and unit2_get==9:
            output.delete(1.0,END)
            value= input_get*(6.213711922E-7)
            output.insert('end',round(value,2))
            output.insert('end','mile')
        elif unit1_get==6 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get*(50399568034E-7)
            output.insert('end',round(value,2))
            output.insert('end',' nautical mile')

        elif unit1_get==7 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*0.0003048
            output.insert('end',round(value,2))
            output.insert('end',' Km')
        elif unit1_get==7 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*0.3048
            output.insert('end',round(value,2))
            output.insert('end',' m')
        elif unit1_get==7 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*30.48
            output.insert('end',round(value,2))
            output.insert('end',' Cm')
        elif unit1_get==7 and unit2_get==4:
            output.delete(1.0,END)
            valur=input_get*12
            output.insert('end',input_get)
            output.insert('end',' Inch')
        elif unit1_get==7 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*304800
            output.insert('end',round(value,2))
            output.insert('end',' micrometer')
        elif unit1_get==7 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*304.8
            output.insert('end',round(value,2))
            output.insert('end',' millimeter')
        elif unit1_get==7 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*1
            output.insert('end',round(value,2))
            output.insert('end',' feet')
        elif unit1_get==7 and unit2_get==8:
            output.delete(1.0,END)
            value= input_get*0.3333333333
            output.insert('end',round(value,2))
            output.insert('end',' yard')
        elif unit1_get==7 and unit2_get==9:
            output.delete(1.0,END)
            value= input_get*0.0001893939
            output.insert('end',round(value,2))
            output.insert('end','mile')
        elif unit1_get==7 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get*0.0001645788
            output.insert('end',round(value,2))
            output.insert('end',' nautical mile')

        elif unit1_get==8 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*0.0009144
            output.insert('end',round(value,2))
            output.insert('end',' Km')
        elif unit1_get==8 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*0.9144
            output.insert('end',round(value,2))
            output.insert('end',' m')
        elif unit1_get==8 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*91.44
            output.insert('end',round(value,2))
            output.insert('end',' Cm')
        elif unit1_get==8 and unit2_get==4:
            output.delete(1.0,END)
            value=input_get*36
            output.insert('end',input_get)
            output.insert('end',' Inch')
        elif unit1_get==8 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*914400
            output.insert('end',round(value,2))
            output.insert('end',' micrometer')
        elif unit1_get==4 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*914.4
            output.insert('end',round(value,2))
            output.insert('end',' millimeter')
        elif unit1_get==8 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*3
            output.insert('end',round(value,2))
            output.insert('end',' feet')
        elif unit1_get==8 and unit2_get==8:
            output.delete(1.0,END)
            value= input_get*1
            output.insert('end',round(value,2))
            output.insert('end',' yard')
        elif unit1_get==8 and unit2_get==9:
            output.delete(1.0,END)
            value= input_get*0.0005681818
            output.insert('end',round(value,2))
            output.insert('end','mile')
        elif unit1_get==8 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get*0.0004937365
            output.insert('end',round(value,2))
            output.insert('end',' nautical mile')
        
        elif unit1_get==9 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*1.609344
            output.insert('end',round(value,2))
            output.insert('end',' Km')
        elif unit1_get==9 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*1609.344
            output.insert('end',round(value,2))
            output.insert('end',' m')
        elif unit1_get==9 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*160934.4
            output.insert('end',round(value,2))
            output.insert('end',' Cm')
        elif unit1_get==9 and unit2_get==4:
            output.delete(1.0,END)
            value=input_get*63360
            output.insert('end',input_get)
            output.insert('end',' Inch')
        elif unit1_get==9 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*1609344000
            output.insert('end',round(value,2))
            output.insert('end',' micrometer')
        elif unit1_get==9 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*1609344
            output.insert('end',round(value,2))
            output.insert('end',' millimeter')
        elif unit1_get==9 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*5280
            output.insert('end',round(value,2))
            output.insert('end',' feet')
        elif unit1_get==9 and unit2_get==8:
            output.delete(1.0,END)
            value= input_get*1760
            output.insert('end',round(value,2))
            output.insert('end',' yard')
        elif unit1_get==9 and unit2_get==9:
            output.delete(1.0,END)
            value= input_get*1
            output.insert('end',round(value,2))
            output.insert('end','mile')
        elif unit1_get==9 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get*0.8689762419
            output.insert('end',round(value,2))
            output.insert('end',' nautical mile')

        elif unit1_get==10 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*1.852
            output.insert('end',round(value,2))
            output.insert('end',' Km')
        elif unit1_get==10 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*1852
            output.insert('end',round(value,2))
            output.insert('end',' m')
        elif unit1_get==10 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*185200
            output.insert('end',round(value,2))
            output.insert('end',' Cm')
        elif unit1_get==10 and unit2_get==4:
            output.delete(1.0,END)
            value=input_get*72913.385827
            output.insert('end',input_get)
            output.insert('end',' Inch')
        elif unit1_get==10 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*1852000000
            output.insert('end',round(value,2))
            output.insert('end',' micrometer')
        elif unit1_get==10 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*1852000
            output.insert('end',round(value,2))
            output.insert('end',' millimeter')
        elif unit1_get==10 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*6076.1154856
            output.insert('end',round(value,2))
            output.insert('end',' feet')
        elif unit1_get==10 and unit2_get==8:
            output.delete(1.0,END)
            value= input_get*2025.3718285
            output.insert('end',round(value,2))
            output.insert('end',' yard')
        elif unit1_get==10 and unit2_get==9:
            output.delete(1.0,END)
            value= input_get*1.150779448
            output.insert('end',round(value,2))
            output.insert('end','mile')
        elif unit1_get==10 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get*1
            output.insert('end',round(value,2))
            output.insert('end',' nautical mile')
        
#create gui
    root = Tk()
    root.title('Length Converter')
    root.geometry('400x300')
    root.resizable(0,0)
    
    root.configure(bg='#7A7AC5')

    Label(root,text='Length Converter', width = '500',
        height = '2',font = ('Helvetica', 13, 'bold')).pack()
    Label(root,text='Enter value To Convert:',
        bg = '#7A7AC5',font = ('Helvetica', 13,)).place(x= 110,y=55)
    
    input_value= DoubleVar(root)
    Entry(root,textvariable= input_value ,width = 30).place(x= 110,y=85)
    Label(root,text='From :',bg = '#7A7AC5').place(x= 110,y=115)
    Label(root,text='  To :',bg = '#7A7AC5').place(x= 110,y=145)

    unit_list = [
        'Kilometre (km)','Metre (m)','Centimeter (Cm)','Inch (In)','Millimeter (mm)','Micrometer (um)','feet (ft)', 'yard (yd)','mile ','nautical mile (n mile)'
    

    ] 

    unit1 = ttk.Combobox(root,values=unit_list)
    unit1.set('Kilometre (km)')
    unit1.place(x=150,y= 115)


    unit2 = ttk.Combobox(root,values=unit_list)
    unit2.set('Metre (m)')
    unit2.place(x=150,y= 145)
    Button(root,text='Convert',width=15,command=convert,bg='light green').place(x=164,y=180)
    exit_button=Button(root,text="Exit",command=root.destroy).place(x=350,y=220)

    output = Text(root,width=25,height=2,)
    output.place(x=110,y=218)
    Label(root,text = 'STANDARD UNIT CONVERTER',bg = '#7A7AC5',).place(x = 128, y =270 )
    
    
    root.mainloop()

def Area_converter():
    def convert():
        input_get=input_value.get()
        unit1_get= unit1.get()
        unit2_get= unit2.get()
        if unit1_get =='Square kilometer (km^2)':
            unit1_get = 1
        elif unit1_get=='Square meter (m^2)':
            unit1_get = 2
        elif unit1_get=='Square centimeter (cm^2)':
            unit1_get = 3
        elif unit1_get=='Square millimeter(mm^2)':
            unit1_get = 4
        elif unit1_get== 'Hectare(ha)':
            unit1_get = 5
        elif unit1_get=='Acre(ac)':
            unit1_get = 6
        elif unit1_get== 'Square mile(mi^2)':
            unit1_get = 7
        elif unit1_get== 'Square yard(yd^2)':
            unit1_get = 8
        elif unit1_get=='Square feet(ft^2)':
            unit1_get = 9
        elif unit1_get== 'Square inch(in^2)':
            unit1_get = 10   
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%unit1_get)


        if unit2_get =='Square kilometer (km^2)':
            unit2_get = 1
        elif unit2_get=='Square meter (m^2)':
            unit2_get = 2
        elif unit2_get=='Square centimeter (cm^2)':
            unit2_get = 3
        elif unit2_get=='Square millimeter(mm^2)':
            unit2_get = 4
        elif unit2_get== 'Hectare(ha)':
            unit2_get = 5
        elif unit2_get=='Acre(ac)':
            unit2_get = 6
        elif unit2_get== 'Square mile(mi^2)':
            unit2_get = 7
        elif unit2_get== 'Square yard(yd^2)':
            unit2_get = 8
        elif unit2_get=='Square feet(ft^2)':
            unit2_get = 9
        elif unit2_get== 'Square inch(in^2)':
            unit2_get = 10      
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%unit2_get)

    
        if unit1_get==1 and unit2_get==1:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end','km^2')
            
        elif unit1_get==1 and unit2_get==2:
            value= input_get*1000000
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end',' m^2')
       
        elif unit1_get==1 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*10000000000
            output.insert('end',round(value,2))
            output.insert('end','cm^2')

        elif unit1_get==1 and unit2_get==4:
            value= input_get*1000000000000
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','mm^2')

        elif unit1_get==1 and unit2_get==5:
            value= input_get*100
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','ha')
        elif unit1_get==1 and unit2_get==6:
            value= input_get*247.10538147
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','ac')
        elif unit1_get==1 and unit2_get==7:
            value= input_get*0.3861021585
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','mi^2')
        elif unit1_get==1 and unit2_get==8:
            value= input_get*1195990.0463
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','yd^2')
        elif unit1_get==1 and unit2_get==9:
            value= input_get*1195990.0463
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','ft^2')
        elif unit1_get==1 and unit2_get==10:
            value= input_get*1550003100
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','in^2')
        
#square meter to all other units
        if unit1_get==2 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get/1000000
            output.insert('end',round(value,2))
            output.insert('end','km^2 ')
        
        elif unit1_get==2 and unit2_get==2:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end','m^2')
            
        elif unit1_get==2 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*10000
            output.insert('end',round(value,2))
            output.insert('end','cm^2')
        
        elif unit1_get==2 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*1000000
            output.insert('end',round(value,2))
            output.insert('end','mm^2')

        elif unit1_get==2 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*0.0001
            output.insert('end',round(value,2))
            output.insert('end',' ha')

        elif unit1_get==2 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*0.0002471054
            output.insert('end',round(value,2))
            output.insert('end',' ac')

        elif unit1_get==2 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*3.861021585E-7
            output.insert('end',round(value,2))
            output.insert('end','mi^2')
        elif unit1_get==2 and unit2_get==8:
            output.delete(1.0,END)
            value= input_get*1.1959900463
            output.insert('end',round(value,2))
            output.insert('end','yd^2')
        elif unit1_get==2 and unit2_get==9:
            output.delete(1.0,END)
            value= input_get*10.763910417
            output.insert('end',round(value,2))
            output.insert('end','ft^2')
        elif unit1_get==2 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get*1550.0031
            output.insert('end',round(value,2))
            output.insert('end','in^2')

        #square centimeter to all other units
        if unit1_get==3 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*1.E-10
            output.insert('end',round(value,2))
            output.insert('end','km^2')
        
        elif unit1_get==3 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*0.0001
            output.insert('end',round(value,2))
            output.insert('end','m^2')
        
        elif unit1_get==3 and unit2_get==3:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end','cm^2')

        elif unit1_get==3 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*100
            output.insert('end',round(value,2))
            output.insert('end','mm^2')

        elif unit1_get==3 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*1.E-8
            output.insert('end',round(value,2))
            output.insert('end','ha')

        elif unit1_get==3 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*2.471053814E-8
            output.insert('end',round(value,2))
            output.insert('end','ac')

        elif unit1_get==3 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*3.861021585E-11
            output.insert('end',round(value,2))
            output.insert('end','mi^2')
        elif unit1_get==3 and unit2_get==8:
            output.delete(1.0,END)
            value= input_get*0.000119599
            output.insert('end',round(value,2))
            output.insert('end','yd^2')
        elif unit1_get==3 and unit2_get==9:
            output.delete(1.0,END)
            value= input_get*0.001076391
            output.insert('end',round(value,2))
            output.insert('end','ft^2')
        elif unit1_get==3 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get*0.15500031
            output.insert('end',round(value,2))
            output.insert('end','in^2')
       
        # square millimeter to all other units
        if unit1_get==4 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*1.E-12
            output.insert('end',round(value,2))
            output.insert('end','km^2')
        
        elif unit1_get==4 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*0.000001
            output.insert('end',input_get)
            output.insert('end','m^2')
            
        elif unit1_get==4 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*0.01
            output.insert('end',round(value,2))
            output.insert('end','cm^2')
        
        elif unit1_get==4 and unit2_get==4:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end','mm^2')

        elif unit1_get==4 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*1.E-10
            output.insert('end',round(value,2))
            output.insert('end','ha')

        elif unit1_get==4 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*2.471053814E-10
            output.insert('end',round(value,2))
            output.insert('end','ac')

        elif unit1_get==4 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*3.861021585E-13
            output.insert('end',round(value,2))
            output.insert('end','mi^2')
        elif unit1_get==4 and unit2_get==8:
            output.delete(1.0,END)
            value= input_get*0.000001196
            output.insert('end',round(value,2))
            output.insert('end','yd^2')
        elif unit1_get==4 and unit2_get==9:
            output.delete(1.0,END)
            value= input_get*0.0000107639
            output.insert('end',round(value,2))
            output.insert('end','ft^2')
        elif unit1_get==4 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get*0.0015500031
            output.insert('end',round(value,2))
            output.insert('end','in^2')

     # Hactare to all other units   
        if unit1_get==5 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*0.01
            output.insert('end',round(value,2))
            output.insert('end','km^2')
        
        elif unit1_get==5 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*10000
            output.insert('end',round(value,2))
            output.insert('end','m^2')
        
        elif unit1_get==5 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*100000000
            output.insert('end',input_get)
            output.insert('end','cm^2')

        elif unit1_get==5 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*10000000000
            output.insert('end',round(value,2))
            output.insert('end','mm^2')

        elif unit1_get==5 and unit2_get==5:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end','ha')

        elif unit1_get==5 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*2.471
            output.insert('end',round(value,2))
            output.insert('end','ac')

        elif unit1_get==5 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*0.0038610216
            output.insert('end',round(value,2))
            output.insert('end','mi^2')
        elif unit1_get==5 and unit2_get==8:
            output.delete(1.0,END)
            value= input_get*11959.900463
            output.insert('end',round(value,2))
            output.insert('end','yd^2')
        elif unit1_get==5 and unit2_get==9:
            output.delete(1.0,END)
            value= input_get*107639.10417
            output.insert('end',round(value,2))
            output.insert('end','ft^2')
        elif unit1_get==5 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get*15500031
            output.insert('end',round(value,2))
            output.insert('end','in^2')

      #Acre  to all other units
        if unit1_get==6 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*100
            output.insert('end',round(value,2))
            output.insert('end','km^2')
        
        elif unit1_get==6 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get/10000
            output.insert('end',round(value,2))
            output.insert('end','m^2')
            
        elif unit1_get==6 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*1000000
            output.insert('end',round(value,2))
            output.insert('end','cm^2')
        
        elif unit1_get==6 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*100000000
            output.insert('end',round(value,2))
            output.insert('end','mm^2')

        elif unit1_get==6 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*0.01
            output.insert('end',round(value,2))
            output.insert('end','ha')

        elif unit1_get==6 and unit2_get==6:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end','ac')

        elif unit1_get==6 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*0.0000386102
            output.insert('end',round(value,2))
            output.insert('end','mi^2')
        elif unit1_get==6 and unit2_get==8:
            output.delete(1.0,END)
            value= input_get*119.59900463
            output.insert('end',round(value,2))
            output.insert('end','yd^2')
        elif unit1_get==6 and unit2_get==9:
            output.delete(1.0,END)
            value= input_get*1076.3910417
            output.insert('end',round(value,2))
            output.insert('end','ft^2')
        elif unit1_get==6 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get*155000.31 
            output.insert('end',round(value,2))
            output.insert('end','in^2')
     # square mile  to all other units   
        if unit1_get==7 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*2.589
            output.insert('end',round(value,2))
            output.insert('end','km^2')
        
        elif unit1_get==7 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*2589988.1103
            output.insert('end',round(value,2))
            output.insert('end','m^2')
        
        elif unit1_get==7 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*25899881103
            output.insert('end',round(value,2))
            output.insert('end','cm^2')

        elif unit1_get==7 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*2589988110336
            output.insert('end',round(value,2))
            output.insert('end','mm^2')

        elif unit1_get==7 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*258.99881103
            output.insert('end',round(value,2))
            output.insert('end','ha')

        elif unit1_get==7 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*640
            output.insert('end',round(value,2))
            output.insert('end','ac')

        elif unit1_get==7 and unit2_get==7:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end','mi^2')
        elif unit1_get==7 and unit2_get==8:
            output.delete(1.0,END)
            value= input_get*3097600
            output.insert('end',round(value,2))
            output.insert('end','yd^2')
        elif unit1_get==7 and unit2_get==9:
            output.delete(1.0,END)
            value= input_get*27878400
            output.insert('end',round(value,2))
            output.insert('end','ft^2')
        elif unit1_get==7 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get*4014489600
            output.insert('end',round(value,2))
            output.insert('end','in^2')
         #square yard to other units
         
        if unit1_get==8 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*8.361273599E-7
            output.insert('end',round(value,2))
            output.insert('end','km^2')
        
        elif unit1_get==8 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*0.83612736
            output.insert('end',round(value,2))
            output.insert('end','m^2')
        
        elif unit1_get==8 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*8361.2736 
            output.insert('end',round(value,2))
            output.insert('end','cm^2')

        elif unit1_get==8 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*836127.36
            output.insert('end',round(value,2))
            output.insert('end','mm^2')

        elif unit1_get==8 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*0.0000836127
            output.insert('end',round(value,2))
            output.insert('end','ha')

        elif unit1_get==8 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*0.0002066116
            output.insert('end',round(value,2))
            output.insert('end','ac')

        elif unit1_get==8 and unit2_get==7:
            output.delete(1.0,END)
            value=input_get*3.228305785E-7
            output.insert('end',round(value,2))
            output.insert('end','mi^2')
        elif unit1_get==8 and unit2_get==8:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end','yd^2')
        elif unit1_get==8 and unit2_get==9:
            output.delete(1.0,END)
            value= input_get*9
            output.insert('end',round(value,2))
            output.insert('end','ft^2')
        elif unit1_get==8 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get*1296 
            output.insert('end',round(value,2))
            output.insert('end','in^2') 
            
    # Square feet to all the units
    
        if unit1_get==9 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*9.290303999E-8
            output.insert('end',round(value,2))
            output.insert('end','km^2')
        
        elif unit1_get==9 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*0.09290304
            output.insert('end',round(value,2))
            output.insert('end','m^2')
        
        elif unit1_get==9 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*929.0304
            output.insert('end',round(value,2))
            output.insert('end','cm^2')

        elif unit1_get==9 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*92903.04
            output.insert('end',round(value,2))
            output.insert('end','mm^2')

        elif unit1_get==9 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*0.0000092903
            output.insert('end',round(value,2))
            output.insert('end','ha')

        elif unit1_get==9 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*0.0000229568
            output.insert('end',round(value,2))
            output.insert('end','ac')

        elif unit1_get==9 and unit2_get==7:
            output.delete(1.0,END)
            value=input_get*3.587006427E-8
            output.insert('end',round(value,2))
            output.insert('end','mi^2')
        elif unit1_get==9 and unit2_get==8:
            output.delete(1.0,END)
            value=input_get*0.1111111111
            output.insert('end',round(value,2))
            output.insert('end','yd^2')
        elif unit1_get==9 and unit2_get==9:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end','ft^2')
        elif unit1_get==9 and unit2_get==10:
            output.delete(1.0,END)
            value= input_get* 144
            output.insert('end',round(value,2))
            output.insert('end','in^2') 
     #Square inch in other units
        if unit1_get==10 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*6.4516E-10
            output.insert('end',round(value,2))
            output.insert('end','km^2')
        
        elif unit1_get==10 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*0.00064516
            output.insert('end',round(value,2))
            output.insert('end','m^2')
        
        elif unit1_get==10 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*6.4516
            output.insert('end',round(value,2))
            output.insert('end','cm^2')

        elif unit1_get==10 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*645.16
            output.insert('end',round(value,2))
            output.insert('end','mm^2')

        elif unit1_get==10 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*6.4516E-8
            output.insert('end',round(value,2))
            output.insert('end','ha')

        elif unit1_get==10 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*1.594225079E-7
            output.insert('end',round(value,2))
            output.insert('end','ac')

        elif unit1_get==10 and unit2_get==7:
            output.delete(1.0,END)
            value=input_get*2.490976686E-10
            output.insert('end',round(value,2))
            output.insert('end','mi^2')
        elif unit1_get==10 and unit2_get==8:
            output.delete(1.0,END)
            value=input_get*0.0007716049
            output.insert('end',round(value,2))
            output.insert('end','yd^2')
        elif unit1_get==10 and unit2_get==9:
            output.delete(1.0,END)
            value=input_get*0.0069444444
            output.insert('end',round(value,2))
            output.insert('end','ft^2')
        elif unit1_get==10 and unit2_get==10:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end','in^2') 
    
    #create gui
    root = Tk()
    root.title('Area Converter')
    root.geometry('400x300')
    root.resizable(0,0)
    
    root.configure(bg='#FFFFAE')

    Label(root,text='Area Converter', width = '500',
        height = '2',font = ('Helvetica', 13, 'bold')).pack()
    Label(root,text='Enter value To Convert:',
        bg = '#FFFFAE',font = ('Helvetica', 13,)).place(x= 110,y=55)
    Button(root,text='Convert',width=15,command=convert,bg='#FFFFAE').place(x=164,y=180)
    exit_button=Button(root,text="Exit",command=root.destroy).place(x=350,y=220)


    input_value= DoubleVar(root)
    Entry(root,textvariable= input_value ,width = 30).place(x= 110,y=85)
    Label(root,text='From :',bg = '#FFFFAE').place(x= 110,y=115)
    Label(root,text='  To :',bg = '#FFFFAE').place(x= 110,y=145)

    unit_list = [
        'Square kilometer (km^2)','Square meter (m^2)','Square centimeter (cm^2)','Square millimeter(mm^2)','Hectare(ha)','Acre(ac)','Square mile(mi^2)','Square yard(yd^2)','Square feet(ft^2)','Square inch(in^2)'
    ] 

    unit1 = ttk.Combobox(root,values=unit_list)
    unit1.set('Square kilometer (km^2)')
    unit1.place(x=150,y= 115)


    unit2 = ttk.Combobox(root,values=unit_list)
    unit2.set('Square meter (m^2)')
    unit2.place(x=150,y= 145)
    Button(root,text='Convert',width=15,command=convert).place(x=164,y=180)

    output = Text(root,width=25,height=2,)
    output.place(x=110,y=218)
    Label(root,text = 'STANDARD UNIT CONVERTER',bg = '#FFFFAE',).place(x = 128, y =270 )
    root.mainloop()

#Time converter
def time_convert():
    def convert():
        input_get=input_value.get()
        unit1_get= unit1.get()
        unit2_get= unit2.get()
        if unit1_get =='Celsius (°C)':
            unit1_get = 1
        elif unit1_get=='Fahrenheit (°F)':
            unit1_get = 2
        elif unit1_get== 'Kelvin (°K)':
            unit1_get = 3
        
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%unit1_get)


        if unit2_get =='Celsius (°C)':
            unit2_get = 1
        elif unit2_get=='Fahrenheit (°F)':
            unit2_get = 2
        elif unit2_get== 'Kelvin (°K)':
            unit2_get = 3
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%unit2_get)
        
        if unit1_get==1 and unit2_get==1:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' °C')
        elif unit1_get==1 and unit2_get==2:
            value= (input_get*9/5)+32
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end',' °F')
        elif unit1_get==1 and unit2_get==3:
            output.delete(1.0,END)
            value= (input_get+ 273.15)
            output.insert('end',round(value,2))
            output.insert('end',' °K')
        
        if unit1_get==2 and unit2_get==1:
            value= (input_get-32)*5/9
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end',' °C')
        elif unit1_get==2 and unit2_get==2:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' °F')
        elif unit1_get==2 and unit2_get==3:
            output.delete(1.0,END)
            value= (input_get-32)*5/9+273.15
            output.insert('end',round(value,2))
            output.insert('end',' °K')
        
        if unit1_get==3 and unit2_get==1:
            value= (input_get-273.15)
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end',' °C')
        elif unit1_get==3 and unit2_get==2:
            value= (input_get - 273.15) * 9/5 + 32
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end',' °F')
        elif unit1_get==3 and unit2_get==3:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' °K')



        #create gui
    root = Tk()
    root.title('Temperature Converter')
    root.geometry('400x300')
    root.resizable(0,0)
    
    root.configure(bg='light yellow')

    Label(root,text='Temperature Converter', width = '500',
        height = '2',font = ('Helvetica', 13, 'bold')).pack()
    Label(root,text='Enter value To Convert:',
        bg = 'light yellow',font = ('Helvetica', 13,)).place(x= 110,y=55)
    
    input_value= DoubleVar(root)
    Entry(root,textvariable= input_value ,width = 30).place(x= 110,y=85)
    Label(root,text='From :',bg = 'light yellow').place(x= 110,y=115)
    Label(root,text='  To :',bg = 'light yellow').place(x= 110,y=145)

    unit_list = [
        'Celsius (°C)','Fahrenheit (°F)','Kelvin (°K)',
    ] 

    unit1 = ttk.Combobox(root,values=unit_list)
    unit1.set('Celsius (°C)')
    unit1.place(x=150,y= 115)


    unit2 = ttk.Combobox(root,values=unit_list)
    unit2.set('Fahrenheit (°F)')
    unit2.place(x=150,y= 145)
    Button(root,text='Convert',width=15,command=convert,bg='light green').place(x=164,y=180)
    exit_button=Button(root,text="Exit",command=root.destroy).place(x=350,y=220)


    output = Text(root,width=25,height=2,)
    output.place(x=110,y=218)
    Label(root,text = 'STANDARD UNIT CONVERTER',bg = 'light yellow',).place(x = 128, y =370 )
    
    
    root.mainloop()


def time_converter():
    
    def convert():
        input_get=input_value.get()
        unit1_get= unit1.get()
        unit2_get= unit2.get()
        if unit1_get =='second':
            unit1_get = 1
        elif unit1_get=='millisecond':
            unit1_get = 2
        elif unit1_get== 'microsecond':
            unit1_get = 3
        elif unit1_get=='nanosecond':
            unit1_get = 4
        elif unit1_get== 'minute':
            unit1_get = 5
        elif unit1_get=='hour':
            unit1_get = 6
        elif unit1_get== 'picosecond':
            unit1_get = 7
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%unit1_get)


        if unit2_get =='second':
            unit2_get = 1
        elif unit2_get=='millisecond':
            unit2_get = 2
        elif unit2_get== 'microsecond':
            unit2_get = 3
        elif unit2_get=='nanosecond':
            unit2_get = 4
        elif unit2_get== 'minute':
            unit2_get = 5
        elif unit2_get=='hour':
            unit2_get = 6
        elif unit2_get== 'picosecond':
            unit2_get = 7
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%unit2_get)

    
        if unit1_get==1 and unit2_get==1:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' sec')
            
        elif unit1_get==1 and unit2_get==2:
            value= input_get*1000
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end',' miilisecond')
       
        elif unit1_get==1 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*1000000
            output.insert('end',round(value,2))
            output.insert('end',' microsecond')

        elif unit1_get==1 and unit2_get==4:
            value= input_get*1000000000
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','nanosecond')

        elif unit1_get==1 and unit2_get==5:
            value= input_get*0.16666667
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','min')
        elif unit1_get==1 and unit2_get==6:
            value= input_get*0.0002777778
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','hr')
        elif unit1_get==1 and unit2_get==7:
            value= input_get*1000000000000
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','ps')
#millisecond to all other units
        elif unit1_get==2 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*0.001
            output.insert('end',round(value,2))
            output.insert('end',' sec')
        
        elif unit1_get==2 and unit2_get==2:
            output.delete(1.0,END)
            value=input_get*1
            output.insert('end',input_get)
            output.insert('end',' millisecond')
            
        elif unit1_get==2 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*1000
            output.insert('end',round(value,2))
            output.insert('end',' microsecond')
        
        elif unit1_get==2 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*1000000
            output.insert('end',round(value,2))
            output.insert('end',' nanosecond')

        elif unit1_get==2 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*0.0000166667
            output.insert('end',round(value,2))
            output.insert('end',' min')

        elif unit1_get==2 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*2.777777777E-7
            output.insert('end',round(value,2))
            output.insert('end',' hr')

        elif unit1_get==2 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*1000000000
            output.insert('end',round(value,2))
            output.insert('end',' ps')
        #microsecond to all other units
        elif unit1_get==3 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*0.000001
            output.insert('end',round(value,2))
            output.insert('end',' sec')
        
        elif unit1_get==3 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*0.001
            output.insert('end',round(value,2))
            output.insert('end','millisecond')
        
        elif unit1_get==3 and unit2_get==3:
            output.delete(1.0,END)
            value=input_get*1
            output.insert('end',input_get)
            output.insert('end',' microsecond')

        elif unit1_get==3 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*1000
            output.insert('end',round(value,2))
            output.insert('end','nanosecond')

        elif unit1_get==3 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*1.66666666666E-8
            output.insert('end',round(value,2))
            output.insert('end','min')

        elif unit1_get==3 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*2.777777777E-10
            output.insert('end',round(value,2))
            output.insert('end','hr')

        elif unit1_get==3 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*1000000
            output.insert('end',round(value,2))
            output.insert('end','ps')
       
        #nanosecond to all other units
        elif unit1_get==4 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*1E-9
            output.insert('end',round(value,2))
            output.insert('end',' sec')
        
        elif unit1_get==4 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*0.000001
            output.insert('end',input_get)
            output.insert('end','millisecond')
            
        elif unit1_get==4 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*0.001
            output.insert('end',round(value,2))
            output.insert('end',' microsecond')
        
        elif unit1_get==4 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*1
            output.insert('end',round(value,2))
            output.insert('end',' nanosecond')

        elif unit1_get==4 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*1.666666666E-11
            output.insert('end',round(value,2))
            output.insert('end',' min')

        elif unit1_get==4 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*2.7777777777E-13
            output.insert('end',round(value,2))
            output.insert('end',' hr')

        elif unit1_get==4 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*1000
            output.insert('end',round(value,2))
            output.insert('end',' ps')
     #hour to all other units   
        elif unit1_get==6 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*3600
            output.insert('end',round(value,2))
            output.insert('end',' sec')
        
        elif unit1_get==6 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*36000000
            output.insert('end',round(value,2))
            output.insert('end','millisecond')
        
        elif unit1_get==6 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*36000000000
            output.insert('end',input_get)
            output.insert('end',' microsecond')

        elif unit1_get==6 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*3600000000000
            output.insert('end',round(value,2))
            output.insert('end','nanosecond')

        elif unit1_get==6 and unit2_get==5:
            output.delete(1.0,END)
            value=input_get*60
            output.insert('end',round(value,2))
            output.insert('end','min')

        elif unit1_get==6 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*1
            output.insert('end',round(value,2))
            output.insert('end','hr')

        elif unit1_get==6 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*3600000000000000
            output.insert('end',round(value,2))
            output.insert('end','ps')
      #picosecond to all other units
        elif unit1_get==7 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*1.E-12
            output.insert('end',round(value,2))
            output.insert('end',' sec')
        
        elif unit1_get==7 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*1.E-9
            output.insert('end',input_get)
            output.insert('end','millisecond')
            
        elif unit1_get==7 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*0.000001
            output.insert('end',round(value,2))
            output.insert('end',' microsecond')
        
        elif unit1_get==7 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*0.001
            output.insert('end',round(value,2))
            output.insert('end',' nanosecond')

        elif unit1_get==7 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*1.6666666666E-14
            output.insert('end',round(value,2))
            output.insert('end',' min')

        elif unit1_get==7 and unit2_get==6:
            output.delete(1.0,END)
            value=input_get*2.7777777777E-16
            output.insert('end',round(value,2))
            output.insert('end',' hr')

        elif unit1_get==7 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*1
            output.insert('end',round(value,2))
            output.insert('end',' ps')
     #minute to all other units   
        elif unit1_get==5 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*60
            output.insert('end',round(value,2))
            output.insert('end',' sec')
        
        elif unit1_get==5 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*60000
            output.insert('end',round(value,2))
            output.insert('end','millisecond')
        
        elif unit1_get==5 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*60000000
            output.insert('end',input_get)
            output.insert('end',' microsecond')

        elif unit1_get==5 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*60000000000
            output.insert('end',round(value,2))
            output.insert('end','nanosecond')

        elif unit1_get==5 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*1
            output.insert('end',round(value,2))
            output.insert('end','min')

        elif unit1_get==5 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*0.166666667
            output.insert('end',round(value,2))
            output.insert('end','hr')

        elif unit1_get==5 and unit2_get==7:
            output.delete(1.0,END)
            value=input_get*60000000000000
            output.insert('end',round(value,2))
            output.insert('end','ps')

    #create gui
    
    root = Tk()
    root.title('Time Converter')
    root.geometry('400x300')
    root.resizable(0,0)
    root.configure(bg='#68999c')
    Label(root,text='Time Converter', width = '500',
        height = '2',font = ('Helvetica', 13, 'bold')).pack()
    Label(root,text='Enter value To Convert:',
        bg = '#68999c',font = ('Helvetica', 13,)).place(x= 110,y=55)
    
    input_value= DoubleVar(root)
    Entry(root,textvariable= input_value ,width = 30).place(x= 110,y=85)
    Label(root,text='Form :',bg = '#68999c').place(x= 110,y=115)
    Label(root,text='  To :',bg = '#68999c').place(x= 110,y=145)

    unit_list = [
        'second','millisecond','microsecond','nanosecond','minute','hour','picosecond'
    ] 

    unit1 = ttk.Combobox(root,values=unit_list)
    unit1.set('second')
    unit1.place(x=150,y= 115)


    unit2 = ttk.Combobox(root,values=unit_list)
    unit2.set('millisecond')
    unit2.place(x=150,y= 145)
    Button(root,text='Convert',width=15,command=convert).place(x=164,y=180)


    output = Text(root,width=25,height=2)
    output.place(x=110,y=218)
    Label(root,text = 'STANDARD UNIT CONVERTER',bg = '#68999c',).place(x = 128, y =270 )
    exit_button=Button(root,text="Exit",command=root.destroy).place(x=350,y=220)

    root.mainloop()


def volume_converter():
    def convert():
        input_get=input_value.get()
        unit1_get= unit1.get()
        unit2_get= unit2.get()
        if unit1_get =='cubic meter':
            unit1_get = 1
            #print(unit1_get)
        elif unit1_get=='cubic kilometer':
            unit1_get = 2
            #print(unit1_get)
        elif unit1_get== 'cubic hectometer':
            unit1_get = 3
            #print(unit1_get)
        elif unit1_get=='cubic decameter':
            unit1_get = 4
            #print(unit1_get)
        
        elif unit1_get=='cubic centimeter':
            unit1_get = 6
            #print(unit1_get)
        elif unit1_get== 'cubic millimeter':
            unit1_get = 7
            #print(unit1_get)
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%unit1_get)


        if unit2_get =='cubic meter':
            unit2_get = 1
            #print(unit2_get)
        elif unit2_get=='cubic kilometer':
            unit2_get = 2
            #print(unit2_get)
        elif unit2_get== 'cubic hectometer':
            unit2_get = 3
            #print(unit2_get)
        elif unit1_get=='cubic decameter':
            unit1_get = 4
            #print(unit1_get)
        
        elif unit1_get=='cubic centimeter':
            unit1_get = 6
            #print(unit1_get)
        elif unit1_get== 'cubic millimeter':
            unit1_get = 7
            #print(unit1_get)
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%unit2_get)

    
        if unit1_get==1 and unit2_get==1:
            value=input_get*1
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end','m³')
            
        elif unit1_get==1 and unit2_get==2:
            value= input_get*(1.E-9)
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end',' km3')
       
        elif unit1_get==1 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*(1.0E-6)
            output.insert('end',round(value,2))
            output.insert('end',' hm3')

        elif unit1_get==1 and unit2_get==4:
            value= input_get/1000
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','dam3')

        elif unit1_get==1 and unit2_get==5:
            value= input_get*1000
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','dm3')

        elif unit1_get==1 and unit2_get==6:
            value= input_get*1000000
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','cm3')
        elif unit1_get==1 and unit2_get==7:
            value= input_get*1.0E9
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','mm3')
#cubic kilomtre to all other units
        elif unit1_get==2 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*1.0E9
            output.insert('end',round(value,2))
            output.insert('end','m3')
        
        elif unit1_get==2 and unit2_get==2:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' km3')
            
        elif unit1_get==2 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*1000
            output.insert('end',round(value,2))
            output.insert('end',' hm3')
        
        elif unit1_get==2 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*1000000
            output.insert('end',round(value,2))
            output.insert('end',' dam3')

        elif unit1_get==2 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*1000000000000
            output.insert('end',round(value,2))
            output.insert('end',' dm3')

        elif unit1_get==2 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*1.0E15
            output.insert('end',round(value,2))
            output.insert('end',' cm3')

        elif unit1_get==2 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*1.0E18
            output.insert('end',round(value,2))
            output.insert('end',' mm3')
        #cubic hectometer to all other units
        elif unit1_get==3 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*1000000
            output.insert('end',round(value,2))
            output.insert('end',' m3')
        
        elif unit1_get==3 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get/1000
            output.insert('end',round(value,2))
            output.insert('end',' km3')
        
        elif unit1_get==3 and unit2_get==3:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' hm3')

        elif unit1_get==3 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*1000
            output.insert('end',round(value,2))
            output.insert('end','dam3')

        elif unit1_get==3 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*1000000000
            output.insert('end',round(value,2))
            output.insert('end','dm3')

        elif unit1_get==3 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*1.0E12
            output.insert('end',round(value,2))
            output.insert('end','cm3')

        elif unit1_get==3 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*1.0E15
            output.insert('end',round(value,2))
            output.insert('end','mm3')
       
        #cubic decametre to all other units
        elif unit1_get==4 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*1000
            output.insert('end',round(value,2))
            output.insert('end',' m3')
        
        elif unit1_get==4 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get/1000000
            output.insert('end',input_get)
            output.insert('end',' km3')
            
        elif unit1_get==4 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get/1000
            output.insert('end',round(value,2))
            output.insert('end',' hm3')
        
        elif unit1_get==4 and unit2_get==4:
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end',' dam3')

        elif unit1_get==4 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get*1000000
            output.insert('end',round(value,2))
            output.insert('end',' dm3')

        elif unit1_get==4 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*1000000000
            output.insert('end',round(value,2))
            output.insert('end','cm3')

        elif unit1_get==4 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*1000000000000
            output.insert('end',round(value,2))
            output.insert('end','mm3')
     #cubic decigram to all other units   
        elif unit1_get==5 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get/1000
            output.insert('end',round(value,2))
            output.insert('end','m3')
        
        elif unit1_get==5 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get/1000000000000
            output.insert('end',round(value,2))
            output.insert('end',' km3')
        
        elif unit1_get==5 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get/1000000000
            output.insert('end',input_get)
            output.insert('end',' hm3')

        elif unit1_get==5 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get/1000000
            output.insert('end',round(value,2))
            output.insert('end','dam3')

        elif unit1_get==5 and unit2_get==5:
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','dm3')

        elif unit1_get==5 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get*1000
            output.insert('end',round(value,2))
            output.insert('end','cm3')

        elif unit1_get==5 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*1000000
            output.insert('end',round(value,2))
            output.insert('end','mm3')
      #cubic centimetre to all other units
        elif unit1_get==6 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get/1000000
            output.insert('end',round(value,2))
            output.insert('end',' m3')
        
        elif unit1_get==6 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*1.0E-15
            output.insert('end',input_get)
            output.insert('end',' km3')
            
        elif unit1_get==6 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*1.0E-12
            output.insert('end',round(value,2))
            output.insert('end',' hm3')
        
        elif unit1_get==6 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*1.0E-9
            output.insert('end',round(value,2))
            output.insert('end',' dam3')

        elif unit1_get==6 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get/1000
            output.insert('end',round(value,2))
            output.insert('end',' dm3')

        elif unit1_get==6 and unit2_get==6:
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end',' cm3')

        elif unit1_get==6 and unit2_get==7:
            output.delete(1.0,END)
            value= input_get*1000
            output.insert('end',round(value,2))
            output.insert('end',' mm3')
    #cubic millimetre to all other units   
        elif unit1_get==7 and unit2_get==1:
            output.delete(1.0,END)
            value= input_get*1.0E-9
            output.insert('end',round(value,2))
            output.insert('end',' m3')
        
        elif unit1_get==7 and unit2_get==2:
            output.delete(1.0,END)
            value= input_get*1.0E-18
            output.insert('end',round(value,2))
            output.insert('end',' km3')
        
        elif unit1_get==7 and unit2_get==3:
            output.delete(1.0,END)
            value= input_get*1.0E-15
            output.insert('end',input_get)
            output.insert('end',' hm3')

        elif unit1_get==7 and unit2_get==4:
            output.delete(1.0,END)
            value= input_get*1.0E-12
            output.insert('end',round(value,2))
            output.insert('end','dam3')

        elif unit1_get==7 and unit2_get==5:
            output.delete(1.0,END)
            value= input_get/1000000
            output.insert('end',round(value,2))
            output.insert('end','dm3')

        elif unit1_get==7 and unit2_get==6:
            output.delete(1.0,END)
            value= input_get/1000
            output.insert('end',round(value,2))
            output.insert('end','cm3')

        elif unit1_get==7 and unit2_get==7:
            output.delete(1.0,END)
            output.insert('end',round(value,2))
            output.insert('end','mm3')

    #create gui
    root = Tk()
    root.title('Volume Converter')
    root.geometry('400x300')
    root.resizable(0,0)
    root.configure(bg='#68999c')

    Label(root,text='Volume Converter', width = '500',
        height = '2',font = ('Helvetica', 13, 'bold')).pack()
    Label(root,text='Enter value To Convert:',
        bg = '#68999c',font = ('Helvetica', 13,)).place(x= 110,y=55)
    
    input_value= DoubleVar(root)
    Entry(root,textvariable= input_value ,width = 30).place(x= 110,y=85)
    Label(root,text='Form :',bg = '#68999c').place(x= 110,y=115)
    Label(root,text='  To :',bg = '#68999c').place(x= 110,y=145)

    unit_list = [
        "cubic meter","cubic kilometer","cubic hectometer","cubic decameter","cubic centimeter","cubic millimeter"
    ]
    
    unit1 = ttk.Combobox(root,values=unit_list)
    unit1.set('cubic meter')
    unit1.place(x=150,y= 115)


    unit2 = ttk.Combobox(root,values=unit_list)
    unit2.set('cubic kilometer')
    unit2.place(x=150,y= 145)
    Button(root,text='Convert',width=15,command=convert).place(x=164,y=180)


    output = Text(root,width=25,height=2)
    output.place(x=110,y=218)
    Label(root,text = 'STANDARD UNIT CONVERTER',bg = '#68999c',).place(x = 128, y =270 )
    exit_button=Button(root,text="Exit",command=root.destroy).place(x=350,y=220)



#create main screen
screen = Tk() 
screen.geometry('300x280')
screen.resizable(0,0)
screen.title('STANDARD UNIT CONVERTER')

screen.configure(bg='light blue')

#create button
length = Button(text='       Length converter       ',command=length_converter).place(x=80,y= 50)
time = Button(text='  Temperature converter  ',command=time_convert).place(x=80,y= 80)
weight= Button(text='       Weight converter       ',command=weight_converter).place(x=80,y= 110)
Area=Button(text='      Area converter     ',command=Area_converter).place(x=80,y=140)
timee=Button(text='     Time converter     ',command=time_converter).place(x=80,y=170)

#create label
Label(text = 'STANDARD UNIT CONVERTER',bg = 'light blue',font=12).place(x = 40, y = 220)

screen.mainloop()