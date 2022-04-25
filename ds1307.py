import time
import smbus

ds1307_addr=0x68#DS1307 Entegresinin I2C Adresi
ds1307 = smbus.SMBus(1)

seconds_addr=0x00#DS1307 second address
minutes_addr=0x01#DS1307 minutes address
hours_addr=0x02#DS1307 hours address
days_addr=0x03#DS1307 days address
dates_addr=0x04#DS1307 dates address
months_addr=0x05#DS1307 months address
years_addr=0x06#DS1307 years address

#Kullanilmak uzere degiskenler tanimlaniyor
seconds: int=0 
minutes: int=0
hours: int=0
days: int=0
dates: int=0
months: int=0
years: int=0
array_days=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

#DS1307 entegresi ile haberlesme icin 10'luk sistemden 2'lik sisteme dönüşütüren fonksiyon
def dec2bcd(num):
    ones: int=0
    tens: int=0
    temp: int=0
    
    ones=int(num%10)
    temp=int(num/10)
    tens=int(temp<<4)
    
    return ones+tens
#DS1307 entegresi ile haberlesme icin 2'lik sistemden 10'luk sisteme dönüşütüren fonksiyon
def bcd2dec(num):
    s: int=0
    s=int(num/16)
    p: int=0
    p=s*10
    f: int=0
    f=num % 16
    o: int=0
    o=p+f
    return o

#DS1307 entegresi Register'lara yazmak icin kullanilan fonksiyon
def set_time(seconds_val:  int,
             minutes_val: int,
             hours_val:   int,
             days_val:    int,
             dates_val:   int,
             months_val:  int,
             years_val:  int):
    #Input degiskenleri DS1307 Register'larina yazmak icin 2'lik sisteme cevirme islemi yapiliyor         
    seconds_val=dec2bcd(seconds_val)
    minutes_val=dec2bcd(minutes_val)
    hours_val=dec2bcd(hours_val)
    days_val=dec2bcd(days_val)
    dates_val=dec2bcd(dates_val)
    months_val=dec2bcd(months_val)
    years_val=dec2bcd(years_val)
    
    #2'lik sisteme donusturulen degiskenler DS1307 Entegresine yaziliyor
    #(Entegre Adresi, Register Adresi, Register Degeri)
    ds1307.write_byte_data(ds1307_addr, seconds_addr, seconds_val)
    ds1307.write_byte_data(ds1307_addr, minutes_addr, minutes_val)
    ds1307.write_byte_data(ds1307_addr, hours_addr, hours_val)
    ds1307.write_byte_data(ds1307_addr, days_addr, days_val)
    ds1307.write_byte_data(ds1307_addr, dates_addr, dates_val)
    ds1307.write_byte_data(ds1307_addr, months_addr, months_val)
    ds1307.write_byte_data(ds1307_addr, years_addr, years_val)
    
    return 0

def read_time():

    #DS1307 Entegresinin Register'larindan veri okumak icin kullanilan fonksiyon
    #Entegreden alinan veri 2'lik sistemden 10'luk sisteme donusturulerek kullanilabilir hale getiriliyor
    seconds=ds1307.read_byte_data(ds1307_addr,seconds_addr)
    seconds=bcd2dec(seconds)
    
    minutes=ds1307.read_byte_data(ds1307_addr,minutes_addr)
    minutes=bcd2dec(minutes)
    
    hours=ds1307.read_byte_data(ds1307_addr,hours_addr)
    hours=bcd2dec(hours)
    
    days=ds1307.read_byte_data(ds1307_addr,days_addr)
    days=bcd2dec(days)
    
    dates=ds1307.read_byte_data(ds1307_addr,dates_addr)
    dates=bcd2dec(dates)
    
    months=ds1307.read_byte_data(ds1307_addr,months_addr)
    months=bcd2dec(months)
    
    years=ds1307.read_byte_data(ds1307_addr,years_addr)
    years=bcd2dec(years)
    years=years+1970+30#Years icin offset degeri mevcut. Bu deger isleme alinmazsa dogru Yil bilgisi elde edilemez 
    date_output="{0:04d}{1:02d}{2:02d}" .format(years,months,dates)
    time_output="{0:2d}:{1:02d}:{2:02d}" .format(hours,minutes,seconds)
    return date_output,time_output
    
#set_time(0, 28, 13, 3, 26,1,22)

print(read_time()[0]+" "+read_time()[1]) 
